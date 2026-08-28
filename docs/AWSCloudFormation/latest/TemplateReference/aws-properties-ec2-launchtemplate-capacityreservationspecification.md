---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-capacityreservationspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate CapacityReservationSpecification
<a name="aws-properties-ec2-launchtemplate-capacityreservationspecification"></a>

Specifies an instance's Capacity Reservation targeting option. You can specify only one option at a time.

`CapacityReservationSpecification` is a property of [AWS::EC2::LaunchTemplate LaunchTemplateData](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html).

## Syntax
<a name="aws-properties-ec2-launchtemplate-capacityreservationspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-capacityreservationspecification-syntax.json"></a>

```
{
  "[CapacityReservationPreference](#cfn-ec2-launchtemplate-capacityreservationspecification-capacityreservationpreference)" : {{String}},
  "[CapacityReservationTarget](#cfn-ec2-launchtemplate-capacityreservationspecification-capacityreservationtarget)" : {{CapacityReservationTarget}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-capacityreservationspecification-syntax.yaml"></a>

```
  [CapacityReservationPreference](#cfn-ec2-launchtemplate-capacityreservationspecification-capacityreservationpreference): {{String}}
  [CapacityReservationTarget](#cfn-ec2-launchtemplate-capacityreservationspecification-capacityreservationtarget): {{
    CapacityReservationTarget}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-capacityreservationspecification-properties"></a>

`CapacityReservationPreference`  <a name="cfn-ec2-launchtemplate-capacityreservationspecification-capacityreservationpreference"></a>
Indicates the instance's Capacity Reservation preferences. Possible preferences include:
+ `capacity-reservations-only` - The instance will only run in a Capacity Reservation or Capacity Reservation group. If capacity isn't available, the instance will fail to launch.
+ `open` - The instance can run in any `open` Capacity Reservation that has matching attributes (instance type, platform, Availability Zone, tenancy).
+ `none` - The instance avoids running in a Capacity Reservation even if one is available. The instance runs in On-Demand capacity.
*Required*: No
*Type*: String
*Allowed values*: `capacity-reservations-only | open | none`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CapacityReservationTarget`  <a name="cfn-ec2-launchtemplate-capacityreservationspecification-capacityreservationtarget"></a>
Information about the target Capacity Reservation or Capacity Reservation group.
*Required*: No
*Type*: [CapacityReservationTarget](aws-properties-ec2-launchtemplate-capacityreservationtarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
