---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_S3KnowledgeBaseParameters.html
---

# S3KnowledgeBaseParameters
<a name="API_S3KnowledgeBaseParameters"></a>

The parameters that are required to connect to an S3 knowledge base data source.

 **Prerequisites: Amazon S3 bucket access**

Before you call `CreateKnowledgeBase` for an Amazon S3 knowledge base, an administrator must grant Amazon QuickSight access to the source S3 bucket. If access has not been granted for the bucket, knowledge base creation fails.

To grant access, an administrator adds the bucket in the Amazon QuickSight admin console, under Permissions, AWS resources, Amazon S3, Select S3 buckets. This authorizes the Amazon QuickSight service role to read the bucket. The bucket can be in the same AWS account or, when the bucket owner has authorized your account, in a different account.

The service role requires at least the following permissions on the bucket:
+  `s3:GetObject`
+  `s3:ListBucket`
+  `s3:GetBucketLocation`
+  `s3:GetObjectVersion`
+  `s3:ListBucketVersions`

For the full procedure, including cross-account buckets and AWS KMS-encrypted buckets, see the Amazon S3 knowledge base administrator setup guide.

**Note**
To grant access for a specific S3 knowledge base data source without granting account-wide S3 access, provide a custom IAM role on the data source by using `RoleArn`.

## Contents
<a name="API_S3KnowledgeBaseParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BucketUrl **   <a name="QS-Type-S3KnowledgeBaseParameters-BucketUrl"></a>
The URL of the S3 bucket that contains the knowledge base data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** MetadataFilesLocation **   <a name="QS-Type-S3KnowledgeBaseParameters-MetadataFilesLocation"></a>
The Amazon S3 location (prefix) of per-document metadata files. Each metadata file describes a single source document and its indexable attributes, such as title, category, and version. This is not the global ACL configuration file. To apply a single global ACL file to the entire knowledge base, use the access control configuration instead.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** RoleArn **   <a name="QS-Type-S3KnowledgeBaseParameters-RoleArn"></a>
Use the `RoleArn` structure to override an account-wide role for a specific S3 Knowledge Base data source. For example, say an account administrator has turned off all S3 access with an account-wide role. The administrator can then use `RoleArn` to bypass the account-wide role and allow S3 access for the single S3 Knowledge Base data source that is specified in the structure, even if the account-wide role forbidding S3 access is still active.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## See Also
<a name="API_S3KnowledgeBaseParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/S3KnowledgeBaseParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/S3KnowledgeBaseParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/S3KnowledgeBaseParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
