---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-defaultrelativedatetimecontroloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DefaultRelativeDateTimeControlOptions
<a name="aws-properties-quicksight-dashboard-defaultrelativedatetimecontroloptions"></a>

The default options that correspond to the `RelativeDateTime` filter control type.

## Syntax
<a name="aws-properties-quicksight-dashboard-defaultrelativedatetimecontroloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-defaultrelativedatetimecontroloptions-syntax.json"></a>

```
{
  "[CommitMode](#cfn-quicksight-dashboard-defaultrelativedatetimecontroloptions-commitmode)" : {{String}},
  "[DisplayOptions](#cfn-quicksight-dashboard-defaultrelativedatetimecontroloptions-displayoptions)" : {{RelativeDateTimeControlDisplayOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-defaultrelativedatetimecontroloptions-syntax.yaml"></a>

```
  [CommitMode](#cfn-quicksight-dashboard-defaultrelativedatetimecontroloptions-commitmode): {{String}}
  [DisplayOptions](#cfn-quicksight-dashboard-defaultrelativedatetimecontroloptions-displayoptions): {{
    RelativeDateTimeControlDisplayOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-defaultrelativedatetimecontroloptions-properties"></a>

`CommitMode`  <a name="cfn-quicksight-dashboard-defaultrelativedatetimecontroloptions-commitmode"></a>
The visibility configuration of the Apply button on a `RelativeDateTimeControl`.
*Required*: No
*Type*: String
*Allowed values*: `AUTO | MANUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayOptions`  <a name="cfn-quicksight-dashboard-defaultrelativedatetimecontroloptions-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [RelativeDateTimeControlDisplayOptions](aws-properties-quicksight-dashboard-relativedatetimecontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
