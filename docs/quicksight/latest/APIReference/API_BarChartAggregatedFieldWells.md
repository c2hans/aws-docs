---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BarChartAggregatedFieldWells.html
---

# BarChartAggregatedFieldWells
<a name="API_BarChartAggregatedFieldWells"></a>

The aggregated field wells of a bar chart.

## Contents
<a name="API_BarChartAggregatedFieldWells_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Category **   <a name="QS-Type-BarChartAggregatedFieldWells-Category"></a>
The category (y-axis) field well of a bar chart.
Type: Array of [DimensionField](API_DimensionField.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** Colors **   <a name="QS-Type-BarChartAggregatedFieldWells-Colors"></a>
The color (group/color) field well of a bar chart.
Type: Array of [DimensionField](API_DimensionField.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** SmallMultiples **   <a name="QS-Type-BarChartAggregatedFieldWells-SmallMultiples"></a>
The small multiples field well of a bar chart.
Type: Array of [DimensionField](API_DimensionField.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** Values **   <a name="QS-Type-BarChartAggregatedFieldWells-Values"></a>
The value field wells of a bar chart. Values are aggregated by category.
Type: Array of [MeasureField](API_MeasureField.md) objects
Array Members: Maximum number of 200 items.
Required: No

## See Also
<a name="API_BarChartAggregatedFieldWells_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BarChartAggregatedFieldWells)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BarChartAggregatedFieldWells)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BarChartAggregatedFieldWells)
