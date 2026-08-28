---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-radarchartconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template RadarChartConfiguration
<a name="aws-properties-quicksight-template-radarchartconfiguration"></a>

The configuration of a `RadarChartVisual`.

## Syntax
<a name="aws-properties-quicksight-template-radarchartconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-radarchartconfiguration-syntax.json"></a>

```
{
  "[AlternateBandColorsVisibility](#cfn-quicksight-template-radarchartconfiguration-alternatebandcolorsvisibility)" : {{String}},
  "[AlternateBandEvenColor](#cfn-quicksight-template-radarchartconfiguration-alternatebandevencolor)" : {{String}},
  "[AlternateBandOddColor](#cfn-quicksight-template-radarchartconfiguration-alternatebandoddcolor)" : {{String}},
  "[AxesRangeScale](#cfn-quicksight-template-radarchartconfiguration-axesrangescale)" : {{String}},
  "[BaseSeriesSettings](#cfn-quicksight-template-radarchartconfiguration-baseseriessettings)" : {{RadarChartSeriesSettings}},
  "[CategoryAxis](#cfn-quicksight-template-radarchartconfiguration-categoryaxis)" : {{AxisDisplayOptions}},
  "[CategoryLabelOptions](#cfn-quicksight-template-radarchartconfiguration-categorylabeloptions)" : {{ChartAxisLabelOptions}},
  "[ColorAxis](#cfn-quicksight-template-radarchartconfiguration-coloraxis)" : {{AxisDisplayOptions}},
  "[ColorLabelOptions](#cfn-quicksight-template-radarchartconfiguration-colorlabeloptions)" : {{ChartAxisLabelOptions}},
  "[FieldWells](#cfn-quicksight-template-radarchartconfiguration-fieldwells)" : {{RadarChartFieldWells}},
  "[Interactions](#cfn-quicksight-template-radarchartconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[Legend](#cfn-quicksight-template-radarchartconfiguration-legend)" : {{LegendOptions}},
  "[Shape](#cfn-quicksight-template-radarchartconfiguration-shape)" : {{String}},
  "[SortConfiguration](#cfn-quicksight-template-radarchartconfiguration-sortconfiguration)" : {{RadarChartSortConfiguration}},
  "[StartAngle](#cfn-quicksight-template-radarchartconfiguration-startangle)" : {{Number}},
  "[VisualPalette](#cfn-quicksight-template-radarchartconfiguration-visualpalette)" : {{VisualPalette}}
}
```

### YAML
<a name="aws-properties-quicksight-template-radarchartconfiguration-syntax.yaml"></a>

```
  [AlternateBandColorsVisibility](#cfn-quicksight-template-radarchartconfiguration-alternatebandcolorsvisibility): {{String}}
  [AlternateBandEvenColor](#cfn-quicksight-template-radarchartconfiguration-alternatebandevencolor): {{String}}
  [AlternateBandOddColor](#cfn-quicksight-template-radarchartconfiguration-alternatebandoddcolor): {{String}}
  [AxesRangeScale](#cfn-quicksight-template-radarchartconfiguration-axesrangescale): {{String}}
  [BaseSeriesSettings](#cfn-quicksight-template-radarchartconfiguration-baseseriessettings): {{
    RadarChartSeriesSettings}}
  [CategoryAxis](#cfn-quicksight-template-radarchartconfiguration-categoryaxis): {{
    AxisDisplayOptions}}
  [CategoryLabelOptions](#cfn-quicksight-template-radarchartconfiguration-categorylabeloptions): {{
    ChartAxisLabelOptions}}
  [ColorAxis](#cfn-quicksight-template-radarchartconfiguration-coloraxis): {{
    AxisDisplayOptions}}
  [ColorLabelOptions](#cfn-quicksight-template-radarchartconfiguration-colorlabeloptions): {{
    ChartAxisLabelOptions}}
  [FieldWells](#cfn-quicksight-template-radarchartconfiguration-fieldwells): {{
    RadarChartFieldWells}}
  [Interactions](#cfn-quicksight-template-radarchartconfiguration-interactions): {{
    VisualInteractionOptions}}
  [Legend](#cfn-quicksight-template-radarchartconfiguration-legend): {{
    LegendOptions}}
  [Shape](#cfn-quicksight-template-radarchartconfiguration-shape): {{String}}
  [SortConfiguration](#cfn-quicksight-template-radarchartconfiguration-sortconfiguration): {{
    RadarChartSortConfiguration}}
  [StartAngle](#cfn-quicksight-template-radarchartconfiguration-startangle): {{Number}}
  [VisualPalette](#cfn-quicksight-template-radarchartconfiguration-visualpalette): {{
    VisualPalette}}
```

