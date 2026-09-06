---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_SelectColumn.html
---

# SelectColumn
<a name="API_query_SelectColumn"></a>

Details of the column that is returned by the query.

## Contents
<a name="API_query_SelectColumn_Contents"></a>

 ** Aliased **   <a name="timestream-Type-query_SelectColumn-Aliased"></a>
True, if the column name was aliased by the query. False otherwise.
Type: Boolean
Required: No

 ** DatabaseName **   <a name="timestream-Type-query_SelectColumn-DatabaseName"></a>
 Database that has this column.
Type: String
Required: No

 ** Name **   <a name="timestream-Type-query_SelectColumn-Name"></a>
Name of the column.
Type: String
Required: No

 ** TableName **   <a name="timestream-Type-query_SelectColumn-TableName"></a>
Table within the database that has this column.
Type: String
Required: No

 ** Type **   <a name="timestream-Type-query_SelectColumn-Type"></a>
Contains the data type of a column in a query result set. The data type can be scalar or complex. The supported scalar data types are integers, Boolean, string, double, timestamp, date, time, and intervals. The supported complex data types are arrays, rows, and timeseries.
Type: [Type](API_query_Type.md) object
Required: No

## See Also
<a name="API_query_SelectColumn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/SelectColumn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/SelectColumn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/SelectColumn)
