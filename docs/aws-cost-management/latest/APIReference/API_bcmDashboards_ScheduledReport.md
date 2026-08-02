---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ScheduledReport.html
---

# ScheduledReport
<a name="API_bcmDashboards_ScheduledReport"></a>

Contains the full configuration and metadata of a scheduled report.

## Contents
<a name="API_bcmDashboards_ScheduledReport_Contents"></a>

 ** dashboardArn **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReport-dashboardArn"></a>
The ARN of the dashboard associated with the scheduled report.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:dashboard/(\*|[-a-z0-9]+)`
Required: Yes

 ** name **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReport-name"></a>
The name of the scheduled report.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `(?!.* {2})[a-zA-Z][a-zA-Z0-9 _-]{0,48}[a-zA-Z0-9_-]`
Required: Yes

 ** scheduleConfig **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReport-scheduleConfig"></a>
The schedule configuration that defines when and how often the report is generated.
Type: [ScheduleConfig](API_bcmDashboards_ScheduleConfig.md) object
Required: Yes

 ** scheduledReportExecutionRoleArn **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReport-scheduledReportExecutionRoleArn"></a>
The ARN of the IAM role that the scheduled report uses to execute. AWS Billing and Cost Management Dashboards will assume this IAM role while executing the scheduled report.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:iam::[0-9]{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: Yes

 ** arn **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReport-arn"></a>
The ARN of the scheduled report.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:scheduled-report/(\*|[-a-z0-9]+)`
Required: No

 ** createdAt **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReport-createdAt"></a>
The timestamp when the scheduled report was created.
Type: Timestamp
Required: No

 ** description **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReport-description"></a>
A description of the scheduled report's purpose or contents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(?!.* {2})[ a-zA-Z0-9.,!?;:@#$%&\-_/\\]*`
Required: No

 ** healthStatus **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReport-healthStatus"></a>
The health status of the scheduled report at last refresh time.
Type: [HealthStatus](API_bcmDashboards_HealthStatus.md) object
Required: No

 ** lastExecutionAt **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReport-lastExecutionAt"></a>
The timestamp of the most recent execution of the scheduled report.
Type: Timestamp
Required: No

 ** updatedAt **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReport-updatedAt"></a>
The timestamp when the scheduled report was last modified.
Type: Timestamp
Required: No

 ** widgetDateRangeOverride **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReport-widgetDateRangeOverride"></a>
The date range override applied to widgets in the scheduled report.
Type: [DateTimeRange](API_bcmDashboards_DateTimeRange.md) object
Required: No

 ** widgetIds **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReport-widgetIds"></a>
The list of widget identifiers included in the scheduled report.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## See Also
<a name="API_bcmDashboards_ScheduledReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/ScheduledReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/ScheduledReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/ScheduledReport)
