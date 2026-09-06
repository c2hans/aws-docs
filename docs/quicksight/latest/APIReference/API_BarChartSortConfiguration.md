---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BarChartSortConfiguration.html
---

# BarChartSortConfiguration
<a name="API_BarChartSortConfiguration"></a>

sort-configuration-description

## Contents
<a name="API_BarChartSortConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CategoryItemsLimit **   <a name="QS-Type-BarChartSortConfiguration-CategoryItemsLimit"></a>
The limit on the number of categories displayed in a bar chart.
Type: [ItemsLimitConfiguration](API_ItemsLimitConfiguration.md) object
Required: No

 ** CategorySort **   <a name="QS-Type-BarChartSortConfiguration-CategorySort"></a>
The sort configuration of category fields.
Type: Array of [FieldSortOptions](API_FieldSortOptions.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** ColorItemsLimit **   <a name="QS-Type-BarChartSortConfiguration-ColorItemsLimit"></a>
The limit on the number of values displayed in a bar chart.
Type: [ItemsLimitConfiguration](API_ItemsLimitConfiguration.md) object
Required: No

 ** ColorSort **   <a name="QS-Type-BarChartSortConfiguration-ColorSort"></a>
The sort configuration of color fields in a bar chart.
Type: Array of [FieldSortOptions](API_FieldSortOptions.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** SmallMultiplesLimitConfiguration **   <a name="QS-Type-BarChartSortConfiguration-SmallMultiplesLimitConfiguration"></a>
The limit on the number of small multiples panels that are displayed.
Type: [ItemsLimitConfiguration](API_ItemsLimitConfiguration.md) object
Required: No

 ** SmallMultiplesSort **   <a name="QS-Type-BarChartSortConfiguration-SmallMultiplesSort"></a>
The sort configuration of the small multiples field.
Type: Array of [FieldSortOptions](API_FieldSortOptions.md) objects
Array Members: Maximum number of 100 items.
Required: No

## See Also
<a name="API_BarChartSortConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BarChartSortConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BarChartSortConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BarChartSortConfiguration)
