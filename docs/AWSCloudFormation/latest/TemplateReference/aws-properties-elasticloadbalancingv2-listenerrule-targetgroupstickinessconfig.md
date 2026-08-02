---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::ListenerRule TargetGroupStickinessConfig
<a name="aws-properties-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig"></a>

Information about the target group stickiness for a rule.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig-syntax.json"></a>

```
{
  "[DurationSeconds](#cfn-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig-durationseconds)" : {{Integer}},
  "[Enabled](#cfn-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig-syntax.yaml"></a>

```
  [DurationSeconds](#cfn-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig-durationseconds): {{Integer}}
  [Enabled](#cfn-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig-properties"></a>

`DurationSeconds`  <a name="cfn-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig-durationseconds"></a>
[Application Load Balancers] The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days). You must specify this value when enabling target group stickiness.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig-enabled"></a>
Indicates whether target group stickiness is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
