---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-datetimepickercontroldisplayoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DateTimePickerControlDisplayOptions
<a name="aws-properties-quicksight-dashboard-datetimepickercontroldisplayoptions"></a>

The display options of a control.

## Syntax
<a name="aws-properties-quicksight-dashboard-datetimepickercontroldisplayoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-datetimepickercontroldisplayoptions-syntax.json"></a>

```
{
  "[DateIconVisibility](#cfn-quicksight-dashboard-datetimepickercontroldisplayoptions-dateiconvisibility)" : {{String}},
  "[DateTimeFormat](#cfn-quicksight-dashboard-datetimepickercontroldisplayoptions-datetimeformat)" : {{String}},
  "[HelperTextVisibility](#cfn-quicksight-dashboard-datetimepickercontroldisplayoptions-helpertextvisibility)" : {{String}},
  "[InfoIconLabelOptions](#cfn-quicksight-dashboard-datetimepickercontroldisplayoptions-infoiconlabeloptions)" : {{SheetControlInfoIconLabelOptions}},
  "[TitleOptions](#cfn-quicksight-dashboard-datetimepickercontroldisplayoptions-titleoptions)" : {{LabelOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-datetimepickercontroldisplayoptions-syntax.yaml"></a>

```
  [DateIconVisibility](#cfn-quicksight-dashboard-datetimepickercontroldisplayoptions-dateiconvisibility): {{String}}
  [DateTimeFormat](#cfn-quicksight-dashboard-datetimepickercontroldisplayoptions-datetimeformat): {{String}}
  [HelperTextVisibility](#cfn-quicksight-dashboard-datetimepickercontroldisplayoptions-helpertextvisibility): {{String}}
  [InfoIconLabelOptions](#cfn-quicksight-dashboard-datetimepickercontroldisplayoptions-infoiconlabeloptions): {{
    SheetControlInfoIconLabelOptions}}
  [TitleOptions](#cfn-quicksight-dashboard-datetimepickercontroldisplayoptions-titleoptions): {{
    LabelOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-datetimepickercontroldisplayoptions-properties"></a>

`DateIconVisibility`  <a name="cfn-quicksight-dashboard-datetimepickercontroldisplayoptions-dateiconvisibility"></a>
The date icon visibility of the `DateTimePickerControlDisplayOptions`.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DateTimeFormat`  <a name="cfn-quicksight-dashboard-datetimepickercontroldisplayoptions-datetimeformat"></a>
Customize how dates are formatted in controls.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HelperTextVisibility`  <a name="cfn-quicksight-dashboard-datetimepickercontroldisplayoptions-helpertextvisibility"></a>
The helper text visibility of the `DateTimePickerControlDisplayOptions`.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InfoIconLabelOptions`  <a name="cfn-quicksight-dashboard-datetimepickercontroldisplayoptions-infoiconlabeloptions"></a>
The configuration of info icon label options.
*Required*: No
*Type*: [SheetControlInfoIconLabelOptions](aws-properties-quicksight-dashboard-sheetcontrolinfoiconlabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TitleOptions`  <a name="cfn-quicksight-dashboard-datetimepickercontroldisplayoptions-titleoptions"></a>
The options to configure the title visibility, name, and font size.
*Required*: No
*Type*: [LabelOptions](aws-properties-quicksight-dashboard-labeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
