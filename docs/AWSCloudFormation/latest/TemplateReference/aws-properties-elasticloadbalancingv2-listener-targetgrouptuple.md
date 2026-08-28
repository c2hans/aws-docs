---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listener-targetgrouptuple.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::Listener TargetGroupTuple
<a name="aws-properties-elasticloadbalancingv2-listener-targetgrouptuple"></a>

Information about how traffic will be distributed between multiple target groups in a forward rule.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listener-targetgrouptuple-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listener-targetgrouptuple-syntax.json"></a>

```
{
  "[TargetGroupArn](#cfn-elasticloadbalancingv2-listener-targetgrouptuple-targetgrouparn)" : {{String}},
  "[Weight](#cfn-elasticloadbalancingv2-listener-targetgrouptuple-weight)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listener-targetgrouptuple-syntax.yaml"></a>

```
  [TargetGroupArn](#cfn-elasticloadbalancingv2-listener-targetgrouptuple-targetgrouparn): {{String}}
  [Weight](#cfn-elasticloadbalancingv2-listener-targetgrouptuple-weight): {{Integer}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listener-targetgrouptuple-properties"></a>

`TargetGroupArn`  <a name="cfn-elasticloadbalancingv2-listener-targetgrouptuple-targetgrouparn"></a>
The Amazon Resource Name (ARN) of the target group.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-elasticloadbalancingv2-listener-targetgrouptuple-weight"></a>
The weight. The range is 0 to 999.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
