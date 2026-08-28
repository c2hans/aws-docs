---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-defaultfiltercontroloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DefaultFilterControlOptions
<a name="aws-properties-quicksight-template-defaultfiltercontroloptions"></a>

The option that corresponds to the control type of the filter.

## Syntax
<a name="aws-properties-quicksight-template-defaultfiltercontroloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-defaultfiltercontroloptions-syntax.json"></a>

```
{
  "[DefaultDateTimePickerOptions](#cfn-quicksight-template-defaultfiltercontroloptions-defaultdatetimepickeroptions)" : {{DefaultDateTimePickerControlOptions}},
  "[DefaultDropdownOptions](#cfn-quicksight-template-defaultfiltercontroloptions-defaultdropdownoptions)" : {{DefaultFilterDropDownControlOptions}},
  "[DefaultListOptions](#cfn-quicksight-template-defaultfiltercontroloptions-defaultlistoptions)" : {{DefaultFilterListControlOptions}},
  "[DefaultRelativeDateTimeOptions](#cfn-quicksight-template-defaultfiltercontroloptions-defaultrelativedatetimeoptions)" : {{DefaultRelativeDateTimeControlOptions}},
  "[DefaultSliderOptions](#cfn-quicksight-template-defaultfiltercontroloptions-defaultslideroptions)" : {{DefaultSliderControlOptions}},
  "[DefaultTextAreaOptions](#cfn-quicksight-template-defaultfiltercontroloptions-defaulttextareaoptions)" : {{DefaultTextAreaControlOptions}},
  "[DefaultTextFieldOptions](#cfn-quicksight-template-defaultfiltercontroloptions-defaulttextfieldoptions)" : {{DefaultTextFieldControlOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-template-defaultfiltercontroloptions-syntax.yaml"></a>

```
  [DefaultDateTimePickerOptions](#cfn-quicksight-template-defaultfiltercontroloptions-defaultdatetimepickeroptions): {{
    DefaultDateTimePickerControlOptions}}
  [DefaultDropdownOptions](#cfn-quicksight-template-defaultfiltercontroloptions-defaultdropdownoptions): {{
    DefaultFilterDropDownControlOptions}}
  [DefaultListOptions](#cfn-quicksight-template-defaultfiltercontroloptions-defaultlistoptions): {{
    DefaultFilterListControlOptions}}
  [DefaultRelativeDateTimeOptions](#cfn-quicksight-template-defaultfiltercontroloptions-defaultrelativedatetimeoptions): {{
    DefaultRelativeDateTimeControlOptions}}
  [DefaultSliderOptions](#cfn-quicksight-template-defaultfiltercontroloptions-defaultslideroptions): {{
    DefaultSliderControlOptions}}
  [DefaultTextAreaOptions](#cfn-quicksight-template-defaultfiltercontroloptions-defaulttextareaoptions): {{
    DefaultTextAreaControlOptions}}
  [DefaultTextFieldOptions](#cfn-quicksight-template-defaultfiltercontroloptions-defaulttextfieldoptions): {{
    DefaultTextFieldControlOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-defaultfiltercontroloptions-properties"></a>

`DefaultDateTimePickerOptions`  <a name="cfn-quicksight-template-defaultfiltercontroloptions-defaultdatetimepickeroptions"></a>
The default options that correspond to the filter control type of a `DateTimePicker`.
*Required*: No
*Type*: [DefaultDateTimePickerControlOptions](aws-properties-quicksight-template-defaultdatetimepickercontroloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultDropdownOptions`  <a name="cfn-quicksight-template-defaultfiltercontroloptions-defaultdropdownoptions"></a>
The default options that correspond to the `Dropdown` filter control type.
*Required*: No
*Type*: [DefaultFilterDropDownControlOptions](aws-properties-quicksight-template-defaultfilterdropdowncontroloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultListOptions`  <a name="cfn-quicksight-template-defaultfiltercontroloptions-defaultlistoptions"></a>
The default options that correspond to the `List` filter control type.
*Required*: No
*Type*: [DefaultFilterListControlOptions](aws-properties-quicksight-template-defaultfilterlistcontroloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultRelativeDateTimeOptions`  <a name="cfn-quicksight-template-defaultfiltercontroloptions-defaultrelativedatetimeoptions"></a>
The default options that correspond to the `RelativeDateTime` filter control type.
*Required*: No
*Type*: [DefaultRelativeDateTimeControlOptions](aws-properties-quicksight-template-defaultrelativedatetimecontroloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultSliderOptions`  <a name="cfn-quicksight-template-defaultfiltercontroloptions-defaultslideroptions"></a>
The default options that correspond to the `Slider` filter control type.
*Required*: No
*Type*: [DefaultSliderControlOptions](aws-properties-quicksight-template-defaultslidercontroloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultTextAreaOptions`  <a name="cfn-quicksight-template-defaultfiltercontroloptions-defaulttextareaoptions"></a>
The default options that correspond to the `TextArea` filter control type.
*Required*: No
*Type*: [DefaultTextAreaControlOptions](aws-properties-quicksight-template-defaulttextareacontroloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultTextFieldOptions`  <a name="cfn-quicksight-template-defaultfiltercontroloptions-defaulttextfieldoptions"></a>
The default options that correspond to the `TextField` filter control type.
*Required*: No
*Type*: [DefaultTextFieldControlOptions](aws-properties-quicksight-template-defaulttextfieldcontroloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
