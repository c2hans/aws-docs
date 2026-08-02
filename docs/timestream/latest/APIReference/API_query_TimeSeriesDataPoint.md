---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_TimeSeriesDataPoint.html
---

# TimeSeriesDataPoint
<a name="API_query_TimeSeriesDataPoint"></a>

The timeseries data type represents the values of a measure over time. A time series is an array of rows of timestamps and measure values, with rows sorted in ascending order of time. A TimeSeriesDataPoint is a single data point in the time series. It represents a tuple of (time, measure value) in a time series.

## Contents
<a name="API_query_TimeSeriesDataPoint_Contents"></a>

 ** Time **   <a name="timestream-Type-query_TimeSeriesDataPoint-Time"></a>
The timestamp when the measure value was collected.
Type: String
Required: Yes

 ** Value **   <a name="timestream-Type-query_TimeSeriesDataPoint-Value"></a>
The measure value for the data point.
Type: [Datum](API_query_Datum.md) object
Required: Yes

## See Also
<a name="API_query_TimeSeriesDataPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/TimeSeriesDataPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/TimeSeriesDataPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/TimeSeriesDataPoint)
