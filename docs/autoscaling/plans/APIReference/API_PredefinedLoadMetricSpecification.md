---
source_url: https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_PredefinedLoadMetricSpecification.html
---

# PredefinedLoadMetricSpecification
<a name="API_PredefinedLoadMetricSpecification"></a>

Represents a predefined metric that can be used for predictive scaling.

After creating your scaling plan, you can use the console to visualize forecasts for the specified metric. For more information, see [View scaling information for a resource](https://docs.aws.amazon.com/autoscaling/plans/userguide/gs-create-scaling-plan.html#gs-view-resource) in the *Scaling Plans User Guide*.

## Contents
<a name="API_PredefinedLoadMetricSpecification_Contents"></a>

 ** PredefinedLoadMetricType **   <a name="autoscaling-Type-PredefinedLoadMetricSpecification-PredefinedLoadMetricType"></a>
The metric type.
Type: String
Valid Values: `ASGTotalCPUUtilization | ASGTotalNetworkIn | ASGTotalNetworkOut | ALBTargetGroupRequestCount`
Required: Yes

 ** ResourceLabel **   <a name="autoscaling-Type-PredefinedLoadMetricSpecification-ResourceLabel"></a>
Identifies the resource associated with the metric type. You can't specify a resource label unless the metric type is `ALBTargetGroupRequestCount` and there is a target group for an Application Load Balancer attached to the Auto Scaling group.
You create the resource label by appending the final portion of the load balancer ARN and the final portion of the target group ARN into a single value, separated by a forward slash (/). The format is app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>, where:
+ app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN
+ targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN.
This is an example: app/EC2Co-EcsEl-1TKLTMITMM0EO/f37c06a68c1748aa/targetgroup/EC2Co-Defau-LDNM7Q3ZH1ZN/6d4ea56ca2d6a18d.
To find the ARN for an Application Load Balancer, use the [DescribeLoadBalancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html) API operation. To find the ARN for the target group, use the [DescribeTargetGroups](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html) API operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1023.
Required: No

## See Also
<a name="API_PredefinedLoadMetricSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-plans-2018-01-06/PredefinedLoadMetricSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-plans-2018-01-06/PredefinedLoadMetricSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-plans-2018-01-06/PredefinedLoadMetricSpecification)
