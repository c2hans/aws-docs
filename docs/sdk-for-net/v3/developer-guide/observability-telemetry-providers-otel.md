---
source_url: https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/observability-telemetry-providers-otel.html
---

The AWS SDK for .NET V3 has reached end-of-support.

We recommend that you migrate to [AWS SDK for .NET V4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html). For additional details and information on how to migrate, please refer to our [end-of-support announcement](https://aws.amazon.com/blogs/developer/aws-sdk-for-net-v3-end-of-support-announcement/).

# Configure the OpenTelemetry-based telemetry provider
<a name="observability-telemetry-providers-otel"></a>

The AWS SDK for .NET includes an implementation of an OpenTelemetry-based telemetry provider. For details about how to set this provider as the global telemetry provider, see [Configure a `TelemetryProvider`](observability.md#observability-conf-telemetry-provider). To use this telemetry provider, you need the following resources in your project:
+ The [OpenTelemetry.Instrumentation.AWS](https://www.nuget.org/packages/OpenTelemetry.Instrumentation.AWS) NuGet package.
+ A telemetry exporter such as OTLP or Console. For more information, see [Exporters](https://opentelemetry.io/docs/languages/net/exporters/) in the OpenTelemetry documentation.

The OpenTelemetry implementation included with the SDK can be configured to reduce the amount of tracing for HTTPS requests, credentials, and compression. To do so, set the `SuppressDownstreamInstrumentation` option to `true`, similar to the following:

```
Sdk.CreateTracerProviderBuilder()
    .ConfigureResource(e => e.AddService("DemoOtel"))
    .AddAWSInstrumentation(options => options.SuppressDownstreamInstrumentation = true)
    .AddConsoleExporter()
    .Build();
```

For additional information about this provider, see the blog post [Enhancing Observability in the AWS SDK for .NET with OpenTelemetry](https://aws.amazon.com/blogs/developer/enhancing-observability-in-the-aws-sdk-for-net-with-opentelemetry/).
