---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-inferencespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard InferenceSpecification
<a name="aws-properties-sagemaker-modelcard-inferencespecification"></a>

Defines how to perform inference generation after a training job is run.

## Syntax
<a name="aws-properties-sagemaker-modelcard-inferencespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-inferencespecification-syntax.json"></a>

```
{
  "[Containers](#cfn-sagemaker-modelcard-inferencespecification-containers)" : {{[ Container, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-inferencespecification-syntax.yaml"></a>

```
  [Containers](#cfn-sagemaker-modelcard-inferencespecification-containers): {{
    - Container}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-inferencespecification-properties"></a>

`Containers`  <a name="cfn-sagemaker-modelcard-inferencespecification-containers"></a>
The Amazon ECR registry path of the Docker image that contains the inference code.
*Required*: Yes
*Type*: Array of [Container](aws-properties-sagemaker-modelcard-container.md)
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
