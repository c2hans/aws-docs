---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AdditionalS3DataSource.html
---

# AdditionalS3DataSource
<a name="API_AdditionalS3DataSource"></a>

A data source used for training or inference that is in addition to the input dataset or model data.

## Contents
<a name="API_AdditionalS3DataSource_Contents"></a>

 ** S3DataType **   <a name="sagemaker-Type-AdditionalS3DataSource-S3DataType"></a>
The data type of the additional data source that you specify for use in inference or training.
Type: String
Valid Values: `S3Object | S3Prefix`
Required: Yes

 ** S3Uri **   <a name="sagemaker-Type-AdditionalS3DataSource-S3Uri"></a>
The uniform resource identifier (URI) used to identify an additional data source used in inference or training.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** CompressionType **   <a name="sagemaker-Type-AdditionalS3DataSource-CompressionType"></a>
The type of compression used for an additional data source used in inference or training. Specify `None` if your additional data source is not compressed.
Type: String
Valid Values: `None | Gzip`
Required: No

 ** ETag **   <a name="sagemaker-Type-AdditionalS3DataSource-ETag"></a>
The ETag associated with S3 URI.
Type: String
Required: No

## See Also
<a name="API_AdditionalS3DataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AdditionalS3DataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AdditionalS3DataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AdditionalS3DataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
