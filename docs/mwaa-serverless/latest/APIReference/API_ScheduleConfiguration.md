---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_ScheduleConfiguration.html
---

# ScheduleConfiguration
<a name="API_ScheduleConfiguration"></a>

The configuration to use to schedule automated workflow execution using cron expressions. Amazon Managed Workflows for Apache Airflow Serverless integrates with EventBridge Scheduler to provide cost-effective, timezone-aware scheduling capabilities. The service supports both time-based and event-based scheduling (event-based scheduling available post-GA). When a workflow definition includes scheduling information, Amazon Managed Workflows for Apache Airflow Serverless automatically configures the appropriate triggers and ensures only one version of a workflow has an active schedule at any time.

## Contents
<a name="API_ScheduleConfiguration_Contents"></a>

 ** CronExpression **   <a name="mwaaserverless-Type-ScheduleConfiguration-CronExpression"></a>
A cron expression that defines when the workflow is automatically executed. Uses standard cron syntax.
Type: String
Required: No

## See Also
<a name="API_ScheduleConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/ScheduleConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/ScheduleConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/ScheduleConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Workflows for Apache Airflow Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
