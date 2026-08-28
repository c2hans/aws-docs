---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PredictiveScalingMetricSpecification.html
---

# PredictiveScalingMetricSpecification
<a name="API_PredictiveScalingMetricSpecification"></a>

This structure specifies the metrics and target utilization settings for a predictive scaling policy.

You must specify either a metric pair, or a load metric and a scaling metric individually. Specifying a metric pair instead of individual metrics provides a simpler way to configure metrics for a scaling policy. You choose the metric pair, and the policy automatically knows the correct sum and average statistics to use for the load metric and the scaling metric.

Example
+ You create a predictive scaling policy and specify `ALBRequestCount` as the value for the metric pair and `1000.0` as the target value. For this type of metric, you must provide the metric dimension for the corresponding target group, so you also provide a resource label for the Application Load Balancer target group that is attached to your Auto Scaling group.
+ The number of requests the target group receives per minute provides the load metric, and the request count averaged between the members of the target group provides the scaling metric. In CloudWatch, this refers to the `RequestCount` and `RequestCountPerTarget` metrics, respectively.
+ For optimal use of predictive scaling, you adhere to the best practice of using a dynamic scaling policy to automatically scale between the minimum capacity and maximum capacity in response to real-time changes in resource utilization.
+ Amazon EC2 Auto Scaling consumes data points for the load metric over the last 14 days and creates an hourly load forecast for predictive scaling. (A minimum of 24 hours of data is required.)
+ After creating the load forecast, Amazon EC2 Auto Scaling determines when to reduce or increase the capacity of your Auto Scaling group in each hour of the forecast period so that the average number of requests received by each instance is as close to 1000 requests per minute as possible at all times.

For information about using custom metrics with predictive scaling, see [Advanced predictive scaling policy configurations using custom metrics](https://docs.aws.amazon.com/autoscaling/ec2/userguide/predictive-scaling-customized-metric-specification.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Contents
<a name="API_PredictiveScalingMetricSpecification_Contents"></a>

 ** TargetValue **
Specifies the target utilization.
Some metrics are based on a count instead of a percentage, such as the request count for an Application Load Balancer or the number of messages in an SQS queue. If the scaling policy specifies one of these metrics, specify the target utilization as the optimal average request or message count per instance during any one-minute interval.
Type: Double
Required: Yes

 ** CustomizedCapacityMetricSpecification **
The customized capacity metric specification.
Type: [PredictiveScalingCustomizedCapacityMetric](API_PredictiveScalingCustomizedCapacityMetric.md) object
Required: No

 ** CustomizedLoadMetricSpecification **
The customized load metric specification.
Type: [PredictiveScalingCustomizedLoadMetric](API_PredictiveScalingCustomizedLoadMetric.md) object
Required: No

 ** CustomizedScalingMetricSpecification **
The customized scaling metric specification.
Type: [PredictiveScalingCustomizedScalingMetric](API_PredictiveScalingCustomizedScalingMetric.md) object
Required: No

 ** PredefinedLoadMetricSpecification **
The predefined load metric specification.
Type: [PredictiveScalingPredefinedLoadMetric](API_PredictiveScalingPredefinedLoadMetric.md) object
Required: No

 ** PredefinedMetricPairSpecification **
The predefined metric pair specification from which Amazon EC2 Auto Scaling determines the appropriate scaling metric and load metric to use.
Type: [PredictiveScalingPredefinedMetricPair](API_PredictiveScalingPredefinedMetricPair.md) object
Required: No

 ** PredefinedScalingMetricSpecification **
The predefined scaling metric specification.
Type: [PredictiveScalingPredefinedScalingMetric](API_PredictiveScalingPredefinedScalingMetric.md) object
Required: No

## See Also
<a name="API_PredictiveScalingMetricSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/PredictiveScalingMetricSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/PredictiveScalingMetricSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/PredictiveScalingMetricSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
