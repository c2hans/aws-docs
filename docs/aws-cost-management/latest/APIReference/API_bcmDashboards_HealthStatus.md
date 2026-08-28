---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_HealthStatus.html
---

# HealthStatus
<a name="API_bcmDashboards_HealthStatus"></a>

Contains the health status information for a scheduled report, including the status code and any reasons for an unhealthy state.

## Contents
<a name="API_bcmDashboards_HealthStatus_Contents"></a>

 ** statusCode **   <a name="awscostmanagement-Type-bcmDashboards_HealthStatus-statusCode"></a>
The health status code. `HEALTHY` indicates the scheduled report is configured properly and has all required permissions to execute. `UNHEALTHY` indicates the scheduled report is unable to deliver the notification to the default Amazon EventBridge EventBus in your account and your action is needed. The reason for the unhealthy state is captured in the health status reasons.
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: Yes

 ** lastRefreshedAt **   <a name="awscostmanagement-Type-bcmDashboards_HealthStatus-lastRefreshedAt"></a>
The timestamp when the health status was last refreshed.
Type: Timestamp
Required: No

 ** statusReasons **   <a name="awscostmanagement-Type-bcmDashboards_HealthStatus-statusReasons"></a>
The list of reasons for the current health status. Only present when the status is `UNHEALTHY`.
Type: Array of strings
Valid Values: `DATA_SOURCE_ACCESS_DENIED | EXECUTION_ROLE_ASSUME_FAILED | EXECUTION_ROLE_INSUFFICIENT_PERMISSIONS | DASHBOARD_NOT_FOUND | DASHBOARD_ACCESS_DENIED | INTERNAL_FAILURE | WIDGET_ID_NOT_FOUND`
Required: No

## See Also
<a name="API_bcmDashboards_HealthStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/HealthStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/HealthStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/HealthStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
