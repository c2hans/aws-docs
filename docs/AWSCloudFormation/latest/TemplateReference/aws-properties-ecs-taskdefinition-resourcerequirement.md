---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-resourcerequirement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition ResourceRequirement
<a name="aws-properties-ecs-taskdefinition-resourcerequirement"></a>

The type and amount of a resource to assign to a container. The supported resource types are GPUs, Neuron devices, and Elastic Inference accelerators. For more information, see [Working with GPUs on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html) or [Working with Amazon Elastic Inference on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-inference.html) in the *Amazon Elastic Container Service Developer Guide*

## Syntax
<a name="aws-properties-ecs-taskdefinition-resourcerequirement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-resourcerequirement-syntax.json"></a>

```
{
  "[Type](#cfn-ecs-taskdefinition-resourcerequirement-type)" : {{String}},
  "[Value](#cfn-ecs-taskdefinition-resourcerequirement-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-resourcerequirement-syntax.yaml"></a>

```
  [Type](#cfn-ecs-taskdefinition-resourcerequirement-type): {{String}}
  [Value](#cfn-ecs-taskdefinition-resourcerequirement-value): {{String}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-resourcerequirement-properties"></a>

`Type`  <a name="cfn-ecs-taskdefinition-resourcerequirement-type"></a>
The type of resource to assign to a container.
*Required*: Yes
*Type*: String
*Allowed values*: `GPU | InferenceAccelerator | NeuronDevice`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-ecs-taskdefinition-resourcerequirement-value"></a>
The value for the specified resource type.
When the type is `GPU`, the value is the number of physical `GPUs` the Amazon ECS container agent reserves for the container. The number of GPUs that's reserved for all containers in a task can't exceed the number of available GPUs on the container instance that the task is launched on. You can also specify `ALL` to allocate all available GPUs on the instance to the container.
When the type is `NeuronDevice`, the value must be `ALL`. This allocates all available Neuron devices on the instance to the container. Only one container in a task can specify `NeuronDevice` resources. This resource type is only supported on Managed Instances.
When the type is `InferenceAccelerator`, the `value` matches the `deviceName` for an [InferenceAccelerator](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_InferenceAccelerator.html) specified in a task definition.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
