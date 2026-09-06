---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-inferencecomponentplacementstatus.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent InferenceComponentPlacementStatus
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentplacementstatus"></a>

The placement status of an inference component on a specific instance type. Shows the number of inference component copies currently placed on instances of a given type.

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentplacementstatus-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentplacementstatus-syntax.json"></a>

```
{
  "[CurrentCopyCount](#cfn-sagemaker-inferencecomponent-inferencecomponentplacementstatus-currentcopycount)" : {{Integer}},
  "[InstanceType](#cfn-sagemaker-inferencecomponent-inferencecomponentplacementstatus-instancetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentplacementstatus-syntax.yaml"></a>

```
  [CurrentCopyCount](#cfn-sagemaker-inferencecomponent-inferencecomponentplacementstatus-currentcopycount): {{Integer}}
  [InstanceType](#cfn-sagemaker-inferencecomponent-inferencecomponentplacementstatus-instancetype): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentplacementstatus-properties"></a>

`CurrentCopyCount`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentplacementstatus-currentcopycount"></a>
The number of inference component copies currently placed on instances of this type.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceType`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentplacementstatus-instancetype"></a>
The ML compute instance type where the inference component copies are placed.
*Required*: Yes
*Type*: String
*Pattern*: `^ml\..*`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
