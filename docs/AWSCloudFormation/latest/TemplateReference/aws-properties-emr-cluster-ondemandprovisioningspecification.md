---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-ondemandprovisioningspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster OnDemandProvisioningSpecification
<a name="aws-properties-emr-cluster-ondemandprovisioningspecification"></a>

 The launch specification for On-Demand Instances in the instance fleet, which determines the allocation strategy.

**Note**
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. On-Demand Instances allocation strategy is available in Amazon EMR releases 5.12.1 and later.

## Syntax
<a name="aws-properties-emr-cluster-ondemandprovisioningspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-ondemandprovisioningspecification-syntax.json"></a>

```
{
  "[AllocationStrategy](#cfn-emr-cluster-ondemandprovisioningspecification-allocationstrategy)" : {{String}},
  "[CapacityReservationOptions](#cfn-emr-cluster-ondemandprovisioningspecification-capacityreservationoptions)" : {{OnDemandCapacityReservationOptions}}
}
```

### YAML
<a name="aws-properties-emr-cluster-ondemandprovisioningspecification-syntax.yaml"></a>

```
  [AllocationStrategy](#cfn-emr-cluster-ondemandprovisioningspecification-allocationstrategy): {{String}}
  [CapacityReservationOptions](#cfn-emr-cluster-ondemandprovisioningspecification-capacityreservationoptions): {{
    OnDemandCapacityReservationOptions}}
```

## Properties
<a name="aws-properties-emr-cluster-ondemandprovisioningspecification-properties"></a>

`AllocationStrategy`  <a name="cfn-emr-cluster-ondemandprovisioningspecification-allocationstrategy"></a>
Specifies the strategy to use in launching On-Demand instance fleets. Available options are `lowest-price` and `prioritized`. `lowest-price` specifies to launch the instances with the lowest price first, and `prioritized` specifies that Amazon EMR should launch the instances with the highest priority first. The default is `lowest-price`.
*Required*: Yes
*Type*: String
*Allowed values*: `lowest-price | prioritized`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CapacityReservationOptions`  <a name="cfn-emr-cluster-ondemandprovisioningspecification-capacityreservationoptions"></a>
The launch specification for On-Demand instances in the instance fleet, which determines the allocation strategy.
*Required*: No
*Type*: [OnDemandCapacityReservationOptions](aws-properties-emr-cluster-ondemandcapacityreservationoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
