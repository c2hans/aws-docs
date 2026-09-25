---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-barchartdefaultseriessettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template BarChartDefaultSeriesSettings
<a name="aws-properties-quicksight-template-barchartdefaultseriessettings"></a>

The options that determine the default presentation of all bar series in `BarChartVisual`.

## Syntax
<a name="aws-properties-quicksight-template-barchartdefaultseriessettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-barchartdefaultseriessettings-syntax.json"></a>

```
{
  "[BorderSettings](#cfn-quicksight-template-barchartdefaultseriessettings-bordersettings)" : {{BorderSettings}},
  "[DecalSettings](#cfn-quicksight-template-barchartdefaultseriessettings-decalsettings)" : {{DecalSettings}}
}
```

### YAML
<a name="aws-properties-quicksight-template-barchartdefaultseriessettings-syntax.yaml"></a>

```
  [BorderSettings](#cfn-quicksight-template-barchartdefaultseriessettings-bordersettings): {{
    BorderSettings}}
  [DecalSettings](#cfn-quicksight-template-barchartdefaultseriessettings-decalsettings): {{
    DecalSettings}}
```

## Properties
<a name="aws-properties-quicksight-template-barchartdefaultseriessettings-properties"></a>

`BorderSettings`  <a name="cfn-quicksight-template-barchartdefaultseriessettings-bordersettings"></a>
Border settings for all bar series in the visual.
*Required*: No
*Type*: [BorderSettings](aws-properties-quicksight-template-bordersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DecalSettings`  <a name="cfn-quicksight-template-barchartdefaultseriessettings-decalsettings"></a>
Decal settings for all bar series in the visual.
*Required*: No
*Type*: [DecalSettings](aws-properties-quicksight-template-decalsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
