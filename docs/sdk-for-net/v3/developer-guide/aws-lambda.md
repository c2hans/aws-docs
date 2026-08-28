---
source_url: https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/aws-lambda.html
---

The AWS SDK for .NET V3 has reached end-of-support.

We recommend that you migrate to [AWS SDK for .NET V4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html). For additional details and information on how to migrate, please refer to our [end-of-support announcement](https://aws.amazon.com/blogs/developer/aws-sdk-for-net-v3-end-of-support-announcement/).

# Using AWS Lambda for compute service
<a name="aws-lambda"></a>

The AWS SDK for .NET supports AWS Lambda, which lets you run code without provisioning or managing servers. For more information, see the [AWS Lambda product page](https://aws.amazon.com/lambda/) and the [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/), particularly the section for [Working with C\#](https://docs.aws.amazon.com/lambda/latest/dg/lambda-csharp.html).

## APIs
<a name="w2aac19c17b5"></a>

The AWS SDK for .NET provides APIs for AWS Lambda. The APIs enable you to work with Lambda features such as [functions](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html#gettingstarted-concepts-function), [triggers](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html#gettingstarted-concepts-trigger), and [events](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html#gettingstarted-concepts-event). To view the full set of APIs, see [Lambda](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Lambda/NLambda.html) in the [AWS SDK for .NET API Reference](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/).

The Lambda APIs are provided by [NuGet packages](https://www.nuget.org/packages?page=2&q=aws%20lambda&sortBy=relevance).

## Prerequisites
<a name="w2aac19c17b7"></a>

Before you begin, be sure you have [set up your environment and project](net-dg-config.md). Also review the information in [SDK features](net-dg-sdk-features.md).

## Additional information
<a name="w2aac19c17b9"></a>

See [Integrating AWS with .NET Aspire](aspire-integrations.md) for information about developing with AWS Lambda through .NET Aspire.

## Topics
<a name="w2aac19c17c11"></a>

**Topics**
+ [APIs](#w2aac19c17b5)
+ [Prerequisites](#w2aac19c17b7)
+ [Additional information](#w2aac19c17b9)
+ [Topics](#w2aac19c17c11)
+ [Lambda Annotations](aws-lambda-annotations.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for .NET. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-net` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
