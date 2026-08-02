---
source_url: https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/cloudformation-apis-intro.html
---

The AWS SDK for .NET V3 has reached end-of-support.

We recommend that you migrate to [AWS SDK for .NET V4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html). For additional details and information on how to migrate, please refer to our [end-of-support announcement](https://aws.amazon.com/blogs/developer/aws-sdk-for-net-v3-end-of-support-announcement/).

# Accessing CloudFormation with the AWS SDK for .NET
<a name="cloudformation-apis-intro"></a>

The AWS SDK for .NET supports [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/), which creates and provisions AWS infrastructure deployments predictably and repeatedly.

## APIs
<a name="w2aac19c15c11b5"></a>

The AWS SDK for .NET provides APIs for CloudFormation clients. The APIs enable you to work with CloudFormation features such as templates and stacks. This section contains a small number of examples that show you the patterns you can follow when working with these APIs. To view the full set of APIs, see the [AWS SDK for .NET API Reference](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/) (and scroll to "Amazon.CloudFormation").

The AWS CloudFormation APIs are provided by the [AWSSDK.CloudFormation](https://www.nuget.org/packages/AWSSDK.CloudFormation/) package.

## Prerequisites
<a name="w2aac19c15c11b7"></a>

Before you begin, be sure you have [set up your environment and project](net-dg-config.md). Also review the information in [SDK features](net-dg-sdk-features.md).

## Topics
<a name="w2aac19c15c11b9"></a>

**Topics**
+ [APIs](#w2aac19c15c11b5)
+ [Prerequisites](#w2aac19c15c11b7)
+ [Topics](#w2aac19c15c11b9)
+ [Listing AWS resources](cfn-list-resources.md)
