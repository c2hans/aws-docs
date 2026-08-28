---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ec2fleet-capacityreservationoptionsrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EC2Fleet CapacityReservationOptionsRequest
<a name="aws-properties-ec2-ec2fleet-capacityreservationoptionsrequest"></a>

Describes the strategy for using unused Capacity Reservations for fulfilling On-Demand capacity.

**Note**
This strategy can only be used if the EC2 Fleet is of type `instant`.

For more information about Capacity Reservations, see [On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) in the *Amazon EC2 User Guide*. For examples of using Capacity Reservations in an EC2 Fleet, see [EC2 Fleet example configurations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-examples.html) in the *Amazon EC2 User Guide*.

## Syntax
<a name="aws-properties-ec2-ec2fleet-capacityreservationoptionsrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ec2fleet-capacityreservationoptionsrequest-syntax.json"></a>

```
{
  "[UsageStrategy](#cfn-ec2-ec2fleet-capacityreservationoptionsrequest-usagestrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-ec2fleet-capacityreservationoptionsrequest-syntax.yaml"></a>

```
  [UsageStrategy](#cfn-ec2-ec2fleet-capacityreservationoptionsrequest-usagestrategy): {{String}}
```

## Properties
<a name="aws-properties-ec2-ec2fleet-capacityreservationoptionsrequest-properties"></a>

`UsageStrategy`  <a name="cfn-ec2-ec2fleet-capacityreservationoptionsrequest-usagestrategy"></a>
Indicates whether to use unused Capacity Reservations for fulfilling On-Demand capacity.
If you specify `use-capacity-reservations-first`, the fleet uses unused Capacity Reservations to fulfill On-Demand capacity up to the target On-Demand capacity. If multiple instance pools have unused Capacity Reservations, the On-Demand allocation strategy (`lowest-price` or `prioritized`) is applied. If the number of unused Capacity Reservations is less than the On-Demand target capacity, the remaining On-Demand target capacity is launched according to the On-Demand allocation strategy (`lowest-price` or `prioritized`).
If you do not specify a value, the fleet fulfils the On-Demand capacity according to the chosen On-Demand allocation strategy.
*Required*: No
*Type*: String
*Allowed values*: `use-capacity-reservations-first`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
