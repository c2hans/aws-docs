---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_ScheduleConfiguration.html
---

# ScheduleConfiguration

Contains the configuration used to schedule automated workflow execution. Only one version of a workflow can have an active schedule at any time.

## Contents
<a name="API_ScheduleConfiguration_Contents"></a>

 ** CronExpression **   <a name="mwaaserverless-Type-ScheduleConfiguration-CronExpression"></a>
The schedule expression that determines when the workflow runs, as specified in the `schedule` parameter of the workflow's YAML definition. You can specify one of the following types of schedule expressions:
+ Apache Airflow cron expression – Five fields, such as `0 12 1 * *`.
+ Apache Airflow schedule preset – `@hourly`, `@daily`, `@weekly`, `@monthly`, `@yearly`, or `@annually`.
+ EventBridge Scheduler rate expression – For example, `rate(5 minutes)`. Supported units are minutes, hours, and days.
+ EventBridge Scheduler cron expression – Six fields, such as `cron(0 12 * * ? *)`.
In a cron expression, specify either a day-of-month or a day-of-week, not both.
Type: String
Required: No

## See Also
<a name="API_ScheduleConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/ScheduleConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/ScheduleConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/ScheduleConfiguration)
