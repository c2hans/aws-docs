---
source_url: https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/aspire-integrations.html
---

The AWS SDK for .NET V3 has reached end-of-support.

We recommend that you migrate to [AWS SDK for .NET V4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html). For additional details and information on how to migrate, please refer to our [end-of-support announcement](https://aws.amazon.com/blogs/developer/aws-sdk-for-net-v3-end-of-support-announcement/).

# Integrating AWS with .NET Aspire in the AWS SDK for .NET
<a name="aspire-integrations"></a>

.NET Aspire is a new way of building cloud-ready applications. In particular, it provides an orchestration for local environments in which to run, connect, and debug the components of distributed applications. To improve the inner dev loop for cloud ready applications, integrations with .NET Aspire have been created for connecting your .NET applications to AWS resources. These integrations are available through the [Aspire.Hosting.AWS](https://www.nuget.org/packages/Aspire.Hosting.AWS) NuGet package.

The following .NET Aspire integrations are available:
+ The ability to provision your AWS resources through [CloudFormation](https://aws.amazon.com/cloudformation/). This integration is utilized within the .NET Aspire AppHost project.

  For more information, see the blog post [Integrating AWS with .NET Aspire](https://aws.amazon.com/blogs/developer/integrating-aws-with-net-aspire/).
+ Installing, configuring, and connecting the AWS SDK for .NET to [Amazon DynamoDB local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html). This integration is utilized within the .NET Aspire AppHost project.

  For more information, see the blog post [Integrating AWS with .NET Aspire](https://aws.amazon.com/blogs/developer/integrating-aws-with-net-aspire/).
+ Enable a local development environment for [AWS Lambda](https://aws.amazon.com/lambda/) functions. This integration is utilized within the .NET Aspire AppHost project.

  For more information, see the blog posts [Building and Debugging .NET Lambda applications with .NET Aspire (Part 1)](https://aws.amazon.com/blogs/developer/building-lambda-with-aspire-part-1/) and [Building and Debugging .NET Lambda applications with .NET Aspire (Part 2)](https://aws.amazon.com/blogs/developer/building-lambda-with-aspire-part-2/).
**Note**
This is prerelease documentation for a feature in preview release. It is subject to change.

  Because this feature is in preview, you will need to opt-in for preview features. For additional information about this preview feature and how to opt-in, see the [development tracker issue on GitHub](https://github.com/aws/integrations-on-dotnet-aspire-for-aws/issues/17).

## Additional information
<a name="aspire-integrations-additional"></a>

For additional information and details about how you can use the integrations that are available in [Aspire.Hosting.AWS](https://www.nuget.org/packages/Aspire.Hosting.AWS), see the following resources.
+ Blog post [Integrating AWS with .NET Aspire](https://aws.amazon.com/blogs/developer/integrating-aws-with-net-aspire/).
+ Blog posts [Building and Debugging .NET Lambda applications with .NET Aspire (Part 1)](https://aws.amazon.com/blogs/developer/building-lambda-with-aspire-part-1/) and [Building and Debugging .NET Lambda applications with .NET Aspire (Part 2)](https://aws.amazon.com/blogs/developer/building-lambda-with-aspire-part-2/).
+ The [integrations-on-dotnet-aspire-for-aws](https://github.com/aws/integrations-on-dotnet-aspire-for-aws) repo on GitHub.
+ The detailed [README](https://github.com/aws/integrations-on-dotnet-aspire-for-aws/blob/main/src/Aspire.Hosting.AWS/README.md) for the [Aspire.Hosting.AWS](https://www.nuget.org/packages/Aspire.Hosting.AWS) NuGet package.
