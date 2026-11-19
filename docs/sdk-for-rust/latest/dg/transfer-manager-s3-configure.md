---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/transfer-manager-s3-configure.html
---

# Configure the Transfer Manager for Amazon S3

The Transfer Manager for Amazon S3 sizes itself for your machine and your workload. The defaults work well for most applications, so start with them and change a setting only when you measure a reason to. This topic explains the settings you can tune and the values the transfer manager uses when you leave a setting at its default.

For how to create a client, see [Create a transfer manager client](transfer-manager-s3.md#transfer-manager-s3-client). The examples here assume you add the `aws-config` and `tokio` dependencies described in [Add the transfer manager to your project](transfer-manager-s3.md#transfer-manager-s3-dependency).

## The three configuration layers
<a name="transfer-manager-s3-config-layers"></a>

Configuration reaches the transfer manager through three layers. The following table describes each layer and what it controls.

| Layer | Type | Controls |
| --- | --- | --- |
| Shared AWS configuration | aws\_config::SdkConfig | AWS Region, credentials, retry policy, timeouts, endpoint URL, and a custom HTTP client. The transfer manager reads these the same way the aws-sdk-s3 crate does. |
| S3 client configuration | S3ClientConfig | The settings of the S3 client that the transfer manager builds. You create it from a shared SdkConfig. With the sdk-v1 feature, you can instead build it from an aws\_sdk\_s3::config::Builder to set S3-specific options such as path-style addressing. |
| Transfer manager configuration | aws\_s3\_transfer::Config | The transfer-specific settings: multipart threshold, part size, concurrency, read-ahead, memory budget, and execution runtime. |

## Loader compared to builder
<a name="transfer-manager-s3-config-loader-builder"></a>

You assemble the configuration with the loader. The loader is the recommended path: it loads your shared AWS configuration, detects your machine, and fills in the defaults. The builder is a lower-level route for the rare setting the loader doesn't expose.

The loader (`from_env().load().await`)
Loads a full configuration from the environment the same way `aws-config` does. It detects your credentials, AWS Region, and retry settings, and it pins the latest behavior version. Because it runs on an async task, it also probes your machine. It reads the vCPU count, available memory, and the Amazon EC2 instance type from the local system. When it can't read the instance type locally, such as in a container, it queries the instance metadata service (IMDS) with one short request. Set any transfer setting it offers — part size, multipart threshold, concurrency, read-ahead, memory, and runtime — before you call `load()`, and the loader fills in everything else.
When you need your own `SdkConfig`, to set an AWS Region, a profile, credentials, or a custom endpoint, load it and pass it with `s3_config(&sdk_config)`. The loader then skips the shared-configuration load but still detects your machine.

The builder (`Config::builder()...build()`)
Sets nothing for you. It loads no shared configuration and makes no instance-metadata request. Its `build()` returns a `Result` that is an error unless you supply an S3 client configuration with `s3_config`. The AWS Region, credentials, the identity cache, and every other shared setting come only from the `SdkConfig` you pass. Reach for the builder only when the S3 configuration is already complete and you want neither environment loading nor machine detection.

We recommend the loader. It and the builder accept the same transfer settings, and the loader also exposes `s3_config` and `read_ahead`, so supplying your own `SdkConfig` or setting a client-wide read-ahead no longer sends you to the builder.

## Default values
<a name="transfer-manager-s3-config-defaults"></a>

When you leave a setting at `Auto`, the transfer manager resolves it to the following values. The part size and threshold values are fixed. The concurrency and memory values depend on your machine. The following table lists the default value of each setting.

| Setting | Default | Notes |
| --- | --- | --- |
| Multipart threshold | 16 MiB | An upload larger than this runs as a multipart upload. A smaller upload is sent as a single request. |
| Part size | 8 MiB | The target size of each part. The same value applies to uploads and downloads. For a multipart download, the transfer manager aligns ranges to the object's stored part size when it can. |
| Memory budget | A quarter of detected memory | A quarter of detected memory, capped at 32 GiB and raised to at least 256 MiB. The transfer manager uses 2 GiB when it can't detect memory. Bounds the payload data buffered at once. |
| Concurrency | Sized from the host | Sized from the host the transfer manager runs on. For more information, see [Concurrency](#transfer-manager-s3-config-concurrency). |

## Part size and multipart threshold
<a name="transfer-manager-s3-config-part-size"></a>

The multipart threshold decides when an upload switches from a single request to a multipart upload. The part size sets the target size of each part. Set either one with `PartSize::Target`, which takes a `ByteSize`. The part size applies to both uploads and downloads.

The following example sets a 32 MiB multipart threshold and 16 MiB parts:

```
use aws_s3_transfer::config::PartSize;
use aws_s3_transfer::types::ByteSize;
use aws_s3_transfer::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = aws_s3_transfer::from_env()
        // Start a multipart upload for objects larger than 32 MiB.
        .multipart_threshold(PartSize::Target(ByteSize::mib(32)))
        // Target 16 MiB parts for both uploads and downloads.
        .part_size(PartSize::Target(ByteSize::mib(16)))
        .load()
        .await;

    let client = Client::new(config);
    let _ = client;
    Ok(())
}
```

The minimum part size is 5 MiB. A value below 5 MiB is raised to 5 MiB. A multipart upload can have at most 10,000 parts, so the transfer manager uses a larger part size than you set if the configured size would produce more than 10,000 parts.

## Concurrency
<a name="transfer-manager-s3-config-concurrency"></a>

Concurrency is the number of in-flight requests the transfer manager runs at once, across all transfers that share the client. Set it with `ConcurrencyMode`.

With `ConcurrencyMode::Auto`, the default, the transfer manager sizes concurrency from the host it runs on. Set an exact number with `ConcurrencyMode::Explicit`. Higher concurrency can raise throughput but uses more connections and memory.

```
use aws_s3_transfer::config::ConcurrencyMode;
use aws_s3_transfer::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = aws_s3_transfer::from_env()
        .concurrency(ConcurrencyMode::Explicit(64))
        .load()
        .await;

    let client = Client::new(config);
    let _ = client;
    Ok(())
}
```

## Read-ahead
<a name="transfer-manager-s3-config-read-ahead"></a>

Read-ahead sets how far a download may prefetch ahead of the consumer. Set a client-wide default on the loader with `read_ahead`, using `ReadAhead::Parts` for an exact number of parts or `ReadAhead::Auto` for the default.

```
use aws_s3_transfer::config::ReadAhead;
use aws_s3_transfer::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = aws_s3_transfer::from_env()
        // Prefetch at most 8 parts ahead of the consumer for every download.
        .read_ahead(ReadAhead::Parts(8))
        .load()
        .await;

    let client = Client::new(config);
    let _ = client;
    Ok(())
}
```

You can also set read-ahead per download, or change it while a download runs. For more information, see [Adjust read-ahead for a download](transfer-manager-s3-download.md#transfer-manager-s3-download-read-ahead).

## Memory budget
<a name="transfer-manager-s3-config-memory"></a>

The memory budget bounds how much payload data the transfer manager buffers at one time across all transfers on the client. To set an explicit budget, build a buffer pool and pass it as `MemoryConfig::Explicit`. Choose the budget with `MemoryBudgetConfig`: `Limit` for an exact size, `Fraction` for a share of detected memory, or `Auto` for the default.

```
use aws_s3_transfer::config::{MemoryBudgetConfig, MemoryConfig};
use aws_s3_transfer::memory::BufferPool;
use aws_s3_transfer::types::ByteSize;
use aws_s3_transfer::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Cap buffered payload data at 2 GiB.
    let pool = BufferPool::builder()
        .memory_budget(MemoryBudgetConfig::Limit(ByteSize::gib(2)))
        .build()?;

    let config = aws_s3_transfer::from_env()
        .memory(MemoryConfig::Explicit(pool))
        .load()
        .await;

    let client = Client::new(config);
    let _ = client;
    Ok(())
}
```

When you leave the memory budget at `Auto`, the transfer manager uses a quarter of detected memory, capped at 32 GiB and raised to at least 256 MiB. On a host with less than 512 MiB of memory, the budget is half of detected memory. When the transfer manager can't detect memory, it uses 2 GiB.

To share one memory budget across several transfers, clone one client and reuse the clones. Every clone of a client draws from the same memory pool.

A `Fraction` budget sizes the pool from detected memory. A `Limit` budget sets an exact size and doesn't detect memory.

## Where transfer work runs
<a name="transfer-manager-s3-config-runtime"></a>

By default, the transfer manager owns and manages its own threads for transfer work. This is the managed runtime, and it suits most applications. To run transfer tasks on your own Tokio runtime instead, use `RuntimeConfig::multi_thread_tokio`.

```
use aws_s3_transfer::config::RuntimeConfig;
use aws_s3_transfer::Client;

#[tokio::main(flavor = "multi_thread")]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = aws_s3_transfer::from_env()
        .runtime_config(RuntimeConfig::multi_thread_tokio())
        .load()
        .await;

    let client = Client::new(config);
    let _ = client;
    Ok(())
}
```

**Note**
Use a multi-thread Tokio runtime with `multi_thread_tokio`. A current-thread runtime runs all transfer work on one thread, which serializes the concurrent requests and removes the transfer manager's main advantage.

## HTTP and TLS
<a name="transfer-manager-s3-config-http"></a>

By default, the transfer manager installs its own managed HTTP transport. This transport partitions connections across the transfer manager's managed threads, which keeps each connection's work on the thread that opened it. We recommend the default unless you need to customize transport settings such as the TLS provider, a proxy, connection limits, or timeouts.

To customize those settings while keeping the partitioned design, build the transport with the companion `aws-smithy-managed-http` crate, run it on a managed runtime from `aws-smithy-execution`, and hand that same runtime to the transfer manager with `aws_s3_transfer_ext::managed`. Add the companion crates to your project:
+ `cargo add aws-s3-transfer-ext`
+ `cargo add aws-smithy-managed-http --features client`
+ `cargo add aws-smithy-execution`
+ `cargo add aws-smithy-http-client --features rustls-aws-lc`

Set the transport options on the native pool builder. This example selects a TLS provider so the transport uses HTTPS, builds a `ManagedHttpPool` bound to the runtime, sets it as the HTTP client on the shared configuration loaded with `aws-config`, and hands the runtime to the transfer manager through the loader:

```
use aws_config::BehaviorVersion;
use aws_s3_transfer::config::RuntimeConfig;
use aws_s3_transfer::Client;
use aws_s3_transfer_ext as tm_ext;
use aws_smithy_execution::ManagedRuntime;
use aws_smithy_http_client::tls::{self, rustls_provider::CryptoMode};
use aws_smithy_managed_http::client::{pool, ManagedHttpPool};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // A managed runtime for the transport's connection work.
    let runtime = ManagedRuntime::builder().build()?;
    let execution = runtime.handle();
    let completion = runtime.shutdown_completion();

    // Configure transport on the native pool builder. Selecting a TLS provider
    // makes the transport use HTTPS.
    let transport =
        pool::ConnectionPool::builder().tls_provider(tls::Provider::rustls(CryptoMode::AwsLc));
    let http = ManagedHttpPool::builder()
        .pool_builder(transport)
        .runtime(execution)
        .build()?;

    // Load the shared configuration and set the managed pool as its HTTP client.
    let sdk_config = aws_config::defaults(BehaviorVersion::latest())
        .load()
        .await
        .into_builder()
        .http_client(http.clone())
        .build();

    // Hand the same runtime to the transfer manager through the loader.
    let config = aws_s3_transfer::from_env()
        .s3_config(&sdk_config)
        .runtime_config(RuntimeConfig::managed(tm_ext::managed(runtime)))
        .load()
        .await;
    let client = Client::new(config);

    // Release the client, then wait for the managed threads to stop.
    drop(client);
    completion.wait().await?;
    Ok(())
}
```

**Note**
These companion crates are at version 0.x. `aws-s3-transfer-ext` pins an exact transfer manager version, so upgrade the transfer manager and the companion crates together. You don't set any feature flag yourself. The extension crate enables the seam it needs.

If you set a plain HTTP client on the shared `SdkConfig` instead, the transfer manager uses that client and replaces its partitioned managed transport. For more information about HTTP clients and TLS in the SDK, see [Configuring HTTP-level settings within the AWS SDK for Rust](http.md) and [Choosing an alternative TLS provider](http.md#tlsProviders).

## Custom and S3-compatible endpoints
<a name="transfer-manager-s3-config-endpoints"></a>

To send requests to a custom endpoint, such as a local test server or an S3-compatible store, set the endpoint URL on the shared configuration and pass it to the loader with `s3_config`. This needs no extra feature.

```
use aws_config::BehaviorVersion;
use aws_s3_transfer::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let sdk_config = aws_config::defaults(BehaviorVersion::latest())
        .endpoint_url("https://s3.example.com")
        .load()
        .await;

    let config = aws_s3_transfer::from_env()
        .s3_config(&sdk_config)
        .load()
        .await;
    let client = Client::new(config);

    let _ = client;
    Ok(())
}
```

Some S3-compatible stores require path-style addressing. To enable it, build an `aws_sdk_s3::config::Builder` from the shared configuration, call `force_path_style`, and pass the builder to the loader's `s3_config`. This path requires the `sdk-v1` feature and the `aws-sdk-s3` dependency. For more information about the feature, see [Add the transfer manager to your project](transfer-manager-s3.md#transfer-manager-s3-dependency).

```
use aws_config::BehaviorVersion;
use aws_s3_transfer::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let sdk_config = aws_config::defaults(BehaviorVersion::latest())
        .endpoint_url("https://s3.example.com")
        .load()
        .await;

    // Requires the sdk-v1 feature and the aws-sdk-s3 dependency.
    let s3_config = aws_sdk_s3::config::Builder::from(&sdk_config).force_path_style(true);

    let config = aws_s3_transfer::from_env()
        .s3_config(s3_config)
        .load()
        .await;
    let client = Client::new(config);

    let _ = client;
    Ok(())
}
```

For more information about endpoints in the SDK, see [Configuring client endpoints in the AWS SDK for Rust](endpoints.md).

## Settings the transfer manager applies to its requests
<a name="transfer-manager-s3-config-overrides"></a>

The transfer manager inherits retry and timeout settings from the shared configuration, but it overrides a few settings on the requests it sends so that transfers behave well under load. Keep these in mind when you compare its behavior to a direct S3 client.
+ Enables stalled-stream protection on the upload and download body requests with a 2-second grace period. If a transfer body makes no progress for 2 seconds, the transfer manager abandons the connection and reissues the request.
+ Disables payload signing on `PutObject` and `UploadPart` requests.
+ Adds its own retry layer on top of the SDK retries. Each bucket gets a shared retry budget, so a transfer that reissues requests after the SDK's retries are exhausted doesn't overwhelm a service that is shedding load.

For more information about the retry and timeout settings you set on the shared configuration, see [Configuring retries in the AWS SDK for Rust](retries.md) and [Configuring timeouts in the AWS SDK for Rust](timeouts.md).

## Behavior version
<a name="transfer-manager-s3-config-behavior-version"></a>

The transfer manager uses the latest behavior version, and the loader pins it for you. The crate doesn't enable the `behavior-version-latest` feature, so when you load your own shared `SdkConfig` you must set a behavior version. Use `aws_config::defaults(BehaviorVersion::latest())` or `aws_config::load_defaults(BehaviorVersion::latest())`, as the endpoint and HTTP examples in this topic do. For more information, see [Using behavior versions in the AWS SDK for Rust](behavior-versions.md).
