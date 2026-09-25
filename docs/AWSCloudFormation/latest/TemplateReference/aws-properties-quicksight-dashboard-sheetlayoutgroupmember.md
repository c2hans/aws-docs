---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-sheetlayoutgroupmember.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SheetLayoutGroupMember
<a name="aws-properties-quicksight-dashboard-sheetlayoutgroupmember"></a>

A member of a sheet layout group.

## Syntax
<a name="aws-properties-quicksight-dashboard-sheetlayoutgroupmember-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-sheetlayoutgroupmember-syntax.json"></a>

```
{
  "[Id](#cfn-quicksight-dashboard-sheetlayoutgroupmember-id)" : {{String}},
  "[Type](#cfn-quicksight-dashboard-sheetlayoutgroupmember-type)" : {{}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-sheetlayoutgroupmember-syntax.yaml"></a>

```
  [Id](#cfn-quicksight-dashboard-sheetlayoutgroupmember-id): {{String}}
  [Type](#cfn-quicksight-dashboard-sheetlayoutgroupmember-type): {{
    }}
```

## Properties
<a name="aws-properties-quicksight-dashboard-sheetlayoutgroupmember-properties"></a>

`Id`  <a name="cfn-quicksight-dashboard-sheetlayoutgroupmember-id"></a>
The unique identifier of the group member.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-dashboard-sheetlayoutgroupmember-type"></a>
The type of the group member.
*Required*: Yes
*Type*:
*Allowed values*: `ELEMENT | GROUP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
