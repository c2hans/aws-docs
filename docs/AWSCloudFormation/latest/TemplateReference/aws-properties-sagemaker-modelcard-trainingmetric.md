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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
