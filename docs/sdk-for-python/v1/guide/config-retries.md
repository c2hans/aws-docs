---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/config-retries.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Retries
<a name="config-retries"></a>

This page explains how the SDK retries failed requests and how to configure retry behavior. It includes the following topics:
+ [Retryable errors](#retryable-errors) describes which errors are retried and which are not.
+ [Standard retry strategy](#standard-retry-strategy) explains the backoff, jitter, and token bucket mechanics.
+ [Configuring retries](#configuring-retries) shows how to set retry mode, max attempts, and custom strategies.

Calls to AWS services occasionally fail for reasons that have nothing to do with your request being wrong. A connection drops, a host is briefly unhealthy, or the service throttles you because too many requests arrived at the same time. Errors of this kind are often successful if the call is simply made again after a short delay, so every client in this SDK retries them automatically. This page explains how that retry behavior works and how to configure it.

## Retryable errors
<a name="retryable-errors"></a>

Only errors that are plausibly transient are retried. These include socket-level failures where no HTTP response was received (connect timeouts, read timeouts, or server-closed connections), HTTP 500, 502, 503, and 504 responses, and a set of service error codes the SDK recognizes as transient or throttling. Errors that signal a problem with the request itself like validation errors, missing or malformed parameters, authentication and authorization failures, and resource-not-found responses are never retried, because sending the same request again cannot change the outcome. Services can also mark their own exceptions as retryable in their service model, and the SDK honors that in addition to the built-in list.

## Standard retry strategy
<a name="standard-retry-strategy"></a>

The standard retry strategy is the default. It makes a maximum of 3 attempts for a single request, including the initial attempt. This means a request is retried up to 2 times. Each retry is delayed using exponential backoff with jitter. The strategy also maintains a retry quota that prevents additional attempts when retries keep failing.

### Backoff header: x-amz-retry-after
<a name="backoff-header"></a>

If a response carries an `x-amz-retry-after` header, the SDK incorporates it into the backoff calculation. The value is an integer number of milliseconds. If it is shorter than the computed delay, the SDK waits the computed delay; if it is longer than the computed delay plus 5 seconds, the SDK waits the computed delay plus 5 seconds. It is not jittered, and the 20-second maximum delay does not apply to it. Invalid values (such as invalid format or exceeding integer limits) specified in `x-amz-retry-after` are ignored and the SDK falls back to exponential backoff. The standard HTTP `Retry-After` header is ignored.

### Calculating exponential backoff and retry quotas
<a name="calculating-backoff-and-quotas"></a>

The base delay doubles with every retry and is capped at 20 seconds. That delay is then multiplied by a random value between 0 and 1. The base delay is 1 second for throttling errors and 50 milliseconds for all other retryable errors. A transient error is therefore retried after up to 50ms, then up to 100ms, while a throttling error is retried after up to 1 second, then up to 2 seconds. DynamoDB and DynamoDB Streams clients make 4 attempts and use a base delay of 25 milliseconds for non-throttling errors.

The retry quota is a token bucket held per client. Each retry must take tokens from the bucket, and if the bucket does not have enough, the SDK returns the error without retrying. The bucket holds 500 tokens. A retry costs 14 tokens after a non-throttling error and 5 after a throttling error; a successful operation returns what its retry consumed, and an operation that succeeds without retrying adds 1 token, up to the 500-token maximum. When the bucket cannot cover the next retry, the SDK raises the error immediately without retrying. The first attempt is always made, only retries are affected.

### Summary: retry strategy default values
<a name="retry-strategy-defaults"></a>

The following table shows the default values for the properties of the standard retry strategy.

| Property | Default value |
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

The standard retry mode is the only retry mode that this SDK currently supports. Setting `retry_mode` explicitly to anything other than `standard` raises a validation error during resolution. Because environment variables and shared config files are frequently shared across tools and SDKs, a `legacy` or `adaptive` value picked up from those sources is not treated as an error. It is mapped to `standard` and a warning is emitted, so a config file written for another SDK does not break your client.

The two settings that control retry behavior are the retry mode and the maximum number of attempts. If you set neither, resolving a configuration fills both in for you:

```
config = await AsyncBedrockRuntimeConfig.resolve()

print(config.retry_mode)     # "standard"
print(config.max_attempts)   # None
```

**Note**
`max_attempts` resolves to `None` when not explicitly set. This means the retry strategy uses its own built-in default (typically 3 for the standard strategy). It does not mean retries are disabled.

Values are resolved in order of precedence. An explicit argument to `resolve()` wins, then the environment variable, then the shared config file, and finally the built-in default. Precedence is evaluated per setting rather than per source, so `max_attempts` can come from your config file while `retry_mode` comes from the environment.

Both can be set in the environment:

```
export AWS_RETRY_MODE=standard
export AWS_MAX_ATTEMPTS=5
```

Or in the shared config file:

```
# ~/.aws/config
[default]
retry_mode = standard
max_attempts = 5
```

Or in code, when resolving a client configuration:

```
config = await AsyncBedrockRuntimeConfig.resolve(
    retry_mode="standard",
    max_attempts=5,
)
async with AsyncBedrockRuntimeClient(config=config) as client:
    response = await client.some_operation(input)
```

`max_attempts` counts total attempts, not retries, so setting it to `1` disables retries entirely while still making the original request:

```
config = await AsyncBedrockRuntimeConfig.resolve(max_attempts=1)
```

If you need behavior the built-in strategy does not provide, you can supply a retry strategy of your own. A strategy passed this way takes precedence, and any `retry_mode` or `max_attempts` set outside of it is not consulted.

```
from smithy_core.aio.retries import SimpleRetryStrategy

config = await AsyncBedrockRuntimeConfig.resolve(
    retry_strategy=SimpleRetryStrategy(max_attempts=10),
)

print(config.retry_strategy.max_attempts)  # 10
```

You can also implement your own retry strategy if the built-in options do not meet your needs. A custom strategy must satisfy the `RetryStrategy` protocol (`smithy_core.aio.interfaces.retries.RetryStrategy`), which requires a `backoff_strategy` attribute, a `max_attempts` attribute, and three async methods: `acquire_initial_retry_token`, `refresh_retry_token_for_retry`, and `record_success`. Any class that implements these is accepted by the SDK.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Python. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-python` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
