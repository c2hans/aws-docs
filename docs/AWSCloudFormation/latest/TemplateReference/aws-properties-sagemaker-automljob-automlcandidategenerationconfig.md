---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-automljob-automlcandidategenerationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AutoMLJob AutoMLCandidateGenerationConfig
<a name="aws-properties-sagemaker-automljob-automlcandidategenerationconfig"></a>

Stores the configuration information for how a candidate is generated (optional).

## Syntax
<a name="aws-properties-sagemaker-automljob-automlcandidategenerationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-automljob-automlcandidategenerationconfig-syntax.json"></a>

```
{
  "[AlgorithmsConfig](#cfn-sagemaker-automljob-automlcandidategenerationconfig-algorithmsconfig)" : {{[ AutoMLAlgorithmConfig, ... ]}},
  "[FeatureSpecificationS3Uri](#cfn-sagemaker-automljob-automlcandidategenerationconfig-featurespecifications3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-automljob-automlcandidategenerationconfig-syntax.yaml"></a>

```
  [AlgorithmsConfig](#cfn-sagemaker-automljob-automlcandidategenerationconfig-algorithmsconfig): {{
    - AutoMLAlgorithmConfig}}
  [FeatureSpecificationS3Uri](#cfn-sagemaker-automljob-automlcandidategenerationconfig-featurespecifications3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-automljob-automlcandidategenerationconfig-properties"></a>

`AlgorithmsConfig`  <a name="cfn-sagemaker-automljob-automlcandidategenerationconfig-algorithmsconfig"></a>
Stores the configuration information for the selection of algorithms trained on tabular data.
The list of available algorithms to choose from depends on the training mode set in [`TabularJobConfig.Mode`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig.html).
+ `AlgorithmsConfig` should not be set if the training mode is set on `AUTO`.
+ When `AlgorithmsConfig` is provided, one `AutoMLAlgorithms` attribute must be set and one only.

  If the list of algorithms provided as values for `AutoMLAlgorithms` is empty, `CandidateGenerationConfig` uses the full set of algorithms for the given training mode.
+ When `AlgorithmsConfig` is not provided, `CandidateGenerationConfig` uses the full set of algorithms for the given training mode.
For the list of all algorithms per problem type and training mode, see [ AutoMLAlgorithmConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html).
For more information on each algorithm, see the [Algorithm support](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support) section in Autopilot developer guide.
*Required*: No
*Type*: Array of [AutoMLAlgorithmConfig](aws-properties-sagemaker-automljob-automlalgorithmconfig.md)
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FeatureSpecificationS3Uri`  <a name="cfn-sagemaker-automljob-automlcandidategenerationconfig-featurespecifications3uri"></a>
A URL to the Amazon S3 data source containing selected features from the input data source to run an Autopilot job. You can input `FeatureAttributeNames` (optional) in JSON format as shown below:
`{ "FeatureAttributeNames":["col1", "col2", ...] }`.
You can also specify the data type of the feature (optional) in the format shown below:
 `{ "FeatureDataTypes":{"col1":"numeric", "col2":"categorical" ... } }`
These column keys may not include the target column.
In ensembling mode, Autopilot only supports the following data types: `numeric`, `categorical`, `text`, and `datetime`. In HPO mode, Autopilot can support `numeric`, `categorical`, `text`, `datetime`, and `sequence`.
If only `FeatureDataTypes` is provided, the column keys (`col1`, `col2`,..) should be a subset of the column names in the input data.
If both `FeatureDataTypes` and `FeatureAttributeNames` are provided, then the column keys should be a subset of the column names provided in `FeatureAttributeNames`.
The key name `FeatureAttributeNames` is fixed. The values listed in `["col1", "col2", ...]` are case sensitive and should be a list of strings containing unique values that are a subset of the column names in the input data. The list of columns provided must not include the target column.
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
