---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
---

# PredefinedMetricSpecification
<a name="API_PredefinedMetricSpecification"></a>

Represents a predefined metric for a target tracking scaling policy to use with Application Auto Scaling.

For more information, [Predefined metrics for target tracking scaling policies](https://docs.aws.amazon.com/autoscaling/application/userguide/monitoring-cloudwatch.html#predefined-metrics) in the *Application Auto Scaling User Guide*.

## Contents
<a name="API_PredefinedMetricSpecification_Contents"></a>

 ** PredefinedMetricType **   <a name="autoscaling-Type-PredefinedMetricSpecification-PredefinedMetricType"></a>
The metric type. The following are notes about specific metric types:
+  `ALBRequestCountPerTarget` - This metric type applies only to Spot Fleets and ECS services.
+  `ECSServiceAverageCPUUtilizationHighResolution` - The high-resolution version of `ECSServiceAverageCPUUtilization` that uses 20-second CloudWatch metrics. Use this metric for target tracking scaling policies that evaluate metrics every 20 seconds. You must enable high-resolution metrics in Amazon ECS before creating a scaling policy with this metric type.
+  `ECSServiceAverageMemoryUtilizationHighResolution` - The high-resolution version of `ECSServiceAverageMemoryUtilization` that uses 20-second CloudWatch metrics. Use this metric for target tracking scaling policies that evaluate metrics every 20 seconds. You must enable high-resolution metrics in Amazon ECS before creating a scaling policy with this metric type.
Type: String
Valid Values: `DynamoDBReadCapacityUtilization | DynamoDBWriteCapacityUtilization | ALBRequestCountPerTarget | RDSReaderAverageCPUUtilization | RDSReaderAverageDatabaseConnections | EC2SpotFleetRequestAverageCPUUtilization | EC2SpotFleetRequestAverageNetworkIn | EC2SpotFleetRequestAverageNetworkOut | SageMakerVariantInvocationsPerInstance | ECSServiceAverageCPUUtilization | ECSServiceAverageMemoryUtilization | AppStreamAverageCapacityUtilization | ComprehendInferenceUtilization | LambdaProvisionedConcurrencyUtilization | CassandraReadCapacityUtilization | CassandraWriteCapacityUtilization | KafkaBrokerStorageUtilization | ElastiCacheEngineCPUUtilization | ElastiCacheDatabaseMemoryUsagePercentage | ElastiCachePrimaryEngineCPUUtilization | ElastiCacheReplicaEngineCPUUtilization | ElastiCacheDatabaseMemoryUsageCountedForEvictPercentage | NeptuneReaderAverageCPUUtilization | SageMakerVariantProvisionedConcurrencyUtilization | ElastiCacheDatabaseCapacityUsageCountedForEvictPercentage | SageMakerInferenceComponentInvocationsPerCopy | WorkSpacesAverageUserSessionsCapacityUtilization | SageMakerInferenceComponentConcurrentRequestsPerCopyHighResolution | SageMakerVariantConcurrentRequestsPerModelHighResolution | ECSServiceAverageCPUUtilizationHighResolution | ECSServiceAverageMemoryUtilizationHighResolution`
Required: Yes

 ** ResourceLabel **   <a name="autoscaling-Type-PredefinedMetricSpecification-ResourceLabel"></a>
Identifies the resource associated with the metric type. You can't specify a resource label unless the metric type is `ALBRequestCountPerTarget` and there is a target group attached to the Spot Fleet or ECS service.
You create the resource label by appending the final portion of the load balancer ARN and the final portion of the target group ARN into a single value, separated by a forward slash (/). The format of the resource label is:
 `app/my-alb/778d41231b141a0f/targetgroup/my-alb-target-group/943f017f100becff`.
Where:
+ app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN
+ targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN.
To find the ARN for an Application Load Balancer, use the [DescribeLoadBalancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html) API operation. To find the ARN for the target group, use the [DescribeTargetGroups](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html) API operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1023.
Required: No

## See Also
<a name="API_PredefinedMetricSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/PredefinedMetricSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/PredefinedMetricSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/PredefinedMetricSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
