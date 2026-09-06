---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-task-filterrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::Task FilterRule
<a name="aws-properties-datasync-task-filterrule"></a>

Specifies which files, folders, and objects to include or exclude when transferring files from source to destination.

## Syntax
<a name="aws-properties-datasync-task-filterrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-task-filterrule-syntax.json"></a>

```
{
  "[FilterType](#cfn-datasync-task-filterrule-filtertype)" : {{String}},
  "[Value](#cfn-datasync-task-filterrule-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-task-filterrule-syntax.yaml"></a>

```
  [FilterType](#cfn-datasync-task-filterrule-filtertype): {{String}}
  [Value](#cfn-datasync-task-filterrule-value): {{String}}
```

## Properties
<a name="aws-properties-datasync-task-filterrule-properties"></a>

`FilterType`  <a name="cfn-datasync-task-filterrule-filtertype"></a>
The type of filter rule to apply. AWS DataSync only supports the SIMPLE\_PATTERN rule type.
*Required*: No
*Type*: String
*Allowed values*: `SIMPLE_PATTERN`
*Pattern*: `^[A-Z0-9_]+$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-datasync-task-filterrule-value"></a>
A single filter string that consists of the patterns to include or exclude. The patterns are delimited by "\|" (that is, a pipe), for example: `/folder1|/folder2`

*Required*: No
*Type*: String
*Pattern*: `^[^\x00]+$`
*Maximum*: `409600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
