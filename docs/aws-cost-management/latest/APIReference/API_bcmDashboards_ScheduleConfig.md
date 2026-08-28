---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ScheduleConfig.html
---

# ScheduleConfig
<a name="API_bcmDashboards_ScheduleConfig"></a>

Defines the schedule for a scheduled report, including the cron expression, time zone, active period, and the schedule state.

## Contents
<a name="API_bcmDashboards_ScheduleConfig_Contents"></a>

 ** scheduleExpression **   <a name="awscostmanagement-Type-bcmDashboards_ScheduleConfig-scheduleExpression"></a>
The schedule expression that specifies when to trigger the scheduled report run. This value must be a cron expression consisting of six fields separated by white spaces: `cron(minutes hours day_of_month month day_of_week year)`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** scheduleExpressionTimeZone **   <a name="awscostmanagement-Type-bcmDashboards_ScheduleConfig-scheduleExpressionTimeZone"></a>
The time zone for the schedule expression, for example, `UTC`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** schedulePeriod **   <a name="awscostmanagement-Type-bcmDashboards_ScheduleConfig-schedulePeriod"></a>
The time period during which the schedule is active.
Type: [SchedulePeriod](API_bcmDashboards_SchedulePeriod.md) object
Required: No

 ** state **   <a name="awscostmanagement-Type-bcmDashboards_ScheduleConfig-state"></a>
The state of the schedule. `ENABLED` means the scheduled report runs according to its schedule expression. `DISABLED` means the scheduled report is paused and will not run until re-enabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_bcmDashboards_ScheduleConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/ScheduleConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/ScheduleConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/ScheduleConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
