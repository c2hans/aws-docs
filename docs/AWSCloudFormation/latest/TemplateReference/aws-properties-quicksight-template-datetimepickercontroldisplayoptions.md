---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-datetimepickercontroldisplayoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DateTimePickerControlDisplayOptions
<a name="aws-properties-quicksight-template-datetimepickercontroldisplayoptions"></a>

The display options of a control.

## Syntax
<a name="aws-properties-quicksight-template-datetimepickercontroldisplayoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-datetimepickercontroldisplayoptions-syntax.json"></a>

```
{
  "[DateIconVisibility](#cfn-quicksight-template-datetimepickercontroldisplayoptions-dateiconvisibility)" : {{String}},
  "[DateTimeFormat](#cfn-quicksight-template-datetimepickercontroldisplayoptions-datetimeformat)" : {{String}},
  "[HelperTextVisibility](#cfn-quicksight-template-datetimepickercontroldisplayoptions-helpertextvisibility)" : {{String}},
  "[InfoIconLabelOptions](#cfn-quicksight-template-datetimepickercontroldisplayoptions-infoiconlabeloptions)" : {{SheetControlInfoIconLabelOptions}},
  "[TitleOptions](#cfn-quicksight-template-datetimepickercontroldisplayoptions-titleoptions)" : {{LabelOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-template-datetimepickercontroldisplayoptions-syntax.yaml"></a>

```
  [DateIconVisibility](#cfn-quicksight-template-datetimepickercontroldisplayoptions-dateiconvisibility): {{String}}
  [DateTimeFormat](#cfn-quicksight-template-datetimepickercontroldisplayoptions-datetimeformat): {{String}}
  [HelperTextVisibility](#cfn-quicksight-template-datetimepickercontroldisplayoptions-helpertextvisibility): {{String}}
  [InfoIconLabelOptions](#cfn-quicksight-template-datetimepickercontroldisplayoptions-infoiconlabeloptions): {{
    SheetControlInfoIconLabelOptions}}
  [TitleOptions](#cfn-quicksight-template-datetimepickercontroldisplayoptions-titleoptions): {{
    LabelOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-datetimepickercontroldisplayoptions-properties"></a>

`DateIconVisibility`  <a name="cfn-quicksight-template-datetimepickercontroldisplayoptions-dateiconvisibility"></a>
The date icon visibility of the `DateTimePickerControlDisplayOptions`.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DateTimeFormat`  <a name="cfn-quicksight-template-datetimepickercontroldisplayoptions-datetimeformat"></a>
Customize how dates are formatted in controls.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HelperTextVisibility`  <a name="cfn-quicksight-template-datetimepickercontroldisplayoptions-helpertextvisibility"></a>
The helper text visibility of the `DateTimePickerControlDisplayOptions`.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InfoIconLabelOptions`  <a name="cfn-quicksight-template-datetimepickercontroldisplayoptions-infoiconlabeloptions"></a>
The configuration of info icon label options.
*Required*: No
*Type*: [SheetControlInfoIconLabelOptions](aws-properties-quicksight-template-sheetcontrolinfoiconlabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TitleOptions`  <a name="cfn-quicksight-template-datetimepickercontroldisplayoptions-titleoptions"></a>
The options to configure the title visibility, name, and font size.
*Required*: No
*Type*: [LabelOptions](aws-properties-quicksight-template-labeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
