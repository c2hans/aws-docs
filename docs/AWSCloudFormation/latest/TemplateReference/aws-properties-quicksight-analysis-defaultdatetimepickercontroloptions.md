---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-defaultdatetimepickercontroloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis DefaultDateTimePickerControlOptions
<a name="aws-properties-quicksight-analysis-defaultdatetimepickercontroloptions"></a>

The default options that correspond to the filter control type of a `DateTimePicker`.

## Syntax
<a name="aws-properties-quicksight-analysis-defaultdatetimepickercontroloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-defaultdatetimepickercontroloptions-syntax.json"></a>

```
{
  "[CommitMode](#cfn-quicksight-analysis-defaultdatetimepickercontroloptions-commitmode)" : {{String}},
  "[DisplayOptions](#cfn-quicksight-analysis-defaultdatetimepickercontroloptions-displayoptions)" : {{DateTimePickerControlDisplayOptions}},
  "[Type](#cfn-quicksight-analysis-defaultdatetimepickercontroloptions-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-defaultdatetimepickercontroloptions-syntax.yaml"></a>

```
  [CommitMode](#cfn-quicksight-analysis-defaultdatetimepickercontroloptions-commitmode): {{String}}
  [DisplayOptions](#cfn-quicksight-analysis-defaultdatetimepickercontroloptions-displayoptions): {{
    DateTimePickerControlDisplayOptions}}
  [Type](#cfn-quicksight-analysis-defaultdatetimepickercontroloptions-type): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-defaultdatetimepickercontroloptions-properties"></a>

`CommitMode`  <a name="cfn-quicksight-analysis-defaultdatetimepickercontroloptions-commitmode"></a>
The visibility configuration of the Apply button on a `DateTimePickerControl`.
*Required*: No
*Type*: String
*Allowed values*: `AUTO | MANUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayOptions`  <a name="cfn-quicksight-analysis-defaultdatetimepickercontroloptions-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [DateTimePickerControlDisplayOptions](aws-properties-quicksight-analysis-datetimepickercontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-analysis-defaultdatetimepickercontroloptions-type"></a>
The date time picker type of the `DefaultDateTimePickerControlOptions`. Choose one of the following options:
+ `SINGLE_VALUED`: The filter condition is a fixed date.
+ `DATE_RANGE`: The filter condition is a date time range.
*Required*: No
*Type*: String
*Allowed values*: `SINGLE_VALUED | DATE_RANGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
