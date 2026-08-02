---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-filterdatetimepickercontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard FilterDateTimePickerControl
<a name="aws-properties-quicksight-dashboard-filterdatetimepickercontrol"></a>

A control from a date filter that is used to specify date and time.

## Syntax
<a name="aws-properties-quicksight-dashboard-filterdatetimepickercontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-filterdatetimepickercontrol-syntax.json"></a>

```
{
  "[CommitMode](#cfn-quicksight-dashboard-filterdatetimepickercontrol-commitmode)" : {{String}},
  "[DisplayOptions](#cfn-quicksight-dashboard-filterdatetimepickercontrol-displayoptions)" : {{DateTimePickerControlDisplayOptions}},
  "[FilterControlId](#cfn-quicksight-dashboard-filterdatetimepickercontrol-filtercontrolid)" : {{String}},
  "[SourceFilterId](#cfn-quicksight-dashboard-filterdatetimepickercontrol-sourcefilterid)" : {{String}},
  "[Title](#cfn-quicksight-dashboard-filterdatetimepickercontrol-title)" : {{String}},
  "[Type](#cfn-quicksight-dashboard-filterdatetimepickercontrol-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-filterdatetimepickercontrol-syntax.yaml"></a>

```
  [CommitMode](#cfn-quicksight-dashboard-filterdatetimepickercontrol-commitmode): {{String}}
  [DisplayOptions](#cfn-quicksight-dashboard-filterdatetimepickercontrol-displayoptions): {{
    DateTimePickerControlDisplayOptions}}
  [FilterControlId](#cfn-quicksight-dashboard-filterdatetimepickercontrol-filtercontrolid): {{String}}
  [SourceFilterId](#cfn-quicksight-dashboard-filterdatetimepickercontrol-sourcefilterid): {{String}}
  [Title](#cfn-quicksight-dashboard-filterdatetimepickercontrol-title): {{String}}
  [Type](#cfn-quicksight-dashboard-filterdatetimepickercontrol-type): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-filterdatetimepickercontrol-properties"></a>

`CommitMode`  <a name="cfn-quicksight-dashboard-filterdatetimepickercontrol-commitmode"></a>
The visibility configurationof the Apply button on a `DateTimePickerControl`.
*Required*: No
*Type*: String
*Allowed values*: `AUTO | MANUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayOptions`  <a name="cfn-quicksight-dashboard-filterdatetimepickercontrol-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [DateTimePickerControlDisplayOptions](aws-properties-quicksight-dashboard-datetimepickercontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterControlId`  <a name="cfn-quicksight-dashboard-filterdatetimepickercontrol-filtercontrolid"></a>
The ID of the `FilterDateTimePickerControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceFilterId`  <a name="cfn-quicksight-dashboard-filterdatetimepickercontrol-sourcefilterid"></a>
The source filter ID of the `FilterDateTimePickerControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-dashboard-filterdatetimepickercontrol-title"></a>
The title of the `FilterDateTimePickerControl`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-dashboard-filterdatetimepickercontrol-type"></a>
The type of the `FilterDropDownControl`. Choose one of the following options:
+ `MULTI_SELECT`: The user can select multiple entries from a dropdown menu.
+ `SINGLE_SELECT`: The user can select a single entry from a dropdown menu.
*Required*: No
*Type*: String
*Allowed values*: `SINGLE_VALUED | DATE_RANGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
