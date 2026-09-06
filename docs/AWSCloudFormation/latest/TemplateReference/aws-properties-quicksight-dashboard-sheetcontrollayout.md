---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-sheetcontrollayout.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SheetControlLayout
<a name="aws-properties-quicksight-dashboard-sheetcontrollayout"></a>

A grid layout to define the placement of sheet control.

## Syntax
<a name="aws-properties-quicksight-dashboard-sheetcontrollayout-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-sheetcontrollayout-syntax.json"></a>

```
{
  "[Configuration](#cfn-quicksight-dashboard-sheetcontrollayout-configuration)" : {{SheetControlLayoutConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-sheetcontrollayout-syntax.yaml"></a>

```
  [Configuration](#cfn-quicksight-dashboard-sheetcontrollayout-configuration): {{
    SheetControlLayoutConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-sheetcontrollayout-properties"></a>

`Configuration`  <a name="cfn-quicksight-dashboard-sheetcontrollayout-configuration"></a>
The configuration that determines the elements and canvas size options of sheet control.
*Required*: Yes
*Type*: [SheetControlLayoutConfiguration](aws-properties-quicksight-dashboard-sheetcontrollayoutconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
