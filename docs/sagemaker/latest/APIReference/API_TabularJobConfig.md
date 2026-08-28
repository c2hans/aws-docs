---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig.html
---

# TabularJobConfig
<a name="API_TabularJobConfig"></a>

The collection of settings used by an AutoML job V2 for the tabular problem type.

## Contents
<a name="API_TabularJobConfig_Contents"></a>

 ** TargetAttributeName **   <a name="sagemaker-Type-TabularJobConfig-TargetAttributeName"></a>
The name of the target variable in supervised learning, usually represented by 'y'.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** CandidateGenerationConfig **   <a name="sagemaker-Type-TabularJobConfig-CandidateGenerationConfig"></a>
The configuration information of how model candidates are generated.
Type: [CandidateGenerationConfig](API_CandidateGenerationConfig.md) object
Required: No

 ** CompletionCriteria **   <a name="sagemaker-Type-TabularJobConfig-CompletionCriteria"></a>
How long a job is allowed to run, or how many candidates a job is allowed to generate.
Type: [AutoMLJobCompletionCriteria](API_AutoMLJobCompletionCriteria.md) object
Required: No

 ** FeatureSpecificationS3Uri **   <a name="sagemaker-Type-TabularJobConfig-FeatureSpecificationS3Uri"></a>
A URL to the Amazon S3 data source containing selected features from the input data source to run an Autopilot job V2. You can input `FeatureAttributeNames` (optional) in JSON format as shown below:
 `{ "FeatureAttributeNames":["col1", "col2", ...] }`.
You can also specify the data type of the feature (optional) in the format shown below:
 `{ "FeatureDataTypes":{"col1":"numeric", "col2":"categorical" ... } }`
These column keys may not include the target column.
In ensembling mode, Autopilot only supports the following data types: `numeric`, `categorical`, `text`, and `datetime`. In HPO mode, Autopilot can support `numeric`, `categorical`, `text`, `datetime`, and `sequence`.
If only `FeatureDataTypes` is provided, the column keys (`col1`, `col2`,..) should be a subset of the column names in the input data.
If both `FeatureDataTypes` and `FeatureAttributeNames` are provided, then the column keys should be a subset of the column names provided in `FeatureAttributeNames`.
The key name `FeatureAttributeNames` is fixed. The values listed in `["col1", "col2", ...]` are case sensitive and should be a list of strings containing unique values that are a subset of the column names in the input data. The list of columns provided must not include the target column.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

 ** GenerateCandidateDefinitionsOnly **   <a name="sagemaker-Type-TabularJobConfig-GenerateCandidateDefinitionsOnly"></a>
Generates possible candidates without training the models. A model candidate is a combination of data preprocessors, algorithms, and algorithm parameter settings.
Type: Boolean
Required: No

 ** Mode **   <a name="sagemaker-Type-TabularJobConfig-Mode"></a>
The method that Autopilot uses to train the data. You can either specify the mode manually or let Autopilot choose for you based on the dataset size by selecting `AUTO`. In `AUTO` mode, Autopilot chooses `ENSEMBLING` for datasets smaller than 100 MB, and `HYPERPARAMETER_TUNING` for larger ones.
The `ENSEMBLING` mode uses a multi-stack ensemble model to predict classification and regression tasks directly from your dataset. This machine learning mode combines several base models to produce an optimal predictive model. It then uses a stacking ensemble method to combine predictions from contributing members. A multi-stack ensemble model can provide better performance over a single model by combining the predictive capabilities of multiple models. See [Autopilot algorithm support](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support) for a list of algorithms supported by `ENSEMBLING` mode.
The `HYPERPARAMETER_TUNING` (HPO) mode uses the best hyperparameters to train the best version of a model. HPO automatically selects an algorithm for the type of problem you want to solve. Then HPO finds the best hyperparameters according to your objective metric. See [Autopilot algorithm support](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support) for a list of algorithms supported by `HYPERPARAMETER_TUNING` mode.
Type: String
Valid Values: `AUTO | ENSEMBLING | HYPERPARAMETER_TUNING`
Required: No

 ** ProblemType **   <a name="sagemaker-Type-TabularJobConfig-ProblemType"></a>
The type of supervised learning problem available for the model candidates of the AutoML job V2. For more information, see [ SageMaker Autopilot problem types](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-datasets-problem-types.html#autopilot-problem-types).
You must either specify the type of supervised learning problem in `ProblemType` and provide the [AutoMLJobObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-AutoMLJobObjective) metric, or none at all.
Type: String
Valid Values: `BinaryClassification | MulticlassClassification | Regression`
Required: No

 ** SampleWeightAttributeName **   <a name="sagemaker-Type-TabularJobConfig-SampleWeightAttributeName"></a>
If specified, this column name indicates which column of the dataset should be treated as sample weights for use by the objective metric during the training, evaluation, and the selection of the best model. This column is not considered as a predictive feature. For more information on Autopilot metrics, see [Metrics and validation](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html).
Sample weights should be numeric, non-negative, with larger values indicating which rows are more important than others. Data points that have invalid or no weight value are excluded.
Support for sample weights is available in [Ensembling](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html) mode only.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

## See Also
<a name="API_TabularJobConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TabularJobConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TabularJobConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TabularJobConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
