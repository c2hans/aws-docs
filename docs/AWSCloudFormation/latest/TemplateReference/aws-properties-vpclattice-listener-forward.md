---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-listener-forward.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::Listener Forward
<a name="aws-properties-vpclattice-listener-forward"></a>

The forward action. Traffic that matches the rule is forwarded to the specified target groups.

## Syntax
<a name="aws-properties-vpclattice-listener-forward-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-listener-forward-syntax.json"></a>

```
{
  "[TargetGroups](#cfn-vpclattice-listener-forward-targetgroups)" : {{[ WeightedTargetGroup, ... ]}}
}
```

### YAML
<a name="aws-properties-vpclattice-listener-forward-syntax.yaml"></a>

```
  [TargetGroups](#cfn-vpclattice-listener-forward-targetgroups): {{
    - WeightedTargetGroup}}
```

## Properties
<a name="aws-properties-vpclattice-listener-forward-properties"></a>

`TargetGroups`  <a name="cfn-vpclattice-listener-forward-targetgroups"></a>
The target groups. Traffic matching the rule is forwarded to the specified target groups. With forward actions, you can assign a weight that controls the prioritization and selection of each target group. This means that requests are distributed to individual target groups based on their weights. For example, if two target groups have the same weight, each target group receives half of the traffic.
The default value is 1. This means that if only one target group is provided, there is no need to set the weight; 100% of the traffic goes to that target group.
*Required*: Yes
*Type*: Array of [WeightedTargetGroup](aws-properties-vpclattice-listener-weightedtargetgroup.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
