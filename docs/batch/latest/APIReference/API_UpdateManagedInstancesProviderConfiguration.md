---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateManagedInstancesProviderConfiguration.html
---

# UpdateManagedInstancesProviderConfiguration
<a name="API_UpdateManagedInstancesProviderConfiguration"></a>

The configuration for updating an Amazon ECS Managed Instances capacity provider. Used in `UpdateComputeEnvironment` requests. The `capacityOptionType` and `fipsEnabled` fields cannot be changed on update.

## Contents
<a name="API_UpdateManagedInstancesProviderConfiguration_Contents"></a>

 ** infrastructureOptimization **   <a name="Batch-Type-UpdateManagedInstancesProviderConfiguration-infrastructureOptimization"></a>
The updated infrastructure optimization configuration.
Type: [InfrastructureOptimization](API_InfrastructureOptimization.md) object
Required: No

 ** infrastructureRoleArn **   <a name="Batch-Type-UpdateManagedInstancesProviderConfiguration-infrastructureRoleArn"></a>
The updated Amazon Resource Name (ARN) of the IAM role that Amazon ECS assumes to manage Amazon EC2 instances on your behalf.
Type: String
Required: No

 ** instanceLaunchTemplate **   <a name="Batch-Type-UpdateManagedInstancesProviderConfiguration-instanceLaunchTemplate"></a>
The updated instance launch configuration for the Amazon ECS Managed Instances capacity provider.
Type: [InstanceLaunchTemplateUpdate](API_InstanceLaunchTemplateUpdate.md) object
Required: No

 ** propagateTags **   <a name="Batch-Type-UpdateManagedInstancesProviderConfiguration-propagateTags"></a>
Specifies whether tags on the capacity provider are propagated to the Amazon EC2 instances it launches. Valid values:
+  `CAPACITY_PROVIDER` — Propagates tags to instances.
+  `NONE` — Does not propagate tags to instances.
Type: String
Required: No

## See Also
<a name="API_UpdateManagedInstancesProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/UpdateManagedInstancesProviderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/UpdateManagedInstancesProviderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/UpdateManagedInstancesProviderConfiguration)
