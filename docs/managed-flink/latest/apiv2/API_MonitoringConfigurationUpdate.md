---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_MonitoringConfigurationUpdate.html
---

# MonitoringConfigurationUpdate
<a name="API_MonitoringConfigurationUpdate"></a>

Describes updates to configuration parameters for Amazon CloudWatch logging for an application.

## Contents
<a name="API_MonitoringConfigurationUpdate_Contents"></a>

 ** ConfigurationTypeUpdate **   <a name="APIReference-Type-MonitoringConfigurationUpdate-ConfigurationTypeUpdate"></a>
Describes updates to whether to use the default CloudWatch logging configuration for an application. You must set this property to `CUSTOM` in order to set the `LogLevel` or `MetricsLevel` parameters.
Type: String
Valid Values: `DEFAULT | CUSTOM`
Required: No

 ** LogLevelUpdate **   <a name="APIReference-Type-MonitoringConfigurationUpdate-LogLevelUpdate"></a>
Describes updates to the verbosity of the CloudWatch Logs for an application.
Type: String
Valid Values: `INFO | WARN | ERROR | DEBUG`
Required: No

 ** MetricsLevelUpdate **   <a name="APIReference-Type-MonitoringConfigurationUpdate-MetricsLevelUpdate"></a>
Describes updates to the granularity of the CloudWatch Logs for an application. The `Parallelism` level is not recommended for applications with a Parallelism over 64 due to excessive costs.
Type: String
Valid Values: `APPLICATION | TASK | OPERATOR | PARALLELISM`
Required: No

## See Also
<a name="API_MonitoringConfigurationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/MonitoringConfigurationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/MonitoringConfigurationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/MonitoringConfigurationUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
