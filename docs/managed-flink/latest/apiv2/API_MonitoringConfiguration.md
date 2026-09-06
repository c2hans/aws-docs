---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_MonitoringConfiguration.html
---

# MonitoringConfiguration
<a name="API_MonitoringConfiguration"></a>

Describes configuration parameters for Amazon CloudWatch logging for an application. For more information about CloudWatch logging, see [Monitoring](https://docs.aws.amazon.com/kinesisanalytics/latest/java/monitoring-overview.html).

## Contents
<a name="API_MonitoringConfiguration_Contents"></a>

 ** ConfigurationType **   <a name="APIReference-Type-MonitoringConfiguration-ConfigurationType"></a>
Describes whether to use the default CloudWatch logging configuration for an application. You must set this property to `CUSTOM` in order to set the `LogLevel` or `MetricsLevel` parameters.
Type: String
Valid Values: `DEFAULT | CUSTOM`
Required: Yes

 ** LogLevel **   <a name="APIReference-Type-MonitoringConfiguration-LogLevel"></a>
Describes the verbosity of the CloudWatch Logs for an application.
Type: String
Valid Values: `INFO | WARN | ERROR | DEBUG`
Required: No

 ** MetricsLevel **   <a name="APIReference-Type-MonitoringConfiguration-MetricsLevel"></a>
Describes the granularity of the CloudWatch Logs for an application. The `Parallelism` level is not recommended for applications with a Parallelism over 64 due to excessive costs.
Type: String
Valid Values: `APPLICATION | TASK | OPERATOR | PARALLELISM`
Required: No

## See Also
<a name="API_MonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/MonitoringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/MonitoringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/MonitoringConfiguration)
