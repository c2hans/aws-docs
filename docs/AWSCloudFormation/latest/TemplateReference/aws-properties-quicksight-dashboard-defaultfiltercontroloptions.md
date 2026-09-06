---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-defaultfiltercontroloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DefaultFilterControlOptions
<a name="aws-properties-quicksight-dashboard-defaultfiltercontroloptions"></a>

The option that corresponds to the control type of the filter.

## Syntax
<a name="aws-properties-quicksight-dashboard-defaultfiltercontroloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-defaultfiltercontroloptions-syntax.json"></a>

```
{
  "[DefaultDateTimePickerOptions](#cfn-quicksight-dashboard-defaultfiltercontroloptions-defaultdatetimepickeroptions)" : {{DefaultDateTimePickerControlOptions}},
  "[DefaultDropdownOptions](#cfn-quicksight-dashboard-defaultfiltercontroloptions-defaultdropdownoptions)" : {{DefaultFilterDropDownControlOptions}},
  "[DefaultListOptions](#cfn-quicksight-dashboard-defaultfiltercontroloptions-defaultlistoptions)" : {{DefaultFilterListControlOptions}},
  "[DefaultRelativeDateTimeOptions](#cfn-quicksight-dashboard-defaultfiltercontroloptions-defaultrelativedatetimeoptions)" : {{DefaultRelativeDateTimeControlOptions}},
  "[DefaultSliderOptions](#cfn-quicksight-dashboard-defaultfiltercontroloptions-defaultslideroptions)" : {{DefaultSliderControlOptions}},
  "[DefaultTextAreaOptions](#cfn-quicksight-dashboard-defaultfiltercontroloptions-defaulttextareaoptions)" : {{DefaultTextAreaControlOptions}},
  "[DefaultTextFieldOptions](#cfn-quicksight-dashboard-defaultfiltercontroloptions-defaulttextfieldoptions)" : {{DefaultTextFieldControlOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-defaultfiltercontroloptions-syntax.yaml"></a>

```
  [DefaultDateTimePickerOptions](#cfn-quicksight-dashboard-defaultfiltercontroloptions-defaultdatetimepickeroptions): {{
    DefaultDateTimePickerControlOptions}}
  [DefaultDropdownOptions](#cfn-quicksight-dashboard-defaultfiltercontroloptions-defaultdropdownoptions): {{
    DefaultFilterDropDownControlOptions}}
  [DefaultListOptions](#cfn-quicksight-dashboard-defaultfiltercontroloptions-defaultlistoptions): {{
    DefaultFilterListControlOptions}}
  [DefaultRelativeDateTimeOptions](#cfn-quicksight-dashboard-defaultfiltercontroloptions-defaultrelativedatetimeoptions): {{
    DefaultRelativeDateTimeControlOptions}}
  [DefaultSliderOptions](#cfn-quicksight-dashboard-defaultfiltercontroloptions-defaultslideroptions): {{
    DefaultSliderControlOptions}}
  [DefaultTextAreaOptions](#cfn-quicksight-dashboard-defaultfiltercontroloptions-defaulttextareaoptions): {{
    DefaultTextAreaControlOptions}}
  [DefaultTextFieldOptions](#cfn-quicksight-dashboard-defaultfiltercontroloptions-defaulttextfieldoptions): {{
    DefaultTextFieldControlOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-defaultfiltercontroloptions-properties"></a>

`DefaultDateTimePickerOptions`  <a name="cfn-quicksight-dashboard-defaultfiltercontroloptions-defaultdatetimepickeroptions"></a>
The default options that correspond to the filter control type of a `DateTimePicker`.
*Required*: No
*Type*: [DefaultDateTimePickerControlOptions](aws-properties-quicksight-dashboard-defaultdatetimepickercontroloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultDropdownOptions`  <a name="cfn-quicksight-dashboard-defaultfiltercontroloptions-defaultdropdownoptions"></a>
The default options that correspond to the `Dropdown` filter control type.
*Required*: No
*Type*: [DefaultFilterDropDownControlOptions](aws-properties-quicksight-dashboard-defaultfilterdropdowncontroloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultListOptions`  <a name="cfn-quicksight-dashboard-defaultfiltercontroloptions-defaultlistoptions"></a>
The default options that correspond to the `List` filter control type.
*Required*: No
*Type*: [DefaultFilterListControlOptions](aws-properties-quicksight-dashboard-defaultfilterlistcontroloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultRelativeDateTimeOptions`  <a name="cfn-quicksight-dashboard-defaultfiltercontroloptions-defaultrelativedatetimeoptions"></a>
The default options that correspond to the `RelativeDateTime` filter control type.
*Required*: No
*Type*: [DefaultRelativeDateTimeControlOptions](aws-properties-quicksight-dashboard-defaultrelativedatetimecontroloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultSliderOptions`  <a name="cfn-quicksight-dashboard-defaultfiltercontroloptions-defaultslideroptions"></a>
The default options that correspond to the `Slider` filter control type.
*Required*: No
*Type*: [DefaultSliderControlOptions](aws-properties-quicksight-dashboard-defaultslidercontroloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultTextAreaOptions`  <a name="cfn-quicksight-dashboard-defaultfiltercontroloptions-defaulttextareaoptions"></a>
The default options that correspond to the `TextArea` filter control type.
*Required*: No
*Type*: [DefaultTextAreaControlOptions](aws-properties-quicksight-dashboard-defaulttextareacontroloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultTextFieldOptions`  <a name="cfn-quicksight-dashboard-defaultfiltercontroloptions-defaulttextfieldoptions"></a>
The default options that correspond to the `TextField` filter control type.
*Required*: No
*Type*: [DefaultTextFieldControlOptions](aws-properties-quicksight-dashboard-defaulttextfieldcontroloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
