---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent InferenceComponentComputeResourceRequirements
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements"></a>

Defines the compute resources to allocate to run a model, plus any adapter models, that you assign to an inference component. These resources include CPU cores, accelerators, and memory.

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-syntax.json"></a>

```
{
  "[MaxMemoryRequiredInMb](#cfn-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-maxmemoryrequiredinmb)" : {{Integer}},
  "[MinMemoryRequiredInMb](#cfn-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-minmemoryrequiredinmb)" : {{Integer}},
  "[NumberOfAcceleratorDevicesRequired](#cfn-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-numberofacceleratordevicesrequired)" : {{Number}},
  "[NumberOfCpuCoresRequired](#cfn-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-numberofcpucoresrequired)" : {{Number}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-syntax.yaml"></a>

```
  [MaxMemoryRequiredInMb](#cfn-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-maxmemoryrequiredinmb): {{Integer}}
  [MinMemoryRequiredInMb](#cfn-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-minmemoryrequiredinmb): {{Integer}}
  [NumberOfAcceleratorDevicesRequired](#cfn-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-numberofacceleratordevicesrequired): {{
    Number}}
  [NumberOfCpuCoresRequired](#cfn-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-numberofcpucoresrequired): {{
    Number}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-properties"></a>

`MaxMemoryRequiredInMb`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-maxmemoryrequiredinmb"></a>
The maximum MB of memory to allocate to run a model that you assign to an inference component.
*Required*: No
*Type*: Integer
*Minimum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinMemoryRequiredInMb`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-minmemoryrequiredinmb"></a>
The minimum MB of memory to allocate to run a model that you assign to an inference component.
*Required*: No
*Type*: Integer
*Minimum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberOfAcceleratorDevicesRequired`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-numberofacceleratordevicesrequired"></a>
The number of accelerators to allocate to run a model that you assign to an inference component. Accelerators include GPUs and AWS Inferentia.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberOfCpuCoresRequired`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-numberofcpucoresrequired"></a>
The number of CPU cores to allocate to run a model that you assign to an inference component.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
