---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listener-targetgroupstickinessconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::Listener TargetGroupStickinessConfig
<a name="aws-properties-elasticloadbalancingv2-listener-targetgroupstickinessconfig"></a>

Information about the target group stickiness for a rule.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listener-targetgroupstickinessconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listener-targetgroupstickinessconfig-syntax.json"></a>

```
{
  "[DurationSeconds](#cfn-elasticloadbalancingv2-listener-targetgroupstickinessconfig-durationseconds)" : {{Integer}},
  "[Enabled](#cfn-elasticloadbalancingv2-listener-targetgroupstickinessconfig-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listener-targetgroupstickinessconfig-syntax.yaml"></a>

```
  [DurationSeconds](#cfn-elasticloadbalancingv2-listener-targetgroupstickinessconfig-durationseconds): {{Integer}}
  [Enabled](#cfn-elasticloadbalancingv2-listener-targetgroupstickinessconfig-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listener-targetgroupstickinessconfig-properties"></a>

`DurationSeconds`  <a name="cfn-elasticloadbalancingv2-listener-targetgroupstickinessconfig-durationseconds"></a>
[Application Load Balancers] The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days). You must specify this value when enabling target group stickiness.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-elasticloadbalancingv2-listener-targetgroupstickinessconfig-enabled"></a>
Indicates whether target group stickiness is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
