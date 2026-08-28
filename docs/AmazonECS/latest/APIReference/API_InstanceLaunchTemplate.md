---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_InstanceLaunchTemplate.html
---

# InstanceLaunchTemplate
<a name="API_InstanceLaunchTemplate"></a>

The launch template configuration for Amazon ECS Managed Instances. This defines how Amazon ECS launches Amazon EC2 instances, including the instance profile for your tasks, network and storage configuration, capacity options, and instance requirements for flexible instance type selection.

## Contents
<a name="API_InstanceLaunchTemplate_Contents"></a>

 ** ec2InstanceProfileArn **   <a name="ECS-Type-InstanceLaunchTemplate-ec2InstanceProfileArn"></a>
The Amazon Resource Name (ARN) of the instance profile that Amazon ECS applies to Amazon ECS Managed Instances. This instance profile must include the necessary permissions for your tasks to access AWS services and resources.
For more information, see [Amazon ECS instance profile for Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-instance-profile.html) in the *Amazon ECS Developer Guide*.
Type: String
Required: Yes

 ** networkConfiguration **   <a name="ECS-Type-InstanceLaunchTemplate-networkConfiguration"></a>
The network configuration for Amazon ECS Managed Instances. This specifies the subnets and security groups that instances use for network connectivity.
Type: [ManagedInstancesNetworkConfiguration](API_ManagedInstancesNetworkConfiguration.md) object
Required: Yes

 ** capacityOptionType **   <a name="ECS-Type-InstanceLaunchTemplate-capacityOptionType"></a>
The capacity option type. This determines whether Amazon ECS launches On-Demand, Spot or Capacity Reservation Instances for your managed instance capacity provider.
Valid values are:
+  `ON_DEMAND` - Launches standard On-Demand Instances. On-Demand Instances provide predictable pricing and availability.
+  `SPOT` - Launches Spot Instances that use spare Amazon EC2 capacity at reduced cost. Spot Instances can be interrupted by Amazon EC2 with a two-minute notification when the capacity is needed back.
+  `RESERVED` - Launches Instances using Amazon EC2 Capacity Reservations. Capacity Reservations allow you to reserve compute capacity for Amazon EC2 instances in a specific Availability Zone.
The default is On-Demand
For more information about Amazon EC2 capacity options, see [Instance purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `ON_DEMAND | SPOT | RESERVED`
Required: No

 ** capacityReservations **   <a name="ECS-Type-InstanceLaunchTemplate-capacityReservations"></a>
Capacity reservation specifications. You can specify:
+ Capacity reservation preference
+ Reservation resource group to be used for targeted capacity reservations
Amazon ECS will launch instances according to the specified criteria.
Type: [CapacityReservationRequest](API_CapacityReservationRequest.md) object
Required: No

 ** fipsEnabled **   <a name="ECS-Type-InstanceLaunchTemplate-fipsEnabled"></a>
Determines whether to enable FIPS 140-2 validated cryptographic modules on EC2 instances launched by the capacity provider. If `true`, instances use FIPS-compliant cryptographic algorithms and modules for enhanced security compliance. If `false`, instances use standard cryptographic implementations.
If not specified, instances are launched with FIPS enabled in AWS GovCloud (US) regions and FIPS disabled in other regions.
Type: Boolean
Required: No

 ** instanceMetadataTagsPropagation **   <a name="ECS-Type-InstanceLaunchTemplate-instanceMetadataTagsPropagation"></a>
Determines whether tags are propagated to the instance metadata service (IMDS) for Amazon EC2 instances launched by the Managed Instances capacity provider. When enabled, all tags associated with the instance are available through the instance metadata service. When disabled, tags are not propagated to IMDS.
Disable this setting if your tags contain characters that are not compatible with IMDS, such as `/`. IMDS requires tag keys to match the pattern `[0-9a-zA-Z\-_+=,.@:]{1,255}`.
The default value is `true`.
For more information, see [Work with instance tags in instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#work-with-tags-in-IMDS) in the *Amazon EC2 User Guide*.
Type: Boolean
Required: No

 ** instanceRequirements **   <a name="ECS-Type-InstanceLaunchTemplate-instanceRequirements"></a>
The instance requirements. You can specify:
+ The instance types
+ Instance requirements such as vCPU count, memory, network performance, and accelerator specifications
Amazon ECS automatically selects the instances that match the specified criteria.
Type: [InstanceRequirementsRequest](API_InstanceRequirementsRequest.md) object
Required: No

 ** localStorageConfiguration **   <a name="ECS-Type-InstanceLaunchTemplate-localStorageConfiguration"></a>
The local storage configuration for Amazon ECS Managed Instances. This defines how ECS uses instance store volumes available on the container instance.
Type: [ManagedInstancesLocalStorageConfiguration](API_ManagedInstancesLocalStorageConfiguration.md) object
Required: No

 ** monitoring **   <a name="ECS-Type-InstanceLaunchTemplate-monitoring"></a>
CloudWatch provides two categories of monitoring: basic monitoring and detailed monitoring. By default, your managed instance is configured for basic monitoring. You can optionally enable detailed monitoring to help you more quickly identify and act on operational issues. You can enable or turn off detailed monitoring at launch or when the managed instance is running or stopped. For more information, see [Detailed monitoring for Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/detailed-monitoring-managed-instances.html) in the Amazon ECS Developer Guide.
Type: String
Valid Values: `BASIC | DETAILED`
Required: No

 ** storageConfiguration **   <a name="ECS-Type-InstanceLaunchTemplate-storageConfiguration"></a>
The storage configuration for Amazon ECS Managed Instances. This defines the data volume properties for the instances.
Type: [ManagedInstancesStorageConfiguration](API_ManagedInstancesStorageConfiguration.md) object
Required: No

## See Also
<a name="API_InstanceLaunchTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/InstanceLaunchTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/InstanceLaunchTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/InstanceLaunchTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
