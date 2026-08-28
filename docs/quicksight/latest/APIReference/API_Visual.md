---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Visual.html
---

# Visual
<a name="API_Visual"></a>

A visual displayed on a sheet in an analysis, dashboard, or template.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_Visual_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BarChartVisual **   <a name="QS-Type-Visual-BarChartVisual"></a>
A bar chart.
For more information, see [Using bar charts](https://docs.aws.amazon.com/quicksight/latest/user/bar-charts.html) in the *Amazon Quick Suite User Guide*.
Type: [BarChartVisual](API_BarChartVisual.md) object
Required: No

 ** BoxPlotVisual **   <a name="QS-Type-Visual-BoxPlotVisual"></a>
A box plot.
For more information, see [Using box plots](https://docs.aws.amazon.com/quicksight/latest/user/box-plots.html) in the *Amazon Quick Suite User Guide*.
Type: [BoxPlotVisual](API_BoxPlotVisual.md) object
Required: No

 ** ComboChartVisual **   <a name="QS-Type-Visual-ComboChartVisual"></a>
A combo chart.
For more information, see [Using combo charts](https://docs.aws.amazon.com/quicksight/latest/user/combo-charts.html) in the *Amazon Quick Suite User Guide*.
Type: [ComboChartVisual](API_ComboChartVisual.md) object
Required: No

 ** CustomContentVisual **   <a name="QS-Type-Visual-CustomContentVisual"></a>
A visual that contains custom content.
For more information, see [Using custom visual content](https://docs.aws.amazon.com/quicksight/latest/user/custom-visual-content.html) in the *Amazon Quick Suite User Guide*.
Type: [CustomContentVisual](API_CustomContentVisual.md) object
Required: No

 ** EmptyVisual **   <a name="QS-Type-Visual-EmptyVisual"></a>
An empty visual.
Type: [EmptyVisual](API_EmptyVisual.md) object
Required: No

 ** FilledMapVisual **   <a name="QS-Type-Visual-FilledMapVisual"></a>
A filled map.
For more information, see [Creating filled maps](https://docs.aws.amazon.com/quicksight/latest/user/filled-maps.html) in the *Amazon Quick Suite User Guide*.
Type: [FilledMapVisual](API_FilledMapVisual.md) object
Required: No

 ** FunnelChartVisual **   <a name="QS-Type-Visual-FunnelChartVisual"></a>
A funnel chart.
For more information, see [Using funnel charts](https://docs.aws.amazon.com/quicksight/latest/user/funnel-visual-content.html) in the *Amazon Quick Suite User Guide*.
Type: [FunnelChartVisual](API_FunnelChartVisual.md) object
Required: No

 ** GaugeChartVisual **   <a name="QS-Type-Visual-GaugeChartVisual"></a>
A gauge chart.
For more information, see [Using gauge charts](https://docs.aws.amazon.com/quicksight/latest/user/gauge-chart.html) in the *Amazon Quick Suite User Guide*.
Type: [GaugeChartVisual](API_GaugeChartVisual.md) object
Required: No

 ** GeospatialMapVisual **   <a name="QS-Type-Visual-GeospatialMapVisual"></a>
A geospatial map or a points on map visual.
For more information, see [Creating point maps](https://docs.aws.amazon.com/quicksight/latest/user/point-maps.html) in the *Amazon Quick Suite User Guide*.
Type: [GeospatialMapVisual](API_GeospatialMapVisual.md) object
Required: No

 ** HeatMapVisual **   <a name="QS-Type-Visual-HeatMapVisual"></a>
A heat map.
For more information, see [Using heat maps](https://docs.aws.amazon.com/quicksight/latest/user/heat-map.html) in the *Amazon Quick Suite User Guide*.
Type: [HeatMapVisual](API_HeatMapVisual.md) object
Required: No

 ** HistogramVisual **   <a name="QS-Type-Visual-HistogramVisual"></a>
A histogram.
For more information, see [Using histograms](https://docs.aws.amazon.com/quicksight/latest/user/histogram-charts.html) in the *Amazon Quick Suite User Guide*.
Type: [HistogramVisual](API_HistogramVisual.md) object
Required: No

 ** InsightVisual **   <a name="QS-Type-Visual-InsightVisual"></a>
An insight visual.
For more information, see [Working with insights](https://docs.aws.amazon.com/quicksight/latest/user/computational-insights.html) in the *Amazon Quick Suite User Guide*.
Type: [InsightVisual](API_InsightVisual.md) object
Required: No

 ** KPIVisual **   <a name="QS-Type-Visual-KPIVisual"></a>
A key performance indicator (KPI).
For more information, see [Using KPIs](https://docs.aws.amazon.com/quicksight/latest/user/kpi.html) in the *Amazon Quick Suite User Guide*.
Type: [KPIVisual](API_KPIVisual.md) object
Required: No

 ** LayerMapVisual **   <a name="QS-Type-Visual-LayerMapVisual"></a>
The properties for a layer map visual
Type: [LayerMapVisual](API_LayerMapVisual.md) object
Required: No

 ** LineChartVisual **   <a name="QS-Type-Visual-LineChartVisual"></a>
A line chart.
For more information, see [Using line charts](https://docs.aws.amazon.com/quicksight/latest/user/line-charts.html) in the *Amazon Quick Suite User Guide*.
Type: [LineChartVisual](API_LineChartVisual.md) object
Required: No

 ** PieChartVisual **   <a name="QS-Type-Visual-PieChartVisual"></a>
A pie or donut chart.
For more information, see [Using pie charts](https://docs.aws.amazon.com/quicksight/latest/user/pie-chart.html) in the *Amazon Quick Suite User Guide*.
Type: [PieChartVisual](API_PieChartVisual.md) object
Required: No

 ** PivotTableVisual **   <a name="QS-Type-Visual-PivotTableVisual"></a>
A pivot table.
For more information, see [Using pivot tables](https://docs.aws.amazon.com/quicksight/latest/user/pivot-table.html) in the *Amazon Quick Suite User Guide*.
Type: [PivotTableVisual](API_PivotTableVisual.md) object
Required: No

 ** PluginVisual **   <a name="QS-Type-Visual-PluginVisual"></a>
The custom plugin visual type.
Type: [PluginVisual](API_PluginVisual.md) object
Required: No

 ** RadarChartVisual **   <a name="QS-Type-Visual-RadarChartVisual"></a>
A radar chart visual.
For more information, see [Using radar charts](https://docs.aws.amazon.com/quicksight/latest/user/radar-chart.html) in the *Amazon Quick Suite User Guide*.
Type: [RadarChartVisual](API_RadarChartVisual.md) object
Required: No

 ** SankeyDiagramVisual **   <a name="QS-Type-Visual-SankeyDiagramVisual"></a>
A sankey diagram.
For more information, see [Using Sankey diagrams](https://docs.aws.amazon.com/quicksight/latest/user/sankey-diagram.html) in the *Amazon Quick Suite User Guide*.
Type: [SankeyDiagramVisual](API_SankeyDiagramVisual.md) object
Required: No

 ** ScatterPlotVisual **   <a name="QS-Type-Visual-ScatterPlotVisual"></a>
A scatter plot.
For more information, see [Using scatter plots](https://docs.aws.amazon.com/quicksight/latest/user/scatter-plot.html) in the *Amazon Quick Suite User Guide*.
Type: [ScatterPlotVisual](API_ScatterPlotVisual.md) object
Required: No

 ** TableVisual **   <a name="QS-Type-Visual-TableVisual"></a>
A table visual.
For more information, see [Using tables as visuals](https://docs.aws.amazon.com/quicksight/latest/user/tabular.html) in the *Amazon Quick Suite User Guide*.
Type: [TableVisual](API_TableVisual.md) object
Required: No

 ** TreeMapVisual **   <a name="QS-Type-Visual-TreeMapVisual"></a>
A tree map.
For more information, see [Using tree maps](https://docs.aws.amazon.com/quicksight/latest/user/tree-map.html) in the *Amazon Quick Suite User Guide*.
Type: [TreeMapVisual](API_TreeMapVisual.md) object
Required: No

 ** WaterfallVisual **   <a name="QS-Type-Visual-WaterfallVisual"></a>
A waterfall chart.
For more information, see [Using waterfall charts](https://docs.aws.amazon.com/quicksight/latest/user/waterfall-chart.html) in the *Amazon Quick Suite User Guide*.
Type: [WaterfallVisual](API_WaterfallVisual.md) object
Required: No

 ** WordCloudVisual **   <a name="QS-Type-Visual-WordCloudVisual"></a>
A word cloud.
For more information, see [Using word clouds](https://docs.aws.amazon.com/quicksight/latest/user/word-cloud.html) in the *Amazon Quick Suite User Guide*.
Type: [WordCloudVisual](API_WordCloudVisual.md) object
Required: No

## See Also
<a name="API_Visual_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/Visual)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/Visual)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/Visual)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
