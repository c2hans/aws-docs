---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/aspire-integrations.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for .NET. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-net` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
