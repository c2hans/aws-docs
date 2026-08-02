---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-inferencecomponentruntimeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent InferenceComponentRuntimeConfig
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentruntimeconfig"></a>

Runtime settings for a model that is deployed with an inference component.

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentruntimeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentruntimeconfig-syntax.json"></a>

```
{
  "[CopyCount](#cfn-sagemaker-inferencecomponent-inferencecomponentruntimeconfig-copycount)" : {{Integer}},
  "[CurrentCopyCount](#cfn-sagemaker-inferencecomponent-inferencecomponentruntimeconfig-currentcopycount)" : {{Integer}},
  "[DesiredCopyCount](#cfn-sagemaker-inferencecomponent-inferencecomponentruntimeconfig-desiredcopycount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentruntimeconfig-syntax.yaml"></a>

```
  [CopyCount](#cfn-sagemaker-inferencecomponent-inferencecomponentruntimeconfig-copycount): {{Integer}}
  [CurrentCopyCount](#cfn-sagemaker-inferencecomponent-inferencecomponentruntimeconfig-currentcopycount): {{Integer}}
  [DesiredCopyCount](#cfn-sagemaker-inferencecomponent-inferencecomponentruntimeconfig-desiredcopycount): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentruntimeconfig-properties"></a>

`CopyCount`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentruntimeconfig-copycount"></a>
The number of runtime copies of the model container to deploy with the inference component. Each copy can serve inference requests.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CurrentCopyCount`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentruntimeconfig-currentcopycount"></a>
The current number of copies of the model deployed for the inference component.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DesiredCopyCount`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentruntimeconfig-desiredcopycount"></a>
The desired number of copies of the model to deploy for the inference component.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
