---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-sharingstrategy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition SharingStrategy
<a name="aws-properties-ecs-taskdefinition-sharingstrategy"></a>

The strategy that a container uses to share a GPU with other containers. Specify exactly one member.

## Syntax
<a name="aws-properties-ecs-taskdefinition-sharingstrategy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-sharingstrategy-syntax.json"></a>

```
{
  "[NvidiaMps](#cfn-ecs-taskdefinition-sharingstrategy-nvidiamps)" : {{NvidiaMpsAllocation}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-sharingstrategy-syntax.yaml"></a>

```
  [NvidiaMps](#cfn-ecs-taskdefinition-sharingstrategy-nvidiamps): {{
    NvidiaMpsAllocation}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-sharingstrategy-properties"></a>

`NvidiaMps`  <a name="cfn-ecs-taskdefinition-sharingstrategy-nvidiamps"></a>
Shares a GPU between containers by using NVIDIA Multi-Process Service (MPS). You specify the GPU memory to allocate to the container and, optionally, the maximum percentage of the GPU's compute capacity that the container can use.
*Required*: Yes
*Type*: [NvidiaMpsAllocation](aws-properties-ecs-taskdefinition-nvidiampsallocation.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
