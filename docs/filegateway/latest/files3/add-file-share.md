---
source_url: https://docs.aws.amazon.com/filegateway/latest/files3/add-file-share.html
---

# Granting access and permissions for file shares and buckets
<a name="add-file-share"></a>

After your S3 File Gateway is activated and running, you can add additional file shares and grant access to Amazon S3 buckets, including buckets in different AWS accounts than your gateways and file shares. The following sections describe how to use IAM roles to provide your gateway with access permissions for Amazon S3 buckets and VPC endpoints, prevent certain security issues, and connect file shares to buckets across AWS accounts.

For information about how to create a new file share, see [Creating a file share](GettingStartedCreateFileShare.md).

This section contains the following topics, which provide additional information about how to grant access and permissions for file shares and Amazon S3 buckets:

**Topics**
+ [Granting access to an Amazon S3 bucket](grant-access-s3.md) - Learn how to grant access for your File Gateway to upload files into your Amazon S3 bucket, and to perform actions on any access points or Amazon Virtual Private Cloud (Amazon VPC) endpoints that it uses to connect to the bucket.
+ [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md) - Learn how to prevent a common security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
+ [Using a file share for cross-account access](cross-account-access.md) - Learn how to grant access for an Amazon Web Services account and users of that account to access resources that belong to another Amazon Web Services account.

**Note**
If your File Gateway uses SSE-KMS or DSSE-KMS for encryption, make sure the IAM role associated with the file share includes *kms:Encrypt*, *kms:Decrypt*, *kms:ReEncrypt\**, *kms:GenerateDataKey*, and *kms:DescribeKey* permissions. For more information, see [Using Identity-Based Policies (IAM Policies) for Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/using-identity-based-policies.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query filegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
