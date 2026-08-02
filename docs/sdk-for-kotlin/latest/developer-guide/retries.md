---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/retries.html
---

# Retries in the AWS SDK for Kotlin
<a name="retries"></a>

Calls to AWS services occasionally return unexpected exceptions. Certain types of errors, such as throttling or transient errors, might be successful if the call is retried.

This page describes how the AWS SDK for Kotlin handles retries automatically and how to customize retry behavior for your applications.

## Understanding retry behavior
<a name="retries-understanding"></a>

The following sections explain how the SDK determines when to retry requests and what exceptions are considered retryable.

### Default retry configuration
<a name="retries-default"></a>

By default, every service client is automatically configured with a [standard retry strategy](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime.retries/-standard-retry-strategy/index.html). The default configuration tries a call that fails up to three times (the initial attempt plus two retries). The intervening delay between each call is configured with exponential backoff and random jitter to avoid retry storms. This configuration works for the majority of use cases but may be unsuitable in some circumstances, such as high-throughput systems.

The SDK attempts retries only on retryable errors. Examples of retryable errors are socket timeouts, service-side throttling, concurrency or optimistic lock failures, and transient service errors. Missing or invalid parameters, authentication/security errors, and misconfiguration exceptions are not considered retryable.

You can customize the standard retry strategy by setting the maximum attempts, delays and backoff, and token bucket configuration.

### Which exceptions are retryable?
<a name="retries-default-policy-details"></a>

The AWS SDK for Kotlin uses a preconfigured retry policy that determines which exceptions are retryable. Service client configuration has a `retryPolicy` property that specifies the policy applied to retries. If no custom value is specified, the default value is [AwsRetryPolicy](/sdk-for-kotlin/api/latest/aws-http/aws.sdk.kotlin.runtime.http.retries/-aws-retry-policy/).

The following exceptions are determined to be retryable by `AwsRetryPolicy`:

#### Retryable by error code
<a name="retries-retryable-by-error-code"></a>

Any `ServiceException` with an `sdkErrorMetadata.errorCode` of:
+  `BandwidthLimitExceeded`
+  `EC2ThrottledException`
+  `IDPCommunicationError`
+  `LimitExceededException`
+  `PriorRequestNotComplete`
+  `ProvisionedThroughputExceededException`
+  `RequestLimitExceeded`
+  `RequestThrottled`
+  `RequestThrottledException`
+  `RequestTimeout`
+  `RequestTimeoutException`
+  `SlowDown`
+  `ThrottledException`
+  `Throttling`
+  `ThrottlingException`
+  `TooManyRequestsException`
+  `TransactionInProgressException`

#### Retryable by HTTP status code
<a name="retries-retryable-by-status-code"></a>

Any `ServiceException` with an `sdkErrorMetadata.statusCode` of:
+ 500 (Internal Service Error)
+ 502 (Bad Gateway)
+ 503 (Service Unavailable)
+ 504 (Gateway Timeout)

#### Retryable by error type
<a name="retries-retryable-by-error-type"></a>

Any `ServiceException` with an `sdkErrorMetadata.errorType` of:
+  `ErrorType.Server` (such as internal service errors)
+  `ErrorType.Client` (such as an invalid request, a resource not found, access denied, etc.)

#### Retryable by SDK metadata
<a name="retries-retryable-by-metadata"></a>

Any `SdkBaseException` where:
+  `sdkErrorMetadata.isRetryable` is `true` (such as a client-side timeout, networking/socket error, etc.)
+  `sdkErrorMetadata.isThrottling` is `true` (such as making too many requests in a short amount of time)

