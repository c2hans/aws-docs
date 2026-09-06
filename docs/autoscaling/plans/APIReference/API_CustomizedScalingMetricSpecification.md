---
source_url: https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_CustomizedScalingMetricSpecification.html
---

# CustomizedScalingMetricSpecification
<a name="API_CustomizedScalingMetricSpecification"></a>

Represents a CloudWatch metric of your choosing for a target tracking scaling policy to use with a scaling plan.

To create your customized scaling metric specification:
+ Add values for each required parameter from CloudWatch. You can use an existing metric, or a new metric that you create. To use your own metric, you must first publish the metric to CloudWatch. For more information, see [Publishing custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) in the *Amazon CloudWatch User Guide*.
+ Choose a metric that changes proportionally with capacity. The value of the metric should increase or decrease in inverse proportion to the number of capacity units. That is, the value of the metric should decrease when capacity increases, and increase when capacity decreases.

For more information about the CloudWatch terminology below, see [Amazon CloudWatch concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html) in the *Amazon CloudWatch User Guide*.

## Contents
<a name="API_CustomizedScalingMetricSpecification_Contents"></a>

 ** MetricName **   <a name="autoscaling-Type-CustomizedScalingMetricSpecification-MetricName"></a>
The name of the metric. To get the exact metric name, namespace, and dimensions, inspect the [Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html) object that is returned by a call to [ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html).
Type: String
Required: Yes

 ** Namespace **   <a name="autoscaling-Type-CustomizedScalingMetricSpecification-Namespace"></a>
The namespace of the metric.
Type: String
Required: Yes

 ** Statistic **   <a name="autoscaling-Type-CustomizedScalingMetricSpecification-Statistic"></a>
The statistic of the metric.
Type: String
Valid Values: `Average | Minimum | Maximum | SampleCount | Sum`
Required: Yes

 ** Dimensions **   <a name="autoscaling-Type-CustomizedScalingMetricSpecification-Dimensions"></a>
The dimensions of the metric.
Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.
Type: Array of [MetricDimension](API_MetricDimension.md) objects
Required: No

 ** Unit **   <a name="autoscaling-Type-CustomizedScalingMetricSpecification-Unit"></a>
The unit of the metric. For a complete list of the units that CloudWatch supports, see the [MetricDatum](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html) data type in the *Amazon CloudWatch API Reference*.
Type: String
Required: No

## See Also
<a name="API_CustomizedScalingMetricSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-plans-2018-01-06/CustomizedScalingMetricSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-plans-2018-01-06/CustomizedScalingMetricSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-plans-2018-01-06/CustomizedScalingMetricSpecification)
