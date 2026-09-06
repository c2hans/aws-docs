---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_InstanceLaunchTemplateUpdate.html
---

# InstanceLaunchTemplateUpdate
<a name="API_InstanceLaunchTemplateUpdate"></a>

The instance launch configuration for updating an Amazon ECS Managed Instances capacity provider. You cannot change `capacityOptionType` or `fipsEnabled` after the compute environment is created.

## Contents
<a name="API_InstanceLaunchTemplateUpdate_Contents"></a>

 ** capacityReservations **   <a name="Batch-Type-InstanceLaunchTemplateUpdate-capacityReservations"></a>
The updated capacity reservation configuration.
Type: [CapacityReservationRequest](API_CapacityReservationRequest.md) object
Required: No

 ** ec2InstanceProfileArn **   <a name="Batch-Type-InstanceLaunchTemplateUpdate-ec2InstanceProfileArn"></a>
The updated Amazon Resource Name (ARN) of the Amazon EC2 instance profile for the managed instances.
Type: String
Required: No

 ** instanceMetadataTagsPropagation **   <a name="Batch-Type-InstanceLaunchTemplateUpdate-instanceMetadataTagsPropagation"></a>
Specifies whether instance tags are accessible from the instance metadata service (IMDS).
Type: Boolean
Required: No

 ** instanceRequirements **   <a name="Batch-Type-InstanceLaunchTemplateUpdate-instanceRequirements"></a>
The updated instance type requirements for the capacity provider.
Type: [InstanceRequirementsRequest](API_InstanceRequirementsRequest.md) object
Required: No

 ** localStorageConfiguration **   <a name="Batch-Type-InstanceLaunchTemplateUpdate-localStorageConfiguration"></a>
The updated local storage configuration.
Type: [ManagedInstancesLocalStorageConfiguration](API_ManagedInstancesLocalStorageConfiguration.md) object
Required: No

 ** monitoring **   <a name="Batch-Type-InstanceLaunchTemplateUpdate-monitoring"></a>
The updated monitoring level. Valid values are `BASIC` and `DETAILED`.
Type: String
Required: No

 ** networkConfiguration **   <a name="Batch-Type-InstanceLaunchTemplateUpdate-networkConfiguration"></a>
The updated network configuration for the managed instances.
Type: [ManagedInstancesNetworkConfiguration](API_ManagedInstancesNetworkConfiguration.md) object
Required: No

 ** storageConfiguration **   <a name="Batch-Type-InstanceLaunchTemplateUpdate-storageConfiguration"></a>
The updated storage configuration for the managed instances.
Type: [ManagedInstancesStorageConfiguration](API_ManagedInstancesStorageConfiguration.md) object
Required: No

## See Also
<a name="API_InstanceLaunchTemplateUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/InstanceLaunchTemplateUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/InstanceLaunchTemplateUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/InstanceLaunchTemplateUpdate)
