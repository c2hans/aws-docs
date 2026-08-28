---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CheckpointConfig.html
---

# CheckpointConfig
<a name="API_CheckpointConfig"></a>

Contains information about the output location for managed spot training checkpoint data.

## Contents
<a name="API_CheckpointConfig_Contents"></a>

 ** S3Uri **   <a name="sagemaker-Type-CheckpointConfig-S3Uri"></a>
Identifies the S3 path where you want SageMaker to store checkpoints. For example, `s3://bucket-name/key-name-prefix`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** LocalPath **   <a name="sagemaker-Type-CheckpointConfig-LocalPath"></a>
(Optional) The local directory where checkpoints are written. The default directory is `/opt/ml/checkpoints/`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Pattern: `.*`
Required: No

## See Also
<a name="API_CheckpointConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CheckpointConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CheckpointConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CheckpointConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
