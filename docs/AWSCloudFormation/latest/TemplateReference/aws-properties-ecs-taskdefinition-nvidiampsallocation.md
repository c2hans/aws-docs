---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-nvidiampsallocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition NvidiaMpsAllocation
<a name="aws-properties-ecs-taskdefinition-nvidiampsallocation"></a>

<a name="aws-properties-ecs-taskdefinition-nvidiampsallocation-description"></a>The `NvidiaMpsAllocation` property type specifies Property description not available. for an [AWS::ECS::TaskDefinition](aws-resource-ecs-taskdefinition.md).

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
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Memory`  <a name="cfn-ecs-taskdefinition-nvidiampsallocation-memory"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
