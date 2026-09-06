---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OptimizationConfig.html
---

# OptimizationConfig
<a name="API_OptimizationConfig"></a>

Settings for an optimization technique that you apply with a model optimization job.

## Contents
<a name="API_OptimizationConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ModelCompilationConfig **   <a name="sagemaker-Type-OptimizationConfig-ModelCompilationConfig"></a>
Settings for the model compilation technique that's applied by a model optimization job.
Type: [ModelCompilationConfig](API_ModelCompilationConfig.md) object
Required: No

 ** ModelQuantizationConfig **   <a name="sagemaker-Type-OptimizationConfig-ModelQuantizationConfig"></a>
Settings for the model quantization technique that's applied by a model optimization job.
Type: [ModelQuantizationConfig](API_ModelQuantizationConfig.md) object
Required: No

 ** ModelShardingConfig **   <a name="sagemaker-Type-OptimizationConfig-ModelShardingConfig"></a>
Settings for the model sharding technique that's applied by a model optimization job.
Type: [ModelShardingConfig](API_ModelShardingConfig.md) object
Required: No

 ** ModelSpeculativeDecodingConfig **   <a name="sagemaker-Type-OptimizationConfig-ModelSpeculativeDecodingConfig"></a>
Settings for the model speculative decoding technique that's applied by a model optimization job.
Type: [ModelSpeculativeDecodingConfig](API_ModelSpeculativeDecodingConfig.md) object
Required: No

## See Also
<a name="API_OptimizationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/OptimizationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/OptimizationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/OptimizationConfig)
