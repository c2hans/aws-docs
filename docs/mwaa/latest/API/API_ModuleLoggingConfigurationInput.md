---
source_url: https://docs.aws.amazon.com/mwaa/latest/API/API_ModuleLoggingConfigurationInput.html
---

# ModuleLoggingConfigurationInput
<a name="API_ModuleLoggingConfigurationInput"></a>

Enables the Apache Airflow log type (e.g. `DagProcessingLogs`) and defines the log level to send to CloudWatch Logs (e.g. `INFO`).

## Contents
<a name="API_ModuleLoggingConfigurationInput_Contents"></a>

 ** Enabled **   <a name="mwaa-Type-ModuleLoggingConfigurationInput-Enabled"></a>
Indicates whether to enable the Apache Airflow log type (e.g. `DagProcessingLogs`).
Type: Boolean
Required: Yes

 ** LogLevel **   <a name="mwaa-Type-ModuleLoggingConfigurationInput-LogLevel"></a>
Defines the Apache Airflow log level (e.g. `INFO`) to send to CloudWatch Logs.
Type: String
Valid Values: `CRITICAL | ERROR | WARNING | INFO | DEBUG`
Required: Yes

## See Also
<a name="API_ModuleLoggingConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/ModuleLoggingConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/ModuleLoggingConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/ModuleLoggingConfigurationInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MWAA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
