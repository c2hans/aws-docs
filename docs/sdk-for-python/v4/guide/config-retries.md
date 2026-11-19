---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/config-retries.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Retries

Calls to AWS services sometimes fail for reasons that have nothing to do with your request. A connection drops, a host is briefly unhealthy, or the service throttles you because too many requests arrived at the same time. A call that fails this way often succeeds if the client sends it again after a short delay, so every client in the AWS SDK for Python v4 retries these errors automatically. Synchronous and asynchronous clients use the same retry rules. Between attempts, a synchronous client sleeps the calling thread. An asynchronous client waits without blocking the event loop.

This page explains how the SDK retries failed requests and how to configure retry behavior. It includes the following topics:
+ [Retry modes](#retry-modes) describes the retry modes that the SDK supports.
+ [Retryable errors](#retryable-errors) describes which errors are retried and which are not.
+ [Standard retry strategy](#standard-retry-strategy) explains the backoff, jitter, and token bucket mechanics.
+ [Configuring retries](#configuring-retries) shows how to set the retry mode, the maximum number of attempts, and custom strategies.

## Retry modes
<a name="retry-modes"></a>

The SDK supports two retry modes:
+ **`standard`** (default): This mode retries transient and throttling errors with exponential backoff and jitter. A retry quota stops retries when they keep failing.
+ **`adaptive`**: This mode retries errors the same way as `standard`. After a service returns a throttling error, the client also limits how fast it sends requests. It adjusts that rate as later requests succeed or are throttled.

To set the mode, see [Configuring retries](#configuring-retries). For more information, see [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) in the *AWS SDKs and Tools Reference Guide*.

## Retryable errors
<a name="retryable-errors"></a>

The SDK retries only errors that are likely to be transient. These errors include socket-level failures, where the client receives no HTTP response, such as connect timeouts, read timeouts, and connections that the server closes. They also include HTTP 500, 502, 503, and 504 responses and a set of service error codes that the SDK recognizes as transient or throttling errors.

The SDK never retries errors that signal a problem with the request itself, such as validation errors, missing or malformed parameters, authentication and authorization failures, and resource-not-found responses. Sending the same request again can't change the outcome. A service can also mark its own errors as retryable in its service model. The SDK retries those errors in addition to the built-in list.

## Standard retry strategy
<a name="standard-retry-strategy"></a>

The standard retry strategy is the default. It makes a maximum of 3 attempts for a single request, including the initial attempt, so the SDK retries a request up to 2 times. The following sections describe how the strategy calculates the delay before each retry and limits retries with a retry quota.

### The x-amz-retry-after header
<a name="backoff-header"></a>

If a response has an `x-amz-retry-after` header, the SDK includes it in the backoff calculation. The value is an integer number of milliseconds. If the value is shorter than the computed delay, the SDK waits the computed delay. If the value is longer than the computed delay plus 5 seconds, the SDK waits the computed delay plus 5 seconds. The SDK doesn't apply jitter or the 20-second maximum delay to this value. The SDK ignores invalid `x-amz-retry-after` values, such as values with an invalid format or values that exceed integer limits, and uses exponential backoff instead. The SDK ignores the standard HTTP `Retry-After` header.

### Calculating exponential backoff and retry quotas
<a name="calculating-backoff-and-quotas"></a>

The base delay doubles with every retry, up to 20 seconds. The SDK then multiplies that delay by a random value between 0 and 1. The base delay is 1 second for throttling errors and 50 milliseconds for all other retryable errors. The SDK retries a transient error after up to 50 ms, then up to 100 ms. It retries a throttling error after up to 1 second, then up to 2 seconds.

The retry quota is a token bucket that each client keeps. Each retry takes tokens from the bucket. If the bucket doesn't have enough tokens for the next retry, the SDK raises the error without retrying. The bucket holds 500 tokens. A retry costs 14 tokens after a non-throttling error and 5 tokens after a throttling error. A successful operation returns the tokens that its retries took. An operation that succeeds without retrying adds 1 token, up to the 500-token maximum. The quota never blocks the first attempt, only retries.

### Retry strategy default values
<a name="retry-strategy-defaults"></a>

The following table shows the default values of the standard retry strategy.

| Setting | Default value |
| --- | --- |
| Maximum attempts | 3 |
| Base delay for non-throttling errors | 50 ms |
| Base delay for throttling errors | 1000 ms |
| Maximum delay | 20 seconds |
| Token bucket size | 500 |
| Token cost per non-throttling retry | 14 |
| Token cost per throttling retry | 5 |
| Tokens added when an operation succeeds without retrying | 1 |

**Note**
DynamoDB and DynamoDB Streams clients use a maximum of 4 attempts and a base delay of 25 ms for non-throttling errors.

## Configuring retries
<a name="configuring-retries"></a>

Set `retry_mode` to `standard` or `adaptive`. For the difference between the modes, see [Retry modes](#retry-modes).

The SDK doesn't support the `legacy` retry mode. If you pass `retry_mode="legacy"` to `resolve()`, resolution raises a validation error. Environment variables and shared config files are often shared with other tools and SDKs, so a `legacy` value from those sources doesn't raise an error. The SDK maps it to `standard` and emits a warning.

The two settings that control retry behavior are the retry mode and the maximum number of attempts. If you set neither, `resolve()` sets `retry_mode` to `standard` and leaves `max_attempts` unset:

```
config = BedrockRuntimeConfig.resolve()

print(config.retry_mode)     # "standard"
print(config.max_attempts)   # None
```

**Note**
`max_attempts` resolves to `None` when you don't set it. The retry strategy then uses its own default (3 for the standard strategy). It doesn't mean that retries are turned off.

The SDK resolves each setting separately, in the order that [Resolution order](config-resolution.md#resolution-order) describes. For example, `max_attempts` can come from your config file while `retry_mode` comes from the environment.

You can set both in the environment:

```
export AWS_RETRY_MODE=adaptive
export AWS_MAX_ATTEMPTS=5
```

Or in the shared config file:

```
# ~/.aws/config
[default]
retry_mode = adaptive
max_attempts = 5
```

Or in code, when you resolve a client configuration:

```
from aws_sdk_bedrock_runtime import BedrockRuntimeClient, BedrockRuntimeConfig

config = BedrockRuntimeConfig.resolve(
    region="us-east-1",
    retry_mode="adaptive",
    max_attempts=5,
)
with BedrockRuntimeClient(config=config) as client:
    response = client.converse(
        model_id="global.amazon.nova-2-lite-v1:0",
        messages=[{"role": "user", "content": [{"text": "Hello"}]}],
    )
```

`max_attempts` counts total attempts, not retries. Setting it to `1` turns off retries and still makes the original request:

```
config = BedrockRuntimeConfig.resolve(max_attempts=1)
```

If you need behavior that the built-in modes don't provide, you can supply your own retry strategy object. A strategy passed this way takes precedence. The SDK ignores any `retry_mode` or `max_attempts` setting.

```
from smithy_core.retries import SimpleRetryStrategy

config = BedrockRuntimeConfig.resolve(
    retry_strategy=SimpleRetryStrategy(max_attempts=10),
)

print(config.retry_strategy.max_attempts)  # 10
```

You can also implement your own retry strategy. A custom strategy must satisfy the `RetryStrategy` protocol (`smithy_core.interfaces.retries.RetryStrategy`), which requires a `backoff_strategy` attribute, a `max_attempts` attribute, and three methods: `acquire_initial_retry_token`, `refresh_retry_token_for_retry`, and `record_success`. The methods are synchronous, so the same strategy works with synchronous and asynchronous clients. The SDK accepts any class that implements them.
