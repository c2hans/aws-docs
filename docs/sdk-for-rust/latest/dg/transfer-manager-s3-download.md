---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/transfer-manager-s3-download.html
---

# Download objects with the Transfer Manager for Amazon S3

The Transfer Manager for Amazon S3 downloads an object as concurrent ranged `GetObject` requests, which gives you higher throughput for a large object than a single request. The transfer manager delivers the object's bytes in order, whether you stream them or write them to a file.

To create the transfer manager client the examples take as a parameter, see [Create a transfer manager client](transfer-manager-s3.md#transfer-manager-s3-client).

## Ways to receive a downloaded object
<a name="transfer-manager-s3-download-ways"></a>

A download starts in one of three ways, depending on where you want the object's bytes to go. The following table lists each method and what it returns.

| Method | Returns | Use when |
| --- | --- | --- |
| initiate() | DownloadHandle | You want to read the object's bytes in your own code, such as into memory or another stream. |
| write\_to\_path(path) | ManagedDownloadHandle | You want the transfer manager to create a file at a path and write the object to it. |
| write\_to\_file(file) | ManagedDownloadHandle | You want the transfer manager to write the object into a file that you already opened. |

With every method, call `join` on the returned handle to wait for the download to finish and to get the authoritative result. The `join` method returns a `DownloadOutput` value that carries the object's metadata, the transfer metrics, and the integrity-check result.

## Download an object to a file path
<a name="transfer-manager-s3-download-to-path"></a>

Call `write_to_path` to have the transfer manager write the object to a file. This method is asynchronous, so await it, and then call `join` on the returned handle:

```
use aws_s3_transfer::Client;

async fn download_to_path(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let handle = client
        .download()
        .bucket("amzn-s3-demo-bucket")
        .key("my-key")
        .write_to_path("downloads/my-key")
        .await?;

    let _output = handle.join().await?;
    Ok(())
}
```

The transfer manager writes to a temporary file in the destination's directory and atomically renames it to the destination path when the download succeeds. The destination's parent directory must already exist. If a file already exists at the destination path, the successful download replaces it.

**Note**
A successful download means the operating system accepted every byte and the rename completed. The transfer manager doesn't synchronize the file data or its directory to disk, so success isn't a guarantee that the file survives a system crash or power loss.

## Stream an object into memory
<a name="transfer-manager-s3-download-stream"></a>

Call `initiate` to get a `DownloadHandle` that you read yourself. The `initiate` method is synchronous. Read chunks from the handle's body in order with `body_mut().next()`, then call `join` after the body is fully read:

```
use aws_s3_transfer::Client;

async fn download_to_memory(client: &Client) -> Result<Vec<u8>, Box<dyn std::error::Error>> {
    let mut handle = client
        .download()
        .bucket("amzn-s3-demo-bucket")
        .key("my-key")
        .initiate()?;

    let mut buffer = Vec::new();
    while let Some(chunk) = handle.body_mut().next().await {
        let chunk = chunk?;
        for segment in chunk.data.into_segments() {
            buffer.extend_from_slice(&segment);
        }
    }

    let _output = handle.join().await?;
    Ok(buffer)
}
```

Each chunk's `data` field holds the bytes for one ranged request. Call `into_segments` to get the segments without copying, or `into_contiguous` to get one contiguous buffer.

**Note**
Read the body to the end before you call `join`. A chunk error from `next` is a generic error. `join` is the authoritative source for the transfer's error with its full context.

## Download an object into an open file
<a name="transfer-manager-s3-download-to-file"></a>

Call `write_to_file` to write the object into a file that you opened. The transfer manager writes to the file with positioned writes that start at offset 0 and resizes it to the exact downloaded length. This method is synchronous:

```
use aws_s3_transfer::Client;
use std::fs::File;

async fn download_to_file(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let file = File::create("downloads/my-key")?;

    let handle = client
        .download()
        .bucket("amzn-s3-demo-bucket")
        .key("my-key")
        .write_to_file(file)?;

    let _output = handle.join().await?;
    Ok(())
}
```

The transfer manager takes ownership of the file, so clone it first if you need to use it afterward. The file cursor is ignored. A file that was opened in append mode is rejected, and no request is sent.

## Download a byte range or a specific version
<a name="transfer-manager-s3-download-range-version"></a>

To download part of an object, set `range` to a single HTTP range header value. Amazon S3 doesn't support more than one range per request:

```
use aws_s3_transfer::Client;

async fn download_range(client: &Client) -> Result<Vec<u8>, Box<dyn std::error::Error>> {
    let mut handle = client
        .download()
        .bucket("amzn-s3-demo-bucket")
        .key("my-key")
        .range("bytes=0-1048575")
        .initiate()?;

    let mut buffer = Vec::new();
    while let Some(chunk) = handle.body_mut().next().await {
        for segment in chunk?.data.into_segments() {
            buffer.extend_from_slice(&segment);
        }
    }

    let _output = handle.join().await?;
    Ok(buffer)
}
```

The transfer manager validates the range when it discovers the object, not when you call `initiate`. An invalid range surfaces as an error from `next` and `join`.

To download a specific version of an object in a versioning-enabled bucket, set `version_id`:

```
use aws_s3_transfer::Client;

async fn download_version(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let handle = client
        .download()
        .bucket("amzn-s3-demo-bucket")
        .key("my-key")
        .version_id("your-version-id")
        .write_to_path("downloads/my-key")
        .await?;

    let _output = handle.join().await?;
    Ok(())
}
```

## Read object metadata before the body
<a name="transfer-manager-s3-download-metadata"></a>

Call `object_meta` on the handle to read the object's metadata, such as its total size, before you consume the body. This method waits for the transfer manager to finish discovery:

```
use aws_s3_transfer::Client;

async fn download_with_size(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let mut handle = client
        .download()
        .bucket("amzn-s3-demo-bucket")
        .key("my-key")
        .initiate()?;

    let total_size = handle.object_meta().await?.total_object_size();
    println!("Downloading {total_size} bytes");

    let mut buffer = Vec::new();
    while let Some(chunk) = handle.body_mut().next().await {
        for segment in chunk?.data.into_segments() {
            buffer.extend_from_slice(&segment);
        }
    }

    let _output = handle.join().await?;
    Ok(())
}
```

The `total_object_size` method reports the size of the whole object, even for a range download. The same metadata is available from the `DownloadOutput` value that `join` returns.

## Verify object integrity with checksums
<a name="transfer-manager-s3-download-checksum"></a>

When you download a whole object, the transfer manager verifies the object's stored checksum across the ranges it downloads concurrently. It computes a checksum for each range and combines the results in object order to compare against the value Amazon S3 stored. The transfer manager verifies the full-object `CRC32`, `CRC32C`, and `CRC64NVME` algorithms, including for an empty object.

Validation is on by default, because the transfer manager validates a response checksum whenever Amazon S3 supplies one. It's off only when you set the client's response-checksum validation to validate when required and you don't request a checksum. To require validation on a request regardless of the client setting, set `checksum_mode` to `ChecksumMode::Enabled`.

After the download finishes, call `join` to get the authoritative result, then read `integrity_checks().checksum_validation()` on the `DownloadOutput`. A `ChecksumValidation::Validated` result means the transfer manager verified every delivered byte. A `ChecksumValidation::NotValidated` result carries a reason, such as `UnsupportedAlgorithm` when the object stored a checksum only in an algorithm the SDK doesn't compute, such as MD5:

```
use aws_s3_transfer::types::ChecksumValidation;
use aws_s3_transfer::Client;

async fn download_and_verify(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let handle = client
        .download()
        .bucket("amzn-s3-demo-bucket")
        .key("my-key")
        .write_to_path("downloads/my-key")
        .await?;

    // On a checksum mismatch, join returns an error before the file is renamed
    // into place, so the destination is never published.
    let output = handle.join().await?;

    match output.integrity_checks().checksum_validation() {
        ChecksumValidation::Validated { .. } => {
            println!("The download was verified against a stored checksum.");
        }
        ChecksumValidation::NotValidated { reason, .. } => {
            println!("The download was not verified: {reason:?}");
        }
        _ => {}
    }

    Ok(())
}
```

If a checksum doesn't match, `join` returns an error whose kind is `IntegrityError`. For a download to a file path, the error is returned before the transfer manager renames the temporary file into place, so it never publishes corrupt data to the destination.

**Note**
When you stream an object with `initiate`, the transfer manager can deliver bytes to you before it finishes the whole-object check. Don't treat streamed bytes as verified until `join` succeeds.

## Read encrypted objects
<a name="transfer-manager-s3-download-options"></a>

To read an object that you stored with server-side encryption using customer-provided keys (SSE-C), supply the same key you used to upload the object. Set the algorithm, the key, and the key's MD5 digest:

```
use aws_s3_transfer::Client;

async fn download_sse_c(
    client: &Client,
    key: &str,
    key_md5: &str,
) -> Result<(), Box<dyn std::error::Error>> {
    let handle = client
        .download()
        .bucket("amzn-s3-demo-bucket")
        .key("my-key")
        .sse_customer_algorithm("AES256")
        .sse_customer_key(key)
        .sse_customer_key_md5(key_md5)
        .write_to_path("downloads/my-key")
        .await?;

    let _output = handle.join().await?;
    Ok(())
}
```

To monitor a download's progress or handle its errors, see [Monitor and control transfers with the Transfer Manager for Amazon S3](transfer-manager-s3-control.md).

## Adjust read-ahead for a download
<a name="transfer-manager-s3-download-read-ahead"></a>

A download prefetches object parts ahead of the code that reads or writes them. Read-ahead bounds how far it prefetches. You can set it on the download request before the transfer starts, or change it while the download runs. The memory budget still bounds the buffered data, so a large window doesn't exceed your memory limit. Read-ahead applies to downloads only.

To set the default read-ahead for every download on a client, use the loader's `read_ahead` method. For more information, see [Read-ahead](transfer-manager-s3-configure.md#transfer-manager-s3-config-read-ahead).

Set the window on the request with the `read_ahead` setter and `ReadAhead::Parts`, where the value is the number of parts fetched beyond the part your reader is waiting on:

```
use aws_s3_transfer::config::ReadAhead;
use aws_s3_transfer::Client;

async fn download_with_read_ahead(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let handle = client
        .download()
        .bucket("amzn-s3-demo-bucket")
        .key("my-key")
        // Fetch up to 32 parts ahead of the writer.
        .read_ahead(ReadAhead::Parts(32))
        .write_to_path("downloads/my-key")
        .await?;

    let _output = handle.join().await?;
    Ok(())
}
```

To change the window while the download runs, call `io_ctl()` on the handle and then `set_read_ahead()`. Lowering the window caps the memory held for a consumer that has fallen behind. Raising it restores prefetch depth once the consumer catches up. The new window takes effect on the next part the transfer requests:

```
use aws_s3_transfer::config::ReadAhead;
use aws_s3_transfer::Client;

async fn adjust_read_ahead(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let handle = client
        .download()
        .bucket("amzn-s3-demo-bucket")
        .key("my-key")
        .write_to_path("downloads/my-key")
        .await?;

    // Lower the window for a consumer that has fallen behind.
    handle.io_ctl().set_read_ahead(ReadAhead::Parts(8));
    // Raise it again once the consumer catches up.
    handle.io_ctl().set_read_ahead(ReadAhead::Parts(64));

    let _output = handle.join().await?;
    Ok(())
}
```
