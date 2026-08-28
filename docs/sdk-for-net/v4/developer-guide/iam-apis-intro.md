---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/iam-apis-intro.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Accessing AWS Identity and Access Management (IAM) with the AWS SDK for .NET
<a name="iam-apis-intro"></a>

The AWS SDK for .NET supports [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/), which is a web service that enables AWS customers to manage users and user permissions in AWS.

An AWS Identity and Access Management (IAM) *user* is an entity that you create in AWS. The entity represents a person or application that interacts with AWS. For more information about IAM users, see [IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) and [IAM and STS Limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the IAM User Guide.

You grant permissions to a user by creating an IAM *policy*. The policy contains a *policy document* that lists the actions that a user can perform and the resources those actions can affect. For more information about IAM policies, see [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.

**Warning**
To avoid security risks, don't use IAM users for authentication when developing purpose-built software or working with real data. Instead, use federation with an identity provider such as [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).

## APIs
<a name="w2aac19c15c23c13"></a>

The AWS SDK for .NET provides APIs for IAM clients. The APIs enable you to work with IAM features such as users, roles, and access keys.

This section contains a small number of examples that show you the patterns you can follow when working with these APIs. To view the full set of APIs, see the [AWS SDK for .NET API Reference](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/) (and scroll to "Amazon.IdentityManagement").

This section also contains [an example](net-dg-hosm.md) that shows you how to attach an IAM role to Amazon EC2 instances to make managing credentials easier.

The IAM APIs are provided by the [AWSSDK.IdentityManagement](https://www.nuget.org/packages/AWSSDK.IdentityManagement) NuGet package.

## Prerequisites
<a name="w2aac19c15c23c15"></a>

Before you begin, be sure you have [set up your environment](net-dg-config.md) and [configured your project](configuring-the-sdk.md). Also review the information in [Using the SDK](net-dg-sdk-features.md).

## Topics
<a name="w2aac19c15c23c17"></a>

**Topics**
+ [APIs](#w2aac19c15c23c13)
+ [Prerequisites](#w2aac19c15c23c15)
+ [Topics](#w2aac19c15c23c17)
+ [Creating managed policies from JSON](iam-policies-create-json.md)
+ [Displaying policy documents](iam-policies-display.md)
+ [Granting access with a role](net-dg-hosm.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for .NET. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-net` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
