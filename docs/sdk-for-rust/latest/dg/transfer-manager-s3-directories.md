---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/transfer-manager-s3-directories.html
---

# Upload directories and download prefixes with the Transfer Manager for Amazon S3

The transfer manager can move a whole directory tree in one call. Uploading a directory walks a local directory and uploads each file it finds. Downloading objects from a prefix lists the objects under a bucket prefix and writes each one to a local directory. The transfer manager runs the individual object transfers concurrently and reports how many succeeded.

To create the transfer manager client the examples take as a parameter, see [Create a transfer manager client](transfer-manager-s3.md#transfer-manager-s3-client).

## Upload a directory
<a name="transfer-manager-s3-dir-upload"></a>

To upload a directory tree, call `upload_objects` with the source directory, the destination bucket, and a key prefix. By default the walker reads only the immediate contents of the source directory. To include subdirectories, pass a walker with `recursive(true)`.

```rust
use aws_s3_transfer::io::walk::FsWalker;
use aws_s3_transfer::Client;

async fn upload_directory(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let handle = client
        .upload_objects()
        .bucket("amzn-s3-demo-bucket")
        .source("photos/2026")
        .key_prefix("backup/photos")
        .walker(FsWalker::builder().recursive(true).build())
        .initiate()?;

    let output = handle.join().await?;
    println!("uploaded {} objects", output.objects_uploaded());
    Ok(())
}
```

The transfer manager builds each object key by joining the key prefix and the file's path relative to the source directory. The parts are joined with a delimiter that defaults to `/`. Set a different one with the `delimiter` setter on the `upload_objects` builder. A file at `photos/2026/spring/trip.jpg` uploads to the key `backup/photos/spring/trip.jpg`. If you omit the key prefix, or set it to an empty string, each file's key is its path relative to the source directory, with no leading delimiter.

By default, the walker:
+ Reads only the immediate contents of the source directory. Call `recursive(true)` to walk the full tree, or `max_depth` to set how many levels of subdirectories to descend.
+ Includes hidden files.
+ Skips symbolic links. Call `follow_symlinks(true)` on the walker builder to traverse them.
+ Returns entries in the operating system's native order. Call `sort(true)` to walk each directory in sorted order.

### Upload only certain files
<a name="transfer-manager-s3-dir-upload-filter"></a>

To upload a subset of the files in the directory, set a filter on the walker. The transfer manager calls your closure for each file and uploads only the files for which it returns `true`. The filter applies to files, so it can't stop the walker from descending into a subdirectory.

```rust
use aws_s3_transfer::io::walk::FsWalker;
use aws_s3_transfer::Client;

async fn upload_directory_filtered(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let walker = FsWalker::builder()
        .recursive(true)
        .filter(|entry| {
            entry
                .relative_path()
                .extension()
                .is_some_and(|ext| ext == "jpg")
        })
        .build();

    let handle = client
        .upload_objects()
        .bucket("amzn-s3-demo-bucket")
        .source("photos/2026")
        .key_prefix("backup/photos")
        .walker(walker)
        .initiate()?;

    handle.join().await?;
    Ok(())
}
```

## Download objects under a prefix
<a name="transfer-manager-s3-dir-download"></a>

To download the objects under a prefix, call `download_objects` with the bucket and a destination directory, and set the prefix on an `S3Walker`. The transfer manager writes each object at its full key under the destination directory. The walker's prefix only selects which objects to download. The transfer manager doesn't remove it from the local path.

```rust
use aws_s3_transfer::io::walk::S3Walker;
use aws_s3_transfer::Client;

async fn download_prefix(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let handle = client
        .download_objects()
        .bucket("amzn-s3-demo-bucket")
        .destination("downloads")
        .walker(S3Walker::builder().prefix("logs/").build())
        .initiate()?;

    let output = handle.join().await?;
    println!("downloaded {} objects", output.objects_downloaded());
    Ok(())
}
```

With the destination `downloads` and the prefix `logs/`, the object `logs/2026/app.log` is written to `downloads/logs/2026/app.log`. The transfer manager recreates the directory layout under the destination by splitting each key on `/`. If your keys use a different delimiter, set it with the `delimiter` setter on the `download_objects` builder, and the transfer manager replaces that delimiter with the local path separator.

The transfer manager creates the destination directory, and any missing parent directories, if it doesn't exist. A destination path that contains `.` or `..` components works. The transfer manager resolves it before writing. The transfer manager skips zero-byte folder marker objects whose key ends with a slash. It fails any object whose local path would resolve outside the destination directory, or onto the destination directory itself, with an `InputInvalid` error and records it as a failed transfer.

### Download only certain objects
<a name="transfer-manager-s3-dir-download-filter"></a>

To download a subset of the objects under the prefix, set a filter on the walker. The transfer manager calls your closure for each listed object and downloads only the objects for which it returns `true`.

```rust
use aws_s3_transfer::io::walk::S3Walker;
use aws_s3_transfer::types::Object;
use aws_s3_transfer::Client;

async fn download_prefix_filtered(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let walker = S3Walker::builder()
        .prefix("logs/")
        .filter(|object: &Object| object.key().is_some_and(|key| key.ends_with(".json")))
        .build();

    let handle = client
        .download_objects()
        .bucket("amzn-s3-demo-bucket")
        .destination("downloads")
        .walker(walker)
        .initiate()?;

    handle.join().await?;
    Ok(())
}
```

## Handle individual object failures
<a name="transfer-manager-s3-dir-failures"></a>

A directory transfer moves many objects, and an individual object can fail. The failure policy controls what happens when one does. The default policy is `FailedTransferPolicy::Abort`, which stops the transfer on the first failure. With `FailedTransferPolicy::Continue`, the transfer runs to the end and records each failure.

Under the `Continue` policy, `join` returns the output even when some objects failed. Read `failed_transfers` for the details of each failure.

```rust
use aws_s3_transfer::io::walk::FsWalker;
use aws_s3_transfer::types::FailedTransferPolicy;
use aws_s3_transfer::Client;

async fn upload_directory_continue(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let handle = client
        .upload_objects()
        .bucket("amzn-s3-demo-bucket")
        .source("photos/2026")
        .key_prefix("backup/photos")
        .walker(FsWalker::builder().recursive(true).build())
        .failure_policy(FailedTransferPolicy::Continue)
        .initiate()?;

    let output = handle.join().await?;
    println!("uploaded {} objects", output.objects_uploaded());
    for failed in output.failed_transfers() {
        eprintln!(
            "failed to upload {:?}: {}",
            failed.source_path(),
            failed.error()
        );
    }
    Ok(())
}
```

Under the default `Abort` policy, `join` returns an error instead of an output when an object fails. The error's `source` is the error of the first object that failed, the one that stopped the transfer. A local I/O failure, such as reading a source file or creating the destination directory, names the path in its message. Return or log that error as you would any other transfer error. For how to inspect which child objects failed, see [Handle transfer errors](transfer-manager-s3-control.md#transfer-manager-s3-control-errors).

```rust
use aws_s3_transfer::io::walk::FsWalker;
use aws_s3_transfer::Client;

async fn upload_directory_abort(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let handle = client
        .upload_objects()
        .bucket("amzn-s3-demo-bucket")
        .source("photos/2026")
        .key_prefix("backup/photos")
        .walker(FsWalker::builder().recursive(true).build())
        .initiate()?;

    let output = handle.join().await?;
    println!("uploaded {} objects", output.objects_uploaded());
    Ok(())
}
```

## Control how many objects transfer at once
<a name="transfer-manager-s3-dir-concurrency"></a>

A directory transfer runs its object transfers concurrently. The `max_concurrent_uploads` and `max_concurrent_downloads` settings cap the number of object transfers the transfer manager runs at once. Both default to 512. This cap is a backstop that bounds working memory. It works within the overall concurrency limit of the client. It doesn't raise throughput beyond what the client allows.

```rust
use aws_s3_transfer::io::walk::S3Walker;
use aws_s3_transfer::Client;

async fn download_prefix_limited(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let handle = client
        .download_objects()
        .bucket("amzn-s3-demo-bucket")
        .destination("downloads")
        .walker(S3Walker::builder().prefix("logs/").build())
        .max_concurrent_downloads(64)
        .initiate()?;

    handle.join().await?;
    Ok(())
}
```

## Limitations
<a name="transfer-manager-s3-dir-limitations"></a>

Directory transfers trade per-object control for a single high-level call. Keep the following limits in mind:
+ Downloading objects from a prefix overwrites a local file that already exists at a target path.
+ Uploading a directory applies only the bucket, key, and file contents to each object. It doesn't set a content type, metadata, storage class, server-side encryption with customer-provided keys (SSE-C), or a checksum strategy. To set these for an object, upload that file on its own with `upload()`. For more information, see [Upload objects with the Transfer Manager for Amazon S3](transfer-manager-s3-upload.md).
+ Downloading objects from a prefix doesn't apply SSE-C or the Requester Pays setting to the object reads. To download an object with those options, download that object on its own. For more information, see [Download objects with the Transfer Manager for Amazon S3](transfer-manager-s3-download.md).
+ The output reports the number of objects transferred and the list of failures. It doesn't report a per-object result for each object that succeeded.
