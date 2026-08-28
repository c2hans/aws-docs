---
source_url: https://docs.aws.amazon.com/mwaa/latest/API/API_LoggingConfigurationInput.html
---

# LoggingConfigurationInput
<a name="API_LoggingConfigurationInput"></a>

Defines the Apache Airflow log types to send to CloudWatch Logs.

## Contents
<a name="API_LoggingConfigurationInput_Contents"></a>

 ** DagProcessingLogs **   <a name="mwaa-Type-LoggingConfigurationInput-DagProcessingLogs"></a>
Publishes Airflow DAG processing logs to CloudWatch Logs.
Type: [ModuleLoggingConfigurationInput](API_ModuleLoggingConfigurationInput.md) object
Required: No

 ** SchedulerLogs **   <a name="mwaa-Type-LoggingConfigurationInput-SchedulerLogs"></a>
Publishes Airflow scheduler logs to CloudWatch Logs.
Type: [ModuleLoggingConfigurationInput](API_ModuleLoggingConfigurationInput.md) object
Required: No

 ** TaskLogs **   <a name="mwaa-Type-LoggingConfigurationInput-TaskLogs"></a>
Publishes Airflow task logs to CloudWatch Logs.
Type: [ModuleLoggingConfigurationInput](API_ModuleLoggingConfigurationInput.md) object
Required: No

 ** WebserverLogs **   <a name="mwaa-Type-LoggingConfigurationInput-WebserverLogs"></a>
Publishes Airflow web server logs to CloudWatch Logs.
Type: [ModuleLoggingConfigurationInput](API_ModuleLoggingConfigurationInput.md) object
Required: No

 ** WorkerLogs **   <a name="mwaa-Type-LoggingConfigurationInput-WorkerLogs"></a>
Publishes Airflow worker logs to CloudWatch Logs.
Type: [ModuleLoggingConfigurationInput](API_ModuleLoggingConfigurationInput.md) object
Required: No

## See Also
<a name="API_LoggingConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/LoggingConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/LoggingConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/LoggingConfigurationInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MWAA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
