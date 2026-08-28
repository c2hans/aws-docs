---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_Schedule.html
---

# Schedule
<a name="API_automation_Schedule"></a>

Configuration for scheduling when automation rules should execute, including timing and execution windows.

## Contents
<a name="API_automation_Schedule_Contents"></a>

 ** executionWindowInMinutes **   <a name="computeoptimizer-Type-automation_Schedule-executionWindowInMinutes"></a>
The time window in minutes during which the automation rule can start implementing recommended actions.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 1440.
Required: No

 ** scheduleExpression **   <a name="computeoptimizer-Type-automation_Schedule-scheduleExpression"></a>
The expression that defines when the schedule runs. `cron` expression is supported. A `cron` expression consists of six fields separated by white spaces: (`minutes` `hours` `day_of_month` `month` `day_of_week` `year`)
You can schedule rules to run at most once per day. Your cron expression must use specific values (not wildcards) for the minutes and hours fields. For example: (`30 12 * * *`) runs daily at 12:30 PM UTC.
Type: String
Required: No

 ** scheduleExpressionTimezone **   <a name="computeoptimizer-Type-automation_Schedule-scheduleExpressionTimezone"></a>
The timezone to use when interpreting the schedule expression.
Type: String
Required: No

## See Also
<a name="API_automation_Schedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/Schedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/Schedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/Schedule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
