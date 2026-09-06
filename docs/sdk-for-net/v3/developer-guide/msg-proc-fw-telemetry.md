---
source_url: https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/msg-proc-fw-telemetry.html
---

The AWS SDK for .NET V3 has reached end-of-support.

We recommend that you migrate to [AWS SDK for .NET V4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html). For additional details and information on how to migrate, please refer to our [end-of-support announcement](https://aws.amazon.com/blogs/developer/aws-sdk-for-net-v3-end-of-support-announcement/).

# Logging and Open Telemetry for the AWS Message Processing Framework for .NET
<a name="msg-proc-fw-telemetry"></a>

The AWS Message Processing Framework for .NET is instrumented for OpenTelemetry to log [traces](https://opentelemetry.io/docs/concepts/signals/traces/) for each message that is published or handled by the framework. This is provided by the [`AWS.Messaging.Telemetry.OpenTelemetry`](https://www.nuget.org/packages/AWS.Messaging.Telemetry.OpenTelemetry) package. Refer to its [README](https://github.com/aws/aws-dotnet-messaging/blob/main/src/AWS.Messaging.Telemetry.OpenTelemetry/README.md) to get started.

**Note**
For security information related to logging, see [Security for the AWS Message Processing Framework for .NET](msg-proc-fw-security.md).
