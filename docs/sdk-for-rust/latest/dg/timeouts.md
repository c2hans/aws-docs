---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/timeouts.html
---

# Configuring timeouts in the AWS SDK for Rust
<a name="timeouts"></a>

The AWS SDK for Rust provides several settings for managing AWS service request timeouts and stalled data streams. These help your application behave optimally when unexpected delays and failures occur in the network.

## API timeouts
<a name="api-timeouts"></a>

When there are transient issues that could cause request attempts to take a long time or fail completely, it is important to review and set timeouts so that your application can fail fast and behave optimally. Requests that fail can be automatically retried by the SDK. It is a good practice to set timeouts for both the individual attempt and the entire request.

The SDK for Rust provides a default timeout for establishing a connection for a request. The SDK doesn't have any default maximum wait-time set for recieving a response for a request attempt or for the entire request. The following timeout options are available:

| Parameter | Default value | Description |
| --- | --- | --- |
| Connect timeout | 3.1 seconds | The maximum amount of time to wait to establish a connection before giving up. |
| Operation timeout | None | The maximum amount of time to wait before receiving a response from the SDK for Rust, including all retries. |
| Operation attempt timeout | None | The maximum amount of time to wait for a single HTTP attempt, after which the API call can be retried. |
| Read timeout | None | The maximum amount of time to wait to read the first byte of a response from the time the request is initiated. |

The following example shows the configuration of an Amazon S3 client with custom timeout values:

```
let config = aws_config::defaults(BehaviorVersion::latest())
    .timeout_config(
        TimeoutConfig::builder()
            .operation_timeout(Duration::from_secs(5))
            .operation_attempt_timeout(Duration::from_millis(1500))
            .build()
    )
    .load()
    .await;

let s3 = aws_sdk_s3::Client::new(&config);
```

When you use both operation and attempt timeouts together, you set a hard limit on the total time spent on all attempts across retries. You also set an individual HTTP request to fail fast on a slow request.

As an alternative to setting these timeout values on the service client for all operations, you can configure or [override them for a single request](peroperation.md) .

**Important**
Operation and attempt timeouts do not apply to streaming data consumed after the SDK for Rust has returned a response. As an example, consuming data from a `ByteStream` member of a response is not subject to operation timeouts.

## Stalled stream protection
<a name="stalled-stream-protection"></a>

The SDK for Rust provides another form of timeout related to detecting stalled streams. A stalled stream is an upload or download stream that produces no data for longer than a configured grace period. This helps prevent applications from hanging indefinitely and never making progress.

 Stalled stream protection will return an error when a stream is idle for longer than the acceptable period.

By default, the SDK for Rust enables stalled stream protection for both uploads and downloads and looks for at least 1 byte/sec of activity with a generous grace period of 20 seconds.

The following example shows a customized `StalledStreamProtectionConfig` that disables upload protection and changes the grace period for no activity to 10 seconds:

```
let config = aws_config::defaults(BehaviorVersion::latest())
    .stalled_stream_protection(
        StalledStreamProtectionConfig::enabled()
            .upload_enabled(false)
            .grace_period(Duration::from_secs(10))
            .build()
    )
    .load()
    .await;
```

**Warning**
Stalled stream protection is an advanced configuration option. We recommend altering these values only if your application needs tighter performance or if it is causing some other issue.

### Disable stalled stream protection
<a name="disable-stalled-stream-protection"></a>

The following example shows how to disable stalled stream protection completely:

```
let config = aws_config::defaults(BehaviorVersion::latest())
    .stalled_stream_protection(StalledStreamProtectionConfig::disabled())
    .load()
    .await;
```
