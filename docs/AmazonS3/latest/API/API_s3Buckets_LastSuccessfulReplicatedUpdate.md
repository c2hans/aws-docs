---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_LastSuccessfulReplicatedUpdate.html
---

# LastSuccessfulReplicatedUpdate
<a name="API_s3Buckets_LastSuccessfulReplicatedUpdate"></a>

Contains information about the most recent successful replication update to a destination.

## Contents
<a name="API_s3Buckets_LastSuccessfulReplicatedUpdate_Contents"></a>

 ** metadataLocation **   <a name="AmazonS3-Type-s3Buckets_LastSuccessfulReplicatedUpdate-metadataLocation"></a>
The S3 location of the metadata that was successfully replicated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** timestamp **   <a name="AmazonS3-Type-s3Buckets_LastSuccessfulReplicatedUpdate-timestamp"></a>
The timestamp when the replication update completed successfully.
Type: Timestamp
Required: Yes

## See Also
<a name="API_s3Buckets_LastSuccessfulReplicatedUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/LastSuccessfulReplicatedUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/LastSuccessfulReplicatedUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/LastSuccessfulReplicatedUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
