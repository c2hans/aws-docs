---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_TimestreamConfiguration.html
---

# TimestreamConfiguration
<a name="API_query_TimestreamConfiguration"></a>

 Configuration to write data into Timestream database and table. This configuration allows the user to map the query result select columns into the destination table columns.

## Contents
<a name="API_query_TimestreamConfiguration_Contents"></a>

 ** DatabaseName **   <a name="timestream-Type-query_TimestreamConfiguration-DatabaseName"></a>
Name of Timestream database to which the query result will be written.
Type: String
Required: Yes

 ** DimensionMappings **   <a name="timestream-Type-query_TimestreamConfiguration-DimensionMappings"></a>
 This is to allow mapping column(s) from the query result to the dimension in the destination table.
Type: Array of [DimensionMapping](API_query_DimensionMapping.md) objects
Required: Yes

 ** TableName **   <a name="timestream-Type-query_TimestreamConfiguration-TableName"></a>
Name of Timestream table that the query result will be written to. The table should be within the same database that is provided in Timestream configuration.
Type: String
Required: Yes

 ** TimeColumn **   <a name="timestream-Type-query_TimestreamConfiguration-TimeColumn"></a>
Column from query result that should be used as the time column in destination table. Column type for this should be TIMESTAMP.
Type: String
Required: Yes

 ** MeasureNameColumn **   <a name="timestream-Type-query_TimestreamConfiguration-MeasureNameColumn"></a>
Name of the measure column.
Type: String
Required: No

 ** MixedMeasureMappings **   <a name="timestream-Type-query_TimestreamConfiguration-MixedMeasureMappings"></a>
Specifies how to map measures to multi-measure records.
Type: Array of [MixedMeasureMapping](API_query_MixedMeasureMapping.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** MultiMeasureMappings **   <a name="timestream-Type-query_TimestreamConfiguration-MultiMeasureMappings"></a>
Multi-measure mappings.
Type: [MultiMeasureMappings](API_query_MultiMeasureMappings.md) object
Required: No

## See Also
<a name="API_query_TimestreamConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/TimestreamConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/TimestreamConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/TimestreamConfiguration)
