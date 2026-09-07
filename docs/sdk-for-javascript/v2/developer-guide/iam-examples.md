---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/iam-examples.html
---

The AWS SDK for JavaScript v2 has reached end-of-support. We recommend that you migrate to [AWS SDK for JavaScript v3](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-javascript-v2/).

# AWS IAM Examples
<a name="iam-examples"></a>

AWS Identity and Access Management (IAM) is a web service that enables Amazon Web Services customers to manage users and user permissions in AWS. The service is targeted at organizations with multiple users or systems in the cloud that use AWS products. With IAM, you can centrally manage users, security credentials such as access keys, and permissions that control which AWS resources users can access.

![Relationship between JavaScript environments, the SDK, and IAM](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/images/code-samples-iam.png)

The JavaScript API for IAM is exposed through the `AWS.IAM` client class. For more information about using the IAM client class, see [`Class: AWS.IAM`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/IAM.html) in the API reference.

**Topics**
+ [Managing IAM Users](iam-examples-managing-users.md)
+ [Working with IAM Policies](iam-examples-policies.md)
+ [Managing IAM Access Keys](iam-examples-managing-access-keys.md)
+ [Working with IAM Server Certificates](iam-examples-server-certificates.md)
+ [Managing IAM Account Aliases](iam-examples-account-aliases.md)
