---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-textfieldcontroldisplayoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard TextFieldControlDisplayOptions
<a name="aws-properties-quicksight-dashboard-textfieldcontroldisplayoptions"></a>

The display options of a control.

## Syntax
<a name="aws-properties-quicksight-dashboard-textfieldcontroldisplayoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-textfieldcontroldisplayoptions-syntax.json"></a>

```
{
  "[InfoIconLabelOptions](#cfn-quicksight-dashboard-textfieldcontroldisplayoptions-infoiconlabeloptions)" : {{SheetControlInfoIconLabelOptions}},
  "[PlaceholderOptions](#cfn-quicksight-dashboard-textfieldcontroldisplayoptions-placeholderoptions)" : {{TextControlPlaceholderOptions}},
  "[TitleOptions](#cfn-quicksight-dashboard-textfieldcontroldisplayoptions-titleoptions)" : {{LabelOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-textfieldcontroldisplayoptions-syntax.yaml"></a>

```
  [InfoIconLabelOptions](#cfn-quicksight-dashboard-textfieldcontroldisplayoptions-infoiconlabeloptions): {{
    SheetControlInfoIconLabelOptions}}
  [PlaceholderOptions](#cfn-quicksight-dashboard-textfieldcontroldisplayoptions-placeholderoptions): {{
    TextControlPlaceholderOptions}}
  [TitleOptions](#cfn-quicksight-dashboard-textfieldcontroldisplayoptions-titleoptions): {{
    LabelOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-textfieldcontroldisplayoptions-properties"></a>

`InfoIconLabelOptions`  <a name="cfn-quicksight-dashboard-textfieldcontroldisplayoptions-infoiconlabeloptions"></a>
The configuration of info icon label options.
*Required*: No
*Type*: [SheetControlInfoIconLabelOptions](aws-properties-quicksight-dashboard-sheetcontrolinfoiconlabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PlaceholderOptions`  <a name="cfn-quicksight-dashboard-textfieldcontroldisplayoptions-placeholderoptions"></a>
The configuration of the placeholder options in a text field control.
*Required*: No
*Type*: [TextControlPlaceholderOptions](aws-properties-quicksight-dashboard-textcontrolplaceholderoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TitleOptions`  <a name="cfn-quicksight-dashboard-textfieldcontroldisplayoptions-titleoptions"></a>
The options to configure the title visibility, name, and font size.
*Required*: No
*Type*: [LabelOptions](aws-properties-quicksight-dashboard-labeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
