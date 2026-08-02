---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_QueryInsightsResponse.html
---

# QueryInsightsResponse
<a name="API_query_QueryInsightsResponse"></a>

Provides various insights and metrics related to the query that you executed.

## Contents
<a name="API_query_QueryInsightsResponse_Contents"></a>

 ** OutputBytes **   <a name="timestream-Type-query_QueryInsightsResponse-OutputBytes"></a>
Indicates the size of query result set in bytes. You can use this data to validate if the result set has changed as part of the query tuning exercise.
Type: Long
Required: No

 ** OutputRows **   <a name="timestream-Type-query_QueryInsightsResponse-OutputRows"></a>
Indicates the total number of rows returned as part of the query result set. You can use this data to validate if the number of rows in the result set have changed as part of the query tuning exercise.
Type: Long
Required: No

 ** QuerySpatialCoverage **   <a name="timestream-Type-query_QueryInsightsResponse-QuerySpatialCoverage"></a>
Provides insights into the spatial coverage of the query, including the table with sub-optimal (max) spatial pruning. This information can help you identify areas for improvement in your partitioning strategy to enhance spatial pruning.
Type: [QuerySpatialCoverage](API_query_QuerySpatialCoverage.md) object
Required: No

 ** QueryTableCount **   <a name="timestream-Type-query_QueryInsightsResponse-QueryTableCount"></a>
Indicates the number of tables in the query.
Type: Long
Required: No

 ** QueryTemporalRange **   <a name="timestream-Type-query_QueryInsightsResponse-QueryTemporalRange"></a>
Provides insights into the temporal range of the query, including the table with the largest (max) time range. Following are some of the potential options for optimizing time-based pruning:
+ Add missing time-predicates.
+ Remove functions around the time predicates.
+ Add time predicates to all the sub-queries.
Type: [QueryTemporalRange](API_query_QueryTemporalRange.md) object
Required: No

 ** UnloadPartitionCount **   <a name="timestream-Type-query_QueryInsightsResponse-UnloadPartitionCount"></a>
Indicates the partitions created by the `Unload` operation.
Type: Long
Required: No

 ** UnloadWrittenBytes **   <a name="timestream-Type-query_QueryInsightsResponse-UnloadWrittenBytes"></a>
Indicates the size, in bytes, written by the `Unload` operation.
Type: Long
Required: No

 ** UnloadWrittenRows **   <a name="timestream-Type-query_QueryInsightsResponse-UnloadWrittenRows"></a>
Indicates the rows written by the `Unload` query.
Type: Long
Required: No

## See Also
<a name="API_query_QueryInsightsResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/QueryInsightsResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/QueryInsightsResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/QueryInsightsResponse)
