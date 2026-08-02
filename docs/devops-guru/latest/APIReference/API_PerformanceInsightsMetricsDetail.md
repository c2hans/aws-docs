---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_PerformanceInsightsMetricsDetail.html
---

# PerformanceInsightsMetricsDetail
<a name="API_PerformanceInsightsMetricsDetail"></a>

Details about Performance Insights metrics.

Amazon RDS Performance Insights enables you to monitor and explore different dimensions of database load based on data captured from a running DB instance. DB load is measured as average active sessions. Performance Insights provides the data to API consumers as a two-dimensional time-series dataset. The time dimension provides DB load data for each time point in the queried time range. Each time point decomposes overall load in relation to the requested dimensions, measured at that time point. Examples include SQL, Wait event, User, and Host.
+ To learn more about Performance Insights and Amazon Aurora DB instances, go to the [ Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.html).
+ To learn more about Performance Insights and Amazon RDS DB instances, go to the [ Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html).

## Contents
<a name="API_PerformanceInsightsMetricsDetail_Contents"></a>

 ** MetricDisplayName **   <a name="DevOpsGuru-Type-PerformanceInsightsMetricsDetail-MetricDisplayName"></a>
The name used for a specific Performance Insights metric.
Type: String
Required: No

 ** MetricQuery **   <a name="DevOpsGuru-Type-PerformanceInsightsMetricsDetail-MetricQuery"></a>
A single query to be processed for the metric. For more information, see ` [PerformanceInsightsMetricQuery](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_PerformanceInsightsMetricQuery.html) `.
Type: [PerformanceInsightsMetricQuery](API_PerformanceInsightsMetricQuery.md) object
Required: No

 ** ReferenceData **   <a name="DevOpsGuru-Type-PerformanceInsightsMetricsDetail-ReferenceData"></a>
 For more information, see ` [PerformanceInsightsReferenceData](https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_PerformanceInsightsReferenceData.html) `.
Type: Array of [PerformanceInsightsReferenceData](API_PerformanceInsightsReferenceData.md) objects
Required: No

 ** StatsAtAnomaly **   <a name="DevOpsGuru-Type-PerformanceInsightsMetricsDetail-StatsAtAnomaly"></a>
The metric statistics during the anomalous period detected by DevOps Guru;
Type: Array of [PerformanceInsightsStat](API_PerformanceInsightsStat.md) objects
Required: No

 ** StatsAtBaseline **   <a name="DevOpsGuru-Type-PerformanceInsightsMetricsDetail-StatsAtBaseline"></a>
Typical metric statistics that are not considered anomalous. When DevOps Guru analyzes metrics, it compares them to `StatsAtBaseline` to help determine if they are anomalous.
Type: Array of [PerformanceInsightsStat](API_PerformanceInsightsStat.md) objects
Required: No

 ** Unit **   <a name="DevOpsGuru-Type-PerformanceInsightsMetricsDetail-Unit"></a>
The unit of measure for a metric. For example, a session or a process.
Type: String
Required: No

## See Also
<a name="API_PerformanceInsightsMetricsDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/PerformanceInsightsMetricsDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/PerformanceInsightsMetricsDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/PerformanceInsightsMetricsDetail)
