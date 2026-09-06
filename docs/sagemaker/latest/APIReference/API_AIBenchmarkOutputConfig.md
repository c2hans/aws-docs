---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIBenchmarkOutputConfig.html
---

# AIBenchmarkOutputConfig
<a name="API_AIBenchmarkOutputConfig"></a>

The output configuration for an AI benchmark job.

## Contents
<a name="API_AIBenchmarkOutputConfig_Contents"></a>

 ** S3OutputLocation **   <a name="sagemaker-Type-AIBenchmarkOutputConfig-S3OutputLocation"></a>
The Amazon S3 URI where benchmark results are stored.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** MlflowConfig **   <a name="sagemaker-Type-AIBenchmarkOutputConfig-MlflowConfig"></a>
The MLflow tracking configuration for the job. If you don't specify this parameter, MLflow tracking is disabled.
Type: [AIMlflowConfig](API_AIMlflowConfig.md) object
Required: No

## See Also
<a name="API_AIBenchmarkOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIBenchmarkOutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIBenchmarkOutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIBenchmarkOutputConfig)
