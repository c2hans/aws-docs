---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PieChartSortConfiguration.html
---

# PieChartSortConfiguration
<a name="API_PieChartSortConfiguration"></a>

The sort configuration of a pie chart.

## Contents
<a name="API_PieChartSortConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CategoryItemsLimit **   <a name="QS-Type-PieChartSortConfiguration-CategoryItemsLimit"></a>
The limit on the number of categories that are displayed in a pie chart.
Type: [ItemsLimitConfiguration](API_ItemsLimitConfiguration.md) object
Required: No

 ** CategorySort **   <a name="QS-Type-PieChartSortConfiguration-CategorySort"></a>
The sort configuration of the category fields.
Type: Array of [FieldSortOptions](API_FieldSortOptions.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** SmallMultiplesLimitConfiguration **   <a name="QS-Type-PieChartSortConfiguration-SmallMultiplesLimitConfiguration"></a>
The limit on the number of small multiples panels that are displayed.
Type: [ItemsLimitConfiguration](API_ItemsLimitConfiguration.md) object
Required: No

 ** SmallMultiplesSort **   <a name="QS-Type-PieChartSortConfiguration-SmallMultiplesSort"></a>
The sort configuration of the small multiples field.
Type: Array of [FieldSortOptions](API_FieldSortOptions.md) objects
Array Members: Maximum number of 100 items.
Required: No

## See Also
<a name="API_PieChartSortConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PieChartSortConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PieChartSortConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PieChartSortConfiguration)
