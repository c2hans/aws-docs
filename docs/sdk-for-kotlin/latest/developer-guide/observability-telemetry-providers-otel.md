---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/observability-telemetry-providers-otel.html
---

# Configure the OpenTelemetry-based telemetry provider
<a name="observability-telemetry-providers-otel"></a>

The SDK for Kotlin provides an implementation of the [`TelemetryProvider`](/smithy-kotlin/api/latest/telemetry-api/aws.smithy.kotlin.runtime.telemetry/-telemetry-provider/index.html) interface backed by OpenTelemetry.

## Prerequisites
<a name="observability-telemetry-providers-otel-prereqs"></a>

Update your project dependencies to add the OpenTelemetry provider as shown in the following Gradle snippet. Replace {{X.Y.Z}} with the version you’re using in your app or with the latest version available ([smithy-kotlin](https://github.com/smithy-lang/smithy-kotlin/releases/latest), [opentelemetry-instrumentation-bom](https://search.maven.org/#search|gav|1|g:io.opentelemetry.instrumentation%20AND%20a:opentelemetry-instrumentation-bom)).

```
dependencies {
    implementation(platform("aws.smithy.kotlin:bom:{{X.Y.Z}}"))
    implementation(platform("io.opentelemetry.instrumentation:opentelemetry-instrumentation-bom:{{X.Y.Z}}"))
    implementation("aws.smithy.kotlin:telemetry-provider-otel")

    // OPTIONAL: If you use log4j, the following entry enables the ability to export logs through OTel.
    runtimeOnly("io.opentelemetry.instrumentation:opentelemetry-log4j-appender-2.17")
}
```

## Configure the SDK
<a name="observability-telemetry-providers-otel-conf"></a>

The following code configures a service client by using the OpenTelemetry telemetry provider.

```
import aws.sdk.kotlin.services.s3.S3Client
import aws.smithy.kotlin.runtime.telemetry.otel.OpenTelemetryProvider
import io.opentelemetry.api.GlobalOpenTelemetry
import kotlinx.coroutines.runBlocking

fun main() = runBlocking {
    val otelProvider = OpenTelemetryProvider(GlobalOpenTelemetry.get())

    S3Client.fromEnvironment().use { s3 ->
        telemetryProvider = otelProvider
        …
    }
}
```

**Note**
A discussion of how to configure the OpenTelemetry SDK is outside of the scope of this guide. The [OpenTelemetry Java documentation](https://opentelemetry.io/docs/instrumentation/java/) contains configuration information on the various approaches: [manually](https://opentelemetry.io/docs/instrumentation/java/manual/), automatically through the [Java agent](https://opentelemetry.io/docs/instrumentation/java/automatic/), or the (optional) [collector](https://opentelemetry.io/docs/collector/).

## Resources
<a name="observability-telemetry-providers-otel-res"></a>

The following resources are available to help you get started with OpenTelemetry.
+  [AWS Distro for OpenTelemetry](https://aws-otel.github.io/docs/introduction) - AWS OTeL Distro homepage
+  [aws-otel-java-instrumentation](https://github.com/aws-observability/aws-otel-java-instrumentation) - AWS Distro for OpenTelemetry Java Instrumentation Library
+  [aws-otel-lambda](https://github.com/aws-observability/aws-otel-lambda) - AWS managed OpenTelemetry Lambda layers
+  [aws-otel-collector](https://github.com/aws-observability/aws-otel-collector) - AWS Distro for OpenTelemetry Collector
+  [AWS Observability Best Practices](https://aws-observability.github.io/observability-best-practices/) - General best practices for observability specific to AWS

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
