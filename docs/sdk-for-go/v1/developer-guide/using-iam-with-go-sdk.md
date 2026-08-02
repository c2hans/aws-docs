---
source_url: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-iam-with-go-sdk.html
---

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs//developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# IAM Examples Using the AWS SDK for Go
<a name="using-iam-with-go-sdk"></a>

AWS Identity and Access Management (IAM) is a web service that enables AWS customers to manage users and user permissions in AWS. The service is targeted at organizations with multiple users or systems in the cloud that use AWS products. With IAM, you can centrally manage users, security credentials such as access keys, and permissions that control which AWS resources users can access.

The examples assume you have already set up and configured the SDK (that is, you’ve imported all required packages and set your credentials and region). For more information, see [Getting Started with the AWS SDK for Go](setting-up.md) and [Configuring the AWS SDK for Go](configuring-sdk.md).

You can download complete versions of these example files from the [aws-doc-sdk-examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/go/example_code/s3) repository on GitHub.

**Topics**
+ [Managing IAM Users](iam-example-managing-users.md)
+ [Managing IAM Access Keys](iam-example-managing-access-keys.md)
+ [Managing IAM Account Aliases](iam-example-account-aliases.md)
+ [Working with IAM Policies](iam-example-policies.md)
+ [Working with IAM Server Certificates](iam-example-server-certificates.md)
