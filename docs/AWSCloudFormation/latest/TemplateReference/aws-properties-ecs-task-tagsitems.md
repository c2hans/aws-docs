---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-task-tagsitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Task TagsItems
<a name="aws-properties-ecs-task-tagsitems"></a>

<a name="aws-properties-ecs-task-tagsitems-description"></a>The `TagsItems` property type specifies Property description not available. for an [AWS::ECS::Task](aws-resource-ecs-task.md).

## Syntax
<a name="aws-properties-ecs-task-tagsitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-task-tagsitems-syntax.json"></a>

```
{
  "[Key](#cfn-ecs-task-tagsitems-key)" : {{String}},
  "[Value](#cfn-ecs-task-tagsitems-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-task-tagsitems-syntax.yaml"></a>

```
  [Key](#cfn-ecs-task-tagsitems-key): {{String}}
  [Value](#cfn-ecs-task-tagsitems-value): {{String}}
```

## Properties
<a name="aws-properties-ecs-task-tagsitems-properties"></a>

`Key`  <a name="cfn-ecs-task-tagsitems-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ecs-task-tagsitems-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
