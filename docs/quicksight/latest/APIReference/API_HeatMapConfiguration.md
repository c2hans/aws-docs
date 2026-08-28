---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_HeatMapConfiguration.html
---

# HeatMapConfiguration
<a name="API_HeatMapConfiguration"></a>

The configuration of a heat map.

## Contents
<a name="API_HeatMapConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColorScale **   <a name="QS-Type-HeatMapConfiguration-ColorScale"></a>
The color options (gradient color, point of divergence) in a heat map.
Type: [ColorScale](API_ColorScale.md) object
Required: No

 ** ColumnAxisDisplayOptions **   <a name="QS-Type-HeatMapConfiguration-ColumnAxisDisplayOptions"></a>
The options that determine the presentation of the row axis label.
Type: [AxisDisplayOptions](API_AxisDisplayOptions.md) object
Required: No

 ** ColumnLabelOptions **   <a name="QS-Type-HeatMapConfiguration-ColumnLabelOptions"></a>
The label options of the column that is displayed in a heat map.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

 ** DataLabels **   <a name="QS-Type-HeatMapConfiguration-DataLabels"></a>
The options that determine if visual data labels are displayed.
Type: [DataLabelOptions](API_DataLabelOptions.md) object
Required: No

 ** FieldWells **   <a name="QS-Type-HeatMapConfiguration-FieldWells"></a>
The field wells of the visual.
Type: [HeatMapFieldWells](API_HeatMapFieldWells.md) object
Required: No

 ** Interactions **   <a name="QS-Type-HeatMapConfiguration-Interactions"></a>
The general visual interactions setup for a visual.
Type: [VisualInteractionOptions](API_VisualInteractionOptions.md) object
Required: No

 ** Legend **   <a name="QS-Type-HeatMapConfiguration-Legend"></a>
The legend display setup of the visual.
Type: [LegendOptions](API_LegendOptions.md) object
Required: No

 ** RowAxisDisplayOptions **   <a name="QS-Type-HeatMapConfiguration-RowAxisDisplayOptions"></a>
The options that determine the presentation of the row axis label.
Type: [AxisDisplayOptions](API_AxisDisplayOptions.md) object
Required: No

 ** RowLabelOptions **   <a name="QS-Type-HeatMapConfiguration-RowLabelOptions"></a>
The label options of the row that is displayed in a `heat map`.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

 ** SortConfiguration **   <a name="QS-Type-HeatMapConfiguration-SortConfiguration"></a>
The sort configuration of a heat map.
Type: [HeatMapSortConfiguration](API_HeatMapSortConfiguration.md) object
Required: No

 ** Tooltip **   <a name="QS-Type-HeatMapConfiguration-Tooltip"></a>
The tooltip display setup of the visual.
Type: [TooltipOptions](API_TooltipOptions.md) object
Required: No

## See Also
<a name="API_HeatMapConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/HeatMapConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/HeatMapConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/HeatMapConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
