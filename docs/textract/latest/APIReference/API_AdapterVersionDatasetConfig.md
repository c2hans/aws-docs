---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_AdapterVersionDatasetConfig.html
---

# AdapterVersionDatasetConfig
<a name="API_AdapterVersionDatasetConfig"></a>

The dataset configuration options for a given version of an adapter. Can include an Amazon S3 bucket if specified.

## Contents
<a name="API_AdapterVersionDatasetConfig_Contents"></a>

 ** ManifestS3Object **   <a name="Textract-Type-AdapterVersionDatasetConfig-ManifestS3Object"></a>
The S3 bucket name and file name that identifies the document.
The AWS Region for the S3 bucket that contains the document must match the Region that you use for Amazon Textract operations.
For Amazon Textract to process a file in an S3 bucket, the user must have permission to access the S3 bucket and file.
Type: [S3Object](API_S3Object.md) object
Required: No

## See Also
<a name="API_AdapterVersionDatasetConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/AdapterVersionDatasetConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/AdapterVersionDatasetConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/AdapterVersionDatasetConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Textract. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query textract` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
