---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_LineChartAggregatedFieldWells.html
---

# LineChartAggregatedFieldWells
<a name="API_LineChartAggregatedFieldWells"></a>

The field well configuration of a line chart.

## Contents
<a name="API_LineChartAggregatedFieldWells_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Category **   <a name="QS-Type-LineChartAggregatedFieldWells-Category"></a>
The category field wells of a line chart. Values are grouped by category fields.
Type: Array of [DimensionField](API_DimensionField.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** Colors **   <a name="QS-Type-LineChartAggregatedFieldWells-Colors"></a>
The color field wells of a line chart. Values are grouped by category fields.
Type: Array of [DimensionField](API_DimensionField.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** SmallMultiples **   <a name="QS-Type-LineChartAggregatedFieldWells-SmallMultiples"></a>
The small multiples field well of a line chart.
Type: Array of [DimensionField](API_DimensionField.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** Values **   <a name="QS-Type-LineChartAggregatedFieldWells-Values"></a>
The value field wells of a line chart. Values are aggregated based on categories.
Type: Array of [MeasureField](API_MeasureField.md) objects
Array Members: Maximum number of 200 items.
Required: No

## See Also
<a name="API_LineChartAggregatedFieldWells_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/LineChartAggregatedFieldWells)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/LineChartAggregatedFieldWells)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/LineChartAggregatedFieldWells)
