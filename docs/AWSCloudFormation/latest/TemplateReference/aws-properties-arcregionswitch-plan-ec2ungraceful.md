---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-ec2ungraceful.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan Ec2Ungraceful
<a name="aws-properties-arcregionswitch-plan-ec2ungraceful"></a>

Configuration for handling failures when performing operations on EC2 resources.

## Syntax
<a name="aws-properties-arcregionswitch-plan-ec2ungraceful-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-ec2ungraceful-syntax.json"></a>

```
{
  "[MinimumSuccessPercentage](#cfn-arcregionswitch-plan-ec2ungraceful-minimumsuccesspercentage)" : {{Number}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-ec2ungraceful-syntax.yaml"></a>

```
  [MinimumSuccessPercentage](#cfn-arcregionswitch-plan-ec2ungraceful-minimumsuccesspercentage): {{Number}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-ec2ungraceful-properties"></a>

`MinimumSuccessPercentage`  <a name="cfn-arcregionswitch-plan-ec2ungraceful-minimumsuccesspercentage"></a>
The minimum success percentage that you specify for EC2 Auto Scaling groups.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `99`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
