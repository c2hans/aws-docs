---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingSessionModelConfig.html
---

# TrainingSessionModelConfig
<a name="API_TrainingSessionModelConfig"></a>

The configuration for the base model used in a training session.

## Contents
<a name="API_TrainingSessionModelConfig_Contents"></a>

 ** BaseModelArn **   <a name="sagemaker-Type-TrainingSessionModelConfig-BaseModelArn"></a>
The Amazon Resource Name (ARN) of the base foundation model from SageMaker Hub.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:[a-z0-9-.]{1,63}:sagemaker:[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)+:([0-9]{12}|aws):hub-content/)[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}/Model/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}(/[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4})?`
Required: Yes

 ** AcceptEula **   <a name="sagemaker-Type-TrainingSessionModelConfig-AcceptEula"></a>
Specifies whether you accept the end-user license agreement (EULA) for gated models.
Type: Boolean
Required: No

## See Also
<a name="API_TrainingSessionModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrainingSessionModelConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrainingSessionModelConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrainingSessionModelConfig)
