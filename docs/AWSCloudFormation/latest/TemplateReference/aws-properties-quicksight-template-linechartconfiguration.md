---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-linechartconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template LineChartConfiguration
<a name="aws-properties-quicksight-template-linechartconfiguration"></a>

The configuration of a line chart.

## Syntax
<a name="aws-properties-quicksight-template-linechartconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-linechartconfiguration-syntax.json"></a>

```
{
  "[ContributionAnalysisDefaults](#cfn-quicksight-template-linechartconfiguration-contributionanalysisdefaults)" : {{[ ContributionAnalysisDefault, ... ]}},
  "[DataLabels](#cfn-quicksight-template-linechartconfiguration-datalabels)" : {{DataLabelOptions}},
  "[DefaultSeriesSettings](#cfn-quicksight-template-linechartconfiguration-defaultseriessettings)" : {{LineChartDefaultSeriesSettings}},
  "[FieldWells](#cfn-quicksight-template-linechartconfiguration-fieldwells)" : {{LineChartFieldWells}},
  "[ForecastConfigurations](#cfn-quicksight-template-linechartconfiguration-forecastconfigurations)" : {{[ ForecastConfiguration, ... ]}},
  "[Interactions](#cfn-quicksight-template-linechartconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[Legend](#cfn-quicksight-template-linechartconfiguration-legend)" : {{LegendOptions}},
  "[PrimaryYAxisDisplayOptions](#cfn-quicksight-template-linechartconfiguration-primaryyaxisdisplayoptions)" : {{LineSeriesAxisDisplayOptions}},
  "[PrimaryYAxisLabelOptions](#cfn-quicksight-template-linechartconfiguration-primaryyaxislabeloptions)" : {{ChartAxisLabelOptions}},
  "[ReferenceLines](#cfn-quicksight-template-linechartconfiguration-referencelines)" : {{[ ReferenceLine, ... ]}},
  "[SecondaryYAxisDisplayOptions](#cfn-quicksight-template-linechartconfiguration-secondaryyaxisdisplayoptions)" : {{LineSeriesAxisDisplayOptions}},
  "[SecondaryYAxisLabelOptions](#cfn-quicksight-template-linechartconfiguration-secondaryyaxislabeloptions)" : {{ChartAxisLabelOptions}},
  "[Series](#cfn-quicksight-template-linechartconfiguration-series)" : {{[ SeriesItem, ... ]}},
  "[SingleAxisOptions](#cfn-quicksight-template-linechartconfiguration-singleaxisoptions)" : {{SingleAxisOptions}},
  "[SmallMultiplesOptions](#cfn-quicksight-template-linechartconfiguration-smallmultiplesoptions)" : {{SmallMultiplesOptions}},
  "[SortConfiguration](#cfn-quicksight-template-linechartconfiguration-sortconfiguration)" : {{LineChartSortConfiguration}},
  "[Tooltip](#cfn-quicksight-template-linechartconfiguration-tooltip)" : {{TooltipOptions}},
  "[Type](#cfn-quicksight-template-linechartconfiguration-type)" : {{String}},
  "[VisualPalette](#cfn-quicksight-template-linechartconfiguration-visualpalette)" : {{VisualPalette}},
  "[XAxisDisplayOptions](#cfn-quicksight-template-linechartconfiguration-xaxisdisplayoptions)" : {{AxisDisplayOptions}},
  "[XAxisLabelOptions](#cfn-quicksight-template-linechartconfiguration-xaxislabeloptions)" : {{ChartAxisLabelOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-template-linechartconfiguration-syntax.yaml"></a>

```
  [ContributionAnalysisDefaults](#cfn-quicksight-template-linechartconfiguration-contributionanalysisdefaults): {{
    - ContributionAnalysisDefault}}
  [DataLabels](#cfn-quicksight-template-linechartconfiguration-datalabels): {{
    DataLabelOptions}}
  [DefaultSeriesSettings](#cfn-quicksight-template-linechartconfiguration-defaultseriessettings): {{
    LineChartDefaultSeriesSettings}}
  [FieldWells](#cfn-quicksight-template-linechartconfiguration-fieldwells): {{
    LineChartFieldWells}}
  [ForecastConfigurations](#cfn-quicksight-template-linechartconfiguration-forecastconfigurations): {{
    - ForecastConfiguration}}
  [Interactions](#cfn-quicksight-template-linechartconfiguration-interactions): {{
    VisualInteractionOptions}}
  [Legend](#cfn-quicksight-template-linechartconfiguration-legend): {{
    LegendOptions}}
  [PrimaryYAxisDisplayOptions](#cfn-quicksight-template-linechartconfiguration-primaryyaxisdisplayoptions): {{
    LineSeriesAxisDisplayOptions}}
  [PrimaryYAxisLabelOptions](#cfn-quicksight-template-linechartconfiguration-primaryyaxislabeloptions): {{
    ChartAxisLabelOptions}}
  [ReferenceLines](#cfn-quicksight-template-linechartconfiguration-referencelines): {{
    - ReferenceLine}}
  [SecondaryYAxisDisplayOptions](#cfn-quicksight-template-linechartconfiguration-secondaryyaxisdisplayoptions): {{
    LineSeriesAxisDisplayOptions}}
  [SecondaryYAxisLabelOptions](#cfn-quicksight-template-linechartconfiguration-secondaryyaxislabeloptions): {{
    ChartAxisLabelOptions}}
  [Series](#cfn-quicksight-template-linechartconfiguration-series): {{
    - SeriesItem}}
  [SingleAxisOptions](#cfn-quicksight-template-linechartconfiguration-singleaxisoptions): {{
    SingleAxisOptions}}
  [SmallMultiplesOptions](#cfn-quicksight-template-linechartconfiguration-smallmultiplesoptions): {{
    SmallMultiplesOptions}}
  [SortConfiguration](#cfn-quicksight-template-linechartconfiguration-sortconfiguration): {{
    LineChartSortConfiguration}}
  [Tooltip](#cfn-quicksight-template-linechartconfiguration-tooltip): {{
    TooltipOptions}}
  [Type](#cfn-quicksight-template-linechartconfiguration-type): {{String}}
  [VisualPalette](#cfn-quicksight-template-linechartconfiguration-visualpalette): {{
    VisualPalette}}
  [XAxisDisplayOptions](#cfn-quicksight-template-linechartconfiguration-xaxisdisplayoptions): {{
    AxisDisplayOptions}}
  [XAxisLabelOptions](#cfn-quicksight-template-linechartconfiguration-xaxislabeloptions): {{
    ChartAxisLabelOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-linechartconfiguration-properties"></a>

`ContributionAnalysisDefaults`  <a name="cfn-quicksight-template-linechartconfiguration-contributionanalysisdefaults"></a>
The default configuration of a line chart's contribution analysis.
*Required*: No
*Type*: Array of [ContributionAnalysisDefault](aws-properties-quicksight-template-contributionanalysisdefault.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataLabels`  <a name="cfn-quicksight-template-linechartconfiguration-datalabels"></a>
The data label configuration of a line chart.
*Required*: No
*Type*: [DataLabelOptions](aws-properties-quicksight-template-datalabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultSeriesSettings`  <a name="cfn-quicksight-template-linechartconfiguration-defaultseriessettings"></a>
The options that determine the default presentation of all line series in `LineChartVisual`.
*Required*: No
*Type*: [LineChartDefaultSeriesSettings](aws-properties-quicksight-template-linechartdefaultseriessettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldWells`  <a name="cfn-quicksight-template-linechartconfiguration-fieldwells"></a>
The field well configuration of a line chart.
*Required*: No
*Type*: [LineChartFieldWells](aws-properties-quicksight-template-linechartfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ForecastConfigurations`  <a name="cfn-quicksight-template-linechartconfiguration-forecastconfigurations"></a>
The forecast configuration of a line chart.
*Required*: No
*Type*: Array of [ForecastConfiguration](aws-properties-quicksight-template-forecastconfiguration.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-template-linechartconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-template-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Legend`  <a name="cfn-quicksight-template-linechartconfiguration-legend"></a>
The legend configuration of a line chart.
*Required*: No
*Type*: [LegendOptions](aws-properties-quicksight-template-legendoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryYAxisDisplayOptions`  <a name="cfn-quicksight-template-linechartconfiguration-primaryyaxisdisplayoptions"></a>
The series axis configuration of a line chart.
*Required*: No
*Type*: [LineSeriesAxisDisplayOptions](aws-properties-quicksight-template-lineseriesaxisdisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryYAxisLabelOptions`  <a name="cfn-quicksight-template-linechartconfiguration-primaryyaxislabeloptions"></a>
The options that determine the presentation of the y-axis label.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-template-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReferenceLines`  <a name="cfn-quicksight-template-linechartconfiguration-referencelines"></a>
The reference lines configuration of a line chart.
*Required*: No
*Type*: Array of [ReferenceLine](aws-properties-quicksight-template-referenceline.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecondaryYAxisDisplayOptions`  <a name="cfn-quicksight-template-linechartconfiguration-secondaryyaxisdisplayoptions"></a>
The series axis configuration of a line chart.
*Required*: No
*Type*: [LineSeriesAxisDisplayOptions](aws-properties-quicksight-template-lineseriesaxisdisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecondaryYAxisLabelOptions`  <a name="cfn-quicksight-template-linechartconfiguration-secondaryyaxislabeloptions"></a>
The options that determine the presentation of the secondary y-axis label.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-template-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Series`  <a name="cfn-quicksight-template-linechartconfiguration-series"></a>
The series item configuration of a line chart.
*Required*: No
*Type*: Array of [SeriesItem](aws-properties-quicksight-template-seriesitem.md)
*Minimum*: `0`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SingleAxisOptions`  <a name="cfn-quicksight-template-linechartconfiguration-singleaxisoptions"></a>
Property description not available.
*Required*: No
*Type*: [SingleAxisOptions](aws-properties-quicksight-template-singleaxisoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmallMultiplesOptions`  <a name="cfn-quicksight-template-linechartconfiguration-smallmultiplesoptions"></a>
The small multiples setup for the visual.
*Required*: No
*Type*: [SmallMultiplesOptions](aws-properties-quicksight-template-smallmultiplesoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-template-linechartconfiguration-sortconfiguration"></a>
The sort configuration of a line chart.
*Required*: No
*Type*: [LineChartSortConfiguration](aws-properties-quicksight-template-linechartsortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tooltip`  <a name="cfn-quicksight-template-linechartconfiguration-tooltip"></a>
The tooltip configuration of a line chart.
*Required*: No
*Type*: [TooltipOptions](aws-properties-quicksight-template-tooltipoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-template-linechartconfiguration-type"></a>
Determines the type of the line chart.
*Required*: No
*Type*: String
*Allowed values*: `LINE | AREA | STACKED_AREA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualPalette`  <a name="cfn-quicksight-template-linechartconfiguration-visualpalette"></a>
The visual palette configuration of a line chart.
*Required*: No
*Type*: [VisualPalette](aws-properties-quicksight-template-visualpalette.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`XAxisDisplayOptions`  <a name="cfn-quicksight-template-linechartconfiguration-xaxisdisplayoptions"></a>
The options that determine the presentation of the x-axis.
*Required*: No
*Type*: [AxisDisplayOptions](aws-properties-quicksight-template-axisdisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`XAxisLabelOptions`  <a name="cfn-quicksight-template-linechartconfiguration-xaxislabeloptions"></a>
The options that determine the presentation of the x-axis label.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-template-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
