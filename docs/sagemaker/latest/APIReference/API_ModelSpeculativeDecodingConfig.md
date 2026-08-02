---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelSpeculativeDecodingConfig.html
---

# ModelSpeculativeDecodingConfig
<a name="API_ModelSpeculativeDecodingConfig"></a>

Settings for the model speculative decoding technique that's applied by a model optimization job.

## Contents
<a name="API_ModelSpeculativeDecodingConfig_Contents"></a>

 ** Technique **   <a name="sagemaker-Type-ModelSpeculativeDecodingConfig-Technique"></a>
The speculative decoding technique to apply during model optimization.
Type: String
Valid Values: `EAGLE`
Required: Yes

 ** TrainingDataSource **   <a name="sagemaker-Type-ModelSpeculativeDecodingConfig-TrainingDataSource"></a>
The location of the training data to use for speculative decoding. The data must be formatted as ShareGPT, OpenAI Completions or OpenAI Chat Completions. The input can also be unencrypted captured data from a SageMaker endpoint as long as the endpoint uses one of the above formats.
Type: [ModelSpeculativeDecodingTrainingDataSource](API_ModelSpeculativeDecodingTrainingDataSource.md) object
Required: No

## See Also
<a name="API_ModelSpeculativeDecodingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelSpeculativeDecodingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelSpeculativeDecodingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelSpeculativeDecodingConfig)
