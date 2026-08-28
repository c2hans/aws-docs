---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-filtercontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FilterControl
<a name="aws-properties-quicksight-analysis-filtercontrol"></a>

The control of a filter that is used to interact with a dashboard or an analysis.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-analysis-filtercontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-filtercontrol-syntax.json"></a>

```
{
  "[CrossSheet](#cfn-quicksight-analysis-filtercontrol-crosssheet)" : {{FilterCrossSheetControl}},
  "[DateTimePicker](#cfn-quicksight-analysis-filtercontrol-datetimepicker)" : {{FilterDateTimePickerControl}},
  "[Dropdown](#cfn-quicksight-analysis-filtercontrol-dropdown)" : {{FilterDropDownControl}},
  "[List](#cfn-quicksight-analysis-filtercontrol-list)" : {{FilterListControl}},
  "[RelativeDateTime](#cfn-quicksight-analysis-filtercontrol-relativedatetime)" : {{FilterRelativeDateTimeControl}},
  "[Slider](#cfn-quicksight-analysis-filtercontrol-slider)" : {{FilterSliderControl}},
  "[TextArea](#cfn-quicksight-analysis-filtercontrol-textarea)" : {{FilterTextAreaControl}},
  "[TextField](#cfn-quicksight-analysis-filtercontrol-textfield)" : {{FilterTextFieldControl}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-filtercontrol-syntax.yaml"></a>

```
  [CrossSheet](#cfn-quicksight-analysis-filtercontrol-crosssheet): {{
    FilterCrossSheetControl}}
  [DateTimePicker](#cfn-quicksight-analysis-filtercontrol-datetimepicker): {{
    FilterDateTimePickerControl}}
  [Dropdown](#cfn-quicksight-analysis-filtercontrol-dropdown): {{
    FilterDropDownControl}}
  [List](#cfn-quicksight-analysis-filtercontrol-list): {{
    FilterListControl}}
  [RelativeDateTime](#cfn-quicksight-analysis-filtercontrol-relativedatetime): {{
    FilterRelativeDateTimeControl}}
  [Slider](#cfn-quicksight-analysis-filtercontrol-slider): {{
    FilterSliderControl}}
  [TextArea](#cfn-quicksight-analysis-filtercontrol-textarea): {{
    FilterTextAreaControl}}
  [TextField](#cfn-quicksight-analysis-filtercontrol-textfield): {{
    FilterTextFieldControl}}
```

## Properties
<a name="aws-properties-quicksight-analysis-filtercontrol-properties"></a>

`CrossSheet`  <a name="cfn-quicksight-analysis-filtercontrol-crosssheet"></a>
A control from a filter that is scoped across more than one sheet. This represents your filter control on a sheet
*Required*: No
*Type*: [FilterCrossSheetControl](aws-properties-quicksight-analysis-filtercrosssheetcontrol.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DateTimePicker`  <a name="cfn-quicksight-analysis-filtercontrol-datetimepicker"></a>
A control from a date filter that is used to specify date and time.
*Required*: No
*Type*: [FilterDateTimePickerControl](aws-properties-quicksight-analysis-filterdatetimepickercontrol.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dropdown`  <a name="cfn-quicksight-analysis-filtercontrol-dropdown"></a>
A control to display a dropdown list with buttons that are used to select a single value.
*Required*: No
*Type*: [FilterDropDownControl](aws-properties-quicksight-analysis-filterdropdowncontrol.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`List`  <a name="cfn-quicksight-analysis-filtercontrol-list"></a>
A control to display a list of buttons or boxes. This is used to select either a single value or multiple values.
*Required*: No
*Type*: [FilterListControl](aws-properties-quicksight-analysis-filterlistcontrol.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RelativeDateTime`  <a name="cfn-quicksight-analysis-filtercontrol-relativedatetime"></a>
A control from a date filter that is used to specify the relative date.
*Required*: No
*Type*: [FilterRelativeDateTimeControl](aws-properties-quicksight-analysis-filterrelativedatetimecontrol.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Slider`  <a name="cfn-quicksight-analysis-filtercontrol-slider"></a>
A control to display a horizontal toggle bar. This is used to change a value by sliding the toggle.
*Required*: No
*Type*: [FilterSliderControl](aws-properties-quicksight-analysis-filterslidercontrol.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextArea`  <a name="cfn-quicksight-analysis-filtercontrol-textarea"></a>
A control to display a text box that is used to enter multiple entries.
*Required*: No
*Type*: [FilterTextAreaControl](aws-properties-quicksight-analysis-filtertextareacontrol.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextField`  <a name="cfn-quicksight-analysis-filtercontrol-textfield"></a>
A control to display a text box that is used to enter a single entry.
*Required*: No
*Type*: [FilterTextFieldControl](aws-properties-quicksight-analysis-filtertextfieldcontrol.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
