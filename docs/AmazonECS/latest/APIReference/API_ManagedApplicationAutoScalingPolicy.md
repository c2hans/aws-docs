---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedApplicationAutoScalingPolicy.html
---

# ManagedApplicationAutoScalingPolicy
<a name="API_ManagedApplicationAutoScalingPolicy"></a>

The Application Auto Scaling policy created by Amazon ECS when you create an Express service.

## Contents
<a name="API_ManagedApplicationAutoScalingPolicy_Contents"></a>

 ** metric **   <a name="ECS-Type-ManagedApplicationAutoScalingPolicy-metric"></a>
The metric used for auto scaling decisions. The available metrics are `ECSServiceAverageCPUUtilization`, `ECSServiceAverageMemoryUtilization`, and `ALBRequestCOuntPerTarget`.
Type: String
Required: Yes

 ** policyType **   <a name="ECS-Type-ManagedApplicationAutoScalingPolicy-policyType"></a>
The type of Application Auto Scaling policy associated with the Express service. Valid values are `TargetTrackingScaling`, `StepScaling`, and `PredictiveScaling`.
Type: String
Required: Yes

 ** status **   <a name="ECS-Type-ManagedApplicationAutoScalingPolicy-status"></a>
The status of Application Auto Scaling policy creation.
Type: String
Valid Values: `PROVISIONING | ACTIVE | DEPROVISIONING | DELETED | FAILED`
Required: Yes

 ** targetValue **   <a name="ECS-Type-ManagedApplicationAutoScalingPolicy-targetValue"></a>
The target value for the auto scaling metric.
Type: Double
Required: Yes

 ** updatedAt **   <a name="ECS-Type-ManagedApplicationAutoScalingPolicy-updatedAt"></a>
The Unix timestamp for when the Application Auto Scaling policy was last updated.
Type: Timestamp
Required: Yes

 ** arn **   <a name="ECS-Type-ManagedApplicationAutoScalingPolicy-arn"></a>
The Amazon Resource Name (ARN) of the Application Auto Scaling policy associated with the Express service.
Type: String
Required: No

 ** statusReason **   <a name="ECS-Type-ManagedApplicationAutoScalingPolicy-statusReason"></a>
Information about why the Application Auto Scaling policy is in the current status.
Type: String
Required: No

## See Also
<a name="API_ManagedApplicationAutoScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedApplicationAutoScalingPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedApplicationAutoScalingPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedApplicationAutoScalingPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
