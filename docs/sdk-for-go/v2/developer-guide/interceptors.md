---
source_url: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/interceptors.html
---

# HTTP Interceptors
<a name="interceptors"></a>

 You can use interceptors to hook into the execution of API requests and responses. Interceptors are open-ended mechanisms in which the SDK calls code that you write to inject behavior into the request/response lifecycle. This way, you can modify an in-flight request, debug request processing, view exceptions, and more.

## Interceptors vs. middleware
<a name="interceptors-vs-middleware"></a>

 The AWS SDK for Go v2 provides both interceptors and middleware for customizing request processing. While both serve similar purposes, they are designed for different audiences and use cases:
+  **Interceptors** are designed for SDK users who want to customize request/response processing with a simple, HTTP-focused API. They provide specific hook points in the request lifecycle and work directly with HTTP requests and responses.
+  **Middleware** is a more advanced, transport-agnostic system primarily used internally by the SDK. While powerful, middleware requires deeper knowledge of SDK internals and involves more complex interfaces.

 Key advantages of interceptors over middleware for common use cases:
+  **HTTP-focused**: Interceptors work directly with HTTP requests and responses, eliminating the need for transport type checking that middleware requires.
+  **Simpler interfaces**: Each interceptor hook has a specific, focused interface rather than the generic middleware pattern.
+  **Clearer execution model**: Interceptors execute at well-defined points in the request lifecycle without requiring knowledge of middleware stack ordering.

**Note**
 Interceptors are built on top of the existing middleware system, so both can coexist in the same application. Middleware remains available for advanced use cases that require transport-agnostic behavior or complex stack manipulation.

## Available interceptor hooks
<a name="interceptor-hooks"></a>

 The AWS SDK for Go v2 provides interceptor hooks at various stages of the request lifecycle. Each hook corresponds to a specific interface that you can implement:
+  `BeforeExecution` - First hook called during operation execution
+  `BeforeSerialization` - Before input message is serialized into transport request
+  `AfterSerialization` - After input message is serialized into transport request
+  `BeforeRetryLoop` - Before entering the retry loop
+  `BeforeAttempt` - First hook called inside retry loop
+  `BeforeSigning` - Before transport request is signed
+  `AfterSigning` - After transport request is signed
+  `BeforeTransmit` - Before transport request is sent
+  `AfterTransmit` - After receiving transport response
+  `BeforeDeserialization` - Before transport response is deserialized
+  `AfterDeserialization` - After unmarshalling transport response
+  `AfterAttempt` - Last hook called inside retry loop
+  `AfterExecution` - Last hook called during operation execution

 You can implement multiple interfaces in a single interceptor to hook into multiple stages of the request lifecycle.

## Interceptor registration
<a name="interceptor-registration"></a>

 You register interceptors when you construct a service client or when you override configuration for a specific operation. The registration differs depending on whether you want the interceptor to apply to all operations for your client or only specific ones.

 Interceptors are managed through an interceptor registry that provides methods to add and remove interceptors. The following example shows a simple interceptor that adds an AWS X-Ray trace ID header to outgoing requests before the signing process:

```
type recursionDetection struct{}

func (recursionDetection) BeforeSigning(ctx context.Context, in *smithyhttp.InterceptorContext) error {
    if traceID := os.Getenv("_X_AMZN_TRACE_ID"); traceID != "" {
        in.Request.Header.Set("X-Amzn-Trace-Id", traceID)
    }
    return nil
}

// use it on the client
svc := s3.NewFromConfig(cfg, func(o *s3.Options) {
    o.Interceptors.AddBeforeSigning(recursionDetection{})
})
```

 The interceptor registry is added to client Options, which enables per-operation interceptor configuration:

```
// ... or use it per-operation
s3.ListBuckets(context.Background(), &s3.ListBucketsInput{
}, func(o *s3.Options) {
   o.Interceptors.AddBeforeSigning(recursionDetection{})
})
```

## Global interceptor configuration
<a name="interceptor-global-config"></a>

 You can also register interceptors globally using the `config.LoadDefaultConfig` function with the appropriate `With*` options for each interceptor type. This applies the interceptor to all AWS service clients created from that configuration:

```
type myExecutionInterceptor struct{}

func (*myExecutionInterceptor) AfterExecution(ctx context.Context, in *smithyhttp.InterceptorContext) error {
    // Add your custom logic here
    return nil
}

cfg, err := config.LoadDefaultConfig(context.Background(),
    config.WithAfterExecution(&myExecutionInterceptor{}))
if err != nil {
    panic(err)
}

// every service client created from the above config
// will include this interceptor
svc := s3.NewFromConfig(cfg)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Go v2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-go` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
