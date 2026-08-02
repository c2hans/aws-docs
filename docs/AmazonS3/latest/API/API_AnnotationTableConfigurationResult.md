---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_AnnotationTableConfigurationResult.html
---

# AnnotationTableConfigurationResult
<a name="API_AnnotationTableConfigurationResult"></a>

Contains the current state of the annotation table associated with a bucket's Amazon S3 Metadata configuration, including its provisioning status and identifiers.

## Contents
<a name="API_AnnotationTableConfigurationResult_Contents"></a>

 ** ConfigurationState **   <a name="AmazonS3-Type-AnnotationTableConfigurationResult-ConfigurationState"></a>
The current configuration state of the annotation table.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** Error **   <a name="AmazonS3-Type-AnnotationTableConfigurationResult-Error"></a>
 If an S3 Metadata V1 `CreateBucketMetadataTableConfiguration` or V2 `CreateBucketMetadataConfiguration` request succeeds, but S3 Metadata was unable to create the table, this structure contains the error code and error message.
If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete and re-create your configuration by using [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) so that you can expire journal table records and create a live inventory table.
Type: [ErrorDetails](API_ErrorDetails.md) data type
Required: No

 ** Role **   <a name="AmazonS3-Type-AnnotationTableConfigurationResult-Role"></a>
The ARN of the IAM role associated with the annotation table.
Type: String
Required: No

 ** TableArn **   <a name="AmazonS3-Type-AnnotationTableConfigurationResult-TableArn"></a>
The ARN of the annotation table.
Type: String
Required: No

 ** TableName **   <a name="AmazonS3-Type-AnnotationTableConfigurationResult-TableName"></a>
The name of the annotation table.
Type: String
Required: No

 ** TableStatus **   <a name="AmazonS3-Type-AnnotationTableConfigurationResult-TableStatus"></a>
The provisioning status of the annotation table. Possible values: `CREATING`, `BACKFILLING`, `ACTIVE`, `FAILED`.
Type: String
Required: No

## See Also
<a name="API_AnnotationTableConfigurationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/AnnotationTableConfigurationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/AnnotationTableConfigurationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/AnnotationTableConfigurationResult)
