---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_MetadataConfiguration.html
---

# MetadataConfiguration
<a name="API_MetadataConfiguration"></a>

 The S3 Metadata configuration for a general purpose bucket.

## Contents
<a name="API_MetadataConfiguration_Contents"></a>

 ** JournalTableConfiguration **   <a name="AmazonS3-Type-MetadataConfiguration-JournalTableConfiguration"></a>
 The journal table configuration for a metadata configuration.
Type: [JournalTableConfiguration](API_JournalTableConfiguration.md) data type
Required: Yes

 ** AnnotationTableConfiguration **   <a name="AmazonS3-Type-MetadataConfiguration-AnnotationTableConfiguration"></a>
Optional annotation table configuration to include with the metadata configuration.
Type: [AnnotationTableConfiguration](API_AnnotationTableConfiguration.md) data type
Required: No

 ** InventoryTableConfiguration **   <a name="AmazonS3-Type-MetadataConfiguration-InventoryTableConfiguration"></a>
 The inventory table configuration for a metadata configuration.
Type: [InventoryTableConfiguration](API_InventoryTableConfiguration.md) data type
Required: No

## See Also
<a name="API_MetadataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/MetadataConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/MetadataConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/MetadataConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
