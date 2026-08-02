---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_QuerySpatialCoverage.html
---

# QuerySpatialCoverage
<a name="API_query_QuerySpatialCoverage"></a>

Provides insights into the spatial coverage of the query, including the table with sub-optimal (max) spatial pruning. This information can help you identify areas for improvement in your partitioning strategy to enhance spatial pruning

For example, you can do the following with the `QuerySpatialCoverage` information:
+ Add measure\_name or use [customer-defined partition key](https://docs.aws.amazon.com/timestream/latest/developerguide/customer-defined-partition-keys.html) (CDPK) predicates.
+ If you've already done the preceding action, remove functions around them or clauses, such as `LIKE`.

## Contents
<a name="API_query_QuerySpatialCoverage_Contents"></a>

 ** Max **   <a name="timestream-Type-query_QuerySpatialCoverage-Max"></a>
Provides insights into the spatial coverage of the executed query and the table with the most inefficient spatial pruning.
+  `Value` – The maximum ratio of spatial coverage.
+  `TableArn` – The Amazon Resource Name (ARN) of the table with sub-optimal spatial pruning.
+  `PartitionKey` – The partition key used for partitioning, which can be a default `measure_name` or a CDPK.
Type: [QuerySpatialCoverageMax](API_query_QuerySpatialCoverageMax.md) object
Required: No

## See Also
<a name="API_query_QuerySpatialCoverage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/QuerySpatialCoverage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/QuerySpatialCoverage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/QuerySpatialCoverage)
