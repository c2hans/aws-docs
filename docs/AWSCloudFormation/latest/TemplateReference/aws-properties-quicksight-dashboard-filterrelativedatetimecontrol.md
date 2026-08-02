---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-filterrelativedatetimecontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard FilterRelativeDateTimeControl
<a name="aws-properties-quicksight-dashboard-filterrelativedatetimecontrol"></a>

A control from a date filter that is used to specify the relative date.

## Syntax
<a name="aws-properties-quicksight-dashboard-filterrelativedatetimecontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-filterrelativedatetimecontrol-syntax.json"></a>

```
{
  "[CommitMode](#cfn-quicksight-dashboard-filterrelativedatetimecontrol-commitmode)" : {{String}},
  "[DisplayOptions](#cfn-quicksight-dashboard-filterrelativedatetimecontrol-displayoptions)" : {{RelativeDateTimeControlDisplayOptions}},
  "[FilterControlId](#cfn-quicksight-dashboard-filterrelativedatetimecontrol-filtercontrolid)" : {{String}},
  "[SourceFilterId](#cfn-quicksight-dashboard-filterrelativedatetimecontrol-sourcefilterid)" : {{String}},
  "[Title](#cfn-quicksight-dashboard-filterrelativedatetimecontrol-title)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-filterrelativedatetimecontrol-syntax.yaml"></a>

```
  [CommitMode](#cfn-quicksight-dashboard-filterrelativedatetimecontrol-commitmode): {{String}}
  [DisplayOptions](#cfn-quicksight-dashboard-filterrelativedatetimecontrol-displayoptions): {{
    RelativeDateTimeControlDisplayOptions}}
  [FilterControlId](#cfn-quicksight-dashboard-filterrelativedatetimecontrol-filtercontrolid): {{String}}
  [SourceFilterId](#cfn-quicksight-dashboard-filterrelativedatetimecontrol-sourcefilterid): {{String}}
  [Title](#cfn-quicksight-dashboard-filterrelativedatetimecontrol-title): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-filterrelativedatetimecontrol-properties"></a>

`CommitMode`  <a name="cfn-quicksight-dashboard-filterrelativedatetimecontrol-commitmode"></a>
The visibility configuration of the Apply button on a `FilterRelativeDateTimeControl`.
*Required*: No
*Type*: String
*Allowed values*: `AUTO | MANUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayOptions`  <a name="cfn-quicksight-dashboard-filterrelativedatetimecontrol-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [RelativeDateTimeControlDisplayOptions](aws-properties-quicksight-dashboard-relativedatetimecontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterControlId`  <a name="cfn-quicksight-dashboard-filterrelativedatetimecontrol-filtercontrolid"></a>
The ID of the `FilterTextAreaControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceFilterId`  <a name="cfn-quicksight-dashboard-filterrelativedatetimecontrol-sourcefilterid"></a>
The source filter ID of the `FilterTextAreaControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-dashboard-filterrelativedatetimecontrol-title"></a>
The title of the `FilterTextAreaControl`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
