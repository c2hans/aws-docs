---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-sheetlayoutgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template SheetLayoutGroup
<a name="aws-properties-quicksight-template-sheetlayoutgroup"></a>

A group of elements within a sheet layout.

## Syntax
<a name="aws-properties-quicksight-template-sheetlayoutgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-sheetlayoutgroup-syntax.json"></a>

```
{
  "[Id](#cfn-quicksight-template-sheetlayoutgroup-id)" : {{String}},
  "[Members](#cfn-quicksight-template-sheetlayoutgroup-members)" : {{[ SheetLayoutGroupMember, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-sheetlayoutgroup-syntax.yaml"></a>

```
  [Id](#cfn-quicksight-template-sheetlayoutgroup-id): {{String}}
  [Members](#cfn-quicksight-template-sheetlayoutgroup-members): {{
    - SheetLayoutGroupMember}}
```

## Properties
<a name="aws-properties-quicksight-template-sheetlayoutgroup-properties"></a>

`Id`  <a name="cfn-quicksight-template-sheetlayoutgroup-id"></a>
A unique identifier for the group.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Members`  <a name="cfn-quicksight-template-sheetlayoutgroup-members"></a>
The members of the group.
*Required*: Yes
*Type*: Array of [SheetLayoutGroupMember](aws-properties-quicksight-template-sheetlayoutgroupmember.md)
*Minimum*: `2`
*Maximum*: `430`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
