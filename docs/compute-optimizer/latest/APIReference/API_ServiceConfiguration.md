---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ServiceConfiguration.html
---

# ServiceConfiguration
<a name="API_ServiceConfiguration"></a>

 The Amazon ECS service configurations used for recommendations.

## Contents
<a name="API_ServiceConfiguration_Contents"></a>

 ** autoScalingConfiguration **   <a name="computeoptimizer-Type-ServiceConfiguration-autoScalingConfiguration"></a>
 Describes the Auto Scaling configuration methods for an Amazon ECS service. This affects the generated recommendations. For example, if Auto Scaling is configured on a service’s CPU, then Compute Optimizer doesn’t generate CPU size recommendations.
The Auto Scaling configuration methods include:
+  `TARGET_TRACKING_SCALING_CPU` — If the Amazon ECS service is configured to use target scaling on CPU, Compute Optimizer doesn't generate CPU recommendations.
+  `TARGET_TRACKING_SCALING_MEMORY` — If the Amazon ECS service is configured to use target scaling on memory, Compute Optimizer doesn't generate memory recommendations.
For more information about step scaling and target scaling, see [ Step scaling policies for Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html) and [ Target tracking scaling policies for Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) in the *Application Auto Scaling User Guide*.
Type: String
Valid Values: `TargetTrackingScalingCpu | TargetTrackingScalingMemory`
Required: No

 ** containerConfigurations **   <a name="computeoptimizer-Type-ServiceConfiguration-containerConfigurations"></a>
 The container configurations within a task of an Amazon ECS service.
Type: Array of [ContainerConfiguration](API_ContainerConfiguration.md) objects
Required: No

 ** cpu **   <a name="computeoptimizer-Type-ServiceConfiguration-cpu"></a>
 The number of CPU units used by the tasks in the Amazon ECS service.
Type: Integer
Required: No

 ** memory **   <a name="computeoptimizer-Type-ServiceConfiguration-memory"></a>
 The amount of memory used by the tasks in the Amazon ECS service.
Type: Integer
Required: No

 ** taskDefinitionArn **   <a name="computeoptimizer-Type-ServiceConfiguration-taskDefinitionArn"></a>
 The task definition ARN used by the tasks in the Amazon ECS service.
Type: String
Required: No

## See Also
<a name="API_ServiceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/ServiceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/ServiceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/ServiceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
