---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig.html
---

# AutoMLJobConfig
<a name="API_AutoMLJobConfig"></a>

A collection of settings used for an AutoML job.

## Contents
<a name="API_AutoMLJobConfig_Contents"></a>

 ** CandidateGenerationConfig **   <a name="sagemaker-Type-AutoMLJobConfig-CandidateGenerationConfig"></a>
The configuration for generating a candidate for an AutoML job (optional).
Type: [AutoMLCandidateGenerationConfig](API_AutoMLCandidateGenerationConfig.md) object
Required: No

 ** CompletionCriteria **   <a name="sagemaker-Type-AutoMLJobConfig-CompletionCriteria"></a>
How long an AutoML job is allowed to run, or how many candidates a job is allowed to generate.
Type: [AutoMLJobCompletionCriteria](API_AutoMLJobCompletionCriteria.md) object
Required: No

 ** DataSplitConfig **   <a name="sagemaker-Type-AutoMLJobConfig-DataSplitConfig"></a>
The configuration for splitting the input training dataset.
Type: AutoMLDataSplitConfig
Type: [AutoMLDataSplitConfig](API_AutoMLDataSplitConfig.md) object
Required: No

 ** Mode **   <a name="sagemaker-Type-AutoMLJobConfig-Mode"></a>
The method that Autopilot uses to train the data. You can either specify the mode manually or let Autopilot choose for you based on the dataset size by selecting `AUTO`. In `AUTO` mode, Autopilot chooses `ENSEMBLING` for datasets smaller than 100 MB, and `HYPERPARAMETER_TUNING` for larger ones.
The `ENSEMBLING` mode uses a multi-stack ensemble model to predict classification and regression tasks directly from your dataset. This machine learning mode combines several base models to produce an optimal predictive model. It then uses a stacking ensemble method to combine predictions from contributing members. A multi-stack ensemble model can provide better performance over a single model by combining the predictive capabilities of multiple models. See [Autopilot algorithm support](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support) for a list of algorithms supported by `ENSEMBLING` mode.
The `HYPERPARAMETER_TUNING` (HPO) mode uses the best hyperparameters to train the best version of a model. HPO automatically selects an algorithm for the type of problem you want to solve. Then HPO finds the best hyperparameters according to your objective metric. See [Autopilot algorithm support](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support) for a list of algorithms supported by `HYPERPARAMETER_TUNING` mode.
Type: String
Valid Values: `AUTO | ENSEMBLING | HYPERPARAMETER_TUNING`
Required: No

 ** SecurityConfig **   <a name="sagemaker-Type-AutoMLJobConfig-SecurityConfig"></a>
The security configuration for traffic encryption or Amazon VPC settings.
Type: [AutoMLSecurityConfig](API_AutoMLSecurityConfig.md) object
Required: No

## See Also
<a name="API_AutoMLJobConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoMLJobConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoMLJobConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoMLJobConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
