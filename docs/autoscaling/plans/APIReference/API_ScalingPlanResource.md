---
source_url: https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ScalingPlanResource.html
---

# ScalingPlanResource
<a name="API_ScalingPlanResource"></a>

Represents a scalable resource.

## Contents
<a name="API_ScalingPlanResource_Contents"></a>

 ** ResourceId **   <a name="autoscaling-Type-ScalingPlanResource-ResourceId"></a>
The ID of the resource. This string consists of the resource type and unique identifier.
+ Auto Scaling group - The resource type is `autoScalingGroup` and the unique identifier is the name of the Auto Scaling group. Example: `autoScalingGroup/my-asg`.
+ ECS service - The resource type is `service` and the unique identifier is the cluster name and service name. Example: `service/default/sample-webapp`.
+ Spot Fleet request - The resource type is `spot-fleet-request` and the unique identifier is the Spot Fleet request ID. Example: `spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`.
+ DynamoDB table - The resource type is `table` and the unique identifier is the resource ID. Example: `table/my-table`.
+ DynamoDB global secondary index - The resource type is `index` and the unique identifier is the resource ID. Example: `table/my-table/index/my-table-index`.
+ Aurora DB cluster - The resource type is `cluster` and the unique identifier is the cluster name. Example: `cluster:my-db-cluster`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** ScalableDimension **   <a name="autoscaling-Type-ScalingPlanResource-ScalableDimension"></a>
The scalable dimension for the resource.
+  `autoscaling:autoScalingGroup:DesiredCapacity` - The desired capacity of an Auto Scaling group.
+  `ecs:service:DesiredCount` - The desired task count of an ECS service.
+  `ec2:spot-fleet-request:TargetCapacity` - The target capacity of a Spot Fleet request.
+  `dynamodb:table:ReadCapacityUnits` - The provisioned read capacity for a DynamoDB table.
+  `dynamodb:table:WriteCapacityUnits` - The provisioned write capacity for a DynamoDB table.
+  `dynamodb:index:ReadCapacityUnits` - The provisioned read capacity for a DynamoDB global secondary index.
+  `dynamodb:index:WriteCapacityUnits` - The provisioned write capacity for a DynamoDB global secondary index.
+  `rds:cluster:ReadReplicaCount` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.
Type: String
Valid Values: `autoscaling:autoScalingGroup:DesiredCapacity | ecs:service:DesiredCount | ec2:spot-fleet-request:TargetCapacity | rds:cluster:ReadReplicaCount | dynamodb:table:ReadCapacityUnits | dynamodb:table:WriteCapacityUnits | dynamodb:index:ReadCapacityUnits | dynamodb:index:WriteCapacityUnits`
Required: Yes

 ** ScalingPlanName **   <a name="autoscaling-Type-ScalingPlanResource-ScalingPlanName"></a>
The name of the scaling plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{Print}&&[^|:/]]+`
Required: Yes

 ** ScalingPlanVersion **   <a name="autoscaling-Type-ScalingPlanResource-ScalingPlanVersion"></a>
The version number of the scaling plan.
Type: Long
Required: Yes

 ** ScalingStatusCode **   <a name="autoscaling-Type-ScalingPlanResource-ScalingStatusCode"></a>
The scaling status of the resource.
+  `Active` - The scaling configuration is active.
+  `Inactive` - The scaling configuration is not active because the scaling plan is being created or the scaling configuration could not be applied. Check the status message for more information.
+  `PartiallyActive` - The scaling configuration is partially active because the scaling plan is being created or deleted or the scaling configuration could not be fully applied. Check the status message for more information.
Type: String
Valid Values: `Inactive | PartiallyActive | Active`
Required: Yes

 ** ServiceNamespace **   <a name="autoscaling-Type-ScalingPlanResource-ServiceNamespace"></a>
The namespace of the AWS service.
Type: String
Valid Values: `autoscaling | ecs | ec2 | rds | dynamodb`
Required: Yes

 ** ScalingPolicies **   <a name="autoscaling-Type-ScalingPlanResource-ScalingPolicies"></a>
The scaling policies.
Type: Array of [ScalingPolicy](API_ScalingPolicy.md) objects
Required: No

 ** ScalingStatusMessage **   <a name="autoscaling-Type-ScalingPlanResource-ScalingStatusMessage"></a>
A simple message about the current scaling status of the resource.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_ScalingPlanResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-plans-2018-01-06/ScalingPlanResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-plans-2018-01-06/ScalingPlanResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-plans-2018-01-06/ScalingPlanResource)
