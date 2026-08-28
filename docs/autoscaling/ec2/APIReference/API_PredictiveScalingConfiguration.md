---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PredictiveScalingConfiguration.html
---

# PredictiveScalingConfiguration
<a name="API_PredictiveScalingConfiguration"></a>

Represents a predictive scaling policy configuration to use with Amazon EC2 Auto Scaling.

## Contents
<a name="API_PredictiveScalingConfiguration_Contents"></a>

 ** MetricSpecifications.member.N **
This structure includes the metrics and target utilization to use for predictive scaling.
This is an array, but we currently only support a single metric specification. That is, you can specify a target value and a single metric pair, or a target value and one scaling metric and one load metric.
Type: Array of [PredictiveScalingMetricSpecification](API_PredictiveScalingMetricSpecification.md) objects
Required: Yes

 ** MaxCapacityBreachBehavior **
Defines the behavior that should be applied if the forecast capacity approaches or exceeds the maximum capacity of the Auto Scaling group. Defaults to `HonorMaxCapacity` if not specified.
The following are possible values:
+  `HonorMaxCapacity` - Amazon EC2 Auto Scaling can't increase the maximum capacity of the group when the forecast capacity is close to or exceeds the maximum capacity.
+  `IncreaseMaxCapacity` - Amazon EC2 Auto Scaling can increase the maximum capacity of the group when the forecast capacity is close to or exceeds the maximum capacity. The upper limit is determined by the forecasted capacity and the value for `MaxCapacityBuffer`.
Use caution when allowing the maximum capacity to be automatically increased. This can lead to more instances being launched than intended if the increased maximum capacity is not monitored and managed. The increased maximum capacity then becomes the new normal maximum capacity for the Auto Scaling group until you manually update it. The maximum capacity does not automatically decrease back to the original maximum.
Type: String
Valid Values: `HonorMaxCapacity | IncreaseMaxCapacity`
Required: No

 ** MaxCapacityBuffer **
The size of the capacity buffer to use when the forecast capacity is close to or exceeds the maximum capacity. The value is specified as a percentage relative to the forecast capacity. For example, if the buffer is 10, this means a 10 percent buffer, such that if the forecast capacity is 50, and the maximum capacity is 40, then the effective maximum capacity is 55.
If set to 0, Amazon EC2 Auto Scaling may scale capacity higher than the maximum capacity to equal but not exceed forecast capacity.
Required if the `MaxCapacityBreachBehavior` property is set to `IncreaseMaxCapacity`, and cannot be used otherwise.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Mode **
The predictive scaling mode. Defaults to `ForecastOnly` if not specified.
Type: String
Valid Values: `ForecastAndScale | ForecastOnly`
Required: No

 ** SchedulingBufferTime **
The amount of time, in seconds, by which the instance launch time can be advanced. For example, the forecast says to add capacity at 10:00 AM, and you choose to pre-launch instances by 5 minutes. In that case, the instances will be launched at 9:55 AM. The intention is to give resources time to be provisioned. It can take a few minutes to launch an EC2 instance. The actual amount of time required depends on several factors, such as the size of the instance and whether there are startup scripts to complete.
The value must be less than the forecast interval duration of 3600 seconds (60 minutes). Defaults to 300 seconds if not specified.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_PredictiveScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/PredictiveScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/PredictiveScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/PredictiveScalingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
