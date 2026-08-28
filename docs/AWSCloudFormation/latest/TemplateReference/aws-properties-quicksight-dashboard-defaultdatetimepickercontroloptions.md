---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-defaultdatetimepickercontroloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DefaultDateTimePickerControlOptions
<a name="aws-properties-quicksight-dashboard-defaultdatetimepickercontroloptions"></a>

The default options that correspond to the filter control type of a `DateTimePicker`.

## Syntax
<a name="aws-properties-quicksight-dashboard-defaultdatetimepickercontroloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-defaultdatetimepickercontroloptions-syntax.json"></a>

```
{
  "[CommitMode](#cfn-quicksight-dashboard-defaultdatetimepickercontroloptions-commitmode)" : {{String}},
  "[DisplayOptions](#cfn-quicksight-dashboard-defaultdatetimepickercontroloptions-displayoptions)" : {{DateTimePickerControlDisplayOptions}},
  "[Type](#cfn-quicksight-dashboard-defaultdatetimepickercontroloptions-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-defaultdatetimepickercontroloptions-syntax.yaml"></a>

```
  [CommitMode](#cfn-quicksight-dashboard-defaultdatetimepickercontroloptions-commitmode): {{String}}
  [DisplayOptions](#cfn-quicksight-dashboard-defaultdatetimepickercontroloptions-displayoptions): {{
    DateTimePickerControlDisplayOptions}}
  [Type](#cfn-quicksight-dashboard-defaultdatetimepickercontroloptions-type): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-defaultdatetimepickercontroloptions-properties"></a>

`CommitMode`  <a name="cfn-quicksight-dashboard-defaultdatetimepickercontroloptions-commitmode"></a>
The visibility configuration of the Apply button on a `DateTimePickerControl`.
*Required*: No
*Type*: String
*Allowed values*: `AUTO | MANUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayOptions`  <a name="cfn-quicksight-dashboard-defaultdatetimepickercontroloptions-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [DateTimePickerControlDisplayOptions](aws-properties-quicksight-dashboard-datetimepickercontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-dashboard-defaultdatetimepickercontroloptions-type"></a>
The date time picker type of the `DefaultDateTimePickerControlOptions`. Choose one of the following options:
+ `SINGLE_VALUED`: The filter condition is a fixed date.
+ `DATE_RANGE`: The filter condition is a date time range.
*Required*: No
*Type*: String
*Allowed values*: `SINGLE_VALUED | DATE_RANGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
