---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_Datum.html
---

# Datum
<a name="API_query_Datum"></a>

 Datum represents a single data point in a query result.

## Contents
<a name="API_query_Datum_Contents"></a>

 ** ArrayValue **   <a name="timestream-Type-query_Datum-ArrayValue"></a>
 Indicates if the data point is an array.
Type: Array of [Datum](#API_query_Datum) objects
Required: No

 ** NullValue **   <a name="timestream-Type-query_Datum-NullValue"></a>
 Indicates if the data point is null.
Type: Boolean
Required: No

 ** RowValue **   <a name="timestream-Type-query_Datum-RowValue"></a>
 Indicates if the data point is a row.
Type: [Row](API_query_Row.md) object
Required: No

 ** ScalarValue **   <a name="timestream-Type-query_Datum-ScalarValue"></a>
 Indicates if the data point is a scalar value such as integer, string, double, or Boolean.
Type: String
Required: No

 ** TimeSeriesValue **   <a name="timestream-Type-query_Datum-TimeSeriesValue"></a>
 Indicates if the data point is a timeseries data type.
Type: Array of [TimeSeriesDataPoint](API_query_TimeSeriesDataPoint.md) objects
Required: No

## See Also
<a name="API_query_Datum_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/Datum)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/Datum)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/Datum)
