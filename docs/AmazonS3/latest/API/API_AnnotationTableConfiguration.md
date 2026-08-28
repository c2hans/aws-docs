---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_AnnotationTableConfiguration.html
---

# AnnotationTableConfiguration
<a name="API_AnnotationTableConfiguration"></a>

Specifies the configuration for the annotation table associated with a bucket's Amazon S3 Metadata configuration. The annotation table is an Iceberg table that records annotation events for objects in the bucket.

## Contents
<a name="API_AnnotationTableConfiguration_Contents"></a>

 ** ConfigurationState **   <a name="AmazonS3-Type-AnnotationTableConfiguration-ConfigurationState"></a>
The state of the annotation table. Valid values are `ENABLED` and `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** EncryptionConfiguration **   <a name="AmazonS3-Type-AnnotationTableConfiguration-EncryptionConfiguration"></a>
 The encryption settings for an S3 Metadata journal table or inventory table configuration.
Type: [MetadataTableEncryptionConfiguration](API_MetadataTableEncryptionConfiguration.md) data type
Required: No

 ** Role **   <a name="AmazonS3-Type-AnnotationTableConfiguration-Role"></a>
The ARN of the IAM role used to manage the annotation table.
Type: String
Required: No

## See Also
<a name="API_AnnotationTableConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/AnnotationTableConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/AnnotationTableConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/AnnotationTableConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
