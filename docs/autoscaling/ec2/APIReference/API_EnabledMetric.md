---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_EnabledMetric.html
---

# EnabledMetric
<a name="API_EnabledMetric"></a>

Describes an enabled Auto Scaling group metric.

## Contents
<a name="API_EnabledMetric_Contents"></a>

 ** Granularity **
The granularity of the metric. The only valid value is `1Minute`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Metric **
One of the following metrics:
+  `GroupMinSize`
+  `GroupMaxSize`
+  `GroupDesiredCapacity`
+  `GroupInServiceInstances`
+  `GroupPendingInstances`
+  `GroupStandbyInstances`
+  `GroupTerminatingInstances`
+  `GroupTotalInstances`
+  `GroupInServiceCapacity`
+  `GroupPendingCapacity`
+  `GroupStandbyCapacity`
+  `GroupTerminatingCapacity`
+  `GroupTotalCapacity`
+  `WarmPoolDesiredCapacity`
+  `WarmPoolWarmedCapacity`
+  `WarmPoolPendingCapacity`
+  `WarmPoolTerminatingCapacity`
+  `WarmPoolTotalCapacity`
+  `GroupAndWarmPoolDesiredCapacity`
+  `GroupAndWarmPoolTotalCapacity`
For more information, see [Amazon CloudWatch metrics for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-metrics.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_EnabledMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/EnabledMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/EnabledMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/EnabledMetric)
