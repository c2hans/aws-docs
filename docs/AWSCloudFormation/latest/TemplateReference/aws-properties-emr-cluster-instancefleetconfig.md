---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-instancefleetconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster InstanceFleetConfig
<a name="aws-properties-emr-cluster-instancefleetconfig"></a>

Use `InstanceFleetConfig` to define instance fleets for an EMR cluster. A cluster can not use both instance fleets and instance groups. For more information, see [Configure Instance Fleets](https://docs.aws.amazon.com//emr/latest/ManagementGuide/emr-instance-group-configuration.html) in the *Amazon EMR Management Guide*.

**Note**
The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.

## Syntax
<a name="aws-properties-emr-cluster-instancefleetconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-instancefleetconfig-syntax.json"></a>

```
{
  "[InstanceTypeConfigs](#cfn-emr-cluster-instancefleetconfig-instancetypeconfigs)" : {{[ InstanceTypeConfig, ... ]}},
  "[LaunchSpecifications](#cfn-emr-cluster-instancefleetconfig-launchspecifications)" : {{InstanceFleetProvisioningSpecifications}},
  "[Name](#cfn-emr-cluster-instancefleetconfig-name)" : {{String}},
  "[ResizeSpecifications](#cfn-emr-cluster-instancefleetconfig-resizespecifications)" : {{InstanceFleetResizingSpecifications}},
  "[TargetOnDemandCapacity](#cfn-emr-cluster-instancefleetconfig-targetondemandcapacity)" : {{Integer}},
  "[TargetSpotCapacity](#cfn-emr-cluster-instancefleetconfig-targetspotcapacity)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-emr-cluster-instancefleetconfig-syntax.yaml"></a>

```
  [InstanceTypeConfigs](#cfn-emr-cluster-instancefleetconfig-instancetypeconfigs): {{
    - InstanceTypeConfig}}
  [LaunchSpecifications](#cfn-emr-cluster-instancefleetconfig-launchspecifications): {{
    InstanceFleetProvisioningSpecifications}}
  [Name](#cfn-emr-cluster-instancefleetconfig-name): {{String}}
  [ResizeSpecifications](#cfn-emr-cluster-instancefleetconfig-resizespecifications): {{
    InstanceFleetResizingSpecifications}}
  [TargetOnDemandCapacity](#cfn-emr-cluster-instancefleetconfig-targetondemandcapacity): {{Integer}}
  [TargetSpotCapacity](#cfn-emr-cluster-instancefleetconfig-targetspotcapacity): {{Integer}}
```

## Properties
<a name="aws-properties-emr-cluster-instancefleetconfig-properties"></a>

`InstanceTypeConfigs`  <a name="cfn-emr-cluster-instancefleetconfig-instancetypeconfigs"></a>
The instance type configurations that define the Amazon EC2 instances in the instance fleet.
*Required*: No
*Type*: Array of [InstanceTypeConfig](aws-properties-emr-cluster-instancetypeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LaunchSpecifications`  <a name="cfn-emr-cluster-instancefleetconfig-launchspecifications"></a>
The launch specification for the instance fleet.
*Required*: No
*Type*: [InstanceFleetProvisioningSpecifications](aws-properties-emr-cluster-instancefleetprovisioningspecifications.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-emr-cluster-instancefleetconfig-name"></a>
The friendly name of the instance fleet.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResizeSpecifications`  <a name="cfn-emr-cluster-instancefleetconfig-resizespecifications"></a>
The resize specification for the instance fleet.
*Required*: No
*Type*: [InstanceFleetResizingSpecifications](aws-properties-emr-cluster-instancefleetresizingspecifications.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetOnDemandCapacity`  <a name="cfn-emr-cluster-instancefleetconfig-targetondemandcapacity"></a>
The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand instances to provision. When the instance fleet launches, Amazon EMR tries to provision On-Demand instances as specified by `InstanceTypeConfig`. Each instance configuration has a specified `WeightedCapacity`. When an On-Demand instance is provisioned, the `WeightedCapacity` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a `WeightedCapacity` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.
If not specified or set to 0, only Spot instances are provisioned for the instance fleet using `TargetSpotCapacity`. At least one of `TargetSpotCapacity` and `TargetOnDemandCapacity` should be greater than 0. For a master instance fleet, only one of `TargetSpotCapacity` and `TargetOnDemandCapacity` can be specified, and its value must be 1.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetSpotCapacity`  <a name="cfn-emr-cluster-instancefleetconfig-targetspotcapacity"></a>
The target capacity of Spot units for the instance fleet, which determines how many Spot instances to provision. When the instance fleet launches, Amazon EMR tries to provision Spot instances as specified by `InstanceTypeConfig`. Each instance configuration has a specified `WeightedCapacity`. When a Spot instance is provisioned, the `WeightedCapacity` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a `WeightedCapacity` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.
If not specified or set to 0, only On-Demand instances are provisioned for the instance fleet. At least one of `TargetSpotCapacity` and `TargetOnDemandCapacity` should be greater than 0. For a master instance fleet, only one of `TargetSpotCapacity` and `TargetOnDemandCapacity` can be specified, and its value must be 1.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
