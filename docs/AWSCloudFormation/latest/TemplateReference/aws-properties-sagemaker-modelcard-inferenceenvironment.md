---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-inferenceenvironment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard InferenceEnvironment
<a name="aws-properties-sagemaker-modelcard-inferenceenvironment"></a>

An overview of a model's inference environment.

## Syntax
<a name="aws-properties-sagemaker-modelcard-inferenceenvironment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-inferenceenvironment-syntax.json"></a>

```
{
  "[ContainerImage](#cfn-sagemaker-modelcard-inferenceenvironment-containerimage)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-inferenceenvironment-syntax.yaml"></a>

```
  [ContainerImage](#cfn-sagemaker-modelcard-inferenceenvironment-containerimage): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-inferenceenvironment-properties"></a>

`ContainerImage`  <a name="cfn-sagemaker-modelcard-inferenceenvironment-containerimage"></a>
The container used to run the inference environment.
*Required*: No
*Type*: Array of String
*Maximum*: `1024 | 15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
