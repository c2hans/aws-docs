---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_MonitoringConfigurationDescription.html
---

# MonitoringConfigurationDescription
<a name="API_MonitoringConfigurationDescription"></a>

Describes configuration parameters for CloudWatch logging for an application.

## Contents
<a name="API_MonitoringConfigurationDescription_Contents"></a>

 ** ConfigurationType **   <a name="APIReference-Type-MonitoringConfigurationDescription-ConfigurationType"></a>
Describes whether to use the default CloudWatch logging configuration for an application.
Type: String
Valid Values: `DEFAULT | CUSTOM`
Required: No

 ** LogLevel **   <a name="APIReference-Type-MonitoringConfigurationDescription-LogLevel"></a>
Describes the verbosity of the CloudWatch Logs for an application.
Type: String
Valid Values: `INFO | WARN | ERROR | DEBUG`
Required: No

 ** MetricsLevel **   <a name="APIReference-Type-MonitoringConfigurationDescription-MetricsLevel"></a>
Describes the granularity of the CloudWatch Logs for an application.
Type: String
Valid Values: `APPLICATION | TASK | OPERATOR | PARALLELISM`
Required: No

## See Also
<a name="API_MonitoringConfigurationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/MonitoringConfigurationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/MonitoringConfigurationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/MonitoringConfigurationDescription)
