---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredictiveScalingPolicyConfiguration.html
---

# PredictiveScalingPolicyConfiguration
<a name="API_PredictiveScalingPolicyConfiguration"></a>

 Represents a predictive scaling policy configuration. Predictive scaling is supported on Amazon ECS services.

## Contents
<a name="API_PredictiveScalingPolicyConfiguration_Contents"></a>

 ** MetricSpecifications **   <a name="autoscaling-Type-PredictiveScalingPolicyConfiguration-MetricSpecifications"></a>
 This structure includes the metrics and target utilization to use for predictive scaling.
This is an array, but we currently only support a single metric specification. That is, you can specify a target value and a single metric pair, or a target value and one scaling metric and one load metric.
Type: Array of [PredictiveScalingMetricSpecification](API_PredictiveScalingMetricSpecification.md) objects
Required: Yes

 ** MaxCapacityBreachBehavior **   <a name="autoscaling-Type-PredictiveScalingPolicyConfiguration-MaxCapacityBreachBehavior"></a>
 Defines the behavior that should be applied if the forecast capacity approaches or exceeds the maximum capacity. Defaults to `HonorMaxCapacity` if not specified.
Type: String
Valid Values: `HonorMaxCapacity | IncreaseMaxCapacity`
Required: No

 ** MaxCapacityBuffer **   <a name="autoscaling-Type-PredictiveScalingPolicyConfiguration-MaxCapacityBuffer"></a>
 The size of the capacity buffer to use when the forecast capacity is close to or exceeds the maximum capacity. The value is specified as a percentage relative to the forecast capacity. For example, if the buffer is 10, this means a 10 percent buffer, such that if the forecast capacity is 50, and the maximum capacity is 40, then the effective maximum capacity is 55.
Required if the `MaxCapacityBreachBehavior` property is set to `IncreaseMaxCapacity`, and cannot be used otherwise.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Mode **   <a name="autoscaling-Type-PredictiveScalingPolicyConfiguration-Mode"></a>
 The predictive scaling mode. Defaults to `ForecastOnly` if not specified.
Type: String
Valid Values: `ForecastOnly | ForecastAndScale`
Required: No

 ** SchedulingBufferTime **   <a name="autoscaling-Type-PredictiveScalingPolicyConfiguration-SchedulingBufferTime"></a>
 The amount of time, in seconds, that the start time can be advanced.
The value must be less than the forecast interval duration of 3600 seconds (60 minutes). Defaults to 300 seconds if not specified.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3600.
Required: No

## See Also
<a name="API_PredictiveScalingPolicyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/PredictiveScalingPolicyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/PredictiveScalingPolicyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/PredictiveScalingPolicyConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
