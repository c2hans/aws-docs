---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataAggregation.html
---

# DataAggregation
<a name="API_DataAggregation"></a>

A structure that represents a data aggregation.

## Contents
<a name="API_DataAggregation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DatasetRowDateGranularity **   <a name="QS-Type-DataAggregation-DatasetRowDateGranularity"></a>
The level of time precision that is used to aggregate `DateTime` values.
Type: String
Valid Values: `SECOND | MINUTE | HOUR | DAY | WEEK | MONTH | QUARTER | YEAR`
Required: No

 ** DefaultDateColumnName **   <a name="QS-Type-DataAggregation-DefaultDateColumnName"></a>
The column name for the default date.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_DataAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataAggregation)
