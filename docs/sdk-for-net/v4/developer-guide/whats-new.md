---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/whats-new.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# What's new in the AWS SDK for .NET
<a name="whats-new"></a>

For high-level information about new developments related to the AWS SDK for .NET, see the product page at [https://aws.amazon.com/sdk-for-net/](https://aws.amazon.com/sdk-for-net/) and the [SDK change logs](https://github.com/aws/aws-sdk-net/tree/main/changelogs).

The following is what's new in the AWS SDK for .NET.

**October 17, 2025: Version 2.0 of the AWS Deploy Tool**

Version 2.0 of the AWS Deploy Tool for .NET CLI has been released. For information about the Deploy Tool, see [Deploy applications to AWS](deploying.md). For information about version 2.0 of the Deploy Tool, see the blog post [What’s New in the AWS Deploy Tool for .NET](https://aws.amazon.com/blogs/developer/whats-new-in-the-aws-deploy-tool-for-net/).

**August 21, 2025: Upcoming end-of-support for version 3 of the AWS SDK for .NET**

The end-of-support for version 3 (V3) of the AWS SDK for .NET has been announced. See the [migration guide](net-dg-v4.md) to migrate your V3 applications and avoid disruptions. For more information, see the blog post [Announcing the end-of-support for the AWS SDK for .NET v3](https://aws.amazon.com/blogs/devops/announcing-the-end-of-support-for-the-aws-sdk-for-net-v3/).

**July 2, 2025: General availability of the Distributed Cache Provider**

The AWS .NET Distributed Cache Provider for Amazon DynamoDB is generally available\! This provider implements the ASP.NET Core [IDistributedCache](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/distributed?view=aspnetcore-9.0#idistributedcache-interface) interface, letting you integrate the fully managed and durable infrastructure of DynamoDB into your caching layer with minimal code changes. The Distributed Cache Provider is available through the [AWS.AspNetCore.DistributedCacheProvider](https://www.nuget.org/packages/AWS.AspNetCore.DistributedCacheProvider) package on NuGet. For additional information, see the blog post [AWS .NET Distributed Cache Provider for Amazon DynamoDB now Generally Available](https://aws.amazon.com/blogs/developer/aws-net-distributed-cache-provider-for-amazon-dynamodb-now-generally-available/).

**Note**
The released version of the Distributed Cache Provider is supported only on V4 of the AWS SDK for .NET. If you tried the preview version of the Distributed Cache Provider, you might need to update package dependencies in your application.

**May 5, 2025: General availability of the AWS Message Processing Framework for .NET**

The [AWS Message Processing Framework for .NET](msg-proc-fw.md) is generally available\! The framework is an AWS-native framework that simplifies the development of .NET message-processing applications that use AWS services such as Amazon Simple Queue Service (SQS), Amazon Simple Notification Service (SNS), and Amazon EventBridge.

**April 28, 2025: Version 4 of the AWS SDK for .NET**

Version 4 of the AWS SDK for .NET is generally available\! For information about migrating your applications to V4, see [Migrating to version 4](net-dg-v4.md). Also see the blog post [General Availability of AWS SDK for .NET V4.0](https://aws.amazon.com/blogs/developer/general-availability-of-aws-sdk-for-net-v4-0/) that announces general availability.

**February 15, 2025: Integrations with .NET Aspire**

Integrations with .NET Aspire to improve the inner dev loop have been released. For information, see [Integrating AWS with .NET Aspire in the AWS SDK for .NET](aspire-integrations.md).

**February 10, 2025: GA release for observability**

Observability is the extent to which a system's current state can be inferred from the data it emits. Observability has been added to the AWS SDK for .NET, including an implementation of a telemetry provider. For more information, see [Observability](observability.md) in this guide and the blog post [Announcing the general availability of AWS .NET OpenTelemetry libraries](https://aws.amazon.com/blogs/dotnet/announcing-the-general-availability-of-aws-net-opentelemetry-libraries/).

**January 15, 2025: New default behavior for integrity protection**

Beginning with version 3.7.412.0 of the AWS SDK for .NET, the SDK provides default integrity protections by automatically calculating a `CRC32` checksum for uploads. For more information, see the announcement on GitHub at [https://github.com/aws/aws-sdk-net/issues/3610](https://github.com/aws/aws-sdk-net/issues/3610). The SDK also provides global settings for data integrity protections that you can set externally, which you can read about in [Data Integrity Protections](https://docs.aws.amazon.com/sdkref/latest/guide/feature-dataintegrity.html) in the [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/).

**November 15, 2024: Blog post for preview 4 release for version 4**

Preview 4 of the AWS SDK for .NET Version 4 was released on November 15, 2024. For more information about this preview, see the blog post [Preview 4 of AWS SDK for .NET V4](https://aws.amazon.com/blogs/developer/preview-4-of-aws-sdk-for-net-v4/).

**August 16, 2024: Blog post for preview 1 release for version 4**

The AWS SDK for .NET Version 4 was released as a first preview on August 16, 2024. For more information about this preview, see the blog post [Preview 1 of AWS SDK for .NET V4](https://aws.amazon.com/blogs/developer/preview-1-of-aws-sdk-for-net-v4/).
