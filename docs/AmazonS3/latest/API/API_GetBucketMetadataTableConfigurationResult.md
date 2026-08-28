---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataTableConfigurationResult.html
---

# GetBucketMetadataTableConfigurationResult
<a name="API_GetBucketMetadataTableConfigurationResult"></a>

 The V1 S3 Metadata configuration for a general purpose bucket.

**Note**
If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete and re-create your configuration by using [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) so that you can expire journal table records and create a live inventory table.

## Contents
<a name="API_GetBucketMetadataTableConfigurationResult_Contents"></a>

 ** MetadataTableConfigurationResult **   <a name="AmazonS3-Type-GetBucketMetadataTableConfigurationResult-MetadataTableConfigurationResult"></a>
 The V1 S3 Metadata configuration for a general purpose bucket.
Type: [MetadataTableConfigurationResult](API_MetadataTableConfigurationResult.md) data type
Required: Yes

 ** Status **   <a name="AmazonS3-Type-GetBucketMetadataTableConfigurationResult-Status"></a>
 The status of the metadata table. The status values are:
+  `CREATING` - The metadata table is in the process of being created in the specified table bucket.
+  `ACTIVE` - The metadata table has been created successfully, and records are being delivered to the table.
+  `FAILED` - Amazon S3 is unable to create the metadata table, or Amazon S3 is unable to deliver records. See `ErrorDetails` for details.
Type: String
Required: Yes

 ** Error **   <a name="AmazonS3-Type-GetBucketMetadataTableConfigurationResult-Error"></a>
 If the `CreateBucketMetadataTableConfiguration` request succeeds, but S3 Metadata was unable to create the table, this structure contains the error code and error message.
Type: [ErrorDetails](API_ErrorDetails.md) data type
Required: No

## See Also
<a name="API_GetBucketMetadataTableConfigurationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketMetadataTableConfigurationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketMetadataTableConfigurationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketMetadataTableConfigurationResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
