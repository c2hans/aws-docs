---
source_url: https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_PredefinedScalingMetricSpecification.html
---

# PredefinedScalingMetricSpecification
<a name="API_PredefinedScalingMetricSpecification"></a>

Represents a predefined metric that can be used for dynamic scaling as part of a target tracking scaling policy.

## Contents
<a name="API_PredefinedScalingMetricSpecification_Contents"></a>

 ** PredefinedScalingMetricType **   <a name="autoscaling-Type-PredefinedScalingMetricSpecification-PredefinedScalingMetricType"></a>
The metric type. The `ALBRequestCountPerTarget` metric type applies only to Auto Scaling groups, Spot Fleet requests, and ECS services.
Type: String
Valid Values: `ASGAverageCPUUtilization | ASGAverageNetworkIn | ASGAverageNetworkOut | DynamoDBReadCapacityUtilization | DynamoDBWriteCapacityUtilization | ECSServiceAverageCPUUtilization | ECSServiceAverageMemoryUtilization | ALBRequestCountPerTarget | RDSReaderAverageCPUUtilization | RDSReaderAverageDatabaseConnections | EC2SpotFleetRequestAverageCPUUtilization | EC2SpotFleetRequestAverageNetworkIn | EC2SpotFleetRequestAverageNetworkOut`
Required: Yes

 ** ResourceLabel **   <a name="autoscaling-Type-PredefinedScalingMetricSpecification-ResourceLabel"></a>
Identifies the resource associated with the metric type. You can't specify a resource label unless the metric type is `ALBRequestCountPerTarget` and there is a target group for an Application Load Balancer attached to the Auto Scaling group, Spot Fleet request, or ECS service.
You create the resource label by appending the final portion of the load balancer ARN and the final portion of the target group ARN into a single value, separated by a forward slash (/). The format is app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>, where:
+ app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN
+ targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN.
This is an example: app/EC2Co-EcsEl-1TKLTMITMM0EO/f37c06a68c1748aa/targetgroup/EC2Co-Defau-LDNM7Q3ZH1ZN/6d4ea56ca2d6a18d.
To find the ARN for an Application Load Balancer, use the [DescribeLoadBalancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html) API operation. To find the ARN for the target group, use the [DescribeTargetGroups](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html) API operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1023.
Required: No

## See Also
<a name="API_PredefinedScalingMetricSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-plans-2018-01-06/PredefinedScalingMetricSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-plans-2018-01-06/PredefinedScalingMetricSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-plans-2018-01-06/PredefinedScalingMetricSpecification)
