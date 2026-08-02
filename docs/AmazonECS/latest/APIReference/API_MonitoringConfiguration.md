---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_MonitoringConfiguration.html
---

# MonitoringConfiguration
<a name="API_MonitoringConfiguration"></a>

The optional monitoring configuration for a service, which defines the resolution for the service-level `CPUUtilization` and `MemoryUtilization` Amazon CloudWatch metrics. When not specified, Amazon ECS uses the default resolution of `60` seconds.

## Contents
<a name="API_MonitoringConfiguration_Contents"></a>

 ** metricConfigurations **   <a name="ECS-Type-MonitoringConfiguration-metricConfigurations"></a>
The list of metric configurations for the service monitoring.
Type: Array of [MetricConfiguration](API_MetricConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

## See Also
<a name="API_MonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/MonitoringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/MonitoringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/MonitoringConfiguration)
