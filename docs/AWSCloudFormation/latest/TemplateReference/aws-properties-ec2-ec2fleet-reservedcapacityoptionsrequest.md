---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ec2fleet-reservedcapacityoptionsrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EC2Fleet ReservedCapacityOptionsRequest
<a name="aws-properties-ec2-ec2fleet-reservedcapacityoptionsrequest"></a>

Defines EC2 Fleet preferences for utilizing reserved capacity when `DefaultTargetCapacityType` is set to `reserved-capacity`. EC2 Fleet can fulfill reserved capacity using On-Demand Capacity Reservations, Capacity Blocks for ML, and interruptible Capacity Reservations.

**Note**
This configuration can only be used if the EC2 Fleet is of type `instant`.

When you specify `ReservedCapacityOptions`, you must also set `DefaultTargetCapacityType` to `reserved-capacity` in the `TargetCapacitySpecification`.

For more information about interruptible Capacity Reservations, see [Launch instances into an interruptible Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-launch-instances-interruptible-cr-walkthrough.html) in the *Amazon EC2 User Guide*.

## Syntax
<a name="aws-properties-ec2-ec2fleet-reservedcapacityoptionsrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ec2fleet-reservedcapacityoptionsrequest-syntax.json"></a>

```
{
  "[ReservationTypes](#cfn-ec2-ec2fleet-reservedcapacityoptionsrequest-reservationtypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-ec2fleet-reservedcapacityoptionsrequest-syntax.yaml"></a>

```
  [ReservationTypes](#cfn-ec2-ec2fleet-reservedcapacityoptionsrequest-reservationtypes): {{
    - String}}
```

## Properties
<a name="aws-properties-ec2-ec2fleet-reservedcapacityoptionsrequest-properties"></a>

`ReservationTypes`  <a name="cfn-ec2-ec2fleet-reservedcapacityoptionsrequest-reservationtypes"></a>
The types of Capacity Reservations to use for fulfilling the EC2 Fleet request. This is an ordered list: EC2 Fleet attempts to launch instances into each Capacity Reservation type in the order that you specify them before moving on to the next type.
*Required*: No
*Type*: Array of String
*Allowed values*: `interruptible-capacity-reservation`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
