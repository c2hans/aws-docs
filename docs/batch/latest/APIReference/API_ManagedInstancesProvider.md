---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_ManagedInstancesProvider.html
---

# ManagedInstancesProvider
<a name="API_ManagedInstancesProvider"></a>

The configuration for an Amazon ECS Managed Instances capacity provider. This object is required when creating a compute environment with `computeResources.type` set to `ECS_MANAGED_INSTANCES`.

## Contents
<a name="API_ManagedInstancesProvider_Contents"></a>

 ** infrastructureRoleArn **   <a name="Batch-Type-ManagedInstancesProvider-infrastructureRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that Amazon ECS assumes to manage Amazon EC2 instances on your behalf. This role must have a trust policy for `ecs.amazonaws.com`. You must have the `iam:PassRole` permission for this role with the condition `iam:PassedToService: ecs.amazonaws.com`.
Type: String
Required: Yes

 ** instanceLaunchTemplate **   <a name="Batch-Type-ManagedInstancesProvider-instanceLaunchTemplate"></a>
The instance launch configuration for the Amazon ECS Managed Instances capacity provider. Contains networking, instance profile, instance requirements, capacity type, storage, and monitoring configuration.
Type: [InstanceLaunchTemplate](API_InstanceLaunchTemplate.md) object
Required: Yes

 ** infrastructureOptimization **   <a name="Batch-Type-ManagedInstancesProvider-infrastructureOptimization"></a>
The infrastructure optimization configuration for the capacity provider. Specifies the idle-instance scale-in behavior.
Type: [InfrastructureOptimization](API_InfrastructureOptimization.md) object
Required: No

 ** propagateTags **   <a name="Batch-Type-ManagedInstancesProvider-propagateTags"></a>
Specifies whether tags on the capacity provider are propagated to the Amazon EC2 instances it launches. Valid values:
+  `CAPACITY_PROVIDER` — Propagates tags to instances.
+  `NONE` (default) — Does not propagate tags to instances.
Type: String
Required: No

## See Also
<a name="API_ManagedInstancesProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ManagedInstancesProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ManagedInstancesProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ManagedInstancesProvider)
