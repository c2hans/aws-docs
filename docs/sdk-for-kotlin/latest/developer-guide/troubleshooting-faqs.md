---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/troubleshooting-faqs.html
---

# Troubleshooting FAQs
<a name="troubleshooting-faqs"></a>

As you use the AWS SDK for Kotlin in your applications, you might encounter some of the issues listed in this topic. Use the following suggestions to help uncover the root cause and resolve the error.

## How do I fix "connection closed" issues?
<a name="ts-faq-connection-closed"></a>

You might encounter “connection closed” issues as exceptions such as one of the following types:
+  `IOException: unexpected end of stream on <URL>`
+  `EOFException: \n not found: limit=0`
+  `HttpException: AWS_ERROR_HTTP_CONNECTION_CLOSED: The connection has closed or is closing.; crtErrorCode=2058; HttpErrorCode(CONNECTION_CLOSED)`

These exceptions indicate that a TCP connection from the SDK to a service was unexpectedly closed or reset. The connection might have been closed by your host, the AWS service, or an intermediary party such as a NAT gateway, proxy, or load balancer.

These types of exceptions are automatically retried but might still appear in SDK logs, depending on your logging configuration. If the exception is thrown into your code, that indicates the active retry strategy has exhausted its configured limits such as maximum attempts or retry token bucket. See the [Retries in the AWS SDK for Kotlin](retries.md) section of this guide for more information about retry strategies. See also [Why are exceptions thrown before reaching the maximum attempts?](#ts-faq-exceptions-before-max).

### Idle connection monitoring with the OkHttpEngine
<a name="ts-faq-connection-closed-okhttp"></a>

If you’re using the `OkHttpEngine` and frequently encounter `IOException: unexpected end of stream on <URL>` exceptions, [consider enabling idle connection monitoring](http-client-config.md#http-idle-connection-monitoring). This feature detects when remote servers have closed connections that are still in the connection pool, which can reduce the occurrence of these exceptions.

## Why are exceptions thrown before reaching the maximum attempts?
<a name="ts-faq-exceptions-before-max"></a>

Sometimes you might see exceptions that you expected to be retried but were thrown instead. In these situations, the following steps might help resolve the issue.
+  **Verify that the exception is retryable.** Some exceptions are not retryable, such as those that indicate a malformed service request, lack of permissions, and non-existent resources, as examples. The SDK does not automatically retry these kinds of exceptions. For information on how to check for retryable exceptions, see [Check if an exception is retryable](retries.md#retries-check-exception-retryable).
+  **Verify that the exception is being thrown into your code.** Some exceptions appear in log messages as information but are not actually thrown into your code. For instance, retryable exceptions such as throttling errors might be logged as the SDK automatically works through multiple backoff-and-retry cycles. The invocation of an SDK operation throws an exception only if it was not handled by the configured retry settings.
+  **Verify your configured retry settings.** See the [Retries in the AWS SDK for Kotlin](retries.md) section of this guide for more information about retry strategies and retry policies. Ensure that your code is using the settings you expect or the automatic defaults.
+  **Consider adjusting your retry settings.** After you verify the previous items, but the issue is not resolved, you might consider adjusting retry settings.
  +  **Increase the maximum number of attempts.** By default the maximum number of attempts for an operation is 3. If you find that this is not enough and exceptions are still occurring at the default setting, consider increasing the `retryStrategy.maxAttempts` property in your client configuration. See [Configure maximum attempts](retries.md#retires-max-attempts) for more information.
  +  **Increase the delay settings.** Some exceptions might be retried too rapidly before the underlying condition has had a chance to resolve. If you suspect that do be the case, consider increasing the `retryStrategy.delayProvider.initialDelay` or `retryStrategy.delayProvider.maxBackoff` properties in your client configuration. See [Configure delays and backoff](retries.md#retries-delays-backoff) for more information.
  +  **Disable circuit breaker mode.** The SDK maintains a bucket of tokens for each service client by default. When the SDK attempts a request and it fails with a retryable exception, the token count is decremented; when the request succeeds the token count is incremented.

    By default, if this token bucket reaches 0 tokens remaining, the circuit is broken. After the circuit is broken, the SDK disables retries and any current and subsequent requests that fail on the first attempt immediately throw an exception. The SDK re-enables retries after successful initial attempts return enough capacity to the token bucket. This behavior is intentional and designed to prevent retry storms during service outages and service recovery.

    If you prefer that the SDK continue retrying up to the maximum configured attempts, consider disabling circuit breaker mode by setting the `retryStrategy.tokenBucket.useCircuitBreakerMode` property to false in your client configuration. With this property set to false, the SDK client waits until the token bucket reaches sufficient capacity rather than abandon further retries that might lead to an exception when there are 0 tokens remaining.

## How do I fix `NoSuchMethodError` or NoClassDefFoundError?
<a name="ts-faq-nusuchmethod"></a>

These errors are most commonly caused by missing or conflicting dependencies. See [How do I resolve dependency conflicts?](ts-faq-dep-conflict-resolution.md) for more information.

### I see a `NoClassDefFoundError` for `okhttp3/coroutines/ExecuteAsyncKt`
<a name="ts-faq-nusuchmethod-okhttp"></a>

This indicates a dependency problem for OkHttp specifically. See [Resolving OkHttp version conflicts in your application](ts-faq-dep-conflict-resolution.md#okhttp-dep-conflicts) for more information.
