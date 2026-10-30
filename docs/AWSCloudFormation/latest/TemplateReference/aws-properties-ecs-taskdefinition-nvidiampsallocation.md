---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-nvidiampsallocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition NvidiaMpsAllocation
<a name="aws-properties-ecs-taskdefinition-nvidiampsallocation"></a>

The GPU memory and compute limits for a container that shares a GPU by using NVIDIA Multi-Process Service (MPS). Amazon ECS assigns the container a single GPU that has enough memory available. Other containers that use MPS can share the same GPU.

## Syntax
<a name="aws-properties-ecs-taskdefinition-nvidiampsallocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-nvidiampsallocation-syntax.json"></a>

```
{
  "[MaxComputePercent](#cfn-ecs-taskdefinition-nvidiampsallocation-maxcomputepercent)" : {{Integer}},
  "[Memory](#cfn-ecs-taskdefinition-nvidiampsallocation-memory)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-nvidiampsallocation-syntax.yaml"></a>

```
  [MaxComputePercent](#cfn-ecs-taskdefinition-nvidiampsallocation-maxcomputepercent): {{Integer}}
  [Memory](#cfn-ecs-taskdefinition-nvidiampsallocation-memory): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-nvidiampsallocation-properties"></a>

`MaxComputePercent`  <a name="cfn-ecs-taskdefinition-nvidiampsallocation-maxcomputepercent"></a>
The maximum percentage of the GPU's compute capacity that the container can use. Amazon ECS sets the `CUDA_MPS_ACTIVE_THREAD_PERCENTAGE` environment variable in the container to this value. This value is a limit, not a reservation.
If you don't specify this parameter, Amazon ECS doesn't set `CUDA_MPS_ACTIVE_THREAD_PERCENTAGE`, and the active thread percentage of the MPS server on the container instance applies. By default, this is 100 percent.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Memory`  <a name="cfn-ecs-taskdefinition-nvidiampsallocation-memory"></a>
The amount of GPU memory, in MiB, to allocate to the container. Amazon ECS assigns the container a GPU that has at least the specified amount of memory available, and sets the `CUDA_MPS_PINNED_DEVICE_MEM_LIMIT` environment variable in the container to limit its memory to this amount. The memory must be available on a single GPU. If more than one container in a task uses `nvidiaMps`, Amazon ECS assigns them the same GPU, which must have enough memory available for all of them.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
