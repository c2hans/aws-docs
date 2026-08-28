---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-ecsinferenceacceleratoroverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe EcsInferenceAcceleratorOverride
<a name="aws-properties-pipes-pipe-ecsinferenceacceleratoroverride"></a>

Details on an Elastic Inference accelerator task override. This parameter is used to override the Elastic Inference accelerator specified in the task definition. For more information, see [Working with Amazon Elastic Inference on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/userguide/ecs-inference.html) in the *Amazon Elastic Container Service Developer Guide*.

## Syntax
<a name="aws-properties-pipes-pipe-ecsinferenceacceleratoroverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-ecsinferenceacceleratoroverride-syntax.json"></a>

```
{
  "[DeviceName](#cfn-pipes-pipe-ecsinferenceacceleratoroverride-devicename)" : {{String}},
  "[DeviceType](#cfn-pipes-pipe-ecsinferenceacceleratoroverride-devicetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-ecsinferenceacceleratoroverride-syntax.yaml"></a>

```
  [DeviceName](#cfn-pipes-pipe-ecsinferenceacceleratoroverride-devicename): {{String}}
  [DeviceType](#cfn-pipes-pipe-ecsinferenceacceleratoroverride-devicetype): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-ecsinferenceacceleratoroverride-properties"></a>

`DeviceName`  <a name="cfn-pipes-pipe-ecsinferenceacceleratoroverride-devicename"></a>
The Elastic Inference accelerator device name to override for the task. This parameter must match a `deviceName` specified in the task definition.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceType`  <a name="cfn-pipes-pipe-ecsinferenceacceleratoroverride-devicetype"></a>
The Elastic Inference accelerator type to use.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