For a complete list of exceptions that may be thrown by each service client, consult [service-specific API reference documentation](/#products).

### Check if an exception is retryable
<a name="retries-check-exception-retryable"></a>

To determine if the SDK considers an exception retryable, check the `isRetryable` property on caught exceptions:

```
try {
    dynamoDbClient.putItem {
        tableName = "MyTable"
        item = mapOf("id" to AttributeValue.S("123"))
    }
} catch (e: SdkBaseException) {
    println("Exception occurred: ${e.message}")

    if (e.sdkErrorMetadata.isRetryable) {
        println("This exception is retryable - SDK will automatically retry")
        println("If you're seeing this, retries may have been exhausted")
    } else {
        println("This exception is not retryable - fix the underlying issue")

        // Common non-retryable scenarios.
        when {
            e.message?.contains("ValidationException") == true ->
                println("Check your request parameters")
            e.message?.contains("AccessDenied") == true ->
                println("Check your IAM permissions")
            e.message?.contains("ResourceNotFound") == true ->
                println("Verify the resource exists")
        }
    }
}
```

### What exceptions reach your code when retries fail
<a name="retries-exception-types-during-retries"></a>

When the SDK’s retry mechanism cannot resolve an issue, exceptions are thrown to your application code. Understanding these exception types helps you implement appropriate error handling. These are *not* the exceptions that trigger retries—those are handled internally by the SDK.

Your code will catch the following types of exceptions when retries are exhausted or disabled:

Service exceptions after retry exhaustion
When all retry attempts fail, your code catches the final service exception (subclass of `AwsServiceException`) that caused the last retry attempt to fail. This could be a throttling error, server error, or other service-specific exception that the SDK could not resolve through retries.

Network exceptions after retry exhaustion
When network issues persist through all retry attempts, your code catches `ClientException` instances for problems like connection timeouts, DNS resolution failures, and other connectivity issues that the SDK could not resolve.

Use the following pattern to handle these exceptions in your application:

```
try {
    s3Client.getObject {
        bucket = "amzn-s3-demo-bucket"
        key = "my-key"
    }
} catch (e: AwsServiceException) {
    // Service-side errors that persisted through all retries.
    println("Service error after retries: ${e.errorDetails?.errorCode} - ${e.message}")

    // Handle specific service errors that couldn't be resolved.
    if (e.errorDetails?.errorCode == "ServiceQuotaExceededException" ||
        e.errorDetails?.errorCode == "ThrottlingException") {
        println("Rate limiting persisted - consider longer delays or quota increase")
    }
} catch (e: ClientException) {
    // Client-side errors (persistent network issues, DNS resolution failures, etc.)
    println("Client error after retries: ${e.message}")
}
```

## Customizing retry behavior
<a name="retries-customizing"></a>

The following sections show how to customize the SDK’s retry behavior for your specific use case.

### Configure maximum attempts
<a name="retires-max-attempts"></a>

You can customize the default maximum attempts (3) in the [retryStrategy DSL block](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime.retries/-standard-retry-strategy/-config/-builder/index.html) during client construction.

```
val dynamoDb = DynamoDbClient.fromEnvironment {
    retryStrategy {
        maxAttempts = 5
    }
}
```

With the DynamoDB service client shown in the previous snippet, the SDK tries API calls that fail up to five times (the initial attempt plus four retries).

You can disable automatic retries completely by setting the maximum attempts to one as shown in the following snippet.

```
val dynamoDb = DynamoDbClient.fromEnvironment {
    retryStrategy {
        maxAttempts = 1  // The SDK makes no retries.
    }
}
```

### Configure delays and backoff
<a name="retries-delays-backoff"></a>

If a retry is necessary, the default retry strategy waits before it makes the subsequent attempt. The delay for the first retry is small but it grows exponentially for later retries. The maximum amount of delay is capped so that it does not grow too large.

Finally, random jitter is applied to the delays between all attempts. The jitter helps mitigate the effect of large fleets that can cause retry storms. (See this [AWS Architecture Blog post](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) for a deeper discussion about exponential backoff and jitter.)

Delay parameters are configurable in the [delayProvider DSL block](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime.retries.delay/-exponential-backoff-with-jitter/-config/index.html).

```
val dynamoDb = DynamoDbClient.fromEnvironment {
    retryStrategy {
        delayProvider {
            initialDelay = 100.milliseconds
            maxBackoff = 5.seconds
        }
    }
}
```

With the configuration shown in the previous snippet, the client delays the first retry attempt for up to 100 milliseconds. The maximum amount of time between any retry attempt is 5 seconds.

The following parameters are available for tuning delays and backoff.

| Parameter | Default value | Description |
| --- | --- | --- |
|  `initialDelay`  | 10 milliseconds | The maximum amount of delay for the first retry. When jitter is applied, the actual amount of delay may be less. |
|  `jitter`  | 1.0 (full jitter) | The maximum amplitude by which to randomly reduce the calculated delay. The default value of 1.0 means that the calculated delay can be reduced to any amount up to 100% (for example, down to 0). A value of 0.5 means that the calculated delay can be reduced by up to half. Thus, a max delay of 10ms could be reduced to anywhere between 5ms and 10ms. A value of 0.0 means that no jitter is applied. Important ️Jitter configuration is an advanced feature. Customizing this behavior is not normally recommended. |
|  `maxBackoff`  | 20 seconds | The maximum amount of delay to apply to any attempt. Setting this value limits the exponential growth that occurs between subsequent attempts and prevents the calculated maximum from being too large. This parameter limits the calculated delay *before* jitter is applied. If applied, jitter might reduce the delay even further. |
|  `scaleFactor`  | 1.5 | The exponential base by which subsequent maximum delays will be increased. For example, given an `initialDelay` of 10ms and a `scaleFactor` of 1.5, the following max delays would be calculated: Retry 1: 10ms × 1.5⁰ = 10ms Retry 2: 10ms × 1.5¹ = 15ms Retry 3: 10ms × 1.5² = 22.5ms Retry 4: 10ms × 1.5³ = 33.75ms When jitter is applied, the actual amount of each delay might be less. |

### Configure retry token bucket
<a name="retries-token-bucket"></a>

You can further modify the behavior of the standard retry strategy by adjusting the default token bucket configuration. The retry token bucket helps to reduce retries that are less likely to succeed or that might take more time to resolve, such as timeout and throttling failures.

**Important**
Token bucket configuration is an advanced feature. Customizing this behavior is not normally recommended.

Each retry attempt (optionally including the initial attempt) decrements some capacity from the token bucket. The amount decremented depends on the type of attempt. For example, retrying transient errors might be cheap, but retrying timeout or throttling errors might be more expensive.

A successful attempt returns capacity to the bucket. The bucket may not be incremented beyond its maximum capacity nor decremented below zero.

Depending on the value of the `useCircuitBreakerMode` setting, attempts to decrement capacity below zero result in one of the following outcomes:
+ If the setting is TRUE, an exception is thrown– For example, if too many retries have occurred and more retries are unlikely to succeed.
+ If the setting is FALSE, there is a delay – For example, delays until the bucket has sufficient capacity again.

**Note**
When the circuit breaker activates (token bucket reaches zero capacity), the SDK throws a `ClientException` with the message "Retry capacity exceeded". This is a client-side exception, not an `AwsServiceException`, because it originates from the SDK’s retry logic rather than the AWS service. The exception is thrown immediately without attempting the operation, helping prevent retry storms during service outages.

The token bucket parameters are configurable in the [tokenBucket DSL block](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime.retries.delay/-standard-retry-token-bucket/-config/index.html):

```
val dynamoDb = DynamoDbClient.fromEnvironment {
    retryStrategy {
        tokenBucket {
            maxCapacity = 100
            refillUnitsPerSecond = 2
        }
    }
}
```

The following parameters are available for tuning the retry token bucket:

| Parameter | Default value | Description |
| --- | --- | --- |
|  `initialTryCost`  | 0 | The amount to decrement from the bucket for initial attempts. The default value of 0 means that no capacity will be decremented and thus initial attempts are not stopped or delayed. |
|  `initialTrySuccessIncrement`  | 1 | The amount to increment capacity when the initial attempt was successful. |
|  `maxCapacity`  | 500 | The maximum capacity of the token bucket. The number of available tokens cannot exceed this number. |
|  `refillUnitsPerSecond`  | 0 | The amount of capacity re-added to the bucket every second. A value of 0 means that no capacity is automatically re-added. (For example, only successful attempts result in incrementing capacity). A value of 0 requires `useCircuitBreakerMode` to be TRUE. |
|  `retryCost`  | 5 | The amount to decrement from the bucket for an attempt following a transient failure. The same amount is re-incremented back to the bucket if the attempt is successful. |
|  `timeoutRetryCost`  | 10 | The amount to decrement from the bucket for an attempt following a timeout or throttling failure. The same amount is re-incremented back to the bucket if the attempt is successful. |
|  `useCircuitBreakerMode`  | TRUE | Determines the behavior when an attempt to decrement capacity would result in the bucket’s capacity to fall below zero. When TRUE, the token bucket will throw an exception indicating that no more retry capacity exists. When FALSE, the token bucket will delay the attempt until sufficient capacity has refilled. |

For detailed information about exception types thrown during retry scenarios, including circuit breaker exceptions, see [What exceptions reach your code when retries fail](#retries-exception-types-during-retries).

### Configure adaptive retries
<a name="retries-adaptive-retries"></a>

As an alternative to the standard retry strategy, the adaptive retry strategy is an advanced approach that seeks the ideal request rate to minimize throttling errors.

**Important**
Adaptive retries is an advanced retry mode. Using this retry strategy is not normally recommended.

Adaptive retries includes all the features of standard retries. It adds a client-side rate limiter that measures the rate of throttled requests compared to non-throttled requests. It also limits traffic to attempt to stay within a safe bandwidth, ideally causing zero throttling errors.

The rate adapts in real time to changing service conditions and traffic patterns and might increase or decrease the rate of traffic accordingly. Critically, the rate limiter might delay initial attempts in high-traffic scenarios.

You select the adaptive retry strategy by providing an additional parameter to the `retryStrategy` method. The rate limiter parameters are configurable in the [rateLimiter DSL block](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime.retries.delay/-adaptive-rate-limiter/-config/index.html).

```
val dynamoDb = DynamoDbClient.fromEnvironment {
    retryStrategy(AdaptiveRetryStrategy) {
        maxAttempts = 10
        rateLimiter {
            minFillRate = 1.0
            smoothing = 0.75
        }
    }
}
```

**Note**
The adaptive retry strategy assumes that the client works against a single resource (for example, one DynamoDB table or one Amazon S3 bucket).
If you use a single client for multiple resources, throttling or outages associated with one resource result in increased latency and failures when the client accesses all other resources. When you use the adaptive retry strategy, we recommend that you use a single client for each resource.
