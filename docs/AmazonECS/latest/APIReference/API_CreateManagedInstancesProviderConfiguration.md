---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateManagedInstancesProviderConfiguration.html
---

# CreateManagedInstancesProviderConfiguration
<a name="API_CreateManagedInstancesProviderConfiguration"></a>

The configuration for creating a Amazon ECS Managed Instances provider. This specifies how Amazon ECS should manage Amazon EC2 instances, including the infrastructure role, instance launch template, and whether to propagate tags from the capacity provider to the instances.

## Contents
<a name="API_CreateManagedInstancesProviderConfiguration_Contents"></a>

 ** infrastructureRoleArn **   <a name="ECS-Type-CreateManagedInstancesProviderConfiguration-infrastructureRoleArn"></a>
The Amazon Resource Name (ARN) of the infrastructure role that Amazon ECS uses to manage instances on your behalf. This role must have permissions to launch, terminate, and manage Amazon EC2 instances, as well as access to other AWS services required for Amazon ECS Managed Instances functionality.
For more information, see [Amazon ECS infrastructure IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html) in the *Amazon ECS Developer Guide*.
Type: String
Required: Yes

 ** instanceLaunchTemplate **   <a name="ECS-Type-CreateManagedInstancesProviderConfiguration-instanceLaunchTemplate"></a>
The launch template configuration that specifies how Amazon ECS should launch Amazon EC2 instances. This includes the instance profile, network configuration, storage settings, and instance requirements for attribute-based instance type selection.
For more information, see [Store instance launch parameters in Amazon EC2 launch templates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon EC2 User Guide*.
Type: [InstanceLaunchTemplate](API_InstanceLaunchTemplate.md) object
Required: Yes

 ** autoRepairConfiguration **   <a name="ECS-Type-CreateManagedInstancesProviderConfiguration-autoRepairConfiguration"></a>
The auto repair configuration for the Amazon ECS Managed Instances capacity provider. Use this to enable or disable automatic replacement of container instances that are detected as unhealthy.
Type: [AutoRepairConfiguration](API_AutoRepairConfiguration.md) object
Required: No

 ** infrastructureOptimization **   <a name="ECS-Type-CreateManagedInstancesProviderConfiguration-infrastructureOptimization"></a>
Defines how Amazon ECS Managed Instances optimizes the infrastastructure in your capacity provider. Provides control over the delay between when EC2 instances become idle or underutilized and when Amazon ECS optimizes them.
Type: [InfrastructureOptimization](API_InfrastructureOptimization.md) object
Required: No

 ** propagateTags **   <a name="ECS-Type-CreateManagedInstancesProviderConfiguration-propagateTags"></a>
Specifies whether to propagate tags from the capacity provider to the Amazon ECS Managed Instances. When enabled, tags applied to the capacity provider are automatically applied to all instances launched by this provider.
Type: String
Valid Values: `CAPACITY_PROVIDER | NONE`
Required: No

## See Also
<a name="API_CreateManagedInstancesProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/CreateManagedInstancesProviderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/CreateManagedInstancesProviderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/CreateManagedInstancesProviderConfiguration)
