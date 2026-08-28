---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-capacityreservationtarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate CapacityReservationTarget
<a name="aws-properties-ec2-launchtemplate-capacityreservationtarget"></a>

Specifies a target Capacity Reservation.

`CapacityReservationTarget` is a property of the [ Amazon EC2 LaunchTemplate LaunchTemplateData](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html) property type.

## Syntax
<a name="aws-properties-ec2-launchtemplate-capacityreservationtarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-capacityreservationtarget-syntax.json"></a>

```
{
  "[CapacityReservationId](#cfn-ec2-launchtemplate-capacityreservationtarget-capacityreservationid)" : {{String}},
  "[CapacityReservationResourceGroupArn](#cfn-ec2-launchtemplate-capacityreservationtarget-capacityreservationresourcegrouparn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-capacityreservationtarget-syntax.yaml"></a>

```
  [CapacityReservationId](#cfn-ec2-launchtemplate-capacityreservationtarget-capacityreservationid): {{String}}
  [CapacityReservationResourceGroupArn](#cfn-ec2-launchtemplate-capacityreservationtarget-capacityreservationresourcegrouparn): {{String}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-capacityreservationtarget-properties"></a>

`CapacityReservationId`  <a name="cfn-ec2-launchtemplate-capacityreservationtarget-capacityreservationid"></a>
The ID of the Capacity Reservation in which to run the instance.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CapacityReservationResourceGroupArn`  <a name="cfn-ec2-launchtemplate-capacityreservationtarget-capacityreservationresourcegrouparn"></a>
The ARN of the Capacity Reservation resource group in which to run the instance.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
