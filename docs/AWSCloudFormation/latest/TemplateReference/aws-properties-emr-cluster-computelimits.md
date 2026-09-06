---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-computelimits.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster ComputeLimits
<a name="aws-properties-emr-cluster-computelimits"></a>

 The Amazon EC2 unit limits for a managed scaling policy. The managed scaling activity of a cluster can not be above or below these limits. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.

## Syntax
<a name="aws-properties-emr-cluster-computelimits-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-computelimits-syntax.json"></a>

```
{
  "[MaximumCapacityUnits](#cfn-emr-cluster-computelimits-maximumcapacityunits)" : {{Integer}},
  "[MaximumCoreCapacityUnits](#cfn-emr-cluster-computelimits-maximumcorecapacityunits)" : {{Integer}},
  "[MaximumOnDemandCapacityUnits](#cfn-emr-cluster-computelimits-maximumondemandcapacityunits)" : {{Integer}},
  "[MinimumCapacityUnits](#cfn-emr-cluster-computelimits-minimumcapacityunits)" : {{Integer}},
  "[UnitType](#cfn-emr-cluster-computelimits-unittype)" : {{String}}
}
```

### YAML
<a name="aws-properties-emr-cluster-computelimits-syntax.yaml"></a>

```
  [MaximumCapacityUnits](#cfn-emr-cluster-computelimits-maximumcapacityunits): {{Integer}}
  [MaximumCoreCapacityUnits](#cfn-emr-cluster-computelimits-maximumcorecapacityunits): {{Integer}}
  [MaximumOnDemandCapacityUnits](#cfn-emr-cluster-computelimits-maximumondemandcapacityunits): {{Integer}}
  [MinimumCapacityUnits](#cfn-emr-cluster-computelimits-minimumcapacityunits): {{Integer}}
  [UnitType](#cfn-emr-cluster-computelimits-unittype): {{String}}
```

## Properties
<a name="aws-properties-emr-cluster-computelimits-properties"></a>

`MaximumCapacityUnits`  <a name="cfn-emr-cluster-computelimits-maximumcapacityunits"></a>
 The upper boundary of Amazon EC2 units. It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumCoreCapacityUnits`  <a name="cfn-emr-cluster-computelimits-maximumcorecapacityunits"></a>
 The upper boundary of Amazon EC2 units for core node type in a cluster. It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. The core units are not allowed to scale beyond this boundary. The parameter is used to split capacity allocation between core and task nodes.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumOnDemandCapacityUnits`  <a name="cfn-emr-cluster-computelimits-maximumondemandcapacityunits"></a>
 The upper boundary of On-Demand Amazon EC2 units. It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. The On-Demand units are not allowed to scale beyond this boundary. The parameter is used to split capacity allocation between On-Demand and Spot Instances.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumCapacityUnits`  <a name="cfn-emr-cluster-computelimits-minimumcapacityunits"></a>
 The lower boundary of Amazon EC2 units. It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnitType`  <a name="cfn-emr-cluster-computelimits-unittype"></a>
 The unit type used for specifying a managed scaling policy.
*Required*: Yes
*Type*: String
*Allowed values*: `InstanceFleetUnits | Instances | VCPU`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
