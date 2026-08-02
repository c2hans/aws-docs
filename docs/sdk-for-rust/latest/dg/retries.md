---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/retries.html
---

# Configuring retries in the AWS SDK for Rust
<a name="retries"></a>

The AWS SDK for Rust provides a default retry behavior for service requests and customizable configuration options. Calls to AWS services occasionally return unexpected exceptions. Certain types of errors, such as throttling or transient errors, might be successful if the call is retried.

Retry behavior can be configured globally using environment variables or settings in the shared AWS `config` file. For information on this approach, see [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) in the *AWS SDKs and Tools Reference Guide*. It also includes detailed information on retry strategy implementations and how to choose one over another.

Alternatively, these options can also be configured in your code, as shown in the following sections.

## Default retry configuration
<a name="defaultRetryConfig"></a>

 Every service client defaults to the `standard` retry strategy configuration provided through the [https://docs.rs/aws-smithy-types/latest/aws_smithy_types/retry/struct.RetryConfig.html](https://docs.rs/aws-smithy-types/latest/aws_smithy_types/retry/struct.RetryConfig.html) struct. By default, a call will be tried three times (*the initial attempt, plus two retries*). Additionally, each retry will be delayed by a short, random duration to avoid retry storms. This convention is suitable for the majority of use cases but might be unsuitable in specific circumstances such as high-throughput systems.

 Only some types of errors are considered retryable by the SDKs. Examples of retryable errors are:
+ socket timeouts
+ service-side throttling
+ transient service errors like HTTP 5XX responses

The following examples are **not** considered retryable:
+ Missing or invalid parameters
+ authentication/security errors
+ misconfiguration exceptions

You can customize the `standard` retry strategy by setting the maximum attempts, delays, and backoff configuration.

## Maximum Attempts
<a name="maxAttempts"></a>

You can customize the maximum attempts in your code by supplying a modified [https://docs.rs/aws-smithy-types/latest/aws_smithy_types/retry/struct.RetryConfig.html](https://docs.rs/aws-smithy-types/latest/aws_smithy_types/retry/struct.RetryConfig.html) to your `aws_config::defaults`:

```
const CUSTOM_MAX_ATTEMPTS: u32 = 5;
let retry_config = RetryConfig::standard()
    // Set max attempts. When max_attempts is 1, there are no retries.
    // This value MUST be greater than zero.
    // Defaults to 3.
    .with_max_attempts(CUSTOM_MAX_ATTEMPTS);

let config = aws_config::defaults(BehaviorVersion::latest())
    .retry_config(retry_config)
    .load()
    .await;
```

## Delays and backoff
<a name="delays"></a>

If a retry is necessary, the default retry strategy waits before it makes the subsequent attempt. The delay for the first retry is small but it grows exponentially for later retries. The maximum amount of delay is capped so that it does not grow too large.

Random jitter is applied to the delays between all attempts. The jitter helps mitigate the effect of large fleets that can cause retry storms. For a deeper discussion about exponential backoff and jitter, see [Exponential Backoff And Jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) in the *AWS Architecture Blog*.

 You can customize the delay settings in your code by supplying a modified [https://docs.rs/aws-smithy-types/latest/aws_smithy_types/retry/struct.RetryConfig.html](https://docs.rs/aws-smithy-types/latest/aws_smithy_types/retry/struct.RetryConfig.html) to your `aws_config::defaults`. The following code sets the configuration to delay the first retry attempt for up to 100 milliseconds and that the maximum amount of time between any retry attempt is 5 seconds.

```
let retry_config = RetryConfig::standard()
    // Defaults to 1 second.
    .with_initial_backoff(Duration::from_millis(100))
    // Defaults to 20 seconds.
    .with_max_backoff(Duration::from_secs(5));

let config = aws_config::defaults(BehaviorVersion::latest())
    .retry_config(retry_config)
    .load()
    .await;
```

## Adaptive Retry Mode
<a name="AdaptiveRetryMode"></a>

 As an alternative to the `standard` mode retry strategy, the `adaptive` mode retry strategy is an advanced approach that seeks the ideal request rate to minimize throttling errors.

**Note**
Adaptive retries is an advanced retry mode. Using this strategy is typically not recommended. See [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html#standardvsadaptive) in the *AWS SDKs and Tools Reference Guide*.

Adaptive retries includes all the features of standard retries. It adds a client-side rate limiter that measures the rate of throttled requests compared to non-throttled requests. It also limits traffic to attempt to stay within a safe bandwidth, ideally causing zero throttling errors.

The rate adapts in real time to changing service conditions and traffic patterns and might increase or decrease the rate of traffic accordingly. Critically, the rate limiter might delay initial attempts in high-traffic scenarios.

You can select the `adaptive` retry strategy in code by supplying a modified [https://docs.rs/aws-smithy-types/latest/aws_smithy_types/retry/struct.RetryConfig.html](https://docs.rs/aws-smithy-types/latest/aws_smithy_types/retry/struct.RetryConfig.html):

```
let config = aws_config::defaults(BehaviorVersion::latest())
    .retry_config(RetryConfig::adaptive())
    .load()
    .await;
```
