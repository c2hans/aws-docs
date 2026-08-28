---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-spotmaintenancestrategies.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet SpotMaintenanceStrategies
<a name="aws-properties-ec2-spotfleet-spotmaintenancestrategies"></a>

The strategies for managing your Spot Instances that are at an elevated risk of being interrupted.

## Syntax
<a name="aws-properties-ec2-spotfleet-spotmaintenancestrategies-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-spotmaintenancestrategies-syntax.json"></a>

```
{
  "[CapacityRebalance](#cfn-ec2-spotfleet-spotmaintenancestrategies-capacityrebalance)" : {{SpotCapacityRebalance}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-spotmaintenancestrategies-syntax.yaml"></a>

```
  [CapacityRebalance](#cfn-ec2-spotfleet-spotmaintenancestrategies-capacityrebalance): {{
    SpotCapacityRebalance}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-spotmaintenancestrategies-properties"></a>

`CapacityRebalance`  <a name="cfn-ec2-spotfleet-spotmaintenancestrategies-capacityrebalance"></a>
The Spot Instance replacement strategy to use when Amazon EC2 emits a signal that your Spot Instance is at an elevated risk of being interrupted. For more information, see [Capacity rebalancing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-capacity-rebalance.html) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: [SpotCapacityRebalance](aws-properties-ec2-spotfleet-spotcapacityrebalance.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
