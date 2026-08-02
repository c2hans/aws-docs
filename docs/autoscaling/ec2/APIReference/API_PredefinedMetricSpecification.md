---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PredefinedMetricSpecification.html
---

# PredefinedMetricSpecification
<a name="API_PredefinedMetricSpecification"></a>

Represents a predefined metric for a target tracking scaling policy to use with Amazon EC2 Auto Scaling.

## Contents
<a name="API_PredefinedMetricSpecification_Contents"></a>

 ** PredefinedMetricType **
The metric type. The following predefined metrics are available:
+  `ASGAverageCPUUtilization` - Average CPU utilization of the Auto Scaling group.
+  `ASGAverageNetworkIn` - Average number of bytes received on all network interfaces by the Auto Scaling group.
+  `ASGAverageNetworkOut` - Average number of bytes sent out on all network interfaces by the Auto Scaling group.
+  `ALBRequestCountPerTarget` - Average Application Load Balancer request count per target for your Auto Scaling group.
Type: String
Valid Values: `ASGAverageCPUUtilization | ASGAverageNetworkIn | ASGAverageNetworkOut | ALBRequestCountPerTarget`
Required: Yes

 ** ResourceLabel **
A label that uniquely identifies a specific Application Load Balancer target group from which to determine the average request count served by your Auto Scaling group. You can't specify a resource label unless the target group is attached to the Auto Scaling group.
You create the resource label by appending the final portion of the load balancer ARN and the final portion of the target group ARN into a single value, separated by a forward slash (/). The format of the resource label is:
 `app/my-alb/778d41231b141a0f/targetgroup/my-alb-target-group/943f017f100becff`.
Where:
+ app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN
+ targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN.
To find the ARN for an Application Load Balancer, use the [DescribeLoadBalancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html) API operation. To find the ARN for the target group, use the [DescribeTargetGroups](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html) API operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1023.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_PredefinedMetricSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/PredefinedMetricSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/PredefinedMetricSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/PredefinedMetricSpecification)
