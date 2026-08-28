---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_AnnotationTableConfigurationUpdates.html
---

# AnnotationTableConfigurationUpdates
<a name="API_AnnotationTableConfigurationUpdates"></a>

Specifies updates to apply to the annotation table configuration. Used as the request body for `UpdateBucketMetadataAnnotationTableConfiguration`.

## Contents
<a name="API_AnnotationTableConfigurationUpdates_Contents"></a>

 ** ConfigurationState **   <a name="AmazonS3-Type-AnnotationTableConfigurationUpdates-ConfigurationState"></a>
The new configuration state to apply.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** EncryptionConfiguration **   <a name="AmazonS3-Type-AnnotationTableConfigurationUpdates-EncryptionConfiguration"></a>
 The encryption settings for an S3 Metadata journal table or inventory table configuration.
Type: [MetadataTableEncryptionConfiguration](API_MetadataTableEncryptionConfiguration.md) data type
Required: No

 ** Role **   <a name="AmazonS3-Type-AnnotationTableConfigurationUpdates-Role"></a>
The new IAM role ARN to apply.
Type: String
Required: No

## See Also
<a name="API_AnnotationTableConfigurationUpdates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/AnnotationTableConfigurationUpdates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/AnnotationTableConfigurationUpdates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/AnnotationTableConfigurationUpdates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
