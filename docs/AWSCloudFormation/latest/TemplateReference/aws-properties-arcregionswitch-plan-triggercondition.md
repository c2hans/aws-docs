---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-triggercondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan TriggerCondition
<a name="aws-properties-arcregionswitch-plan-triggercondition"></a>

Defines a condition that must be met for a trigger to fire.

## Syntax
<a name="aws-properties-arcregionswitch-plan-triggercondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-triggercondition-syntax.json"></a>

```
{
  "[AssociatedAlarmName](#cfn-arcregionswitch-plan-triggercondition-associatedalarmname)" : {{String}},
  "[Condition](#cfn-arcregionswitch-plan-triggercondition-condition)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-triggercondition-syntax.yaml"></a>

```
  [AssociatedAlarmName](#cfn-arcregionswitch-plan-triggercondition-associatedalarmname): {{String}}
  [Condition](#cfn-arcregionswitch-plan-triggercondition-condition): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-triggercondition-properties"></a>

`AssociatedAlarmName`  <a name="cfn-arcregionswitch-plan-triggercondition-associatedalarmname"></a>
The name of the CloudWatch alarm associated with the condition.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Condition`  <a name="cfn-arcregionswitch-plan-triggercondition-condition"></a>
The condition that must be met. Valid values include `green` and `red`.
*Required*: Yes
*Type*: String
*Allowed values*: `red | green`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
