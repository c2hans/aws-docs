---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ScheduledReportSummary.html
---

# ScheduledReportSummary
<a name="API_bcmDashboards_ScheduledReportSummary"></a>

Contains summary information for a scheduled report.

## Contents
<a name="API_bcmDashboards_ScheduledReportSummary_Contents"></a>

 ** arn **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReportSummary-arn"></a>
The ARN of the scheduled report.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:scheduled-report/(\*|[-a-z0-9]+)`
Required: Yes

 ** dashboardArn **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReportSummary-dashboardArn"></a>
The ARN of the dashboard associated with the scheduled report.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:dashboard/(\*|[-a-z0-9]+)`
Required: Yes

 ** healthStatus **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReportSummary-healthStatus"></a>
The health status of the scheduled report as of its last refresh time.
Type: [HealthStatus](API_bcmDashboards_HealthStatus.md) object
Required: Yes

 ** name **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReportSummary-name"></a>
The name of the scheduled report.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `(?!.* {2})[a-zA-Z][a-zA-Z0-9 _-]{0,48}[a-zA-Z0-9_-]`
Required: Yes

 ** scheduleExpression **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReportSummary-scheduleExpression"></a>
The schedule expression that defines when the report runs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** state **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReportSummary-state"></a>
The state of the schedule: `ENABLED` or `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** scheduleExpressionTimeZone **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReportSummary-scheduleExpressionTimeZone"></a>
The time zone for the schedule expression, for example, `UTC`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** widgetIds **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReportSummary-widgetIds"></a>
The list of widget identifiers included in the scheduled report.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## See Also
<a name="API_bcmDashboards_ScheduledReportSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/ScheduledReportSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/ScheduledReportSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/ScheduledReportSummary)
