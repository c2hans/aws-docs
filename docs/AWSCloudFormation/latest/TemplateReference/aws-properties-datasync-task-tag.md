---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-task-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::Task Tag
<a name="aws-properties-datasync-task-tag"></a>

<a name="aws-properties-datasync-task-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::DataSync::Task](aws-resource-datasync-task.md).

## Syntax
<a name="aws-properties-datasync-task-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-task-tag-syntax.json"></a>

```
{
  "[Key](#cfn-datasync-task-tag-key)" : {{String}},
  "[Value](#cfn-datasync-task-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-task-tag-syntax.yaml"></a>

```
  [Key](#cfn-datasync-task-tag-key): {{String}}
  [Value](#cfn-datasync-task-tag-value): {{String}}
```

## Properties
<a name="aws-properties-datasync-task-tag-properties"></a>

`Key`  <a name="cfn-datasync-task-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s+=._:/-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-datasync-task-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s+=._:@/-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
