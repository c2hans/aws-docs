---
source_url: https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/whats-new.html
---

The AWS SDK for .NET V3 has reached end-of-support.

We recommend that you migrate to [AWS SDK for .NET V4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html). For additional details and information on how to migrate, please refer to our [end-of-support announcement](https://aws.amazon.com/blogs/developer/aws-sdk-for-net-v3-end-of-support-announcement/).

# What's new in the AWS SDK for .NET
<a name="whats-new"></a>

For high-level information about new developments related to the AWS SDK for .NET see the product page at [https://aws.amazon.com/sdk-for-net/](https://aws.amazon.com/sdk-for-net/) and the [SDK change logs](https://github.com/aws/aws-sdk-net/tree/aws-sdk-net-v3.7/changelogs).

The following is what's new in the AWS SDK for .NET.

**October 17, 2025: Version 2.0 of the AWS Deploy Tool**

Version 2.0 of the AWS Deploy Tool for .NET CLI has been released. For information about the Deploy Tool, see [Deploy applications to AWS](deploying.md). For information about version 2.0 of the Deploy Tool, see the blog post [What’s New in the AWS Deploy Tool for .NET](https://aws.amazon.com/blogs/developer/whats-new-in-the-aws-deploy-tool-for-net/).

**August 21, 2025: Upcoming end-of-support for version 3 of the AWS SDK for .NET**

The end-of-support for this version (V3) of the AWS SDK for .NET has been announced. See the [V4 migration guide](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html) to migrate your V3 applications and avoid disruptions. For more information, see the blog post [Announcing the end-of-support for the AWS SDK for .NET v3](https://aws.amazon.com/blogs/devops/announcing-the-end-of-support-for-the-aws-sdk-for-net-v3/).

**May 5, 2025: General availability of the AWS Message Processing Framework for .NET**

The [AWS Message Processing Framework for .NET](msg-proc-fw.md) is generally available\! The framework is an AWS-native framework that simplifies the development of .NET message-processing applications that use AWS services such as Amazon Simple Queue Service (SQS), Amazon Simple Notification Service (SNS), and Amazon EventBridge.

**April 28, 2025: Version 4 of the AWS SDK for .NET**

Version 4 of the AWS SDK for .NET is generally available\! For more information, see the [AWS SDK for .NET (V4) Developer Guide](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html), especially the topic for [Migrating to version 4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

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

**February 23, 2024: Added support for .NET 8**

Support for .NET 8 was added to the AWS SDK for .NET. Use the latest [NuGet packages](https://www.nuget.org/packages?q=awssdk) or the [assemblies that support .NET 8 and later](net-dg-obtain-assemblies.md#download-zip-files). You can find additional information about this support, including [support for Lambda](https://aws.amazon.com/blogs/compute/introducing-the-net-8-runtime-for-aws-lambda/) in the blog post [.NET 8 Support on AWS.](https://aws.amazon.com/blogs/dotnet/net-8-support-on-aws/)

**February 18, 2024: Upcoming changes to .NET Framework support**

Starting August 15th, 2024, the AWS SDK for .NET will end support for .NET Framework 3.5 and will change the minimum .NET Framework version to 4.7.2. For more information, see the blog post [Important changes coming for .NET Framework 3.5 and 4.5 targets of the AWS SDK for .NET](https://aws.amazon.com/blogs/developer/important-changes-coming-for-net-framework-3-5-and-4-5-targets-of-the-aws-sdk-for-net/).

**2023-07-17: The AWS Lambda Annotations framework has been released for general availability**

The [AWS Lambda Annotations framework](aws-lambda-annotations.md) makes the experience of writing Lambda functions in C\# feel more natural for .NET developers by using C\# source generator technology. It is now generally available.

**2023-07-15: The Distributed Cache Provider for DynamoDB has been released in preview**

The Distributed Cache Provider library enables Amazon DynamoDB to be used as the storage for ASP.NET Core's distributed cache framework. For more information, see the blog post [Introducing the AWS .NET Distributed Cache Provider for DynamoDB (Preview)](https://aws.amazon.com/blogs/developer/introducing-the-aws-net-distributed-cache-provider-for-dynamodb-preview/) and the [GitHub repository](https://github.com/awslabs/aws-dotnet-distributed-cache-provider).

**2022-07-13: The AWS Deploy Tool has been released**

The AWS Deploy Tool has been released. This tool is an interactive tooling for the .NET CLI and the AWS Toolkit for Visual Studio that helps deploy .NET applications with minimum AWS knowledge, and with the fewest clicks or commands. For more information, see [Deploy applications to AWS](deploying.md).

**2020-08-24: Version 3.5 of the SDK has been released**
+ Standardized the .NET experience by transitioning support for all non-Framework variations of the SDK to .NET Standard 2.0. See [Migrating to version 3.5](net-dg-v35.md) for more information.
+ Added paginators to many service clients, which make pagination of API results more convenient. For more information, see [Paginators](paginators.md).
