---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-sheetcontrollayoutconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template SheetControlLayoutConfiguration
<a name="aws-properties-quicksight-template-sheetcontrollayoutconfiguration"></a>

The configuration that determines the elements and canvas size options of sheet control.

## Syntax
<a name="aws-properties-quicksight-template-sheetcontrollayoutconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-sheetcontrollayoutconfiguration-syntax.json"></a>

```
{
  "[GridLayout](#cfn-quicksight-template-sheetcontrollayoutconfiguration-gridlayout)" : {{GridLayoutConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-template-sheetcontrollayoutconfiguration-syntax.yaml"></a>

```
  [GridLayout](#cfn-quicksight-template-sheetcontrollayoutconfiguration-gridlayout): {{
    GridLayoutConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-sheetcontrollayoutconfiguration-properties"></a>

`GridLayout`  <a name="cfn-quicksight-template-sheetcontrollayoutconfiguration-gridlayout"></a>
The configuration that determines the elements and canvas size options of sheet control.
*Required*: No
*Type*: [GridLayoutConfiguration](aws-properties-quicksight-template-gridlayoutconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
