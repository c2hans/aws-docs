---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-barchartdefaultseriessettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard BarChartDefaultSeriesSettings
<a name="aws-properties-quicksight-dashboard-barchartdefaultseriessettings"></a>

The options that determine the default presentation of all bar series in `BarChartVisual`.

## Syntax
<a name="aws-properties-quicksight-dashboard-barchartdefaultseriessettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-barchartdefaultseriessettings-syntax.json"></a>

```
{
  "[BorderSettings](#cfn-quicksight-dashboard-barchartdefaultseriessettings-bordersettings)" : {{BorderSettings}},
  "[DecalSettings](#cfn-quicksight-dashboard-barchartdefaultseriessettings-decalsettings)" : {{DecalSettings}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-barchartdefaultseriessettings-syntax.yaml"></a>

```
  [BorderSettings](#cfn-quicksight-dashboard-barchartdefaultseriessettings-bordersettings): {{
    BorderSettings}}
  [DecalSettings](#cfn-quicksight-dashboard-barchartdefaultseriessettings-decalsettings): {{
    DecalSettings}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-barchartdefaultseriessettings-properties"></a>

`BorderSettings`  <a name="cfn-quicksight-dashboard-barchartdefaultseriessettings-bordersettings"></a>
Border settings for all bar series in the visual.
*Required*: No
*Type*: [BorderSettings](aws-properties-quicksight-dashboard-bordersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DecalSettings`  <a name="cfn-quicksight-dashboard-barchartdefaultseriessettings-decalsettings"></a>
Decal settings for all bar series in the visual.
*Required*: No
*Type*: [DecalSettings](aws-properties-quicksight-dashboard-decalsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
