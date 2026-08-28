---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-baselineebsbandwidthmbpsrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider BaselineEbsBandwidthMbpsRequest
<a name="aws-properties-ecs-capacityprovider-baselineebsbandwidthmbpsrequest"></a>

The minimum and maximum baseline Amazon EBS bandwidth in megabits per second (Mbps) for instance type selection. This is important for workloads with high storage I/O requirements.

## Syntax
<a name="aws-properties-ecs-capacityprovider-baselineebsbandwidthmbpsrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-baselineebsbandwidthmbpsrequest-syntax.json"></a>

```
{
  "[Max](#cfn-ecs-capacityprovider-baselineebsbandwidthmbpsrequest-max)" : {{Integer}},
  "[Min](#cfn-ecs-capacityprovider-baselineebsbandwidthmbpsrequest-min)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-baselineebsbandwidthmbpsrequest-syntax.yaml"></a>

```
  [Max](#cfn-ecs-capacityprovider-baselineebsbandwidthmbpsrequest-max): {{Integer}}
  [Min](#cfn-ecs-capacityprovider-baselineebsbandwidthmbpsrequest-min): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-baselineebsbandwidthmbpsrequest-properties"></a>

`Max`  <a name="cfn-ecs-capacityprovider-baselineebsbandwidthmbpsrequest-max"></a>
The maximum baseline Amazon EBS bandwidth in Mbps. Instance types with higher Amazon EBS bandwidth are excluded from selection.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-ecs-capacityprovider-baselineebsbandwidthmbpsrequest-min"></a>
The minimum baseline Amazon EBS bandwidth in Mbps. Instance types with lower Amazon EBS bandwidth are excluded from selection.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
