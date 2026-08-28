---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableReplicationRule.html
---

# TableReplicationRule
<a name="API_s3Buckets_TableReplicationRule"></a>

Defines a rule for replicating a table to one or more destination tables.

## Contents
<a name="API_s3Buckets_TableReplicationRule_Contents"></a>

 ** destinations **   <a name="AmazonS3-Type-s3Buckets_TableReplicationRule-destinations"></a>
An array of destination table buckets where this table should be replicated.
Type: Array of [ReplicationDestination](API_s3Buckets_ReplicationDestination.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

## See Also
<a name="API_s3Buckets_TableReplicationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/TableReplicationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/TableReplicationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/TableReplicationRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
