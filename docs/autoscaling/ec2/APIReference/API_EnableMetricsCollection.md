---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_EnableMetricsCollection.html
---

# EnableMetricsCollection
<a name="API_EnableMetricsCollection"></a>

Enables group metrics collection for the specified Auto Scaling group.

You can use these metrics to track changes in an Auto Scaling group and to set alarms on threshold values. You can view group metrics using the Amazon EC2 Auto Scaling console or the CloudWatch console. For more information, see [Monitor CloudWatch metrics for your Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-cloudwatch-monitoring.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Request Parameters
<a name="API_EnableMetricsCollection_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** Granularity **
The frequency at which Amazon EC2 Auto Scaling sends aggregated data to CloudWatch. The only valid value is `1Minute`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 **Metrics.member.N**
Identifies the metrics to enable.
You can specify one or more of the following metrics:
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
If you specify `Granularity` and don't specify any metrics, all metrics are enabled.
For more information, see [Amazon CloudWatch metrics for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-metrics.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## Errors
<a name="API_EnableMetricsCollection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_EnableMetricsCollection_Examples"></a>

### Example
<a name="API_EnableMetricsCollection_Example_1"></a>

This example illustrates one usage of EnableMetricsCollection.

#### Sample Request
<a name="API_EnableMetricsCollection_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=EnableMetricsCollection
&AutoScalingGroupName=my-asg
&Granularity=1Minute
&Metrics.member.1=GroupDesiredCapacity
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_EnableMetricsCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/EnableMetricsCollection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/EnableMetricsCollection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/EnableMetricsCollection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/EnableMetricsCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/EnableMetricsCollection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/EnableMetricsCollection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/EnableMetricsCollection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/EnableMetricsCollection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/EnableMetricsCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/EnableMetricsCollection)
