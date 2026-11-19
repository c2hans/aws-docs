---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/transfer-manager-s3-upload.html
---

# Upload objects with the Transfer Manager for Amazon S3

To upload an object, you start an upload on the transfer manager client, set the bucket, key, and body, and then wait for the transfer to finish. An upload follows the same shape every time:
+ Call `upload()` on the client and set the destination `bucket` and `key`.
+ Set the object content with `body`, which takes an `InputStream`.
+ Call `initiate()` to validate and schedule the transfer. This method is synchronous: it returns a handle immediately, so you apply `?` to it and don't await it.
+ Call `join().await` on the handle to wait for the upload to finish and read the result.

The transfer manager sends an object smaller than the multipart threshold as a single `PutObject` request. It uploads a larger object as concurrent parts with a multipart upload.

The examples in this topic assume a transfer manager `client`. To create one, see [Create a transfer manager client](transfer-manager-s3.md#transfer-manager-s3-client).

## Upload bytes from memory
<a name="transfer-manager-s3-upload-memory"></a>

To upload data that you already hold in memory, create an `InputStream` from a byte buffer with `InputStream::from`:

```
use aws_s3_transfer::io::InputStream;
use aws_s3_transfer::Client;

async fn upload_bytes(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let data = b"Hello from the transfer manager!".to_vec();

    let handle = client
        .upload()
        .bucket("amzn-s3-demo-bucket")
        .key("greetings/hello.txt")
        .body(InputStream::from(data))
        .initiate()?;

    let output = handle.join().await?;
    println!("Uploaded object with ETag {:?}", output.e_tag());
    Ok(())
}
```

## Upload a file
<a name="transfer-manager-s3-upload-file"></a>

To upload a file from the local file system, create an `InputStream` with `InputStream::from_path`. The transfer manager reads the file size and streams the file for you:

```
use aws_s3_transfer::io::InputStream;
use aws_s3_transfer::Client;

async fn upload_file(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let handle = client
        .upload()
        .bucket("amzn-s3-demo-bucket")
        .key("backups/archive.zip")
        .body(InputStream::from_path("archive.zip")?)
        .initiate()?;

    let _output = handle.join().await?;
    Ok(())
}
```

**Note**
`InputStream::from_path` returns an error if the path doesn't name a regular file, such as a directory, or if the file's metadata can't be read. Apply `?` to it, as in the preceding example.

## Upload part of a file
<a name="transfer-manager-s3-upload-file-part"></a>

To upload a byte range of a file, build the `InputStream` with `read_from` and set an `offset` and `length` in bytes:

```
use aws_s3_transfer::io::InputStream;
use aws_s3_transfer::Client;

async fn upload_file_range(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    // Upload 4 MiB starting 1 MiB into the file.
    let body = InputStream::read_from()
        .path("archive.zip")
        .offset(1024 * 1024)
        .length(4 * 1024 * 1024)
        .build()?;

    let handle = client
        .upload()
        .bucket("amzn-s3-demo-bucket")
        .key("backups/archive-chunk.bin")
        .body(body)
        .initiate()?;

    let _output = handle.join().await?;
    Ok(())
}
```

**Note**
When you set `length` explicitly, the transfer manager does not check it against the real file size. A length longer than the remaining bytes fails the upload, and a shorter length uploads a truncated object.

## Upload a stream of unknown length
<a name="transfer-manager-s3-upload-stream"></a>

To upload data as it is produced, when you don't know the total length in advance, wrap any reader that implements the Tokio `AsyncRead` trait with `TokioIo` and pass it to `InputStream::from_part_stream`. This is one way to supply a part stream. For full control over how parts are produced, you can instead implement a custom part producer (see [Provide a custom part producer](#transfer-manager-s3-upload-custom-stream)). A stream of unknown length is always uploaded as a multipart upload:

```
use aws_s3_transfer::io::adapters::TokioIo;
use aws_s3_transfer::io::{InputStream, SizeHint};
use aws_s3_transfer::Client;

async fn upload_stream<R>(client: &Client, reader: R) -> Result<(), Box<dyn std::error::Error>>
where
    R: tokio::io::AsyncRead + Send + Sync + 'static,
{
    // SizeHint::default() declares an unknown length.
    let body = InputStream::from_part_stream(TokioIo::new(reader, SizeHint::default()));

    let handle = client
        .upload()
        .bucket("amzn-s3-demo-bucket")
        .key("streams/live.dat")
        .body(body)
        .initiate()?;

    let _output = handle.join().await?;
    Ok(())
}
```

A multipart upload can have at most [10,000 parts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html). Without a declared length, the object is limited to 10,000 times the part size, which is about 78 GiB at the default upload part size of 8 MiB. To upload a larger object, declare an upper bound with `SizeHint::default().with_upper(Some(total_bytes))` so the transfer manager can size the parts, or increase the part size. For more information about the part size, see [Configure the Transfer Manager for Amazon S3](transfer-manager-s3-configure.md).

## Set upload options
<a name="transfer-manager-s3-upload-options"></a>

The upload builder accepts the same object options as the `aws-sdk-s3` `PutObject` request, such as a content type and user metadata. The following example sets a content type, adds metadata, chooses a checksum algorithm, and writes the object only if it doesn't already exist:

```
use aws_s3_transfer::io::InputStream;
use aws_s3_transfer::types::checksum::Crc32C;
use aws_s3_transfer::types::ChecksumStrategy;
use aws_s3_transfer::Client;

async fn upload_with_options(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let handle = client
        .upload()
        .bucket("amzn-s3-demo-bucket")
        .key("reports/quarterly.txt")
        .body(InputStream::from("quarterly results"))
        .content_type("text/plain")
        .metadata("team", "finance")
        .checksum_strategy(ChecksumStrategy::full_object(Crc32C))
        // Conditional write: upload only if this key doesn't exist yet; otherwise
        // join().await returns an error whose code() is PreconditionFailed.
        .if_none_match("*")
        .initiate()?;

    let _output = handle.join().await?;
    Ok(())
}
```

By default, when the request checksum calculation policy is `WhenSupported` (the SDK default), the transfer manager stores a full-object CRC64NVME checksum with the object. To store a different checksum, set a strategy with `checksum_strategy`, as in the preceding example. A strategy chooses the algorithm that Amazon S3 stores and whether the checksum covers the whole object. You pass the algorithm as a type from the `aws_s3_transfer::types::checksum` module, such as `Crc32C`. An algorithm that the chosen checksum type doesn't support is a compile error:
+ `full_object(algorithm)` stores a checksum of the whole object, which you can compare with one computed elsewhere. The algorithm is CRC64NVME, CRC32, or CRC32C.
+ `composite(algorithm)` stores, for a multipart upload, a checksum of the part checksums. The algorithm is CRC32, CRC32C, SHA-1, or SHA-256. SHA-1 and SHA-256 are available only as composite checksums.
+ `with_expected_value(value)` gives Amazon S3 a checksum you already know, and Amazon S3 rejects the upload unless the stored checksum matches. With `composite`, this is valid only for a single-request upload, and `initiate()` returns an `InputInvalid` error otherwise.

For more information about these choices, see [ChecksumStrategy](https://docs.rs/aws-s3-transfer/latest/aws_s3_transfer/types/struct.ChecksumStrategy.html) in the API reference on the docs.rs website.

## Read the upload result
<a name="transfer-manager-s3-upload-result"></a>

The `UploadOutput` that `join().await` returns carries the object's metadata from Amazon S3. Which fields are present depends on whether the upload used a single request or a multipart upload:

```
use aws_s3_transfer::io::InputStream;
use aws_s3_transfer::Client;

async fn read_upload_result(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    let handle = client
        .upload()
        .bucket("amzn-s3-demo-bucket")
        .key("data/archive.zip")
        .body(InputStream::from_path("archive.zip")?)
        .initiate()?;

    let output = handle.join().await?;

    // version_id is set when the bucket has versioning enabled; upload_id is set
    // only when the transfer used a multipart upload.
    println!(
        "ETag: {:?}, CRC64NVME: {:?}, version ID: {:?}, multipart upload ID: {:?}",
        output.e_tag(),
        output.checksum_crc64_nvme(),
        output.version_id(),
        output.upload_id(),
    );
    Ok(())
}
```

The `e_tag` and the checksum fields identify the stored object. `version_id` is present when the bucket has versioning enabled. `upload_id` is present only when the transfer used a multipart upload. For more information about tracking a transfer while it runs, see [Monitor and control transfers with the Transfer Manager for Amazon S3](transfer-manager-s3-control.md).

## Cancel an upload
<a name="transfer-manager-s3-upload-cancel"></a>

To cancel an upload, call `abort().await` on the handle instead of `join()`. The transfer manager cancels uploads and downloads the same way, including how it cleans up a multipart upload that already started. For more information, see [Cancel a transfer](transfer-manager-s3-control.md#transfer-manager-s3-control-cancel).

## Provide a custom part producer
<a name="transfer-manager-s3-upload-custom-stream"></a>

For advanced cases, you can implement the `PartStream` trait to produce upload parts yourself, including per-part checksums. For most uploads, use `InputStream` and the adapters shown in this topic instead. For more information, see [aws\_s3\_transfer::io::PartStream](https://docs.rs/aws-s3-transfer/latest/aws_s3_transfer/io/trait.PartStream.html) in the API reference on the docs.rs website.
