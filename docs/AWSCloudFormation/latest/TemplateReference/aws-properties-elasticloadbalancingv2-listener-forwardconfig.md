---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listener-forwardconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::Listener ForwardConfig
<a name="aws-properties-elasticloadbalancingv2-listener-forwardconfig"></a>

Information for creating an action that distributes requests among multiple target groups. Specify only when `Type` is `forward`.

If you specify both `ForwardConfig` and `TargetGroupArn`, you can specify only one target group using `ForwardConfig` and it must be the same target group specified in `TargetGroupArn`.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listener-forwardconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listener-forwardconfig-syntax.json"></a>

```
{
  "[TargetGroups](#cfn-elasticloadbalancingv2-listener-forwardconfig-targetgroups)" : {{[ TargetGroupTuple, ... ]}},
  "[TargetGroupStickinessConfig](#cfn-elasticloadbalancingv2-listener-forwardconfig-targetgroupstickinessconfig)" : {{TargetGroupStickinessConfig}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listener-forwardconfig-syntax.yaml"></a>

```
  [TargetGroups](#cfn-elasticloadbalancingv2-listener-forwardconfig-targetgroups): {{
    - TargetGroupTuple}}
  [TargetGroupStickinessConfig](#cfn-elasticloadbalancingv2-listener-forwardconfig-targetgroupstickinessconfig): {{
    TargetGroupStickinessConfig}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listener-forwardconfig-properties"></a>

`TargetGroups`  <a name="cfn-elasticloadbalancingv2-listener-forwardconfig-targetgroups"></a>
Information about how traffic will be distributed between multiple target groups in a forward rule.
*Required*: No
*Type*: Array of [TargetGroupTuple](aws-properties-elasticloadbalancingv2-listener-targetgrouptuple.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetGroupStickinessConfig`  <a name="cfn-elasticloadbalancingv2-listener-forwardconfig-targetgroupstickinessconfig"></a>
Information about the target group stickiness for a rule.
*Required*: No
*Type*: [TargetGroupStickinessConfig](aws-properties-elasticloadbalancingv2-listener-targetgroupstickinessconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-elasticloadbalancingv2-listener-forwardconfig--examples"></a>

The following example defines a listener with a default action that forwards traffic to the specified target group. You can create the target group using [AWS::ElasticLoadBalancingV2::TargetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html).

###
<a name="aws-properties-elasticloadbalancingv2-listener-forwardconfig--examples--"></a>

#### YAML
<a name="aws-properties-elasticloadbalancingv2-listener-forwardconfig--examples----yaml"></a>

```
myTCPListener:
  Type: 'AWS::ElasticLoadBalancingV2::Listener'
  Properties:
    LoadBalancerArn: !Ref myLoadBalancer
    Protocol: TCP
    Port: 80
    DefaultActions:
      - Type: forward
        TargetGroupArn: !Ref myTargetGroup
```

#### JSON
<a name="aws-properties-elasticloadbalancingv2-listener-forwardconfig--examples----json"></a>

```
{
    "myTCPListener": {
        "Type": "AWS::ElasticLoadBalancingV2::Listener",
        "Properties": {
            "LoadBalancerArn": {
                "Ref": "myLoadBalancer"
            },
            "Protocol": "TCP",
            "Port": 80,
            "DefaultActions": [
                {
                    "Type": "forward",
                    "TargetGroupArn": {
                        "Ref": "myTargetGroup"
                    }
                }
            ]
        }
    }
}
```
