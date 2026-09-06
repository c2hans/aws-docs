---
source_url: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-logging.html
---

# Logging
<a name="configure-logging"></a>

 The AWS SDK for Go has logging facilities available that allow your application to enable debugging information for debugging and diagnosing request issues or failures. The [Logger](https://pkg.go.dev/github.com/aws/smithy-go/logging#Logger) interface and [ClientLogMode](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#ClientLogMode) are the main components available to you for determining how and what should be logged by clients.

## Logger
<a name="logger"></a>

 When constructing an [Config](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#Config) using [LoadDefaultConfig](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/config#LoadDefaultConfig) a default `Logger` is configured to send log messages to the process' standard error (stderr). A custom logger that satisfies the [Logger](https://pkg.go.dev/github.com/aws/smithy-go/logging#Logger) interface can be passed as an argument to `LoadDefaultConfig` by wrapping it with [config.WithLogger](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/config#WithLogger).

 For example, to configure our clients to use our `applicationLogger`:

```
cfg, err := config.LoadDefaultConfig(context.TODO(), config.WithLogger(applicationLogger))
```

 Now clients configured using the constructed `aws.Config` will send log messages to `applicationLogger`.

### Context-Aware Loggers
<a name="context-aware-loggers"></a>

 A Logger implementation may implement the optional [ContextLogger](https://pkg.go.dev/github.com/aws/smithy-go/logging#ContextLogger) interface. Loggers that implement this interface will have their `WithContext` methods invoked with the current context. This allows your logging implementations to return a new `Logger` that can write additional logging metadata based on values present in the context.

## ClientLogMode
<a name="clientlogmode"></a>

 By default, service clients do not produce log messages. To configure clients to send log messages for debugging purposes, use the [ClientLogMode](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#ClientLogMode) member on `Config`. `ClientLogMode` can be set to enable debugging messaging for:
+  Signature Version 4 (SigV4) Signing
+  Request Retries
+  HTTP Requests
+  HTTP Responses

 For example, to enable logging of HTTP requests and retries:

```
cfg, err := config.LoadDefaultConfig(context.TODO(), config.WithClientLogMode(aws.LogRetries | aws.LogRequest))
```

 See [ClientLogMode](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#ClientLogMode) for the different client log modes available.
