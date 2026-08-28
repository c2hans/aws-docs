---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/retry-strategy.html
---

# Configure retry behavior in the AWS SDK for Java 2.x
<a name="retry-strategy"></a>

Calls to AWS services can fail occasionally for unexpected reasons. Certain errors, such as throttling (rate exceeded) or transient errors, might succeed if the call is retried. The AWS SDK for Java 2.x has a built-in mechanism to detect such errors and automatically retry the call that is enabled by default for all clients.

This page describes how this works, how to configure the distinct modes, and tailor the retry behavior.

## Retry strategies
<a name="retry-strategies"></a>

A retry strategy is a mechanism used in the SDK to implement retries. Each SDK client has a retry strategy created at build time that cannot be modified after the client is built.

The retry strategy has the following responsibilities.
+ Classify exceptions as retryable or not.
+ Compute the suggested delay to wait before the next attempt.
+ Maintain a [token bucket](https://en.wikipedia.org/wiki/Token_bucket) that provides a mechanism to stop retries when a large percentage of requests are failing and retries are unsuccessful.

**Note**
Before the release of retry *strategies* with version 2.26.0 of the SDK, retry *policies* provided the retry mechanism in the SDK. The retry *policy* API is made up of the core [`RetryPolicy`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/retry/RetryPolicy.html) class in the `software.amazon.awssdk.core.retry` package, whereas the `[software.amazon.awssdk.retries](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/retries/package-summary.html)` package contains the retry *strategy* API elements.
The retry strategy API was introduced as part of the AWS-wide effort to unify the interfaces and behavior of the core components of the SDKs.

The SDK for Java 2.x has three built-in retry strategies: standard, legacy, and adaptive. All three retry strategies are preconfigured to retry on a set of retryable exceptions. Examples of retryable errors are socket timeouts, service-side throttling, concurrency or optimistic lock failures, and transient service errors.

### Standard retry strategy
<a name="retry-strategy-standard"></a>

The [standard retry strategy](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/retries/StandardRetryStrategy.html) is the recommended `RetryStrategy` implementation for normal use cases. Unlike the `AdaptiveRetryStrategy`, the standard strategy is generally useful across all retry use cases.

By default, the standard retry strategy does the following.
+ Retries on the conditions that are configured at build time. You can adjust this with `[StandardRetryStrategy.Builder](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/retries/StandardRetryStrategy.Builder.html)#retryOnException`.
+ Retries 2 times for a total of 3 attempts. You can adjust this with `StandardRetryStrategy.Builder#maxAttempts(int)`.
+ For non-throttling exceptions, it uses the `[BackoffStrategy](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/retries/api/BackoffStrategy.html)#exponentialDelay` backoff strategy, with a base delay of 100 milliseconds and a max delay of 20 seconds. You can adjust this with `StandardRetryStrategy.Builder#backoffStrategy`.
+ For throttling exceptions, it uses the `BackoffStrategy#exponentialDelay` backoff strategy, with a base delay of 1 second and a max delay of 20 seconds. You can adjust this with `StandardRetryStrategy.Builder#throttlingBackoffStrategy`.
+ Performs circuit breaking (disabling retries) in the event of high downstream failures. The first attempt is always executed, only retries are disabled. Adjust with `StandardRetryStrategy.Builder#circuitBreakerEnabled`.

### Legacy retry strategy
<a name="retry-strategy-legacy"></a>

The [legacy retry strategy](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/retries/LegacyRetryStrategy.html) is a `RetryStrategy` for normal use cases, however, it is deprecated in favor of the `StandardRetryStrategy`. This is the default retry strategy used by clients when you don't specify another strategy.

It is characterized by treating throttling and non-throttling exceptions differently, for throttling exceptions the base delay for the backoff is larger (500ms) than the base delay for non-throttling exceptions (100ms), and throttling exceptions do not affect the token bucket state.

Experience using this strategy at scale inside AWS has shown that is not particularly better than the standard retry strategy. Moreover, it fails to protect downstream services from retry storms and can lead to resource starvation on the client side.

By default, the legacy retry strategy does the following.
+ Retries on the conditions that are configured at build time. You can adjust this with `[LegacyRetryStrategy.Builder](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/retries/LegacyRetryStrategy.Builder.html)#retryOnException` .
+ Retries 3 times for a total of 4 attempts. You can adjust this with `LegacyRetryStrategy.Builder#maxAttempts(int)`.
+ For non-throttling exceptions, it uses the `BackoffStrategy#exponentialDelay` backoff strategy, with a base delay of 100 milliseconds and a max delay of 20 seconds. You can adjust this with `LegacyRetryStrategy.Builder#backoffStrategy.`
+ For throttling exceptions, it uses the `BackoffStrategy#exponentialDelay` backoff strategy, with a base delay of 500 milliseconds and a max delay of 20 seconds. You can adjust this with `LegacyRetryStrategy.Builder#throttlingBackoffStrategy`.
+ Performs circuit breaking (disabling retries) in the event of high downstream failures. Circuit breaking never prevents a successful first attempt. You can adjust this behavior with `LegacyRetryStrategy.Builder#circuitBreakerEnabled`.
+ The state of the circuit breaker is not affected by throttling exceptions.

### Adaptive retry strategy
<a name="retry-strategy-adaptive"></a>

The [adaptive retry strategy](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/retries/AdaptiveRetryStrategy.html) is a `RetryStrategy` for use cases with a high level of resource constraints.

The adaptive retry strategy includes all the features of the standard strategy and adds a client-side rate limiter that measures the rate of throttled requests compared to non-throttled requests. The strategy uses this measurement to slow down the requests in an attempt to stay within a safe bandwidth, ideally causing zero throttling errors.

By default, the adaptive retry strategy does the following.
+ Retries on the conditions that are configured at build time. You can adjust this with `[AdaptiveRetryStrategy.Builder](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/retries/AdaptiveRetryStrategy.Builder.html)#retryOnException` .
+ Retries 2 times for a total of 3 attempts. You can adjust this with `AdaptiveRetryStrategy.Builder#maxAttempts(int)`.
+ Uses a dynamic backoff delay that is based on the current load against the downstream resource.
+ Performs circuit breaking (disabling retries) when there are high number of downstream failures. Circuit breaking may prevent a second attempt in outage scenarios to protect the downstream service.

**Warning**
The adaptive retry strategy assumes that the client works against a single resource (for example, one DynamoDB table or one Amazon S3 bucket).
If you use a single client for multiple resources, throttling or outages associated with one resource result in increased latency and failures when the client accesses all other resources. When you use the adaptive retry strategy, we recommend that you use a single client for each resource.
We also recommend that you use this strategy in situations where all clients use the adaptive retry strategy against the resource.

**Important**
The release of retry strategies with 2.26.0 of the Java SDK includes the new [`RetryMode.ADAPTIVE_V2`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/retry/RetryMode.html#ADAPTIVE_V2) enumeration value. The `ADAPTIVE_V2` mode corrects an error that failed to delay the first attempt when throttling errors were detected previously.
With the 2.26.0 release, users automatically get the `ADAPTIVE_V2` mode behavior by setting the mode as `adaptive` with an environment variable, system property, or profile setting. There is no `adaptive_v2` value for these settings. See the following [Specify a strategy](#retry-strategies-specify) section for how to set the mode.
Users can get the previous behavior by setting the mode in code using `RetryMode.ADAPTIVE`.

### Summary: Comparison of retry strategy default values
<a name="retry-strategy-comparison"></a>

The following table shows the default values for the properties of each retry strategy.

| Strategy | Maximum attempts | Base delay for non-throttling errors | Base delay for throttling errors | Token bucket size | Token cost per non-throttling retry | Token cost per throttling retry |
| --- | --- | --- | --- | --- | --- | --- |
| Standard | 3 | 100 ms | 1000 ms | 500 | 5 | 5 |
| Legacy | 4 | 100 ms | 500 ms | 500 | 5 | 0 |
| Adaptive | 3 | 100 ms | 100 ms | 500 | 5 | 5 |

**Note**
DynamoDB clients use a default maximum retry count of 8 for all retry strategies, which is higher than the values shown in the table above for other AWS service clients.

## Specify a strategy
<a name="retry-strategies-specify"></a>

You have four ways to specify a strategy for your service client.

### In code
<a name="retry-strategies-specify-code"></a>

When you build a client, you can configure a lambda expression with a retry strategy. The following snippet configures a standard retry strategy that uses default values on a DynamoDB service client.

```
DynamoDbClient client = DynamoDbClient.builder()
        .overrideConfiguration(o -> o.retryStrategy(RetryMode.STANDARD))
        .build();
```

You can specify `RetryMode.LEGACY` or `RetryMode.ADAPTIVE` in place of `RetryMode.STANDARD`.

### As a profile setting
<a name="retry-strategies-specify-conf"></a>

Include `retry_mode` as profile setting in the [shared AWS config file](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html). Specify `standard`, `legacy`, or `adaptive` as a value. When set as a profile setting, all service clients that are created while the profile is active use the specified retry strategy with default values. You can override this setting by configuring a retry strategy in code as shown previously.

With the following profile, all service clients use the standard retry strategy.

```
[profile dev]
region = us-east-2
retry_mode = standard
```

### As a JVM system property
<a name="retry-strategies-specify-sysprop"></a>

You can configure a retry stategy for all service clients, unless overridden in code, by using the system property `aws.retryMode`. Specify `standard`, `legacy`, or `adaptive` as a value.

Use the `-D` switch when you invoke Java as shown in the following command.

```
java -Daws.retryMode=standard ...
```

Alternatively, set the system property in the code *before* creating any client as shown in the following snippet.

```
public void main(String[] args) {
    // Set the property BEFORE any AWS service clients are created.
    System.setProperty("aws.retryMode", "standard");
    ...
}
```

### With an environment variable
<a name="retry-strategies-specify-envvar"></a>

You can also use the `AWS_RETRY_MODE` environment variable with a value of `standard`, `legacy`, or `adaptive`. As with a profile setting or JVM system property, the environment variable configures all service clients with the specified retry mode unless you configure a client in code.

The following command sets the retry mode to `standard` for the current shell session.

```
export AWS_RETRY_MODE=standard
```

## Customize a strategy
<a name="customize-strategy"></a>

You can customize any retry strategy by setting the maximum attempts, backoff strategy, and exceptions that are retryable. You can customize when you build a retry strategy or when you build a client by using a override builder that allows further refinements of the configured strategy.

### Customize maximum attempts
<a name="customize-strategy-max-attempts"></a>

You can configure the maximum number of attempts during client construction as shown in the following statement. The following statement customizes the default retry strategy for the client to a maximum of 5 attempt--a first attempt plus 4 retries.

```
DynamoDbClient client = DynamoDbClient.builder()
        .overrideConfiguration(o -> o.retryStrategy(b -> b.maxAttempts(5)))
        .build();
```

Alternatively, you can build the strategy and provide it to the client as in the following code example. The following code replaces the standard 3 maximum attempts with 10 and configures a DynamoDB client with the customized strategy.

```
StandardRetryStrategy strategy = AwsRetryStrategy.standardRetryStrategy()
         .toBuilder()
         .maxAttempts(10)
         .build();
DynamoDbClient client = DynamoDbClient.builder()
        .overrideConfiguration(o -> o.retryStrategy(strategy))
        .build();
```

**Warning**
We recommended that you configure each client with a unique `RetryStrategy` instance. If a `RetryStrategy` instance is shared, failures in one client might affect the retry behavior in the other.

You can also set the maximum number of attempts for all clients by using [external settings](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) instead of code. You configure this setting as describe in the [Specify a strategy](#retry-strategies-specify) section.

### Customize retryable exceptions
<a name="customize-strategy-retryable-exceptions"></a>

You can configure additional exceptions that trigger retries during client construction. This customization is provided for edge cases where exceptions are thrown that are not included in the default set of retryable exceptions.

The `retryOnException` and `retryOnExceptionOrCause` methods **add** new exception types to the existing set of retryable exceptions; they do not replace the default set. This allows you to extend the retry behavior while maintaining the SDK's default retry capabilities.

The `retryOnExceptionOrCause` method adds a retryable exception if the SDK throws the direct exception or if the exception is wrapped as a cause in another exception.

The following code snippet shows the methods you use to customize the retry exceptions--`retryOnException` and `retryOnExceptionOrCause`. The `retryOnExceptionOrCause` methods adds a retryable exception if the SDK throws the direct exception or if the exception is wrapped.

```
DynamoDbClient client = DynamoDbClient.builder()
        .overrideConfiguration(o -> o.retryStrategy(
                 b -> b.retryOnException(EdgeCaseException.class)
                       .retryOnExceptionOrCause(WrappedEdgeCaseException.class)))
        .build();
```

**Important**
Retries are disabled for the Kinesis asynchronous client when you call a [`subscribeToShard`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/kinesis/KinesisAsyncClient.html#subscribeToShard(software.amazon.awssdk.services.kinesis.model.SubscribeToShardRequest,software.amazon.awssdk.services.kinesis.model.SubscribeToShardResponseHandler)) method, regardless of the retry strategy configuration.

### Customize the backoff strategy
<a name="customize-strategy-backoff"></a>

You can build the backoff strategy and supply it to the client.

The following code builds a `BackoffStrategy` that replaces the default, standard strategy's exponential delay backoff strategy.

```
BackoffStrategy backoffStrategy =
        BackoffStrategy.exponentialDelay(Duration.ofMillis(150),  // The base delay.
                                         Duration.ofSeconds(15)); // The maximum delay.
DynamoDbClient client = DynamoDbClient.builder()
        .overrideConfiguration(o -> o.retryStrategy(
                b -> b.backoffStrategy(backoffStrategy)))
        .build();
```

## Migrating from `RetryPolicy` to `RetryStrategy`
<a name="migrate-from-retry-policies"></a>

`RetryPolicy` (the retry policy API) will be supported for the foreseeable future. If you currently use an instance of `RetryPolicy` to configure your client, everything is going to work as before. Behind the scenes the Java SDK adapts it to a `RetryStrategy`. The new retry strategy interfaces provide the same functionality as a `RetryPolicy` but are created and configured differently.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
