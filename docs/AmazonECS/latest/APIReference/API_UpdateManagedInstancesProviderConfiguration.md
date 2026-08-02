---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateManagedInstancesProviderConfiguration.html
---

# UpdateManagedInstancesProviderConfiguration
<a name="API_UpdateManagedInstancesProviderConfiguration"></a>

The updated configuration for a Amazon ECS Managed Instances provider. You can modify the infrastructure role, instance launch template, and tag propagation settings. Changes apply to new instances launched after the update.

## Contents
<a name="API_UpdateManagedInstancesProviderConfiguration_Contents"></a>

 ** infrastructureRoleArn **   <a name="ECS-Type-UpdateManagedInstancesProviderConfiguration-infrastructureRoleArn"></a>
The updated Amazon Resource Name (ARN) of the infrastructure role. The new role must have the necessary permissions to manage instances and access required AWS services.
For more information, see [Amazon ECS infrastructure IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html) in the *Amazon ECS Developer Guide*.
Type: String
Required: Yes

 ** instanceLaunchTemplate **   <a name="ECS-Type-UpdateManagedInstancesProviderConfiguration-instanceLaunchTemplate"></a>
The updated launch template configuration. Changes to the launch template affect new instances launched after the update, while existing instances continue to use their original configuration.
Type: [InstanceLaunchTemplateUpdate](API_InstanceLaunchTemplateUpdate.md) object
Required: Yes

 ** autoRepairConfiguration **   <a name="ECS-Type-UpdateManagedInstancesProviderConfiguration-autoRepairConfiguration"></a>
The updated auto repair configuration for the Amazon ECS Managed Instances capacity provider.
Type: [AutoRepairConfiguration](API_AutoRepairConfiguration.md) object
Required: No

 ** infrastructureOptimization **   <a name="ECS-Type-UpdateManagedInstancesProviderConfiguration-infrastructureOptimization"></a>
The updated infrastructure optimization configuration. Changes to this setting affect how Amazon ECS optimizes instances going forward.
Type: [InfrastructureOptimization](API_InfrastructureOptimization.md) object
Required: No

 ** propagateTags **   <a name="ECS-Type-UpdateManagedInstancesProviderConfiguration-propagateTags"></a>
The updated tag propagation setting. When changed, this affects only new instances launched after the update.
Type: String
Valid Values: `CAPACITY_PROVIDER | NONE`
Required: No

## See Also
<a name="API_UpdateManagedInstancesProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/UpdateManagedInstancesProviderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/UpdateManagedInstancesProviderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/UpdateManagedInstancesProviderConfiguration)
