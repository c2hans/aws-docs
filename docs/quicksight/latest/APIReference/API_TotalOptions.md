---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TotalOptions.html
---

# TotalOptions
<a name="API_TotalOptions"></a>

The total options for a table visual.

## Contents
<a name="API_TotalOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomLabel **   <a name="QS-Type-TotalOptions-CustomLabel"></a>
The custom label string for the total cells.
Type: String
Required: No

 ** Placement **   <a name="QS-Type-TotalOptions-Placement"></a>
The placement (start, end) for the total cells.
Type: String
Valid Values: `START | END | AUTO`
Required: No

 ** ScrollStatus **   <a name="QS-Type-TotalOptions-ScrollStatus"></a>
The scroll status (pinned, scrolled) for the total cells.
Type: String
Valid Values: `PINNED | SCROLLED`
Required: No

 ** TotalAggregationOptions **   <a name="QS-Type-TotalOptions-TotalAggregationOptions"></a>
The total aggregation settings for each value field.
Type: Array of [TotalAggregationOption](API_TotalAggregationOption.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** TotalCellStyle **   <a name="QS-Type-TotalOptions-TotalCellStyle"></a>
Cell styling options for the total cells.
Type: [TableCellStyle](API_TableCellStyle.md) object
Required: No

 ** TotalsVisibility **   <a name="QS-Type-TotalOptions-TotalsVisibility"></a>
The visibility configuration for the total cells.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

## See Also
<a name="API_TotalOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TotalOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TotalOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TotalOptions)
