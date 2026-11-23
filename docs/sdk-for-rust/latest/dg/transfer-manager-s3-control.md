---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/transfer-manager-s3-control.html
---

# Monitor and control transfers with the Transfer Manager for Amazon S3

After you start a transfer with the transfer manager, the operation handle it returns lets you watch the transfer, change how it's scheduled, and cancel it. This topic shows how to monitor progress, log activity, cancel transfers, handle errors, and set priority.

To create the transfer manager client the examples take as a parameter, see [Create a transfer manager client](transfer-manager-s3.md#transfer-manager-s3-client).

## Log transfer activity
<a name="transfer-manager-s3-control-logging"></a>

The transfer manager logs through the `tracing` crate, the same framework as the rest of the SDK for Rust: add and initialize a tracing subscriber, then set the `RUST_LOG` environment variable to choose what to log. For how to set up a subscriber, see [Configuring and using logging in the AWS SDK for Rust](logging.md).

Start with the crate at the `info` level, and raise an individual target for more detail, such as `aws_s3_transfer::transfer` for per-transfer activity:

```
RUST_LOG=aws_s3_transfer=info,aws_s3_transfer::transfer=debug
```

The transfer manager emits events under these targets, all namespaced under `aws_s3_transfer`:

| Target | What it covers |
| --- | --- |
| aws\_s3\_transfer::transfer | Transfer lifecycle and state transitions. Each operation also logs under its own child target: ::upload, ::download, ::upload\_objects, and ::download\_objects. Enabling transfer enables all four. |
| aws\_s3\_transfer::memory | Buffer-pool admission, storage, and reclamation. |
| aws\_s3\_transfer::concurrency | Concurrency resolution and control. |
| aws\_s3\_transfer::scheduling | Scheduler capacity decisions and memory-budget admission. |
| aws\_s3\_transfer::execution | Per-work-item dispatch and completion on the managed runtime. |

When you create a client, the transfer manager logs one record at the `INFO` level with the sizing it resolved for the client: the concurrency target, the memory ceiling, the part size, and the per-host connection cap.

For deeper troubleshooting, the `AWS_S3_TM_DIAGNOSTICS` environment variable turns on extra diagnostic records. For more information, see [Runtime diagnostics](https://docs.rs/aws-s3-transfer/latest/aws_s3_transfer/#runtime-diagnostics) in the API reference on the docs.rs website.

## Track transfer progress
<a name="transfer-manager-s3-control-progress"></a>

A transfer handle reports progress at any time while the transfer runs, without consuming the handle. Call `status()` for a `TransferStatus` snapshot (`Active`, `Completed`, `Failed`, or `Cancelled`), and `metrics()` for a `TransferMetrics` snapshot. To test whether the transfer has finished, call `is_terminal()`. The metrics carry the payload bytes sent and received (`network_tx`, `network_rx`), the bytes read from and written to disk (`disk_read`, `disk_write`), the elapsed time, and `total_bytes`, the expected payload size when the transfer manager knows it. Read them on an interval to report progress.

The byte counts advance as whole parts complete, so a snapshot taken mid-transfer is coarse rather than byte-exact. For a directory transfer, the counts move only as each child object finishes, and `total_bytes` isn't set for the directory transfer as a whole. When the transfer finishes, the output returned by `join()` carries the final metrics.

## Cancel a transfer
<a name="transfer-manager-s3-control-cancel"></a>

To cancel a transfer, call `abort().await` on the handle. It stops the transfer and waits for its cleanup to finish. For an upload, if a multipart upload was started, it sends `AbortMultipartUpload` to Amazon S3 to remove the incomplete parts. It returns an `AbortedUpload` that reports whether the object was canceled or had already been stored, and the open upload ID if a multipart upload was left in place:

```rust
use aws_s3_transfer::io::InputStream;
use aws_s3_transfer::types::AbortOutcome;
use aws_s3_transfer::Client;

async fn cancel_upload(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let handle = client
        .upload()
        .bucket("amzn-s3-demo-bucket")
        .key("data/large.bin")
        .body(InputStream::from_path("large.bin")?)
        .initiate()?;

    // Later, cancel the upload.
    let aborted = handle.abort().await?;
    match aborted.outcome() {
        AbortOutcome::Cancelled => println!("Upload cancelled"),
        AbortOutcome::AlreadyCompleted => println!("Object was already stored"),
        AbortOutcome::Retained => {
            // The multipart upload was left open. Its upload ID is available for cleanup.
            match aborted.upload_id() {
                Some(upload_id) => println!("Multipart upload {upload_id} left open"),
                None => println!("Multipart upload left open"),
            }
        }
        _ => {}
    }
    Ok(())
}
```

**Warning**
Dropping a handle also cancels the transfer, but it returns immediately without waiting for in-flight work, and it does not send `AbortMultipartUpload`. A started multipart upload can be left incomplete in Amazon S3 (the open upload ID is logged at the `WARN` level), and writes already in flight may still land. To clean up, call `abort().await` instead of dropping the handle, and add an Amazon S3 Lifecycle rule to remove incomplete multipart uploads.

## Handle transfer errors
<a name="transfer-manager-s3-control-errors"></a>

Transfer methods return `aws_s3_transfer::error::Error`. Treat the error from `join()` as authoritative. Errors from streaming a download body are generic, and `join()` reports the underlying cause.

Call `kind()` to get the `ErrorKind`. The kinds a caller usually acts on are:
+ `InputInvalid` — the request was rejected before any call to Amazon S3, for example because a source path doesn't name a regular file. A failure tied to a local path names the operation and the path.
+ `IOError` — a local filesystem or stream read or write failed. A local filesystem failure names the operation and the path, as in `I/O error opening "archive.zip"`.
+ `ServiceError` — a request to Amazon S3 failed. Identify the specific outcome with `code()` (for example, `PreconditionFailed` for a conditional write) or with `is_not_found()`. Service failures also carry `operation_name()` and `request_id()`.
+ `IntegrityError` — a download failed checksum validation because the received bytes didn't match the object's stored checksum.
+ `ChildOperationFailed` — one or more objects in a directory transfer failed. Call `failed_uploads()` or `failed_downloads()` for the objects that failed. The error's `source()` is the first failed object's error.
+ `OperationCancelled` — the transfer was canceled.

When an upload fails but leaves a multipart upload open in Amazon S3, the error's `upload_id()` returns that upload's ID. This happens when the failed multipart upload policy is `FailedMultipartUploadPolicy::Retain`, when `AbortMultipartUpload` failed, or when a worker panic ended the upload. Amazon S3 keeps, and bills for, the uploaded parts until you complete or abort the multipart upload with that ID, so clean it up or add an Amazon S3 Lifecycle rule that removes incomplete multipart uploads.

The error's own display text carries limited local detail, so for a filesystem failure you have two options to reach the operating system message: wrap the error in `DisplayErrorContext` from the `aws-smithy-types` crate, or walk the error's source chain yourself with `std::error::Error::source`. Add the crate with `cargo add aws-smithy-types`:

```rust
use aws_s3_transfer::error::{Error, ErrorKind};
use aws_smithy_types::error::display::DisplayErrorContext;

fn handle_transfer_error(err: Error) {
    match err.kind() {
        ErrorKind::ServiceError if err.is_not_found() => {
            eprintln!("the bucket or object was not found");
        }
        ErrorKind::ServiceError => {
            eprintln!(
                "service error calling {:?}: code {:?}, request id {:?}",
                err.operation_name(),
                err.code(),
                err.request_id(),
            );
        }
        ErrorKind::ChildOperationFailed => {
            if let Some(failed) = err.failed_uploads() {
                eprintln!("{} object(s) failed to upload", failed.len());
            }
            if let Some(failed) = err.failed_downloads() {
                eprintln!("{} object(s) failed to download", failed.len());
            }
        }
        _ => {
            // Other kinds: print the full cause chain.
            eprintln!("transfer failed: {}", DisplayErrorContext(&err));
        }
    }
}
```

## Monitor client memory usage
<a name="transfer-manager-s3-control-memory"></a>

The transfer manager buffers object parts in a shared memory pool. Call `metrics()` on the client and then `memory()` to read the pool's current accounting, such as the configured capacity and how much is in use:

```rust
use aws_s3_transfer::Client;

async fn print_memory_usage(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let metrics = client.metrics();
    let memory = metrics.memory();
    println!(
        "memory pool: {} bytes in use of {} bytes configured",
        memory.in_use_bytes(),
        memory.capacity_bytes(),
    );
    Ok(())
}
```

Clients that share one memory pool report the same shared accounting. For how to size the memory budget, see [Configure the Transfer Manager for Amazon S3](transfer-manager-s3-configure.md).

## Shut down the client
<a name="transfer-manager-s3-control-shutdown"></a>

By default, the transfer manager runs transfers on its own managed runtime. That runtime stops automatically when the last clone of the client and every transfer handle are dropped. You don't need to shut it down explicitly.

To wait for the runtime's background threads to stop, call `shutdown_completion()` on the client before you release it. This returns an observer, or `None` if you run transfers on your own Tokio runtime instead of the managed one. Waiting does not request shutdown, so release every clone and handle, and the client itself, first:

```rust
async fn shut_down_client(
    client: aws_s3_transfer::Client,
) -> Result<(), Box<dyn std::error::Error>> {
    // Get the observer before releasing the client.
    let completion = client.shutdown_completion();

    // Release every clone and transfer handle, then the client itself.
    drop(client);

    // Wait for the managed runtime threads to stop.
    if let Some(completion) = completion {
        completion.wait().await?;
    }
    Ok(())
}
```

**Note**
Don't await `wait()` while a client clone or a transfer handle is still alive. Active work keeps the runtime owner alive, so the wait would never return.

## Prioritize transfers
<a name="transfer-manager-s3-control-priority"></a>

When several transfers share one client, you can bias the scheduler toward the ones that matter most. Call `scheduling()` on a handle to get its scheduling controls, and change the transfer's priority while it runs, for example to boost a background download once a user is waiting on it:

```rust
use aws_s3_transfer::Client;

async fn prioritize_transfer(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let handle = client
        .download()
        .bucket("amzn-s3-demo-bucket")
        .key("my-key")
        .write_to_path("my-file")
        .await?;

    // Start as a low-priority background transfer.
    handle.scheduling().set_priority(64);

    // Later, raise the priority when the data is needed sooner.
    handle.scheduling().set_priority(255);

    let _output = handle.join().await?;
    Ok(())
}
```

Priority is a relative weight, not a bandwidth limit: it changes how often a transfer is scheduled against its peers rather than capping throughput. Set it with `set_priority()` to a value from 1 through 255, where higher values get a larger share of the client's work and the default is 128.
