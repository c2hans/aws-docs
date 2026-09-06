---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RadarChartConfiguration.html
---

# RadarChartConfiguration
<a name="API_RadarChartConfiguration"></a>

The configuration of a `RadarChartVisual`.

## Contents
<a name="API_RadarChartConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AlternateBandColorsVisibility **   <a name="QS-Type-RadarChartConfiguration-AlternateBandColorsVisibility"></a>
Determines the visibility of the colors of alternatign bands in a radar chart.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** AlternateBandEvenColor **   <a name="QS-Type-RadarChartConfiguration-AlternateBandEvenColor"></a>
The color of the even-numbered alternate bands of a radar chart.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** AlternateBandOddColor **   <a name="QS-Type-RadarChartConfiguration-AlternateBandOddColor"></a>
The color of the odd-numbered alternate bands of a radar chart.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** AxesRangeScale **   <a name="QS-Type-RadarChartConfiguration-AxesRangeScale"></a>
The axis behavior options of a radar chart.
Type: String
Valid Values: `AUTO | INDEPENDENT | SHARED`
Required: No

 ** BaseSeriesSettings **   <a name="QS-Type-RadarChartConfiguration-BaseSeriesSettings"></a>
The base sreies settings of a radar chart.
Type: [RadarChartSeriesSettings](API_RadarChartSeriesSettings.md) object
Required: No

 ** CategoryAxis **   <a name="QS-Type-RadarChartConfiguration-CategoryAxis"></a>
The category axis of a radar chart.
Type: [AxisDisplayOptions](API_AxisDisplayOptions.md) object
Required: No

 ** CategoryLabelOptions **   <a name="QS-Type-RadarChartConfiguration-CategoryLabelOptions"></a>
The category label options of a radar chart.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

 ** ColorAxis **   <a name="QS-Type-RadarChartConfiguration-ColorAxis"></a>
The color axis of a radar chart.
Type: [AxisDisplayOptions](API_AxisDisplayOptions.md) object
Required: No

 ** ColorLabelOptions **   <a name="QS-Type-RadarChartConfiguration-ColorLabelOptions"></a>
The color label options of a radar chart.
Type: [ChartAxisLabelOptions](API_ChartAxisLabelOptions.md) object
Required: No

 ** FieldWells **   <a name="QS-Type-RadarChartConfiguration-FieldWells"></a>
The field well configuration of a `RadarChartVisual`.
Type: [RadarChartFieldWells](API_RadarChartFieldWells.md) object
Required: No

 ** Interactions **   <a name="QS-Type-RadarChartConfiguration-Interactions"></a>
The general visual interactions setup for a visual.
Type: [VisualInteractionOptions](API_VisualInteractionOptions.md) object
Required: No

 ** Legend **   <a name="QS-Type-RadarChartConfiguration-Legend"></a>
The legend display setup of the visual.
Type: [LegendOptions](API_LegendOptions.md) object
Required: No

 ** Shape **   <a name="QS-Type-RadarChartConfiguration-Shape"></a>
The shape of the radar chart.
Type: String
Valid Values: `CIRCLE | POLYGON`
Required: No

 ** SortConfiguration **   <a name="QS-Type-RadarChartConfiguration-SortConfiguration"></a>
The sort configuration of a `RadarChartVisual`.
Type: [RadarChartSortConfiguration](API_RadarChartSortConfiguration.md) object
Required: No

 ** StartAngle **   <a name="QS-Type-RadarChartConfiguration-StartAngle"></a>
The start angle of a radar chart's axis.
Type: Double
Valid Range: Minimum value of -360. Maximum value of 360.
Required: No

 ** VisualPalette **   <a name="QS-Type-RadarChartConfiguration-VisualPalette"></a>
The palette (chart color) display setup of the visual.
Type: [VisualPalette](API_VisualPalette.md) object
Required: No

## See Also
<a name="API_RadarChartConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RadarChartConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RadarChartConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RadarChartConfiguration)
