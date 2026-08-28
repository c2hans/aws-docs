---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ReplicationInformation.html
---

# ReplicationInformation
<a name="API_s3Buckets_ReplicationInformation"></a>

Contains information about the source of a replicated table.

## Contents
<a name="API_s3Buckets_ReplicationInformation_Contents"></a>

 ** sourceTableARN **   <a name="AmazonS3-Type-s3Buckets_ReplicationInformation-sourceTableARN"></a>
The Amazon Resource Name (ARN) of the source table from which this table is replicated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`
Required: Yes

## See Also
<a name="API_s3Buckets_ReplicationInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/ReplicationInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/ReplicationInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/ReplicationInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
