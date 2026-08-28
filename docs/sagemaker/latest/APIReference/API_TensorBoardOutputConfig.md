---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TensorBoardOutputConfig.html
---

# TensorBoardOutputConfig
<a name="API_TensorBoardOutputConfig"></a>

Configuration of storage locations for the Amazon SageMaker Debugger TensorBoard output data.

## Contents
<a name="API_TensorBoardOutputConfig_Contents"></a>

 ** S3OutputPath **   <a name="sagemaker-Type-TensorBoardOutputConfig-S3OutputPath"></a>
Path to Amazon S3 storage location for TensorBoard output.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** LocalPath **   <a name="sagemaker-Type-TensorBoardOutputConfig-LocalPath"></a>
Path to local storage location for tensorBoard output. Defaults to `/opt/ml/output/tensorboard`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Pattern: `.*`
Required: No

## See Also
<a name="API_TensorBoardOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TensorBoardOutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TensorBoardOutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TensorBoardOutputConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
