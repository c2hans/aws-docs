---
source_url: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-observability.html
---

# Traces and metrics
<a name="configure-observability"></a>

 The AWS SDK for Go is instrumented to record trace spans and client-side metrics for SDK operations. By default, clients use no-op implementations for both tracing and metrics, meaning no data is collected unless you configure a provider.

 Service clients have two configuration options for observability:
+  [TracerProvider](https://pkg.go.dev/github.com/aws/smithy-go/tracing#TracerProvider) – Entry point for creating tracers and recording client trace spans.
+  [MeterProvider](https://pkg.go.dev/github.com/aws/smithy-go/metrics#MeterProvider) – Entry point for creating meters and recording client-side metrics.

 While inspired by the OpenTelemetry (OTel) specifications, these APIs are defined independently in `smithy-go`. The SDK provides adapter modules to connect concrete OTel SDK implementations to the SDK's provider interfaces.

## Tracing
<a name="configure-tracing"></a>

 Use the [smithyoteltracing](https://pkg.go.dev/github.com/aws/smithy-go/tracing/smithyoteltracing) adapter module to connect an OTel `trace.TracerProvider` to a service client.

 The following example shows how to configure tracing for an Amazon S3 client:

```
import (
    "github.com/aws/aws-sdk-go-v2/service/s3"
    "github.com/aws/smithy-go/tracing/smithyoteltracing"
    "go.opentelemetry.io/otel/trace"
)

// provider is an OTel trace.TracerProvider that you have configured.
var provider trace.TracerProvider

svc := s3.NewFromConfig(cfg, func(o *s3.Options) {
    o.TracerProvider = smithyoteltracing.Adapt(provider)
})
```

 SDK operations are instrumented with a span hierarchy that covers the high-level components of the operation lifecycle, such as request serialization, signing, and the retry loop.

## Metrics
<a name="configure-metrics"></a>

 Use the [smithyotelmetrics](https://pkg.go.dev/github.com/aws/smithy-go/metrics/smithyotelmetrics) adapter module to connect an OTel `metric.MeterProvider` to a service client.

 The following example shows how to configure metrics for an Amazon S3 client:

```
import (
    "github.com/aws/aws-sdk-go-v2/service/s3"
    "github.com/aws/smithy-go/metrics/smithyotelmetrics"
    "go.opentelemetry.io/otel/metric"
)

// provider is an OTel metric.MeterProvider that you have configured.
var provider metric.MeterProvider

svc := s3.NewFromConfig(cfg, func(o *s3.Options) {
    o.MeterProvider = smithyotelmetrics.Adapt(provider)
})
```

### Supported metrics
<a name="supported-metrics"></a>

 SDK clients collect the following metrics:

| Metric name | Unit | Type | Description |
| --- | --- | --- | --- |
| client.call.duration | s | Histogram | Overall call duration including retries and time to send or receive request and response body. |
| client.call.attempts | {attempt} | MonotonicCounter | The number of attempts for an individual operation. |
| client.call.errors | {error} | MonotonicCounter | The number of errors for an operation. |
| client.call.attempt\_duration | s | Histogram | The time to connect to the service, send the request, and get back HTTP status code and headers (including time queued waiting to be sent). |
| client.call.resolve\_endpoint\_duration | s | Histogram | The time to resolve an endpoint (endpoint resolver, not DNS) for the request. |
| client.call.deserialization\_duration | s | Histogram | The time to deserialize a message body. |
| client.call.auth.signing\_duration | s | Histogram | The time to sign a request. |
| client.call.auth.resolve\_identity\_duration | s | Histogram | The time to acquire an identity (AWS credentials, bearer token, etc.) from an identity provider. |

 The following attributes (dimensions) are included with each metric where applicable:
+ `rpc.service` – The service name.
+ `rpc.method` – The operation name.
+ `exception.type` – The error type (included with `client.call.errors`).
+ `auth.scheme_id` – The authentication scheme (included with auth-related metrics).

### HTTP client metrics
<a name="http-client-metrics"></a>

 The SDK's HTTP client collects the following additional metrics related to the underlying HTTP connection lifecycle:

| Metric name | Unit | Type | Description |
| --- | --- | --- | --- |
| client.http.connections.acquire\_duration | s | Histogram | The time it takes a request to acquire a connection. |
| client.http.connections.dns\_lookup\_duration | s | Histogram | The time it takes to perform a DNS lookup. |
| client.http.connections.tls\_handshake\_duration | s | Histogram | The time it takes to perform a TLS handshake. |
| client.http.connections.usage | {connection} | UpDownCounter | The current state of connections in the pool. Uses a state dimension with a value of idle or acquired. |
| client.http.do\_request\_duration | s | Histogram | The total time spent performing the HTTP request. |
| client.http.time\_to\_first\_byte | s | Histogram | The time from sending the request to receiving the first response byte. |
