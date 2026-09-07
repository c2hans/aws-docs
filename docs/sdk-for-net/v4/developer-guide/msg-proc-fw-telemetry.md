---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/msg-proc-fw-telemetry.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Logging and Open Telemetry for the AWS Message Processing Framework for .NET
<a name="msg-proc-fw-telemetry"></a>

The AWS Message Processing Framework for .NET is instrumented for OpenTelemetry to log [traces](https://opentelemetry.io/docs/concepts/signals/traces/) for each message that is published or handled by the framework. This is provided by the [`AWS.Messaging.Telemetry.OpenTelemetry`](https://www.nuget.org/packages/AWS.Messaging.Telemetry.OpenTelemetry) package. Refer to its [README](https://github.com/aws/aws-dotnet-messaging/blob/main/src/AWS.Messaging.Telemetry.OpenTelemetry/README.md) to get started.

**Note**
For security information related to logging, see [Security for the AWS Message Processing Framework for .NET](msg-proc-fw-security.md).
