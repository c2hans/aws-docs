---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/cloudformation-apis-intro.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Accessing CloudFormation with the AWS SDK for .NET
<a name="cloudformation-apis-intro"></a>

The AWS SDK for .NET supports [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/), which creates and provisions AWS infrastructure deployments predictably and repeatedly.

## APIs
<a name="w2aac19c15c15b5"></a>

The AWS SDK for .NET provides APIs for CloudFormation clients. The APIs enable you to work with CloudFormation features such as templates and stacks. This section contains a small number of examples that show you the patterns you can follow when working with these APIs. To view the full set of APIs, see the [AWS SDK for .NET API Reference](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/) (and scroll to "Amazon.CloudFormation").

The AWS CloudFormation APIs are provided by the [AWSSDK.CloudFormation](https://www.nuget.org/packages/AWSSDK.CloudFormation/) package.

## Prerequisites
<a name="w2aac19c15c15b7"></a>

Before you begin, be sure you have [set up your environment](net-dg-config.md) and [configured your project](configuring-the-sdk.md). Also review the information in [Using the SDK](net-dg-sdk-features.md).

## Topics
<a name="w2aac19c15c15b9"></a>

**Topics**
+ [APIs](#w2aac19c15c15b5)
+ [Prerequisites](#w2aac19c15c15b7)
+ [Topics](#w2aac19c15c15b9)
+ [Listing AWS resources](cfn-list-resources.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for .NET. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-net` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
