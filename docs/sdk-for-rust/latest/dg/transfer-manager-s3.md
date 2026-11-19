---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/transfer-manager-s3.html
---

# Using the Transfer Manager for Amazon S3

The Transfer Manager for Amazon S3 is a high-level library for the AWS SDK for Rust that transfers data to and from Amazon S3 with high throughput. The transfer manager splits each transfer into concurrent part requests and manages that concurrency for you, so you get multipart performance without writing the orchestration yourself.

The transfer manager is distributed in the `aws-s3-transfer` crate, separate from the `aws-sdk-s3` crate. You can use both crates in the same application.

## When to use the transfer manager
<a name="transfer-manager-s3-when-to-use"></a>

Use the transfer manager instead of calling Amazon S3 operations directly with the `aws-sdk-s3` crate when you want to do any of the following:
+ Transfer large objects. The transfer manager uploads and downloads an object as concurrent parts instead of a single request.
+ Transfer many objects. You can upload a local directory tree or download a bucket prefix with one call.
+ Upload a stream whose length you don't know in advance.
+ Maximize throughput and network utilization without hand-tuning concurrency.

## How the transfer manager works
<a name="transfer-manager-s3-how-it-works"></a>

The transfer manager wraps the Amazon S3 API and schedules the underlying requests for you:
+ For an upload larger than the multipart threshold, the transfer manager runs a multipart upload and sends the parts concurrently. A smaller upload is sent as a single `PutObject` request.
+ For a download, the transfer manager first discovers the object's size and entity tag (ETag). With checksum validation enabled, which is the default, it uses a `HeadObject` request. With validation off, it uses a first ranged `GetObject` request. It then fetches the object as concurrent ranged `GetObject` requests. Each ranged request carries an `If-Match` condition set to the discovered ETag, so a download of an object that changes partway through fails instead of mixing content from two versions.
+ Downloaded chunks are delivered in object order, whether you stream them or write them to a file.
+ The transfer manager retries failed requests and bounds the amount of data buffered in memory with a memory budget.
+ You build one client and share it. The client is cheap to clone, and clones share the same runtime, memory budget, and concurrency limits.

## Prerequisites
<a name="transfer-manager-s3-prerequisites"></a>

Before you use the transfer manager, make sure that you have the following:
+ A Rust toolchain that meets the crate's minimum supported Rust version (MSRV). The MSRV can change over time, so check the `aws-s3-transfer` crate's documentation for the current minimum.
+ An async runtime to await transfer results. The examples use Tokio with `#[tokio::main]`. By default, the transfer manager runs the transfers themselves on its own managed runtime, so you don't need to provide one for them.
+ Configured AWS credentials and a AWS Region. For more information, see [Authenticating with AWS using AWS SDK for Rust](credentials.md).

## Add the transfer manager to your project
<a name="transfer-manager-s3-dependency"></a>

Add the transfer manager crate along with `aws-config` and `tokio`. Run the following commands in your project directory:
+ `cargo add aws-s3-transfer`
+ `cargo add aws-config`
+ `cargo add tokio --features full`

The `full` Tokio feature is convenient while you get started. For a smaller build, enable only the features you use, such as `macros` and `rt-multi-thread`.

The crate also has an optional `sdk-v1` feature. Enable it when you need to pass Amazon S3-specific client settings (such as path-style addressing) or to convert between transfer manager types and `aws-sdk-s3` types. You don't need this feature for the examples in this section unless they state otherwise.

## Create a transfer manager client
<a name="transfer-manager-s3-client"></a>

A transfer manager client has the type [aws\_s3\_transfer::Client](https://docs.rs/aws-s3-transfer/latest/aws_s3_transfer/struct.Client.html). The examples in the child topics assume a `client` value of this type.

The simplest way is to load configuration from the environment, the same way `aws-config` does. This detects your settings and pins the latest behavior version:

```
use aws_s3_transfer::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = aws_s3_transfer::from_env().load().await;
    let client = Client::new(config);

    // Use client to upload, download, and transfer directories.
    let _ = client;
    Ok(())
}
```

To control the AWS Region, profile, or credentials, or to share configuration with an Amazon S3 client, build the client from an existing `SdkConfig`. Pass the configuration to `s3_config`, which is required:

```
use aws_config::BehaviorVersion;
use aws_s3_transfer::{Client, Config};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let sdk_config = aws_config::defaults(BehaviorVersion::latest()).load().await;

    let client = Client::new(Config::builder().s3_config(&sdk_config).build()?);

    let _ = client;
    Ok(())
}
```

Sharing one `SdkConfig` lets a transfer manager client and an Amazon S3 client read the same Region, credentials, and retry settings. The two clients still build their own connections, so they don't share a connection pool.

**Tip**
Create the client once and reuse it. The client is cheap to clone, and every clone shares the same runtime, memory budget, and concurrency limits. Clone the client for each task that runs a transfer instead of building a new client.

```
use aws_s3_transfer::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = aws_s3_transfer::from_env().load().await;
    let client = Client::new(config);

    // Clone the client into a spawned task. The clone shares the client's
    // runtime, memory budget, and concurrency limits.
    let client = client.clone();
    tokio::spawn(async move {
        // Start a transfer with this clone.
        let _ = &client;
    });

    Ok(())
}
```

## Required IAM permissions
<a name="transfer-manager-s3-permissions"></a>

The identity that runs a transfer needs permission for the Amazon S3 operations that the transfer manager calls on your behalf. The following table lists, for each kind of transfer, the Amazon S3 API operations the transfer manager may call and the IAM action that authorizes each one.

| Transfer | Amazon S3 API operations | IAM action |
| --- | --- | --- |
| Upload an object or a directory | PutObject, CreateMultipartUpload, UploadPart, CompleteMultipartUpload | s3:PutObject |
| Cancel or clean up a multipart upload | AbortMultipartUpload | s3:AbortMultipartUpload |
| Download an object or a prefix | GetObject, HeadObject | s3:GetObject (s3:GetObjectVersion when you request a version ID) |
| Download a prefix | ListObjectsV2 | s3:ListBucket |

Which operations a transfer actually runs depends on the object's size and the options you set. A small upload is a single `PutObject` request, while a larger upload runs a multipart upload that calls `CreateMultipartUpload`, `UploadPart`, and `CompleteMultipartUpload`.

Grant the upload actions on the object resources you write to, and grant `s3:ListBucket` on the bucket resource. If your objects use server-side encryption with AWS KMS keys (SSE-KMS), also grant `kms:GenerateDataKey` for uploads and `kms:Decrypt` for downloads and for multipart uploads.

## Additional resources
<a name="transfer-manager-s3-resources"></a>
+ The crate, [aws-s3-transfer](https://crates.io/crates/aws-s3-transfer), on the crates.io website.
+ The API reference, [aws\_s3\_transfer](https://docs.rs/aws-s3-transfer/latest/aws_s3_transfer/), on the docs.rs website.
+ The source repository, [aws-s3-transfer-manager-rs](https://github.com/awslabs/aws-s3-transfer-manager-rs), on the GitHub website.
