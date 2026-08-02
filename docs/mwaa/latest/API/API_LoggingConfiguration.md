---
source_url: https://docs.aws.amazon.com/mwaa/latest/API/API_LoggingConfiguration.html
---

# LoggingConfiguration
<a name="API_LoggingConfiguration"></a>

Describes the Apache Airflow log types that are published to CloudWatch Logs.

## Contents
<a name="API_LoggingConfiguration_Contents"></a>

 ** DagProcessingLogs **   <a name="mwaa-Type-LoggingConfiguration-DagProcessingLogs"></a>
The Airflow DAG processing logs published to CloudWatch Logs and the log level.
Type: [ModuleLoggingConfiguration](API_ModuleLoggingConfiguration.md) object
Required: No

 ** SchedulerLogs **   <a name="mwaa-Type-LoggingConfiguration-SchedulerLogs"></a>
The Airflow scheduler logs published to CloudWatch Logs and the log level.
Type: [ModuleLoggingConfiguration](API_ModuleLoggingConfiguration.md) object
Required: No

 ** TaskLogs **   <a name="mwaa-Type-LoggingConfiguration-TaskLogs"></a>
The Airflow task logs published to CloudWatch Logs and the log level.
Type: [ModuleLoggingConfiguration](API_ModuleLoggingConfiguration.md) object
Required: No

 ** WebserverLogs **   <a name="mwaa-Type-LoggingConfiguration-WebserverLogs"></a>
The Airflow web server logs published to CloudWatch Logs and the log level.
Type: [ModuleLoggingConfiguration](API_ModuleLoggingConfiguration.md) object
Required: No

 ** WorkerLogs **   <a name="mwaa-Type-LoggingConfiguration-WorkerLogs"></a>
The Airflow worker logs published to CloudWatch Logs and the log level.
Type: [ModuleLoggingConfiguration](API_ModuleLoggingConfiguration.md) object
Required: No

## See Also
<a name="API_LoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/LoggingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/LoggingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/LoggingConfiguration)
