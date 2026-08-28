---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableSummary.html
---

# TableSummary
<a name="API_s3Buckets_TableSummary"></a>

Contains details about a table.

## Contents
<a name="API_s3Buckets_TableSummary_Contents"></a>

 ** createdAt **   <a name="AmazonS3-Type-s3Buckets_TableSummary-createdAt"></a>
The date and time the table was created at.
Type: Timestamp
Required: Yes

 ** modifiedAt **   <a name="AmazonS3-Type-s3Buckets_TableSummary-modifiedAt"></a>
The date and time the table was last modified at.
Type: Timestamp
Required: Yes

 ** name **   <a name="AmazonS3-Type-s3Buckets_TableSummary-name"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`
Required: Yes

 ** namespace **   <a name="AmazonS3-Type-s3Buckets_TableSummary-namespace"></a>
The name of the namespace.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`
Required: Yes

 ** tableARN **   <a name="AmazonS3-Type-s3Buckets_TableSummary-tableARN"></a>
The Amazon Resource Name (ARN) of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`
Required: Yes

 ** type **   <a name="AmazonS3-Type-s3Buckets_TableSummary-type"></a>
The type of the table.
Type: String
Valid Values: `customer | aws`
Required: Yes

 ** managedByService **   <a name="AmazonS3-Type-s3Buckets_TableSummary-managedByService"></a>
The AWS service managing this table, if applicable. For example, a replicated table is managed by the S3 Tables replication service.
Type: String
Required: No

 ** namespaceId **   <a name="AmazonS3-Type-s3Buckets_TableSummary-namespaceId"></a>
The unique identifier for the namespace that contains this table.
Type: String
Required: No

 ** tableBucketId **   <a name="AmazonS3-Type-s3Buckets_TableSummary-tableBucketId"></a>
The unique identifier for the table bucket that contains this table.
Type: String
Required: No

## See Also
<a name="API_s3Buckets_TableSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/TableSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/TableSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/TableSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
