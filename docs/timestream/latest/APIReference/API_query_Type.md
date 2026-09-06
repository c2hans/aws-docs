---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_Type.html
---

# Type
<a name="API_query_Type"></a>

Contains the data type of a column in a query result set. The data type can be scalar or complex. The supported scalar data types are integers, Boolean, string, double, timestamp, date, time, and intervals. The supported complex data types are arrays, rows, and timeseries.

## Contents
<a name="API_query_Type_Contents"></a>

 ** ArrayColumnInfo **   <a name="timestream-Type-query_Type-ArrayColumnInfo"></a>
Indicates if the column is an array.
Type: [ColumnInfo](API_query_ColumnInfo.md) object
Required: No

 ** RowColumnInfo **   <a name="timestream-Type-query_Type-RowColumnInfo"></a>
Indicates if the column is a row.
Type: Array of [ColumnInfo](API_query_ColumnInfo.md) objects
Required: No

 ** ScalarType **   <a name="timestream-Type-query_Type-ScalarType"></a>
Indicates if the column is of type string, integer, Boolean, double, timestamp, date, time. For more information, see [Supported data types](https://docs.aws.amazon.com/timestream/latest/developerguide/supported-data-types.html).
Type: String
Valid Values: `VARCHAR | BOOLEAN | BIGINT | DOUBLE | TIMESTAMP | DATE | TIME | INTERVAL_DAY_TO_SECOND | INTERVAL_YEAR_TO_MONTH | UNKNOWN | INTEGER`
Required: No

 ** TimeSeriesMeasureValueColumnInfo **   <a name="timestream-Type-query_Type-TimeSeriesMeasureValueColumnInfo"></a>
Indicates if the column is a timeseries data type.
Type: [ColumnInfo](API_query_ColumnInfo.md) object
Required: No

## See Also
<a name="API_query_Type_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/Type)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/Type)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/Type)
