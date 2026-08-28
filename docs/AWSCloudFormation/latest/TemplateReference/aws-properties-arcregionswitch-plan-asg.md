---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-asg.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan Asg
<a name="aws-properties-arcregionswitch-plan-asg"></a>

Configuration for an Amazon EC2 Auto Scaling group used in a Region switch plan.

## Syntax
<a name="aws-properties-arcregionswitch-plan-asg-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-asg-syntax.json"></a>

```
{
  "[Arn](#cfn-arcregionswitch-plan-asg-arn)" : {{String}},
  "[CrossAccountRole](#cfn-arcregionswitch-plan-asg-crossaccountrole)" : {{String}},
  "[ExternalId](#cfn-arcregionswitch-plan-asg-externalid)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-asg-syntax.yaml"></a>

```
  [Arn](#cfn-arcregionswitch-plan-asg-arn): {{String}}
  [CrossAccountRole](#cfn-arcregionswitch-plan-asg-crossaccountrole): {{String}}
  [ExternalId](#cfn-arcregionswitch-plan-asg-externalid): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-asg-properties"></a>

`Arn`  <a name="cfn-arcregionswitch-plan-asg-arn"></a>
The Amazon Resource Name (ARN) of the EC2 Auto Scaling group.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:autoscaling:[a-z0-9-]+:\d{12}:autoScalingGroup:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}:autoScalingGroupName/[\S\s]{1,255}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CrossAccountRole`  <a name="cfn-arcregionswitch-plan-asg-crossaccountrole"></a>
The cross account role for the configuration.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-arcregionswitch-plan-asg-externalid"></a>
The external ID (secret key) for the configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
