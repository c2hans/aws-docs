---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_InstanceLaunchTemplate.html
---

# InstanceLaunchTemplate
<a name="API_InstanceLaunchTemplate"></a>

The instance launch configuration for an Amazon ECS Managed Instances capacity provider. Specifies the instance profile, networking, instance selection constraints, capacity pricing model, storage, and monitoring settings.

## Contents
<a name="API_InstanceLaunchTemplate_Contents"></a>

 ** ec2InstanceProfileArn **   <a name="Batch-Type-InstanceLaunchTemplate-ec2InstanceProfileArn"></a>
The Amazon Resource Name (ARN) of the Amazon EC2 instance profile for the managed instances. The instance profile must use the `AmazonECSInstanceRolePolicyForManagedInstances` managed policy with a trust policy for `ec2.amazonaws.com`.
Type: String
Required: Yes

 ** networkConfiguration **   <a name="Batch-Type-InstanceLaunchTemplate-networkConfiguration"></a>
The network configuration for the managed instances. Specifies the VPC subnets and security groups where instances are launched.
Type: [ManagedInstancesNetworkConfiguration](API_ManagedInstancesNetworkConfiguration.md) object
Required: Yes

 ** capacityOptionType **   <a name="Batch-Type-InstanceLaunchTemplate-capacityOptionType"></a>
The capacity pricing model for the managed instances. Valid values:
+  `ON_DEMAND` (default) — On-Demand pricing.
+  `SPOT` — Spot Instances, which can provide significant cost savings for fault-tolerant workloads.
Type: String
Required: No

 ** capacityReservations **   <a name="Batch-Type-InstanceLaunchTemplate-capacityReservations"></a>
The capacity reservation configuration for the managed instances. Use this to target On-Demand Capacity Reservations or Reserved Instances for predictable capacity and cost optimization.
Type: [CapacityReservationRequest](API_CapacityReservationRequest.md) object
Required: No

 ** fipsEnabled **   <a name="Batch-Type-InstanceLaunchTemplate-fipsEnabled"></a>
Specifies whether FIPS 140-2 validated cryptographic modules are enabled on the managed instances. Not available in all Regions.
Type: Boolean
Required: No

 ** instanceMetadataTagsPropagation **   <a name="Batch-Type-InstanceLaunchTemplate-instanceMetadataTagsPropagation"></a>
Specifies whether instance tags are accessible from the instance metadata service (IMDS). If not specified, instance tags are not accessible from IMDS.
Type: Boolean
Required: No

 ** instanceRequirements **   <a name="Batch-Type-InstanceLaunchTemplate-instanceRequirements"></a>
The instance type requirements for the capacity provider. Use this to constrain which Amazon EC2 instance types Amazon ECS can launch. If not specified, all available instance types are eligible.
Type: [InstanceRequirementsRequest](API_InstanceRequirementsRequest.md) object
Required: No

 ** localStorageConfiguration **   <a name="Batch-Type-InstanceLaunchTemplate-localStorageConfiguration"></a>
The local storage configuration for the managed instances. If not specified, instance store volumes are not available to containers.
Type: [ManagedInstancesLocalStorageConfiguration](API_ManagedInstancesLocalStorageConfiguration.md) object
Required: No

 ** monitoring **   <a name="Batch-Type-InstanceLaunchTemplate-monitoring"></a>
The level of CloudWatch monitoring for the managed instances. Valid values are `BASIC` and `DETAILED`.
Type: String
Required: No

 ** storageConfiguration **   <a name="Batch-Type-InstanceLaunchTemplate-storageConfiguration"></a>
The storage configuration for the managed instances. Configures the root EBS volume size. If not specified, the service uses the default EBS volume size for the instance type.
Type: [ManagedInstancesStorageConfiguration](API_ManagedInstancesStorageConfiguration.md) object
Required: No

## See Also
<a name="API_InstanceLaunchTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/InstanceLaunchTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/InstanceLaunchTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/InstanceLaunchTemplate)
