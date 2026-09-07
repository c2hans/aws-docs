---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/observability.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Observability
<a name="observability"></a>

Observability is the extent to which a system's current state can be inferred from the data it emits. The data emitted is commonly referred to as telemetry.

The AWS SDK for .NET can provide two common telemetry signals, metrics and traces, as well as logging. You can wire up a [TelemetryProvider](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TTelemetryProvider.html) to send telemetry data to an observability backend (such as [AWS X-Ray](https://docs.aws.amazon.com/xray/?icmpid=docs_homepage_devtools) or [Amazon CloudWatch](https://docs.aws.amazon.com/cloudwatch/?icmpid=docs_homepage_mgmtgov)) and then act on it.

By default, telemetry signals are disabled in the SDK. This topic explains how to enable and configure telemetry output.

## Additional resources
<a name="observability-resources"></a>

For more information about enabling and using observability, see the following resources:
+ [OpenTelemetry](https://opentelemetry.io/)
+ The blog post [Enhancing Observability in the AWS SDK for .NET with OpenTelemetry](https://aws.amazon.com/blogs/developer/enhancing-observability-in-the-aws-sdk-for-net-with-opentelemetry/).
+ The blog post [Announcing the general availability of AWS .NET OpenTelemetry libraries](https://aws.amazon.com/blogs/dotnet/announcing-the-general-availability-of-aws-net-opentelemetry-libraries/).
+ [Exporters for OpenTelemetry](https://opentelemetry.io/docs/languages/net/exporters/)
+ For examples of observability in the AWS Tools for PowerShell, see [Observability](https://docs.aws.amazon.com/powershell/latest/userguide/observability.html) in the [Tools for PowerShell User Guide](https://docs.aws.amazon.com/powershell/latest/userguide/).

## Configure a `TelemetryProvider`
<a name="observability-conf-telemetry-provider"></a>

You can configure a `TelemetryProvider` in your application globally for all service clients or for individual clients, as shown in the following examples. The [Telemetry providers](observability-telemetry-providers.md) section contains information about telemetry implementations, including information about implementations that are provided with the SDK.

### Configure the default global telemetry provider
<a name="observability-conf-telemetry-provider-global"></a>

By default, every service client attempts to use the globally available telemetry provider. This way, you can set the provider once, and all clients will use it. This should be done only once, before you create any service clients.

The following code snippet shows you how to set the global telemetry provider. It then creates an Amazon S3 service client and tries to perform an operation that fails. The code adds both tracing and metrics to the application. This code uses the following NuGet packages: `OpenTelemetry.Exporter.Console` and `OpenTelemetry.Instrumentation.AWS`.

**Note**
If you're using AWS IAM Identity Center for authentication, be sure to also add `AWSSDK.SSO` and `AWSSDK.SSOOIDC`.

```
using Amazon.S3;
using OpenTelemetry;
using OpenTelemetry.Metrics;
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;

Sdk.CreateTracerProviderBuilder()
    .ConfigureResource(e => e.AddService("DemoOtel"))
    .AddAWSInstrumentation()
    .AddConsoleExporter()
    .Build();

Sdk.CreateMeterProviderBuilder()
    .ConfigureResource(e => e.AddService("DemoOtel"))
    .AddAWSInstrumentation()
    .AddConsoleExporter()
    .Build();

var s3Client = new AmazonS3Client();

try
{
    var listBucketsResponse = await s3Client.ListBucketsAsync();
    // Attempt to delete a bucket that doesn't exist.
    var deleteBucketResponse = await s3Client.DeleteBucketAsync("{{amzn-s3-demo-bucket}}");
}
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
}

Console.Read();
```

### Configure a telemetry provider for a specific service client
<a name="observability-conf-telemetry-provider-client"></a>

You can configure an individual service client with a specific telemetry provider (other than the global one). To do so, use the `TelemetryProvider` class of the Config object of a service client constructor. For example, see [AmazonS3Config](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TS3Config.html) and look for the `TelemetryProvider` property. See [Telemetry providers](observability-telemetry-providers.md) for information about custom telemetry implementations.

**Topics**
+ [Additional resources](#observability-resources)
+ [Configure a `TelemetryProvider`](#observability-conf-telemetry-provider)
+ [Metrics](observability-metrics.md)
+ [Telemetry providers](observability-telemetry-providers.md)
