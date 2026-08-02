---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-trainingmetric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard TrainingMetric
<a name="aws-properties-sagemaker-modelcard-trainingmetric"></a>

A result from a SageMaker AI training job.

## Syntax
<a name="aws-properties-sagemaker-modelcard-trainingmetric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-trainingmetric-syntax.json"></a>

```
{
  "[Name](#cfn-sagemaker-modelcard-trainingmetric-name)" : {{String}},
  "[Notes](#cfn-sagemaker-modelcard-trainingmetric-notes)" : {{String}},
  "[Value](#cfn-sagemaker-modelcard-trainingmetric-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-trainingmetric-syntax.yaml"></a>

```
  [Name](#cfn-sagemaker-modelcard-trainingmetric-name): {{String}}
  [Notes](#cfn-sagemaker-modelcard-trainingmetric-notes): {{String}}
  [Value](#cfn-sagemaker-modelcard-trainingmetric-value): {{Number}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-trainingmetric-properties"></a>

`Name`  <a name="cfn-sagemaker-modelcard-trainingmetric-name"></a>
The name of the result from the SageMaker AI training job.
*Required*: Yes
*Type*: String
*Pattern*: `.{1,255}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Notes`  <a name="cfn-sagemaker-modelcard-trainingmetric-notes"></a>
Any additional notes describing the result of the training job.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-sagemaker-modelcard-trainingmetric-value"></a>
The value of a result from the SageMaker AI training job.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
