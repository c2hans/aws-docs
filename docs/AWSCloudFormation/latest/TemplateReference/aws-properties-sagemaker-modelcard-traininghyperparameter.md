---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-traininghyperparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard TrainingHyperParameter
<a name="aws-properties-sagemaker-modelcard-traininghyperparameter"></a>

A hyper parameter that was configured in training the model.

## Syntax
<a name="aws-properties-sagemaker-modelcard-traininghyperparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-traininghyperparameter-syntax.json"></a>

```
{
  "[Name](#cfn-sagemaker-modelcard-traininghyperparameter-name)" : {{String}},
  "[Value](#cfn-sagemaker-modelcard-traininghyperparameter-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-traininghyperparameter-syntax.yaml"></a>

```
  [Name](#cfn-sagemaker-modelcard-traininghyperparameter-name): {{String}}
  [Value](#cfn-sagemaker-modelcard-traininghyperparameter-value): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-traininghyperparameter-properties"></a>

`Name`  <a name="cfn-sagemaker-modelcard-traininghyperparameter-name"></a>
The name of the hyper parameter.
*Required*: Yes
*Type*: String
*Pattern*: `.{1,255}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-sagemaker-modelcard-traininghyperparameter-value"></a>
The value specified for the hyper parameter.
*Required*: Yes
*Type*: String
*Pattern*: `.{1,255}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
