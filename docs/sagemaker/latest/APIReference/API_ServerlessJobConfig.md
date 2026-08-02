---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ServerlessJobConfig.html
---

# ServerlessJobConfig
<a name="API_ServerlessJobConfig"></a>

 The configuration for the serverless training job.

## Contents
<a name="API_ServerlessJobConfig_Contents"></a>

 ** BaseModelArn **   <a name="sagemaker-Type-ServerlessJobConfig-BaseModelArn"></a>
 The base model Amazon Resource Name (ARN) in [SageMaker Public Hub](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use.html). SageMaker always selects the latest version of the provided model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:(\d{12}|aws):hub-content\/)[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}\/Model\/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}(\/\d{1,4}.\d{1,4}.\d{1,4})?`
Required: Yes

 ** JobType **   <a name="sagemaker-Type-ServerlessJobConfig-JobType"></a>
 The serverless training job type.
Type: String
Valid Values: `FineTuning | Evaluation`
Required: Yes

 ** AcceptEula **   <a name="sagemaker-Type-ServerlessJobConfig-AcceptEula"></a>
 Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model. For more information, see [End-user license agreements](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html#jumpstart-foundation-models-choose-eula) section for more details on accepting the EULA.
Type: Boolean
Required: No

 ** CustomizationTechnique **   <a name="sagemaker-Type-ServerlessJobConfig-CustomizationTechnique"></a>
 The model customization technique.
Type: String
Valid Values: `SFT | DPO | RLVR | RLAIF`
Required: No

 ** EvaluationType **   <a name="sagemaker-Type-ServerlessJobConfig-EvaluationType"></a>
 The evaluation job type. Required when serverless job type is `Evaluation`.
Type: String
Valid Values: `LLMAJEvaluation | CustomScorerEvaluation | BenchmarkEvaluation`
Required: No

 ** EvaluatorArn **   <a name="sagemaker-Type-ServerlessJobConfig-EvaluatorArn"></a>
 The evaluator Amazon Resource Name (ARN) used as reward function or reward prompt.
Type: String
Pattern: `.*`
Required: No

 ** Peft **   <a name="sagemaker-Type-ServerlessJobConfig-Peft"></a>
 The parameter-efficient fine-tuning configuration.
Type: String
Valid Values: `LORA`
Required: No

## See Also
<a name="API_ServerlessJobConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ServerlessJobConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ServerlessJobConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ServerlessJobConfig)
