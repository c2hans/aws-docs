---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-instancelaunchtemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment InstanceLaunchTemplate
<a name="aws-properties-batch-computeenvironment-instancelaunchtemplate"></a>

The instance launch configuration for an Amazon ECS Managed Instances capacity provider. Specifies the instance profile, networking, instance selection constraints, capacity pricing model, storage, and monitoring settings.

## Syntax
<a name="aws-properties-batch-computeenvironment-instancelaunchtemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-instancelaunchtemplate-syntax.json"></a>

```
{
  "[CapacityOptionType](#cfn-batch-computeenvironment-instancelaunchtemplate-capacityoptiontype)" : {{String}},
  "[CapacityReservations](#cfn-batch-computeenvironment-instancelaunchtemplate-capacityreservations)" : {{CapacityReservations}},
  "[Ec2InstanceProfileArn](#cfn-batch-computeenvironment-instancelaunchtemplate-ec2instanceprofilearn)" : {{String}},
  "[FipsEnabled](#cfn-batch-computeenvironment-instancelaunchtemplate-fipsenabled)" : {{Boolean}},
  "[InstanceMetadataTagsPropagation](#cfn-batch-computeenvironment-instancelaunchtemplate-instancemetadatatagspropagation)" : {{Boolean}},
  "[InstanceRequirements](#cfn-batch-computeenvironment-instancelaunchtemplate-instancerequirements)" : {{InstanceRequirements}},
  "[LocalStorageConfiguration](#cfn-batch-computeenvironment-instancelaunchtemplate-localstorageconfiguration)" : {{ManagedInstancesLocalStorageConfiguration}},
  "[Monitoring](#cfn-batch-computeenvironment-instancelaunchtemplate-monitoring)" : {{String}},
  "[NetworkConfiguration](#cfn-batch-computeenvironment-instancelaunchtemplate-networkconfiguration)" : {{ManagedInstancesNetworkConfiguration}},
  "[StorageConfiguration](#cfn-batch-computeenvironment-instancelaunchtemplate-storageconfiguration)" : {{ManagedInstancesStorageConfiguration}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-instancelaunchtemplate-syntax.yaml"></a>

```
  [CapacityOptionType](#cfn-batch-computeenvironment-instancelaunchtemplate-capacityoptiontype): {{String}}
  [CapacityReservations](#cfn-batch-computeenvironment-instancelaunchtemplate-capacityreservations): {{
    CapacityReservations}}
  [Ec2InstanceProfileArn](#cfn-batch-computeenvironment-instancelaunchtemplate-ec2instanceprofilearn): {{String}}
  [FipsEnabled](#cfn-batch-computeenvironment-instancelaunchtemplate-fipsenabled): {{Boolean}}
  [InstanceMetadataTagsPropagation](#cfn-batch-computeenvironment-instancelaunchtemplate-instancemetadatatagspropagation): {{Boolean}}
  [InstanceRequirements](#cfn-batch-computeenvironment-instancelaunchtemplate-instancerequirements): {{
    InstanceRequirements}}
  [LocalStorageConfiguration](#cfn-batch-computeenvironment-instancelaunchtemplate-localstorageconfiguration): {{
    ManagedInstancesLocalStorageConfiguration}}
  [Monitoring](#cfn-batch-computeenvironment-instancelaunchtemplate-monitoring): {{String}}
  [NetworkConfiguration](#cfn-batch-computeenvironment-instancelaunchtemplate-networkconfiguration): {{
    ManagedInstancesNetworkConfiguration}}
  [StorageConfiguration](#cfn-batch-computeenvironment-instancelaunchtemplate-storageconfiguration): {{
    ManagedInstancesStorageConfiguration}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-instancelaunchtemplate-properties"></a>

`CapacityOptionType`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-capacityoptiontype"></a>
The capacity pricing model for the managed instances. Valid values:
+ `ON_DEMAND` (default) — On-Demand pricing.
+ `SPOT` — Spot Instances, which can provide significant cost savings for fault-tolerant workloads.
*Required*: No
*Type*: String
*Allowed values*: `ON_DEMAND | SPOT | RESERVED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CapacityReservations`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-capacityreservations"></a>
The capacity reservation configuration for the managed instances. Use this to target On-Demand Capacity Reservations or Reserved Instances for predictable capacity and cost optimization.
*Required*: No
*Type*: [CapacityReservations](aws-properties-batch-computeenvironment-capacityreservations.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ec2InstanceProfileArn`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-ec2instanceprofilearn"></a>
The Amazon Resource Name (ARN) of the Amazon EC2 instance profile for the managed instances. The instance profile must use the `AmazonECSInstanceRolePolicyForManagedInstances` managed policy with a trust policy for `ec2.amazonaws.com`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FipsEnabled`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-fipsenabled"></a>
Specifies whether FIPS 140-2 validated cryptographic modules are enabled on the managed instances. Not available in all Regions.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceMetadataTagsPropagation`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-instancemetadatatagspropagation"></a>
Specifies whether instance tags are accessible from the instance metadata service (IMDS). If not specified, instance tags are not accessible from IMDS.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceRequirements`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-instancerequirements"></a>
The instance type requirements for the capacity provider. Use this to constrain which Amazon EC2 instance types Amazon ECS can launch. If not specified, all available instance types are eligible.
*Required*: No
*Type*: [InstanceRequirements](aws-properties-batch-computeenvironment-instancerequirements.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalStorageConfiguration`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-localstorageconfiguration"></a>
The local storage configuration for the managed instances. If not specified, instance store volumes are not available to containers.
*Required*: No
*Type*: [ManagedInstancesLocalStorageConfiguration](aws-properties-batch-computeenvironment-managedinstanceslocalstorageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Monitoring`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-monitoring"></a>
The level of CloudWatch monitoring for the managed instances. Valid values are `BASIC` and `DETAILED`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkConfiguration`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-networkconfiguration"></a>
The network configuration for the managed instances. Specifies the VPC subnets and security groups where instances are launched.
*Required*: Yes
*Type*: [ManagedInstancesNetworkConfiguration](aws-properties-batch-computeenvironment-managedinstancesnetworkconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageConfiguration`  <a name="cfn-batch-computeenvironment-instancelaunchtemplate-storageconfiguration"></a>
The storage configuration for the managed instances. Configures the root EBS volume size. If not specified, the service uses the default EBS volume size for the instance type.
*Required*: No
*Type*: [ManagedInstancesStorageConfiguration](aws-properties-batch-computeenvironment-managedinstancesstorageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
