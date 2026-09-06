---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DateColumnStatisticsData.html
---

# DateColumnStatisticsData
<a name="API_DateColumnStatisticsData"></a>

Defines column statistics supported for timestamp data columns.

## Contents
<a name="API_DateColumnStatisticsData_Contents"></a>

 ** NumberOfDistinctValues **   <a name="Glue-Type-DateColumnStatisticsData-NumberOfDistinctValues"></a>
The number of distinct values in a column.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** NumberOfNulls **   <a name="Glue-Type-DateColumnStatisticsData-NumberOfNulls"></a>
The number of null values in the column.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** MaximumValue **   <a name="Glue-Type-DateColumnStatisticsData-MaximumValue"></a>
The highest value in the column.
Type: Timestamp
Required: No

 ** MinimumValue **   <a name="Glue-Type-DateColumnStatisticsData-MinimumValue"></a>
The lowest value in the column.
Type: Timestamp
Required: No

## See Also
<a name="API_DateColumnStatisticsData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DateColumnStatisticsData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DateColumnStatisticsData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DateColumnStatisticsData)
