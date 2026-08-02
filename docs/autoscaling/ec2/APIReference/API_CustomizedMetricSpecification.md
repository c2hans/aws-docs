---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CustomizedMetricSpecification.html
---

# CustomizedMetricSpecification
<a name="API_CustomizedMetricSpecification"></a>

Represents a CloudWatch metric of your choosing for a target tracking scaling policy to use with Amazon EC2 Auto Scaling.

To create your customized metric specification:
+ Add values for each required property from CloudWatch. You can use an existing metric, or a new metric that you create. To use your own metric, you must first publish the metric to CloudWatch. For more information, see [Publish custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) in the *Amazon CloudWatch User Guide*.
+ Choose a metric that changes proportionally with capacity. The value of the metric should increase or decrease in inverse proportion to the number of capacity units. That is, the value of the metric should decrease when capacity increases.

For more information about the CloudWatch terminology below, see [Amazon CloudWatch concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html).

**Note**
Each individual service provides information about the metrics, namespace, and dimensions they use. For more information, see [AWS services that publish CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) in the *Amazon CloudWatch User Guide*.

## Contents
<a name="API_CustomizedMetricSpecification_Contents"></a>

 ** Dimensions.member.N **
The dimensions of the metric.
Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.
Type: Array of [MetricDimension](API_MetricDimension.md) objects
Required: No

 ** MetricName **
The name of the metric. To get the exact metric name, namespace, and dimensions, inspect the [Metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html) object that is returned by a call to [ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html).
Type: String
Required: No

 ** Metrics.member.N **
The metrics to include in the target tracking scaling policy, as a metric data query. This can include both raw metric and metric math expressions.
Type: Array of [TargetTrackingMetricDataQuery](API_TargetTrackingMetricDataQuery.md) objects
Required: No

 ** Namespace **
The namespace of the metric.
Type: String
Required: No

 ** Period **
 The period of the metric in seconds. The default value is 60. Accepted values are 10, 30, and 60. For high resolution metric, set the value to less than 60. For more information, see [Create a target tracking policy using high-resolution metrics for faster response](https://docs.aws.amazon.com/autoscaling/ec2/userguide/policy-creating-high-resolution-metrics.html).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** Statistic **
The statistic of the metric.
Type: String
Valid Values: `Average | Minimum | Maximum | SampleCount | Sum`
Required: No

 ** Unit **
The unit of the metric. For a complete list of the units that CloudWatch supports, see the [MetricDatum](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html) data type in the *Amazon CloudWatch API Reference*.
Type: String
Required: No

## See Also
<a name="API_CustomizedMetricSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/CustomizedMetricSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/CustomizedMetricSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/CustomizedMetricSpecification)
