---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/msg-proc-fw.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# AWS Message Processing Framework for .NET
<a name="msg-proc-fw"></a>

The AWS Message Processing Framework for .NET is an AWS-native framework that simplifies the development of .NET message processing applications that use AWS services such as Amazon Simple Queue Service (SQS), Amazon Simple Notification Service (SNS), and Amazon EventBridge. The framework reduces the amount of boiler-plate code developers need to write, allowing you to focus on your business logic when publishing and consuming messages. For details about how the framework can simplify your development, see the blog post [Introducing the AWS Message Processing Framework for .NET (Preview)](https://aws.amazon.com/blogs/developer/introducing-the-aws-message-processing-framework-for-net-preview/). The first part in particular provides a demonstration that shows the difference between using low-level API calls and using the framework.

The Message Processing Framework supports the following activities and features:
+ Sending messages to SQS and publishing events to SNS and EventBridge.
+ Receiving and handling messages from SQS by using a long-running poller, which is typically used in background services. This includes managing the visibility timeout while a message is being handled to prevent other clients from processing it.
+ Handling messages in AWS Lambda functions.
+ FIFO (first-in-first-out) SQS queues and SNS topics.
+ OpenTelemetry for logging.

For details about these activities and features see the **Features** section of the [blog post](https://aws.amazon.com/blogs/developer/introducing-the-aws-message-processing-framework-for-net-preview/) and the topics listed below.

Before you begin, be sure you have [set up your environment](net-dg-config.md) and [configured your project](configuring-the-sdk.md). Also review the information in [Using the SDK](net-dg-sdk-features.md).

**Additional resources**
+ The [`AWS.Messaging`](https://www.nuget.org/packages/AWS.Messaging/) package on [NuGet.org](https://www.nuget.org/).
+ The [API reference](https://aws.github.io/aws-dotnet-messaging/).
+ The `README` file in the GitHub repo at [https://github.com/aws/aws-dotnet-messaging/](https://github.com/aws/aws-dotnet-messaging/)
+ [.NET dependency injection](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection) from Microsoft.
+ [.NET Generic Host](https://learn.microsoft.com/en-us/dotnet/core/extensions/generic-host) from Microsoft.

**Topics**
+ [Get started](msg-proc-fw-get-started.md)
+ [Publish messages](msg-proc-fw-publish.md)
+ [Consume messages](msg-proc-fw-consume.md)
+ [FIFO](msg-proc-fw-fifo.md)
+ [Logging and Open Telemetry](msg-proc-fw-telemetry.md)
+ [Customize](msg-proc-fw-customize.md)
+ [Security](msg-proc-fw-security.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for .NET. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-net` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
