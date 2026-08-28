---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_JournalTableConfigurationResult.html
---

# JournalTableConfigurationResult
<a name="API_JournalTableConfigurationResult"></a>

 The journal table configuration for the S3 Metadata configuration.

## Contents
<a name="API_JournalTableConfigurationResult_Contents"></a>

 ** RecordExpiration **   <a name="AmazonS3-Type-JournalTableConfigurationResult-RecordExpiration"></a>
 The journal table record expiration settings for the journal table.
Type: [RecordExpiration](API_RecordExpiration.md) data type
Required: Yes

 ** TableName **   <a name="AmazonS3-Type-JournalTableConfigurationResult-TableName"></a>
 The name of the journal table.
Type: String
Required: Yes

 ** TableStatus **   <a name="AmazonS3-Type-JournalTableConfigurationResult-TableStatus"></a>
 The status of the journal table. The status values are:
+  `CREATING` - The journal table is in the process of being created in the specified table bucket.
+  `ACTIVE` - The journal table has been created successfully, and records are being delivered to the table.
+  `FAILED` - Amazon S3 is unable to create the journal table, or Amazon S3 is unable to deliver records.
Type: String
Required: Yes

 ** Error **   <a name="AmazonS3-Type-JournalTableConfigurationResult-Error"></a>
 If an S3 Metadata V1 `CreateBucketMetadataTableConfiguration` or V2 `CreateBucketMetadataConfiguration` request succeeds, but S3 Metadata was unable to create the table, this structure contains the error code and error message.
If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete and re-create your configuration by using [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) so that you can expire journal table records and create a live inventory table.
Type: [ErrorDetails](API_ErrorDetails.md) data type
Required: No

 ** TableArn **   <a name="AmazonS3-Type-JournalTableConfigurationResult-TableArn"></a>
 The Amazon Resource Name (ARN) for the journal table.
Type: String
Required: No

## See Also
<a name="API_JournalTableConfigurationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/JournalTableConfigurationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/JournalTableConfigurationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/JournalTableConfigurationResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
