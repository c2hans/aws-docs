---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-automljob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AutoMLJob
<a name="aws-resource-sagemaker-automljob"></a>

Creates an Autopilot job also referred to as Autopilot experiment or AutoML job.

An AutoML job in SageMaker AI is a fully automated process that allows you to build machine learning models with minimal effort and machine learning expertise. When initiating an AutoML job, you provide your data and optionally specify parameters tailored to your use case. SageMaker AI then automates the entire model development lifecycle, including data preprocessing, model training, tuning, and evaluation. AutoML jobs are designed to simplify and accelerate the model building process by automating various tasks and exploring different combinations of machine learning algorithms, data preprocessing techniques, and hyperparameter values. The output of an AutoML job comprises one or more trained models ready for deployment and inference. Additionally, SageMaker AI AutoML jobs generate a candidate model leaderboard, allowing you to select the best-performing model for deployment.

For more information about AutoML jobs, see [https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html) in the SageMaker AI developer guide.

**Note**
We recommend using the new versions [CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html) and [DescribeAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html), which offer backward compatibility.
`CreateAutoMLJobV2` can manage tabular problem types identical to those of its previous version `CreateAutoMLJob`, as well as time-series forecasting, non-tabular problem types such as image or text classification, and text generation (LLMs fine-tuning).
Find guidelines about how to migrate a `CreateAutoMLJob` to `CreateAutoMLJobV2` in [Migrate a CreateAutoMLJob to CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-create-experiment.html#autopilot-create-experiment-api-migrate-v1-v2).

You can find the best-performing model after you run an AutoML job by calling [DescribeAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html) (recommended) or [DescribeAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJob.html).

## Syntax
<a name="aws-resource-sagemaker-automljob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-automljob-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::AutoMLJob",
  "Properties" : {
      "[AutoMLJobConfig](#cfn-sagemaker-automljob-automljobconfig)" : {{AutoMLJobConfig}},
      "[AutoMLJobObjective](#cfn-sagemaker-automljob-automljobobjective)" : {{AutoMLJobObjective}},
      "[GenerateCandidateDefinitionsOnly](#cfn-sagemaker-automljob-generatecandidatedefinitionsonly)" : {{Boolean}},
      "[InputDataConfig](#cfn-sagemaker-automljob-inputdataconfig)" : {{[ AutoMLChannel, ... ]}},
      "[OutputDataConfig](#cfn-sagemaker-automljob-outputdataconfig)" : {{AutoMLOutputDataConfig}},
      "[ProblemType](#cfn-sagemaker-automljob-problemtype)" : {{String}},
      "[RoleArn](#cfn-sagemaker-automljob-rolearn)" : {{String}},
      "[Tags](#cfn-sagemaker-automljob-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-automljob-syntax.yaml"></a>

```
Type: AWS::SageMaker::AutoMLJob
Properties:
  [AutoMLJobConfig](#cfn-sagemaker-automljob-automljobconfig): {{
    AutoMLJobConfig}}
  [AutoMLJobObjective](#cfn-sagemaker-automljob-automljobobjective): {{
    AutoMLJobObjective}}
  [GenerateCandidateDefinitionsOnly](#cfn-sagemaker-automljob-generatecandidatedefinitionsonly): {{Boolean}}
  [InputDataConfig](#cfn-sagemaker-automljob-inputdataconfig): {{
    - AutoMLChannel}}
  [OutputDataConfig](#cfn-sagemaker-automljob-outputdataconfig): {{
    AutoMLOutputDataConfig}}
  [ProblemType](#cfn-sagemaker-automljob-problemtype): {{String}}
  [RoleArn](#cfn-sagemaker-automljob-rolearn): {{String}}
  [Tags](#cfn-sagemaker-automljob-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sagemaker-automljob-properties"></a>

`AutoMLJobConfig`  <a name="cfn-sagemaker-automljob-automljobconfig"></a>
A collection of settings used for an AutoML job.
*Required*: No
*Type*: [AutoMLJobConfig](aws-properties-sagemaker-automljob-automljobconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AutoMLJobObjective`  <a name="cfn-sagemaker-automljob-automljobobjective"></a>
Specifies a metric to minimize or maximize as the objective of an AutoML job.
*Required*: No
*Type*: [AutoMLJobObjective](aws-properties-sagemaker-automljob-automljobobjective.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GenerateCandidateDefinitionsOnly`  <a name="cfn-sagemaker-automljob-generatecandidatedefinitionsonly"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InputDataConfig`  <a name="cfn-sagemaker-automljob-inputdataconfig"></a>
Property description not available.
*Required*: No
*Type*: Array of [AutoMLChannel](aws-properties-sagemaker-automljob-automlchannel.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputDataConfig`  <a name="cfn-sagemaker-automljob-outputdataconfig"></a>
Provides information about how to store model training results (model artifacts).
*Required*: No
*Type*: [AutoMLOutputDataConfig](aws-properties-sagemaker-automljob-automloutputdataconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProblemType`  <a name="cfn-sagemaker-automljob-problemtype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `BinaryClassification | MulticlassClassification | Regression`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-sagemaker-automljob-rolearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-automljob-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-automljob-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-automljob-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-automljob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-automljob-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-automljob-return-values-fn--getatt-fn--getatt"></a>

`AutoMLJobArn`  <a name="AutoMLJobArn-fn::getatt"></a>
The ARN of the AutoML job.

`AutoMLJobName`  <a name="AutoMLJobName-fn::getatt"></a>
The name of the AutoML job you are requesting.

`AutoMLJobSecondaryStatus`  <a name="AutoMLJobSecondaryStatus-fn::getatt"></a>
The secondary status of the AutoML job.

`AutoMLJobStatus`  <a name="AutoMLJobStatus-fn::getatt"></a>
The status of the AutoML job.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
When the AutoML job was created.

`EndTime`  <a name="EndTime-fn::getatt"></a>
The end time of an AutoML job.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
When the AutoML job was last modified.
