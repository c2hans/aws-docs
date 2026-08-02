---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ScatterPlotFieldWells.html
---

# ScatterPlotFieldWells
<a name="API_ScatterPlotFieldWells"></a>

The field well configuration of a scatter plot.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_ScatterPlotFieldWells_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ScatterPlotCategoricallyAggregatedFieldWells **   <a name="QS-Type-ScatterPlotFieldWells-ScatterPlotCategoricallyAggregatedFieldWells"></a>
The aggregated field wells of a scatter plot. The x and y-axes of scatter plots with aggregated field wells are aggregated by category, label, or both.
Type: [ScatterPlotCategoricallyAggregatedFieldWells](API_ScatterPlotCategoricallyAggregatedFieldWells.md) object
Required: No

 ** ScatterPlotUnaggregatedFieldWells **   <a name="QS-Type-ScatterPlotFieldWells-ScatterPlotUnaggregatedFieldWells"></a>
The unaggregated field wells of a scatter plot. The x and y-axes of these scatter plots are unaggregated.
Type: [ScatterPlotUnaggregatedFieldWells](API_ScatterPlotUnaggregatedFieldWells.md) object
Required: No

## See Also
<a name="API_ScatterPlotFieldWells_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ScatterPlotFieldWells)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ScatterPlotFieldWells)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ScatterPlotFieldWells)
