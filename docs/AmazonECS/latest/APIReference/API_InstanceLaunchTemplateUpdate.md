---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_InstanceLaunchTemplateUpdate.html
---

# InstanceLaunchTemplateUpdate
<a name="API_InstanceLaunchTemplateUpdate"></a>

The updated launch template configuration for Amazon ECS Managed Instances. You can modify the instance profile, network configuration, storage settings, and instance requirements. Changes apply to new instances launched after the update.

For more information, see [Store instance launch parameters in Amazon EC2 launch templates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_InstanceLaunchTemplateUpdate_Contents"></a>

 ** capacityReservations **   <a name="ECS-Type-InstanceLaunchTemplateUpdate-capacityReservations"></a>
The updated capacity reservations specifications for Amazon ECS Managed Instances. Changes to capacity reservations settings apply to new instances launched after the update.
Type: [CapacityReservationRequest](API_CapacityReservationRequest.md) object
Required: No

 ** ec2InstanceProfileArn **   <a name="ECS-Type-InstanceLaunchTemplateUpdate-ec2InstanceProfileArn"></a>
The updated Amazon Resource Name (ARN) of the instance profile. The new instance profile must have the necessary permissions for your tasks.
For more information, see [Amazon ECS instance profile for Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-instance-profile.html) in the *Amazon ECS Developer Guide*.
Type: String
Required: No

 ** instanceMetadataTagsPropagation **   <a name="ECS-Type-InstanceLaunchTemplateUpdate-instanceMetadataTagsPropagation"></a>
Determines whether tags are propagated to the instance metadata service (IMDS) for Amazon EC2 instances launched by the Managed Instances capacity provider. When enabled, all tags associated with the instance are available through the instance metadata service. When disabled, tags are not propagated to IMDS.
Disable this setting if your tags contain characters that are not compatible with IMDS, such as `/`. IMDS requires tag keys to match the pattern `[0-9a-zA-Z\-_+=,.@:]{1,255}`.
The default value is `true`.
For more information, see [Work with instance tags in instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#work-with-tags-in-IMDS) in the *Amazon EC2 User Guide*.
Type: Boolean
Required: No

 ** instanceRequirements **   <a name="ECS-Type-InstanceLaunchTemplateUpdate-instanceRequirements"></a>
The updated instance requirements for attribute-based instance type selection. Changes to instance requirements affect which instance types Amazon ECS selects for new instances.
Type: [InstanceRequirementsRequest](API_InstanceRequirementsRequest.md) object
Required: No

 ** localStorageConfiguration **   <a name="ECS-Type-InstanceLaunchTemplateUpdate-localStorageConfiguration"></a>
The updated local storage configuration for Amazon ECS Managed Instances. Changes to local storage settings apply to new instances launched after the update.
Type: [ManagedInstancesLocalStorageConfiguration](API_ManagedInstancesLocalStorageConfiguration.md) object
Required: No

 ** monitoring **   <a name="ECS-Type-InstanceLaunchTemplateUpdate-monitoring"></a>
CloudWatch provides two categories of monitoring: basic monitoring and detailed monitoring. By default, your managed instance is configured for basic monitoring. You can optionally enable detailed monitoring to help you more quickly identify and act on operational issues. You can enable or turn off detailed monitoring at launch or when the managed instance is running or stopped. For more information, see [Detailed monitoring for Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/detailed-monitoring-managed-instances.html) in the Amazon ECS Developer Guide.
Type: String
Valid Values: `BASIC | DETAILED`
Required: No

 ** networkConfiguration **   <a name="ECS-Type-InstanceLaunchTemplateUpdate-networkConfiguration"></a>
The updated network configuration for Amazon ECS Managed Instances. Changes to subnets and security groups affect new instances launched after the update.
Type: [ManagedInstancesNetworkConfiguration](API_ManagedInstancesNetworkConfiguration.md) object
Required: No

 ** storageConfiguration **   <a name="ECS-Type-InstanceLaunchTemplateUpdate-storageConfiguration"></a>
The updated storage configuration for Amazon ECS Managed Instances. Changes to storage settings apply to new instances launched after the update.
Type: [ManagedInstancesStorageConfiguration](API_ManagedInstancesStorageConfiguration.md) object
Required: No

## See Also
<a name="API_InstanceLaunchTemplateUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/InstanceLaunchTemplateUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/InstanceLaunchTemplateUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/InstanceLaunchTemplateUpdate)
