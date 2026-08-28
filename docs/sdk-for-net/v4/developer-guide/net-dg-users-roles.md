---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-users-roles.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Additional information about users and roles
<a name="net-dg-users-roles"></a>

For doing .NET development on AWS or for running .NET applications on AWS, you need to have some combination of users, permission sets, and service roles that are appropriate for these tasks.

The specific users, permission sets, and service roles that you create, and the way in which you use them, will depend on the requirements of your applications. The following is some additional information about why they might be used and how to create them.

## Users and permission sets
<a name="net-dg-users-roles-user"></a>

Although it's possible to use an IAM user account with long-term credentials to access AWS services, this is no longer a best practice and should be avoided. Even during development, it is a best practice to create users and permission sets in AWS IAM Identity Center and use temporary credentials provided by an identity source.

For development, you can use the user that you created or were given in [Authenticating with AWS](creds-idc.md). If you have appropriate AWS Management Console permissions, you can also create different permission sets with least privilege for that user or create new users specifically for development projects, providing permission sets with least privilege. The course of action you choose, if any, depends on your circumstances.

For more information about these users and permissions sets and how to create them, see [Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) in the *AWS SDKs and Tools Reference Guide* and [Getting started](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) in the *AWS IAM Identity Center User Guide*.

## Service roles
<a name="net-dg-users-roles-service-role"></a>

You can set up an AWS service role to access AWS services on behalf of users. This type of access is appropriate if multiple people will be running your application remotely; for example, on an Amazon EC2 instance that you have created for this purpose.

The process for creating a service role varies depending on the situation, but is essentially the following.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Choose **Roles**, and then choose **Create role**.

1. Choose **AWS service**, find and select **EC2** (for example), and then choose the **EC2** use case (for example).

1. Choose **Next: Permissions**, and select the [appropriate policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) for the AWS services that your application will use.
**Warning**
Do ***NOT*** choose the **AdministratorAccess** policy because that policy enables read and write permissions to almost everything in your account.

1. Choose **Next: Tags** and enter any tags you want.

   You can find information about tags in [Control access using AWS resource tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/).

1. Choose **Next: Review** and provide a **Role name** and **Role description**. Then choose **Create role**.

You can find high-level information about IAM roles in [Identities (users, groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/). Find detailed information about roles in that guide's [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) topic.

**Additional information about roles**
+ Use [IAM roles for tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) for Amazon Elastic Container Service (Amazon ECS) tasks.
+ Use [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) for applications that are running on Amazon EC2 instances.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for .NET. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-net` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
