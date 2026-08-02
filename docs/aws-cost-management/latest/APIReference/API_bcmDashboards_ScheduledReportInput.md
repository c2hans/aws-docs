---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ScheduledReportInput.html
---

# ScheduledReportInput
<a name="API_bcmDashboards_ScheduledReportInput"></a>

Defines the configuration for creating a new scheduled report, including the dashboard, schedule, execution role, and optional widget settings.

## Contents
<a name="API_bcmDashboards_ScheduledReportInput_Contents"></a>

 ** dashboardArn **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReportInput-dashboardArn"></a>
The ARN of the dashboard to generate the scheduled report from.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:dashboard/(\*|[-a-z0-9]+)`
Required: Yes

 ** name **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReportInput-name"></a>
The name of the scheduled report.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `(?!.* {2})[a-zA-Z][a-zA-Z0-9 _-]{0,48}[a-zA-Z0-9_-]`
Required: Yes

 ** scheduleConfig **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReportInput-scheduleConfig"></a>
The schedule configuration that defines when and how often the report is generated. If the schedule state is not specified, it defaults to `ENABLED`.
Type: [ScheduleConfig](API_bcmDashboards_ScheduleConfig.md) object
Required: Yes

 ** scheduledReportExecutionRoleArn **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReportInput-scheduledReportExecutionRoleArn"></a>
The ARN of the IAM role that the scheduled report uses to execute. AWS Billing and Cost Management Dashboards will assume this IAM role while executing the scheduled report.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:iam::[0-9]{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: Yes

 ** description **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReportInput-description"></a>
A description of the scheduled report's purpose or contents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(?!.* {2})[ a-zA-Z0-9.,!?;:@#$%&\-_/\\]*`
Required: No

 ** widgetDateRangeOverride **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReportInput-widgetDateRangeOverride"></a>
The date range override to apply to widgets in the scheduled report.
Type: [DateTimeRange](API_bcmDashboards_DateTimeRange.md) object
Required: No

 ** widgetIds **   <a name="awscostmanagement-Type-bcmDashboards_ScheduledReportInput-widgetIds"></a>
The list of widget identifiers to include in the scheduled report. If not specified, all widgets in the dashboard are included.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## See Also
<a name="API_bcmDashboards_ScheduledReportInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/ScheduledReportInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/ScheduledReportInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/ScheduledReportInput)
