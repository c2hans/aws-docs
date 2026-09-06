---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-container.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard Container
<a name="aws-properties-sagemaker-modelcard-container"></a>

Information about the container used for the model.

## Syntax
<a name="aws-properties-sagemaker-modelcard-container-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-container-syntax.json"></a>

```
{
  "[Image](#cfn-sagemaker-modelcard-container-image)" : {{String}},
  "[ModelDataUrl](#cfn-sagemaker-modelcard-container-modeldataurl)" : {{String}},
  "[NearestModelName](#cfn-sagemaker-modelcard-container-nearestmodelname)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-container-syntax.yaml"></a>

```
  [Image](#cfn-sagemaker-modelcard-container-image): {{String}}
  [ModelDataUrl](#cfn-sagemaker-modelcard-container-modeldataurl): {{String}}
  [NearestModelName](#cfn-sagemaker-modelcard-container-nearestmodelname): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-container-properties"></a>

`Image`  <a name="cfn-sagemaker-modelcard-container-image"></a>
The Amazon EC2 Container Registry (Amazon ECR) path where the model container image is stored.
*Required*: Yes
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelDataUrl`  <a name="cfn-sagemaker-modelcard-container-modeldataurl"></a>
The Amazon S3 path where the model artifacts are stored.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NearestModelName`  <a name="cfn-sagemaker-modelcard-container-nearestmodelname"></a>
The name of a pre-trained model in the registry that is similar to this model.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