## Properties
<a name="aws-properties-quicksight-template-radarchartconfiguration-properties"></a>

`AlternateBandColorsVisibility`  <a name="cfn-quicksight-template-radarchartconfiguration-alternatebandcolorsvisibility"></a>
Determines the visibility of the colors of alternatign bands in a radar chart.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AlternateBandEvenColor`  <a name="cfn-quicksight-template-radarchartconfiguration-alternatebandevencolor"></a>
The color of the even-numbered alternate bands of a radar chart.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AlternateBandOddColor`  <a name="cfn-quicksight-template-radarchartconfiguration-alternatebandoddcolor"></a>
The color of the odd-numbered alternate bands of a radar chart.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AxesRangeScale`  <a name="cfn-quicksight-template-radarchartconfiguration-axesrangescale"></a>
The axis behavior options of a radar chart.
*Required*: No
*Type*: String
*Allowed values*: `AUTO | INDEPENDENT | SHARED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BaseSeriesSettings`  <a name="cfn-quicksight-template-radarchartconfiguration-baseseriessettings"></a>
The base sreies settings of a radar chart.
*Required*: No
*Type*: [RadarChartSeriesSettings](aws-properties-quicksight-template-radarchartseriessettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CategoryAxis`  <a name="cfn-quicksight-template-radarchartconfiguration-categoryaxis"></a>
The category axis of a radar chart.
*Required*: No
*Type*: [AxisDisplayOptions](aws-properties-quicksight-template-axisdisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CategoryLabelOptions`  <a name="cfn-quicksight-template-radarchartconfiguration-categorylabeloptions"></a>
The category label options of a radar chart.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-template-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorAxis`  <a name="cfn-quicksight-template-radarchartconfiguration-coloraxis"></a>
The color axis of a radar chart.
*Required*: No
*Type*: [AxisDisplayOptions](aws-properties-quicksight-template-axisdisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorLabelOptions`  <a name="cfn-quicksight-template-radarchartconfiguration-colorlabeloptions"></a>
The color label options of a radar chart.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-template-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldWells`  <a name="cfn-quicksight-template-radarchartconfiguration-fieldwells"></a>
The field well configuration of a `RadarChartVisual`.
*Required*: No
*Type*: [RadarChartFieldWells](aws-properties-quicksight-template-radarchartfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-template-radarchartconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-template-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Legend`  <a name="cfn-quicksight-template-radarchartconfiguration-legend"></a>
The legend display setup of the visual.
*Required*: No
*Type*: [LegendOptions](aws-properties-quicksight-template-legendoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Shape`  <a name="cfn-quicksight-template-radarchartconfiguration-shape"></a>
The shape of the radar chart.
*Required*: No
*Type*: String
*Allowed values*: `CIRCLE | POLYGON`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-template-radarchartconfiguration-sortconfiguration"></a>
The sort configuration of a `RadarChartVisual`.
*Required*: No
*Type*: [RadarChartSortConfiguration](aws-properties-quicksight-template-radarchartsortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartAngle`  <a name="cfn-quicksight-template-radarchartconfiguration-startangle"></a>
The start angle of a radar chart's axis.
*Required*: No
*Type*: Number
*Minimum*: `-360`
*Maximum*: `360`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualPalette`  <a name="cfn-quicksight-template-radarchartconfiguration-visualpalette"></a>
The palette (chart color) display setup of the visual.
*Required*: No
*Type*: [VisualPalette](aws-properties-quicksight-template-visualpalette.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
