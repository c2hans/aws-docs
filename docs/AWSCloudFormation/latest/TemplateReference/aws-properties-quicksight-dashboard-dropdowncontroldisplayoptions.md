---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-dropdowncontroldisplayoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DropDownControlDisplayOptions
<a name="aws-properties-quicksight-dashboard-dropdowncontroldisplayoptions"></a>

The display options of a control.

## Syntax
<a name="aws-properties-quicksight-dashboard-dropdowncontroldisplayoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-dropdowncontroldisplayoptions-syntax.json"></a>

```
{
  "[InfoIconLabelOptions](#cfn-quicksight-dashboard-dropdowncontroldisplayoptions-infoiconlabeloptions)" : {{SheetControlInfoIconLabelOptions}},
  "[SelectAllOptions](#cfn-quicksight-dashboard-dropdowncontroldisplayoptions-selectalloptions)" : {{ListControlSelectAllOptions}},
  "[TitleOptions](#cfn-quicksight-dashboard-dropdowncontroldisplayoptions-titleoptions)" : {{LabelOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-dropdowncontroldisplayoptions-syntax.yaml"></a>

```
  [InfoIconLabelOptions](#cfn-quicksight-dashboard-dropdowncontroldisplayoptions-infoiconlabeloptions): {{
    SheetControlInfoIconLabelOptions}}
  [SelectAllOptions](#cfn-quicksight-dashboard-dropdowncontroldisplayoptions-selectalloptions): {{
    ListControlSelectAllOptions}}
  [TitleOptions](#cfn-quicksight-dashboard-dropdowncontroldisplayoptions-titleoptions): {{
    LabelOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-dropdowncontroldisplayoptions-properties"></a>

`InfoIconLabelOptions`  <a name="cfn-quicksight-dashboard-dropdowncontroldisplayoptions-infoiconlabeloptions"></a>
The configuration of info icon label options.
*Required*: No
*Type*: [SheetControlInfoIconLabelOptions](aws-properties-quicksight-dashboard-sheetcontrolinfoiconlabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectAllOptions`  <a name="cfn-quicksight-dashboard-dropdowncontroldisplayoptions-selectalloptions"></a>
The configuration of the `Select all` options in a dropdown control.
*Required*: No
*Type*: [ListControlSelectAllOptions](aws-properties-quicksight-dashboard-listcontrolselectalloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TitleOptions`  <a name="cfn-quicksight-dashboard-dropdowncontroldisplayoptions-titleoptions"></a>
The options to configure the title visibility, name, and font size.
*Required*: No
*Type*: [LabelOptions](aws-properties-quicksight-dashboard-labeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
