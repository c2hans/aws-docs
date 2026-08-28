---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelSpeculativeDecodingTrainingDataSource.html
---

# ModelSpeculativeDecodingTrainingDataSource
<a name="API_ModelSpeculativeDecodingTrainingDataSource"></a>

Contains information about the training data source for speculative decoding.

## Contents
<a name="API_ModelSpeculativeDecodingTrainingDataSource_Contents"></a>

 ** S3DataType **   <a name="sagemaker-Type-ModelSpeculativeDecodingTrainingDataSource-S3DataType"></a>
The type of data stored in the Amazon S3 location. Valid values are `S3Prefix` or `ManifestFile`.
Type: String
Valid Values: `S3Prefix | ManifestFile`
Required: Yes

 ** S3Uri **   <a name="sagemaker-Type-ModelSpeculativeDecodingTrainingDataSource-S3Uri"></a>
The Amazon S3 URI that points to the training data for speculative decoding.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

## See Also
<a name="API_ModelSpeculativeDecodingTrainingDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelSpeculativeDecodingTrainingDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelSpeculativeDecodingTrainingDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelSpeculativeDecodingTrainingDataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
