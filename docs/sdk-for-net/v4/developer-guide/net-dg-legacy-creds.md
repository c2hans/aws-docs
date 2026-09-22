---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-legacy-creds.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Using legacy credentials
<a name="net-dg-legacy-creds"></a>

The topics in this section provide information about using long-term or short-term credentials without using AWS IAM Identity Center.

**Warning**
To avoid security risks, don't use IAM users for authentication when developing purpose-built software or working with real data. Instead, use federation with an identity provider such as [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).

**Note**
The information in this topic is for circumstances where you need to obtain and manage short-term or long-term credentials manually. For additional information about short-term and long-term credentials, see [Other ways to authenticate](https://docs.aws.amazon.com/sdkref/latest/guide/access-users.html) in the *AWS SDKs and Tools Reference Guide*.
For best security practices, use AWS IAM Identity Center, as described in [Authenticating with AWS](creds-idc.md).

## Important warnings and guidance for credentials
<a name="net-dg-config-creds-warnings-and-guidelines"></a>

**Warnings for credentials**
+ ***Do NOT*** use your account's root credentials to access AWS resources. These credentials provide unrestricted account access and are difficult to revoke.
+ ***Do NOT*** put literal access keys or credential information in your application files. If you do, you create a risk of accidentally exposing your credentials if, for example, you upload the project to a public repository.
+ ***Do NOT*** include files that contain credentials in your project area.
+ Be aware that any credentials stored in the shared AWS `credentials` file, are stored in plaintext.

**Additional guidance for securely managing credentials**

For a general discussion of how to securely manage AWS credentials, see [AWS security credentials](https://docs.aws.amazon.com/general/latest/gr/Welcome.html#aws-security-credentials) in the [AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/) and [Security best practices and use cases](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPracticesAndUseCases.html) in the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/). In addition to those discussions, consider the following:
+ Create additional users, such as users in IAM Identity Center, and use their credentials instead of using your AWS root user credentials. Credentials for other users can be revoked if necessary or are temporary by nature. In addition, you can apply a policy to each user for access to only certain resources and actions and thereby take a stance of least-privilege permissions.
+ Use [IAM roles for tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) for Amazon Elastic Container Service (Amazon ECS) tasks.
+ Use [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) for applications that are running on Amazon EC2 instances.
+ Use [temporary credentials](creds-assign.md#net-dg-config-creds-assign-role) or environment variables for applications that are available to users outside your organization.

**Topics**
+ [Important warnings and guidance for credentials](#net-dg-config-creds-warnings-and-guidelines)
+ [Shared AWS credentials file](creds-file.md)
+ [SDK Store (Windows only)](sdk-store.md)
