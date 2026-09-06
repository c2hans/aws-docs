---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_MetricConfiguration.html
---

# MetricConfiguration
<a name="API_MetricConfiguration"></a>

The configuration for a specific set of metrics to collect for a service.

## Contents
<a name="API_MetricConfiguration_Contents"></a>

 ** metricNames **   <a name="ECS-Type-MetricConfiguration-metricNames"></a>
The list of metric names to configure. The supported metric names are `CPUUtilization` and `MemoryUtilization`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** resolutionSeconds **   <a name="ECS-Type-MetricConfiguration-resolutionSeconds"></a>
The resolution, in seconds, at which to collect the metrics. The valid values are `20` and `60`.
Type: Integer
Valid Range: Minimum value of 20. Maximum value of 60.
Required: Yes

## See Also
<a name="API_MetricConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/MetricConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/MetricConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/MetricConfiguration)
