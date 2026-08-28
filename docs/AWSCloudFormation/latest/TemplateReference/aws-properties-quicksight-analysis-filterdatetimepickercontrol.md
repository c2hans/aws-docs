---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-filterdatetimepickercontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FilterDateTimePickerControl
<a name="aws-properties-quicksight-analysis-filterdatetimepickercontrol"></a>

A control from a date filter that is used to specify date and time.

## Syntax
<a name="aws-properties-quicksight-analysis-filterdatetimepickercontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-filterdatetimepickercontrol-syntax.json"></a>

```
{
  "[CommitMode](#cfn-quicksight-analysis-filterdatetimepickercontrol-commitmode)" : {{String}},
  "[DisplayOptions](#cfn-quicksight-analysis-filterdatetimepickercontrol-displayoptions)" : {{DateTimePickerControlDisplayOptions}},
  "[FilterControlId](#cfn-quicksight-analysis-filterdatetimepickercontrol-filtercontrolid)" : {{String}},
  "[SourceFilterId](#cfn-quicksight-analysis-filterdatetimepickercontrol-sourcefilterid)" : {{String}},
  "[Title](#cfn-quicksight-analysis-filterdatetimepickercontrol-title)" : {{String}},
  "[Type](#cfn-quicksight-analysis-filterdatetimepickercontrol-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-filterdatetimepickercontrol-syntax.yaml"></a>

```
  [CommitMode](#cfn-quicksight-analysis-filterdatetimepickercontrol-commitmode): {{String}}
  [DisplayOptions](#cfn-quicksight-analysis-filterdatetimepickercontrol-displayoptions): {{
    DateTimePickerControlDisplayOptions}}
  [FilterControlId](#cfn-quicksight-analysis-filterdatetimepickercontrol-filtercontrolid): {{String}}
  [SourceFilterId](#cfn-quicksight-analysis-filterdatetimepickercontrol-sourcefilterid): {{String}}
  [Title](#cfn-quicksight-analysis-filterdatetimepickercontrol-title): {{String}}
  [Type](#cfn-quicksight-analysis-filterdatetimepickercontrol-type): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-filterdatetimepickercontrol-properties"></a>

`CommitMode`  <a name="cfn-quicksight-analysis-filterdatetimepickercontrol-commitmode"></a>
The visibility configurationof the Apply button on a `DateTimePickerControl`.
*Required*: No
*Type*: String
*Allowed values*: `AUTO | MANUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayOptions`  <a name="cfn-quicksight-analysis-filterdatetimepickercontrol-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [DateTimePickerControlDisplayOptions](aws-properties-quicksight-analysis-datetimepickercontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterControlId`  <a name="cfn-quicksight-analysis-filterdatetimepickercontrol-filtercontrolid"></a>
The ID of the `FilterDateTimePickerControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceFilterId`  <a name="cfn-quicksight-analysis-filterdatetimepickercontrol-sourcefilterid"></a>
The source filter ID of the `FilterDateTimePickerControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-analysis-filterdatetimepickercontrol-title"></a>
The title of the `FilterDateTimePickerControl`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-analysis-filterdatetimepickercontrol-type"></a>
The type of the `FilterDropDownControl`. Choose one of the following options:
+ `MULTI_SELECT`: The user can select multiple entries from a dropdown menu.
+ `SINGLE_SELECT`: The user can select a single entry from a dropdown menu.
*Required*: No
*Type*: String
*Allowed values*: `SINGLE_VALUED | DATE_RANGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
