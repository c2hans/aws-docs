---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TextGenerationJobConfig.html
---

# TextGenerationJobConfig
<a name="API_TextGenerationJobConfig"></a>

The collection of settings used by an AutoML job V2 for the text generation problem type.

**Note**
The text generation models that support fine-tuning in Autopilot are currently accessible exclusively in regions supported by Canvas. Refer to the documentation of Canvas for the [full list of its supported Regions](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html).

## Contents
<a name="API_TextGenerationJobConfig_Contents"></a>

 ** BaseModelName **   <a name="sagemaker-Type-TextGenerationJobConfig-BaseModelName"></a>
The name of the base model to fine-tune. Autopilot supports fine-tuning a variety of large language models. For information on the list of supported models, see [Text generation models supporting fine-tuning in Autopilot](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-llms-finetuning-models.html#autopilot-llms-finetuning-supported-llms). If no `BaseModelName` is provided, the default model used is **Falcon7BInstruct**.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** CompletionCriteria **   <a name="sagemaker-Type-TextGenerationJobConfig-CompletionCriteria"></a>
How long a fine-tuning job is allowed to run. For `TextGenerationJobConfig` problem types, the `MaxRuntimePerTrainingJobInSeconds` attribute of `AutoMLJobCompletionCriteria` defaults to 72h (259200s).
Type: [AutoMLJobCompletionCriteria](API_AutoMLJobCompletionCriteria.md) object
Required: No

 ** ModelAccessConfig **   <a name="sagemaker-Type-TextGenerationJobConfig-ModelAccessConfig"></a>
The access configuration file to control access to the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig`.
+ If you are a Jumpstart user, see the [End-user license agreements](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html#jumpstart-foundation-models-choose-eula) section for more details on accepting the EULA.
+ If you are an AutoML user, see the *Optional Parameters* section of *Create an AutoML job to fine-tune text generation models using the API* for details on [How to set the EULA acceptance when fine-tuning a model using the AutoML API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-finetune-llms.html#autopilot-llms-finetuning-api-optional-params).
Type: [ModelAccessConfig](API_ModelAccessConfig.md) object
Required: No

 ** TextGenerationHyperParameters **   <a name="sagemaker-Type-TextGenerationJobConfig-TextGenerationHyperParameters"></a>
The hyperparameters used to configure and optimize the learning process of the base model. You can set any combination of the following hyperparameters for all base models. For more information on each supported hyperparameter, see [Optimize the learning process of your text generation models with hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-llms-finetuning-set-hyperparameters.html).
+  `"epochCount"`: The number of times the model goes through the entire training dataset. Its value should be a string containing an integer value within the range of "1" to "10".
+  `"batchSize"`: The number of data samples used in each iteration of training. Its value should be a string containing an integer value within the range of "1" to "64".
+  `"learningRate"`: The step size at which a model's parameters are updated during training. Its value should be a string containing a floating-point value within the range of "0" to "1".
+  `"learningRateWarmupSteps"`: The number of training steps during which the learning rate gradually increases before reaching its target or maximum value. Its value should be a string containing an integer value within the range of "0" to "250".
Here is an example where all four hyperparameters are configured.
 `{ "epochCount":"5", "learningRate":"0.5", "batchSize": "32", "learningRateWarmupSteps": "10" }`
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 30 items.
Key Length Constraints: Minimum length of 0. Maximum length of 32.
Key Pattern: `[a-zA-Z0-9._-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 16.
Value Pattern: `[a-zA-Z0-9._-]+`
Required: No

## See Also
<a name="API_TextGenerationJobConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TextGenerationJobConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TextGenerationJobConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TextGenerationJobConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
