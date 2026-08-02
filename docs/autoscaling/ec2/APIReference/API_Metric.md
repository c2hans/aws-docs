---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_Metric.html
---

# Metric
<a name="API_Metric"></a>

Represents a specific metric.

 `Metric` is a property of the [MetricStat](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_MetricStat.html) object.

## Contents
<a name="API_Metric_Contents"></a>

 ** MetricName **
The name of the metric.
Type: String
Required: Yes

 ** Namespace **
The namespace of the metric. For more information, see the table in [AWS services that publish CloudWatch metrics ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) in the *Amazon CloudWatch User Guide*.
Type: String
Required: Yes

 ** Dimensions.member.N **
The dimensions for the metric. For the list of available dimensions, see the AWS documentation available from the table in [AWS services that publish CloudWatch metrics ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) in the *Amazon CloudWatch User Guide*.
Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.
Type: Array of [MetricDimension](API_MetricDimension.md) objects
Required: No

## See Also
<a name="API_Metric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/Metric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/Metric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/Metric)
