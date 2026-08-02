---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_PerformanceInsightsMetricQuery.html
---

# PerformanceInsightsMetricQuery
<a name="API_PerformanceInsightsMetricQuery"></a>

A single query to be processed. Use these parameters to query the Performance Insights `GetResourceMetrics` API to retrieve the metrics for an anomaly. For more information, see ` [GetResourceMetrics](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_GetResourceMetrics.html) ` in the *Amazon RDS Performance Insights API Reference*.

Amazon RDS Performance Insights enables you to monitor and explore different dimensions of database load based on data captured from a running DB instance. DB load is measured as average active sessions. Performance Insights provides the data to API consumers as a two-dimensional time-series dataset. The time dimension provides DB load data for each time point in the queried time range. Each time point decomposes overall load in relation to the requested dimensions, measured at that time point. Examples include SQL, Wait event, User, and Host.
+ To learn more about Performance Insights and Amazon Aurora DB instances, go to the [ Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.html).
+ To learn more about Performance Insights and Amazon RDS DB instances, go to the [ Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html).

## Contents
<a name="API_PerformanceInsightsMetricQuery_Contents"></a>

 ** Filter **   <a name="DevOpsGuru-Type-PerformanceInsightsMetricQuery-Filter"></a>
One or more filters to apply to a Performance Insights `GetResourceMetrics` API query. Restrictions:
+ Any number of filters by the same dimension, as specified in the `GroupBy` parameter.
+ A single filter for any other dimension in this dimension group.
Type: String to string map
Required: No

 ** GroupBy **   <a name="DevOpsGuru-Type-PerformanceInsightsMetricQuery-GroupBy"></a>
The specification for how to aggregate the data points from a Performance Insights `GetResourceMetrics` API query. The Performance Insights query returns all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.
Type: [PerformanceInsightsMetricDimensionGroup](API_PerformanceInsightsMetricDimensionGroup.md) object
Required: No

 ** Metric **   <a name="DevOpsGuru-Type-PerformanceInsightsMetricQuery-Metric"></a>
The name of the meteric used used when querying an Performance Insights `GetResourceMetrics` API for anomaly metrics.
Valid values for `Metric` are:
+  `db.load.avg` - a scaled representation of the number of active sessions for the database engine.
+  `db.sampledload.avg` - the raw number of active sessions for the database engine.
If the number of active sessions is less than an internal Performance Insights threshold, `db.load.avg` and `db.sampledload.avg` are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with `db.load.avg` showing the scaled values, `db.sampledload.avg` showing the raw values, and `db.sampledload.avg` less than `db.load.avg`. For most use cases, you can query `db.load.avg` only.
Type: String
Required: No

## See Also
<a name="API_PerformanceInsightsMetricQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/PerformanceInsightsMetricQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/PerformanceInsightsMetricQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/PerformanceInsightsMetricQuery)
