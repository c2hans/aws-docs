---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_CostAnomalyDetectedQuery.html
---

# CostAnomalyDetectedQuery
<a name="API_bcmDashboards_CostAnomalyDetectedQuery"></a>

Defines the parameters for retrieving detected AWS cost anomalies. Anomaly widgets display cost anomalies identified by AWS Cost Anomaly Detection, including their cost impact and severity. Supports an anomaly date range and optional filtering by anomaly dimensions.

## Contents
<a name="API_bcmDashboards_CostAnomalyDetectedQuery_Contents"></a>

 ** timeRange **   <a name="awscostmanagement-Type-bcmDashboards_CostAnomalyDetectedQuery-timeRange"></a>
The anomaly date range for which to retrieve detected anomalies. Can be specified as absolute dates or relative time periods.
Type: [DateTimeRange](API_bcmDashboards_DateTimeRange.md) object
Required: Yes

 ** filter **   <a name="awscostmanagement-Type-bcmDashboards_CostAnomalyDetectedQuery-filter"></a>
The filter expression to apply to detected anomalies. Supports filtering by anomaly dimensions such as `SEVERITY`, `ASSESSMENT`, `MONITOR_TYPE`, and `ANOMALY_ID`.
Type: [Expression](API_bcmDashboards_Expression.md) object
Required: No

## See Also
<a name="API_bcmDashboards_CostAnomalyDetectedQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/CostAnomalyDetectedQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/CostAnomalyDetectedQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/CostAnomalyDetectedQuery)
