---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancefleetconfig-ondemandprovisioningspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceFleetConfig OnDemandProvisioningSpecification
<a name="aws-properties-emr-instancefleetconfig-ondemandprovisioningspecification"></a>

 The launch specification for On-Demand Instances in the instance fleet, which determines the allocation strategy.

**Note**
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. On-Demand Instances allocation strategy is available in Amazon EMR releases 5.12.1 and later.

## Syntax
<a name="aws-properties-emr-instancefleetconfig-ondemandprovisioningspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancefleetconfig-ondemandprovisioningspecification-syntax.json"></a>

```
{
  "[AllocationStrategy](#cfn-emr-instancefleetconfig-ondemandprovisioningspecification-allocationstrategy)" : {{String}},
  "[CapacityReservationOptions](#cfn-emr-instancefleetconfig-ondemandprovisioningspecification-capacityreservationoptions)" : {{OnDemandCapacityReservationOptions}}
}
```

### YAML
<a name="aws-properties-emr-instancefleetconfig-ondemandprovisioningspecification-syntax.yaml"></a>

```
  [AllocationStrategy](#cfn-emr-instancefleetconfig-ondemandprovisioningspecification-allocationstrategy): {{String}}
  [CapacityReservationOptions](#cfn-emr-instancefleetconfig-ondemandprovisioningspecification-capacityreservationoptions): {{
    OnDemandCapacityReservationOptions}}
```

## Properties
<a name="aws-properties-emr-instancefleetconfig-ondemandprovisioningspecification-properties"></a>

`AllocationStrategy`  <a name="cfn-emr-instancefleetconfig-ondemandprovisioningspecification-allocationstrategy"></a>
Specifies the strategy to use in launching On-Demand instance fleets. Available options are `lowest-price` and `prioritized`. `lowest-price` specifies to launch the instances with the lowest price first, and `prioritized` specifies that Amazon EMR should launch the instances with the highest priority first. The default is `lowest-price`.
*Required*: Yes
*Type*: String
*Allowed values*: `lowest-price | prioritized`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CapacityReservationOptions`  <a name="cfn-emr-instancefleetconfig-ondemandprovisioningspecification-capacityreservationoptions"></a>
The launch specification for On-Demand instances in the instance fleet, which determines the allocation strategy.
*Required*: No
*Type*: [OnDemandCapacityReservationOptions](aws-properties-emr-instancefleetconfig-ondemandcapacityreservationoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
