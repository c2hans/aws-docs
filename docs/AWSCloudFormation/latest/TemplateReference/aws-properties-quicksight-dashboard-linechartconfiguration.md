---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-linechartconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard LineChartConfiguration
<a name="aws-properties-quicksight-dashboard-linechartconfiguration"></a>

The configuration of a line chart.

## Syntax
<a name="aws-properties-quicksight-dashboard-linechartconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-linechartconfiguration-syntax.json"></a>

```
{
  "[ContributionAnalysisDefaults](#cfn-quicksight-dashboard-linechartconfiguration-contributionanalysisdefaults)" : {{[ ContributionAnalysisDefault, ... ]}},
  "[DataLabels](#cfn-quicksight-dashboard-linechartconfiguration-datalabels)" : {{DataLabelOptions}},
  "[DefaultSeriesSettings](#cfn-quicksight-dashboard-linechartconfiguration-defaultseriessettings)" : {{LineChartDefaultSeriesSettings}},
  "[FieldWells](#cfn-quicksight-dashboard-linechartconfiguration-fieldwells)" : {{LineChartFieldWells}},
  "[ForecastConfigurations](#cfn-quicksight-dashboard-linechartconfiguration-forecastconfigurations)" : {{[ ForecastConfiguration, ... ]}},
  "[Interactions](#cfn-quicksight-dashboard-linechartconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[Legend](#cfn-quicksight-dashboard-linechartconfiguration-legend)" : {{LegendOptions}},
  "[PrimaryYAxisDisplayOptions](#cfn-quicksight-dashboard-linechartconfiguration-primaryyaxisdisplayoptions)" : {{LineSeriesAxisDisplayOptions}},
  "[PrimaryYAxisLabelOptions](#cfn-quicksight-dashboard-linechartconfiguration-primaryyaxislabeloptions)" : {{ChartAxisLabelOptions}},
  "[ReferenceLines](#cfn-quicksight-dashboard-linechartconfiguration-referencelines)" : {{[ ReferenceLine, ... ]}},
  "[SecondaryYAxisDisplayOptions](#cfn-quicksight-dashboard-linechartconfiguration-secondaryyaxisdisplayoptions)" : {{LineSeriesAxisDisplayOptions}},
  "[SecondaryYAxisLabelOptions](#cfn-quicksight-dashboard-linechartconfiguration-secondaryyaxislabeloptions)" : {{ChartAxisLabelOptions}},
  "[Series](#cfn-quicksight-dashboard-linechartconfiguration-series)" : {{[ SeriesItem, ... ]}},
  "[SingleAxisOptions](#cfn-quicksight-dashboard-linechartconfiguration-singleaxisoptions)" : {{SingleAxisOptions}},
  "[SmallMultiplesOptions](#cfn-quicksight-dashboard-linechartconfiguration-smallmultiplesoptions)" : {{SmallMultiplesOptions}},
  "[SortConfiguration](#cfn-quicksight-dashboard-linechartconfiguration-sortconfiguration)" : {{LineChartSortConfiguration}},
  "[Tooltip](#cfn-quicksight-dashboard-linechartconfiguration-tooltip)" : {{TooltipOptions}},
  "[Type](#cfn-quicksight-dashboard-linechartconfiguration-type)" : {{String}},
  "[VisualPalette](#cfn-quicksight-dashboard-linechartconfiguration-visualpalette)" : {{VisualPalette}},
  "[XAxisDisplayOptions](#cfn-quicksight-dashboard-linechartconfiguration-xaxisdisplayoptions)" : {{AxisDisplayOptions}},
  "[XAxisLabelOptions](#cfn-quicksight-dashboard-linechartconfiguration-xaxislabeloptions)" : {{ChartAxisLabelOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-linechartconfiguration-syntax.yaml"></a>

```
  [ContributionAnalysisDefaults](#cfn-quicksight-dashboard-linechartconfiguration-contributionanalysisdefaults): {{
    - ContributionAnalysisDefault}}
  [DataLabels](#cfn-quicksight-dashboard-linechartconfiguration-datalabels): {{
    DataLabelOptions}}
  [DefaultSeriesSettings](#cfn-quicksight-dashboard-linechartconfiguration-defaultseriessettings): {{
    LineChartDefaultSeriesSettings}}
  [FieldWells](#cfn-quicksight-dashboard-linechartconfiguration-fieldwells): {{
    LineChartFieldWells}}
  [ForecastConfigurations](#cfn-quicksight-dashboard-linechartconfiguration-forecastconfigurations): {{
    - ForecastConfiguration}}
  [Interactions](#cfn-quicksight-dashboard-linechartconfiguration-interactions): {{
    VisualInteractionOptions}}
  [Legend](#cfn-quicksight-dashboard-linechartconfiguration-legend): {{
    LegendOptions}}
  [PrimaryYAxisDisplayOptions](#cfn-quicksight-dashboard-linechartconfiguration-primaryyaxisdisplayoptions): {{
    LineSeriesAxisDisplayOptions}}
  [PrimaryYAxisLabelOptions](#cfn-quicksight-dashboard-linechartconfiguration-primaryyaxislabeloptions): {{
    ChartAxisLabelOptions}}
  [ReferenceLines](#cfn-quicksight-dashboard-linechartconfiguration-referencelines): {{
    - ReferenceLine}}
  [SecondaryYAxisDisplayOptions](#cfn-quicksight-dashboard-linechartconfiguration-secondaryyaxisdisplayoptions): {{
    LineSeriesAxisDisplayOptions}}
  [SecondaryYAxisLabelOptions](#cfn-quicksight-dashboard-linechartconfiguration-secondaryyaxislabeloptions): {{
    ChartAxisLabelOptions}}
  [Series](#cfn-quicksight-dashboard-linechartconfiguration-series): {{
    - SeriesItem}}
  [SingleAxisOptions](#cfn-quicksight-dashboard-linechartconfiguration-singleaxisoptions): {{
    SingleAxisOptions}}
  [SmallMultiplesOptions](#cfn-quicksight-dashboard-linechartconfiguration-smallmultiplesoptions): {{
    SmallMultiplesOptions}}
  [SortConfiguration](#cfn-quicksight-dashboard-linechartconfiguration-sortconfiguration): {{
    LineChartSortConfiguration}}
  [Tooltip](#cfn-quicksight-dashboard-linechartconfiguration-tooltip): {{
    TooltipOptions}}
  [Type](#cfn-quicksight-dashboard-linechartconfiguration-type): {{String}}
  [VisualPalette](#cfn-quicksight-dashboard-linechartconfiguration-visualpalette): {{
    VisualPalette}}
  [XAxisDisplayOptions](#cfn-quicksight-dashboard-linechartconfiguration-xaxisdisplayoptions): {{
    AxisDisplayOptions}}
  [XAxisLabelOptions](#cfn-quicksight-dashboard-linechartconfiguration-xaxislabeloptions): {{
    ChartAxisLabelOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-linechartconfiguration-properties"></a>

`ContributionAnalysisDefaults`  <a name="cfn-quicksight-dashboard-linechartconfiguration-contributionanalysisdefaults"></a>
The default configuration of a line chart's contribution analysis.
*Required*: No
*Type*: Array of [ContributionAnalysisDefault](aws-properties-quicksight-dashboard-contributionanalysisdefault.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataLabels`  <a name="cfn-quicksight-dashboard-linechartconfiguration-datalabels"></a>
The data label configuration of a line chart.
*Required*: No
*Type*: [DataLabelOptions](aws-properties-quicksight-dashboard-datalabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultSeriesSettings`  <a name="cfn-quicksight-dashboard-linechartconfiguration-defaultseriessettings"></a>
The options that determine the default presentation of all line series in `LineChartVisual`.
*Required*: No
*Type*: [LineChartDefaultSeriesSettings](aws-properties-quicksight-dashboard-linechartdefaultseriessettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldWells`  <a name="cfn-quicksight-dashboard-linechartconfiguration-fieldwells"></a>
The field well configuration of a line chart.
*Required*: No
*Type*: [LineChartFieldWells](aws-properties-quicksight-dashboard-linechartfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ForecastConfigurations`  <a name="cfn-quicksight-dashboard-linechartconfiguration-forecastconfigurations"></a>
The forecast configuration of a line chart.
*Required*: No
*Type*: Array of [ForecastConfiguration](aws-properties-quicksight-dashboard-forecastconfiguration.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-dashboard-linechartconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-dashboard-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Legend`  <a name="cfn-quicksight-dashboard-linechartconfiguration-legend"></a>
The legend configuration of a line chart.
*Required*: No
*Type*: [LegendOptions](aws-properties-quicksight-dashboard-legendoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryYAxisDisplayOptions`  <a name="cfn-quicksight-dashboard-linechartconfiguration-primaryyaxisdisplayoptions"></a>
The series axis configuration of a line chart.
*Required*: No
*Type*: [LineSeriesAxisDisplayOptions](aws-properties-quicksight-dashboard-lineseriesaxisdisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryYAxisLabelOptions`  <a name="cfn-quicksight-dashboard-linechartconfiguration-primaryyaxislabeloptions"></a>
The options that determine the presentation of the y-axis label.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-dashboard-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReferenceLines`  <a name="cfn-quicksight-dashboard-linechartconfiguration-referencelines"></a>
The reference lines configuration of a line chart.
*Required*: No
*Type*: Array of [ReferenceLine](aws-properties-quicksight-dashboard-referenceline.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecondaryYAxisDisplayOptions`  <a name="cfn-quicksight-dashboard-linechartconfiguration-secondaryyaxisdisplayoptions"></a>
The series axis configuration of a line chart.
*Required*: No
*Type*: [LineSeriesAxisDisplayOptions](aws-properties-quicksight-dashboard-lineseriesaxisdisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecondaryYAxisLabelOptions`  <a name="cfn-quicksight-dashboard-linechartconfiguration-secondaryyaxislabeloptions"></a>
The options that determine the presentation of the secondary y-axis label.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-dashboard-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Series`  <a name="cfn-quicksight-dashboard-linechartconfiguration-series"></a>
The series item configuration of a line chart.
*Required*: No
*Type*: Array of [SeriesItem](aws-properties-quicksight-dashboard-seriesitem.md)
*Minimum*: `0`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SingleAxisOptions`  <a name="cfn-quicksight-dashboard-linechartconfiguration-singleaxisoptions"></a>
Property description not available.
*Required*: No
*Type*: [SingleAxisOptions](aws-properties-quicksight-dashboard-singleaxisoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmallMultiplesOptions`  <a name="cfn-quicksight-dashboard-linechartconfiguration-smallmultiplesoptions"></a>
The small multiples setup for the visual.
*Required*: No
*Type*: [SmallMultiplesOptions](aws-properties-quicksight-dashboard-smallmultiplesoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-dashboard-linechartconfiguration-sortconfiguration"></a>
The sort configuration of a line chart.
*Required*: No
*Type*: [LineChartSortConfiguration](aws-properties-quicksight-dashboard-linechartsortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tooltip`  <a name="cfn-quicksight-dashboard-linechartconfiguration-tooltip"></a>
The tooltip configuration of a line chart.
*Required*: No
*Type*: [TooltipOptions](aws-properties-quicksight-dashboard-tooltipoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-dashboard-linechartconfiguration-type"></a>
Determines the type of the line chart.
*Required*: No
*Type*: String
*Allowed values*: `LINE | AREA | STACKED_AREA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualPalette`  <a name="cfn-quicksight-dashboard-linechartconfiguration-visualpalette"></a>
The visual palette configuration of a line chart.
*Required*: No
*Type*: [VisualPalette](aws-properties-quicksight-dashboard-visualpalette.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`XAxisDisplayOptions`  <a name="cfn-quicksight-dashboard-linechartconfiguration-xaxisdisplayoptions"></a>
The options that determine the presentation of the x-axis.
*Required*: No
*Type*: [AxisDisplayOptions](aws-properties-quicksight-dashboard-axisdisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`XAxisLabelOptions`  <a name="cfn-quicksight-dashboard-linechartconfiguration-xaxislabeloptions"></a>
The options that determine the presentation of the x-axis label.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-dashboard-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
