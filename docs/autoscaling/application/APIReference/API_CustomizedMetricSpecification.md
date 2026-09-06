---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_CustomizedMetricSpecification.html
---

# CustomizedMetricSpecification
<a name="API_CustomizedMetricSpecification"></a>

Represents a CloudWatch metric of your choosing for a target tracking scaling policy to use with Application Auto Scaling.

For information about the available metrics for a service, see [AWS services that publish CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) in the *Amazon CloudWatch User Guide*.

To create your customized metric specification:
+ Add values for each required parameter from CloudWatch. You can use an existing metric, or a new metric that you create. To use your own metric, you must first publish the metric to CloudWatch. For more information, see [Publish custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) in the *Amazon CloudWatch User Guide*.
+ Choose a metric that changes proportionally with capacity. The value of the metric should increase or decrease in inverse proportion to the number of capacity units. That is, the value of the metric should decrease when capacity increases, and increase when capacity decreases.

For more information about the CloudWatch terminology below, see [Amazon CloudWatch concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html) in the *Amazon CloudWatch User Guide*.

## Contents
<a name="API_CustomizedMetricSpecification_Contents"></a>

 ** Dimensions **   <a name="autoscaling-Type-CustomizedMetricSpecification-Dimensions"></a>
The dimensions of the metric.
Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.
Type: Array of [MetricDimension](API_MetricDimension.md) objects
Required: No

 ** MetricName **   <a name="autoscaling-Type-CustomizedMetricSpecification-MetricName"></a>
The name of the metric. To get the exact metric name, namespace, and dimensions, inspect the [Metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html) object that's returned by a call to [ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html).
Type: String
Required: No

 ** Metrics **   <a name="autoscaling-Type-CustomizedMetricSpecification-Metrics"></a>
The metrics to include in the target tracking scaling policy, as a metric data query. This can include both raw metric and metric math expressions.
Type: Array of [TargetTrackingMetricDataQuery](API_TargetTrackingMetricDataQuery.md) objects
Required: No

 ** Namespace **   <a name="autoscaling-Type-CustomizedMetricSpecification-Namespace"></a>
The namespace of the metric.
Type: String
Required: No

 ** Statistic **   <a name="autoscaling-Type-CustomizedMetricSpecification-Statistic"></a>
The statistic of the metric.
Type: String
Valid Values: `Average | Minimum | Maximum | SampleCount | Sum`
Required: No

 ** Unit **   <a name="autoscaling-Type-CustomizedMetricSpecification-Unit"></a>
The unit of the metric. For a complete list of the units that CloudWatch supports, see the [MetricDatum](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html) data type in the *Amazon CloudWatch API Reference*.
Type: String
Required: No

## See Also
<a name="API_CustomizedMetricSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/CustomizedMetricSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/CustomizedMetricSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/CustomizedMetricSpecification)
