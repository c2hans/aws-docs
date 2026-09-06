---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_MetricQuery.html
---

# MetricQuery
<a name="API_MetricQuery"></a>

A single query to be processed. You must provide the metric to query and append an aggregate function to the metric. For example, to find the average for the metric `db.load` you must use `db.load.avg`. Valid values for aggregate functions include `.avg`, `.min`, `.max`, and `.sum`. If no other parameters are specified, Performance Insights returns all data points for the specified metric. Optionally, you can request that the data points be aggregated by dimension group (`GroupBy`), and return only those data points that match your criteria (`Filter`).

## Contents
<a name="API_MetricQuery_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Metric **   <a name="performanceinsights-Type-MetricQuery-Metric"></a>
The name of a Performance Insights metric to be measured.
Valid values for `Metric` are:
+  `db.load.avg` - A scaled representation of the number of active sessions for the database engine.
+  `db.sampledload.avg` - The raw number of active sessions for the database engine.
+ The counter metrics listed in [Performance Insights operating system counters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS) in the *Amazon Aurora User Guide*.
+ The counter metrics listed in [Performance Insights operating system counters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS) in the *Amazon RDS User Guide*.
If the number of active sessions is less than an internal Performance Insights threshold, `db.load.avg` and `db.sampledload.avg` are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with `db.load.avg` showing the scaled values, `db.sampledload.avg` showing the raw values, and `db.sampledload.avg` less than `db.load.avg`. For most use cases, you can query `db.load.avg` only.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9-_\.:/*)( ]+$`
Required: Yes

 ** Filter **   <a name="performanceinsights-Type-MetricQuery-Filter"></a>
One or more filters to apply in the request. Restrictions:
+ Any number of filters by the same dimension, as specified in the `GroupBy` parameter.
+ A single filter for any other dimension in this dimension group.
The `db.sql.db_id` filter isn't available for RDS for SQL Server DB instances.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `^[a-zA-Z0-9-_\.:/*)( ]+$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*\S.*`
Required: No

 ** GroupBy **   <a name="performanceinsights-Type-MetricQuery-GroupBy"></a>
A specification for how to aggregate the data points from a query result. You must specify a valid dimension group. Performance Insights will return all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.
Type: [DimensionGroup](API_DimensionGroup.md) object
Required: No

## See Also
<a name="API_MetricQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/MetricQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/MetricQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/MetricQuery)
