---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-instancelaunchtemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider InstanceLaunchTemplate
<a name="aws-properties-ecs-capacityprovider-instancelaunchtemplate"></a>

The launch template configuration for Amazon ECS Managed Instances. This defines how Amazon ECS launches Amazon EC2 instances, including the instance profile for your tasks, network and storage configuration, capacity options, and instance requirements for flexible instance type selection.

## Syntax
<a name="aws-properties-ecs-capacityprovider-instancelaunchtemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-instancelaunchtemplate-syntax.json"></a>

```
{
  "[CapacityOptionType](#cfn-ecs-capacityprovider-instancelaunchtemplate-capacityoptiontype)" : {{String}},
  "[CapacityReservations](#cfn-ecs-capacityprovider-instancelaunchtemplate-capacityreservations)" : {{CapacityReservationRequest}},
  "[Ec2InstanceProfileArn](#cfn-ecs-capacityprovider-instancelaunchtemplate-ec2instanceprofilearn)" : {{String}},
  "[FipsEnabled](#cfn-ecs-capacityprovider-instancelaunchtemplate-fipsenabled)" : {{Boolean}},
  "[InstanceMetadataTagsPropagation](#cfn-ecs-capacityprovider-instancelaunchtemplate-instancemetadatatagspropagation)" : {{Boolean}},
  "[InstanceRequirements](#cfn-ecs-capacityprovider-instancelaunchtemplate-instancerequirements)" : {{InstanceRequirementsRequest}},
  "[LocalStorageConfiguration](#cfn-ecs-capacityprovider-instancelaunchtemplate-localstorageconfiguration)" : {{ManagedInstancesLocalStorageConfiguration}},
  "[Monitoring](#cfn-ecs-capacityprovider-instancelaunchtemplate-monitoring)" : {{String}},
  "[NetworkConfiguration](#cfn-ecs-capacityprovider-instancelaunchtemplate-networkconfiguration)" : {{ManagedInstancesNetworkConfiguration}},
  "[StorageConfiguration](#cfn-ecs-capacityprovider-instancelaunchtemplate-storageconfiguration)" : {{ManagedInstancesStorageConfiguration}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-instancelaunchtemplate-syntax.yaml"></a>

```
  [CapacityOptionType](#cfn-ecs-capacityprovider-instancelaunchtemplate-capacityoptiontype): {{String}}
  [CapacityReservations](#cfn-ecs-capacityprovider-instancelaunchtemplate-capacityreservations): {{
    CapacityReservationRequest}}
  [Ec2InstanceProfileArn](#cfn-ecs-capacityprovider-instancelaunchtemplate-ec2instanceprofilearn): {{String}}
  [FipsEnabled](#cfn-ecs-capacityprovider-instancelaunchtemplate-fipsenabled): {{Boolean}}
  [InstanceMetadataTagsPropagation](#cfn-ecs-capacityprovider-instancelaunchtemplate-instancemetadatatagspropagation): {{Boolean}}
  [InstanceRequirements](#cfn-ecs-capacityprovider-instancelaunchtemplate-instancerequirements): {{
    InstanceRequirementsRequest}}
  [LocalStorageConfiguration](#cfn-ecs-capacityprovider-instancelaunchtemplate-localstorageconfiguration): {{
    ManagedInstancesLocalStorageConfiguration}}
  [Monitoring](#cfn-ecs-capacityprovider-instancelaunchtemplate-monitoring): {{String}}
  [NetworkConfiguration](#cfn-ecs-capacityprovider-instancelaunchtemplate-networkconfiguration): {{
    ManagedInstancesNetworkConfiguration}}
  [StorageConfiguration](#cfn-ecs-capacityprovider-instancelaunchtemplate-storageconfiguration): {{
    ManagedInstancesStorageConfiguration}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-instancelaunchtemplate-properties"></a>

`CapacityOptionType`  <a name="cfn-ecs-capacityprovider-instancelaunchtemplate-capacityoptiontype"></a>
The capacity option type. This determines whether Amazon ECS launches On-Demand, Spot or Capacity Reservation Instances for your managed instance capacity provider.
Valid values are:
+ `ON_DEMAND` - Launches standard On-Demand Instances. On-Demand Instances provide predictable pricing and availability.
+ `SPOT` - Launches Spot Instances that use spare Amazon EC2 capacity at reduced cost. Spot Instances can be interrupted by Amazon EC2 with a two-minute notification when the capacity is needed back.
+ `RESERVED` - Launches Instances using Amazon EC2 Capacity Reservations. Capacity Reservations allow you to reserve compute capacity for Amazon EC2 instances in a specific Availability Zone.
The default is On-Demand
For more information about Amazon EC2 capacity options, see [Instance purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `ON_DEMAND | SPOT | RESERVED`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`CapacityReservations`  <a name="cfn-ecs-capacityprovider-instancelaunchtemplate-capacityreservations"></a>
Capacity reservation specifications. You can specify:
+ Capacity reservation preference
+ Reservation resource group to be used for targeted capacity reservations
Amazon ECS will launch instances according to the specified criteria.
*Required*: No
*Type*: [CapacityReservationRequest](aws-properties-ecs-capacityprovider-capacityreservationrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ec2InstanceProfileArn`  <a name="cfn-ecs-capacityprovider-instancelaunchtemplate-ec2instanceprofilearn"></a>
The Amazon Resource Name (ARN) of the instance profile that Amazon ECS applies to Amazon ECS Managed Instances. This instance profile must include the necessary permissions for your tasks to access AWS services and resources.
For more information, see [Amazon ECS instance profile for Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-instance-profile.html) in the *Amazon ECS Developer Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FipsEnabled`  <a name="cfn-ecs-capacityprovider-instancelaunchtemplate-fipsenabled"></a>
Determines whether to enable FIPS 140-2 validated cryptographic modules on EC2 instances launched by the capacity provider. If `true`, instances use FIPS-compliant cryptographic algorithms and modules for enhanced security compliance. If `false`, instances use standard cryptographic implementations.
If not specified, instances are launched with FIPS enabled in AWS GovCloud (US) regions and FIPS disabled in other regions.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceMetadataTagsPropagation`  <a name="cfn-ecs-capacityprovider-instancelaunchtemplate-instancemetadatatagspropagation"></a>
Determines whether tags are propagated to the instance metadata service (IMDS) for Amazon EC2 instances launched by the Managed Instances capacity provider. When enabled, all tags associated with the instance are available through the instance metadata service. When disabled, tags are not propagated to IMDS.
Disable this setting if your tags contain characters that are not compatible with IMDS, such as `/`. IMDS requires tag keys to match the pattern `[0-9a-zA-Z\-_+=,.@:]{1,255}`.
The default value is `true`.
For more information, see [Work with instance tags in instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#work-with-tags-in-IMDS) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceRequirements`  <a name="cfn-ecs-capacityprovider-instancelaunchtemplate-instancerequirements"></a>
The instance requirements. You can specify:
+ The instance types
+ Instance requirements such as vCPU count, memory, network performance, and accelerator specifications
Amazon ECS automatically selects the instances that match the specified criteria.
*Required*: No
*Type*: [InstanceRequirementsRequest](aws-properties-ecs-capacityprovider-instancerequirementsrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalStorageConfiguration`  <a name="cfn-ecs-capacityprovider-instancelaunchtemplate-localstorageconfiguration"></a>
The local storage configuration for Amazon ECS Managed Instances. This defines how ECS uses instance store volumes available on the container instance.
*Required*: No
*Type*: [ManagedInstancesLocalStorageConfiguration](aws-properties-ecs-capacityprovider-managedinstanceslocalstorageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Monitoring`  <a name="cfn-ecs-capacityprovider-instancelaunchtemplate-monitoring"></a>
CloudWatch provides two categories of monitoring: basic monitoring and detailed monitoring. By default, your managed instance is configured for basic monitoring. You can optionally enable detailed monitoring to help you more quickly identify and act on operational issues. You can enable or turn off detailed monitoring at launch or when the managed instance is running or stopped. For more information, see [Detailed monitoring for Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/detailed-monitoring-managed-instances.html) in the Amazon ECS Developer Guide.
*Required*: No
*Type*: String
*Allowed values*: `BASIC | DETAILED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkConfiguration`  <a name="cfn-ecs-capacityprovider-instancelaunchtemplate-networkconfiguration"></a>
The network configuration for Amazon ECS Managed Instances. This specifies the subnets and security groups that instances use for network connectivity.
*Required*: Yes
*Type*: [ManagedInstancesNetworkConfiguration](aws-properties-ecs-capacityprovider-managedinstancesnetworkconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageConfiguration`  <a name="cfn-ecs-capacityprovider-instancelaunchtemplate-storageconfiguration"></a>
The storage configuration for Amazon ECS Managed Instances. This defines the data volume properties for the instances.
*Required*: No
*Type*: [ManagedInstancesStorageConfiguration](aws-properties-ecs-capacityprovider-managedinstancesstorageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
