---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/interceptors.html
---

# HTTP interceptors
<a name="interceptors"></a>

You can use interceptors to hook into the execution of API requests and responses. Interceptors are open-ended mechanisms in which the SDK calls code that you write to inject behavior into the request/response lifecycle. This way, you can modify an in-flight request, debug request processing, view exceptions, and more.

The following example shows a simple interceptor that adds an additional header to all outgoing requests before the retry loop is entered.

```
class AddHeader(
    private val key: String,
    private val value: String
) : HttpInterceptor {
    override suspend fun modifyBeforeRetryLoop(context: ProtocolRequestInterceptorContext<Any, HttpRequest>): HttpRequest {
        val httpReqBuilder = context.protocolRequest.toBuilder()
        httpReqBuilder.headers[key] = value
        return httpReqBuilder.build()
    }
}
```

For more information and the available interception hooks, see the [Interceptor interface](/smithy-kotlin/api/latest/smithy-client/aws.smithy.kotlin.runtime.client/-interceptor/index.html).

## Interceptor registration
<a name="interceptor-registration"></a>

You register interceptors when you construct a service client or when you override configuration for a specific set of operations.

### Interceptor for all service client operations
<a name="interceptor-all-ops"></a>

The following code adds an `AddHeader` instance to the interceptors property of the builder. This addition adds the `x-foo-version` header to all operations before the retry loop is entered.

```
val s3 = S3Client.fromEnvironment {
    interceptors += AddHeader("x-foo-version", "1.0")
}

// All service operations invoked using 's3' will have the header appended.
s3.listBuckets { ... }
s3.listObjectsV2 { ... }
```

### Interceptor for only specific operations
<a name="interceptor-specific-ops"></a>

By using the `withConfig` extension, you can [override service client configuration](override-client-config.md) for one or more operations for any service client. With this capability, you can register additional interceptors for a subset of operations.

The following example overrides the configuration of the `s3` instance for operations within the `use` extension. Operations called on `s3Scoped` contain both the `x-foo-version` and the `x-bar-version` headers.

```
// 's3' instance created in the previous code snippet.
s3.withConfig {
    interceptors += AddHeader("x-bar-version", "3.7")
}.use { s3Scoped ->
    // All service operations invoked using 's3Scoped' trigger interceptors
    // that were registered when the client was created and any added in the
    // withConfig { ... } extension.
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
