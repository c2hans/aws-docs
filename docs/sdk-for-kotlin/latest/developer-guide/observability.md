---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/observability.html
---

# Observability
<a name="observability"></a>

Observability is the extent to which a system’s current state can be inferred from the data it emits. The data emitted is commonly referred to as telemetry.

The AWS SDK for Kotlin can provide all three common telemetry signals: metrics, traces, and logs. You can wire up a [TelemetryProvider](/smithy-kotlin/api/latest/telemetry-api/aws.smithy.kotlin.runtime.telemetry/-telemetry-provider/index.html) to send telemetry data to an observability backend (such as [AWS X-Ray](/xray/?icmpid=docs_homepage_devtools) or [Amazon CloudWatch](/cloudwatch/?icmpid=docs_homepage_mgmtgov)) and then act on it.

By default, only logging is enabled and other telemetry signals are disabled in the SDK. This topic explains how to enable and configure telemetry output.

## Configure a `TelemetryProvider`
<a name="observability-conf-telemetry-provider"></a>

You can configure a [`TelemetryProvider`](/smithy-kotlin/api/latest/telemetry-api/aws.smithy.kotlin.runtime.telemetry/-telemetry-provider/index.html) in your application globally for all service clients or for individual clients. The following examples use a hypothetical `getConfiguredProvider()` function to demonstrate the [`TelemetryProvider`](/smithy-kotlin/api/latest/telemetry-api/aws.smithy.kotlin.runtime.telemetry/-telemetry-provider/index.html) API operations. The [Telemetry providers](observability-telemetry-providers.md) section describes information for implementations provided by the SDK. If a provider isn’t supported, you can implement your own support or [open a feature request on GitHub](https://github.com/awslabs/aws-sdk-kotlin/issues/new/choose).

### Configure the default global telemetry provider
<a name="observability-conf-telemetry-provider-global"></a>

By default, every service client attempts to use the globally available telemetry provider. This way, you can set the provider once, and all clients will use it. This should be done only once, before you instantiate any service clients.

To use the global telemetry provider, first update your project dependencies to add the telemetry defaults module as shown in the following Gradle snippet.

Replace {{X.Y.Z}} with the version you’re using in your app or with the [latest version available](https://github.com/smithy-lang/smithy-kotlin/releases/latest).

```
dependencies {
    implementation(platform("aws.smithy.kotlin:bom:{{X.Y.Z}}"))
    implementation("aws.smithy.kotlin:telemetry-defaults")
    ...
}
```

Then set the global telemetry provider before creating a service client as shown in the following code.

```
import aws.sdk.kotlin.services.s3.S3Client
import aws.smithy.kotlin.runtime.telemetry.GlobalTelemetryProvider
import kotlinx.coroutines.runBlocking

fun main() = runBlocking {
    val myTelemetryProvider = getConfiguredProvider()
    GlobalTelemetryProvider.set(myTelemetryProvider)

    S3Client.fromEnvironment().use { s3 ->
        …
    }
}

fun getConfiguredProvider(): TelemetryProvider {
    TODO("TODO - configure a provider")
}
```

### Configure a telemetry provider for a specific service client
<a name="observability-conf-telemetry-provider-client"></a>

You can configure an individual service client with a specific telemetry provider (other than the global one). This is shown in the following example.

```
import aws.sdk.kotlin.services.s3.S3Client
import kotlinx.coroutines.runBlocking

fun main() = runBlocking {
    S3Client.fromEnvironment{
        telemetryProvider = getConfiguredProvider()
    }.use { s3 ->
        ...
    }
}

fun getConfiguredProvider(): TelemetryProvider {
    TODO("TODO - configure a provider")
}
```
