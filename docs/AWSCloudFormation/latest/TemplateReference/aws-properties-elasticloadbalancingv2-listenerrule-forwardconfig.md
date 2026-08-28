---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listenerrule-forwardconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::ListenerRule ForwardConfig
<a name="aws-properties-elasticloadbalancingv2-listenerrule-forwardconfig"></a>

Information for creating an action that distributes requests among multiple target groups. Specify only when `Type` is `forward`.

If you specify both `ForwardConfig` and `TargetGroupArn`, you can specify only one target group using `ForwardConfig` and it must be the same target group specified in `TargetGroupArn`.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listenerrule-forwardconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listenerrule-forwardconfig-syntax.json"></a>

```
{
  "[TargetGroups](#cfn-elasticloadbalancingv2-listenerrule-forwardconfig-targetgroups)" : {{[ TargetGroupTuple, ... ]}},
  "[TargetGroupStickinessConfig](#cfn-elasticloadbalancingv2-listenerrule-forwardconfig-targetgroupstickinessconfig)" : {{TargetGroupStickinessConfig}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-forwardconfig-syntax.yaml"></a>

```
  [TargetGroups](#cfn-elasticloadbalancingv2-listenerrule-forwardconfig-targetgroups): {{
    - TargetGroupTuple}}
  [TargetGroupStickinessConfig](#cfn-elasticloadbalancingv2-listenerrule-forwardconfig-targetgroupstickinessconfig): {{
    TargetGroupStickinessConfig}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listenerrule-forwardconfig-properties"></a>

`TargetGroups`  <a name="cfn-elasticloadbalancingv2-listenerrule-forwardconfig-targetgroups"></a>
Information about how traffic will be distributed between multiple target groups in a forward rule.
*Required*: No
*Type*: Array of [TargetGroupTuple](aws-properties-elasticloadbalancingv2-listenerrule-targetgrouptuple.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetGroupStickinessConfig`  <a name="cfn-elasticloadbalancingv2-listenerrule-forwardconfig-targetgroupstickinessconfig"></a>
Information about the target group stickiness for a rule.
*Required*: No
*Type*: [TargetGroupStickinessConfig](aws-properties-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-elasticloadbalancingv2-listenerrule-forwardconfig--examples"></a>

###
<a name="aws-properties-elasticloadbalancingv2-listenerrule-forwardconfig--examples--"></a>

The following example sets the relative weight of traffic between two traffic groups. Because the `weight` property of each group is set to the same value, `1`, traffic is split 50/50 between the two target groups. You can create the target group using [AWS::ElasticLoadBalancingV2::TargetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html).

#### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-forwardconfig--examples----yaml"></a>

```
myListenerRule:
  Type: 'AWS::ElasticLoadBalancingV2::ListenerRule'
  Properties:
    Actions:
      - Type: forward
        ForwardConfig:
          TargetGroups:
            - TargetGroupArn: !Ref TargetGroup1
              Weight: 1
            - TargetGroupArn: !Ref TargetGroup2
              Weight: 1
    Conditions:
      - Field: path-pattern
        Values:
          - test
    ListenerArn: !Ref Listener
    Priority: 10
```

#### JSON
<a name="aws-properties-elasticloadbalancingv2-listenerrule-forwardconfig--examples----json"></a>

```
{
    "myListenerRule": {
        "Type": "AWS::ElasticLoadBalancingV2::ListenerRule",
        "Properties": {
            "Actions": [
                {
                    "Type": "forward",
                    "ForwardConfig": {
                        "TargetGroups": [
                            {
                                "TargetGroupArn": {
                                    "Ref": "TargetGroup1"
                                },
                                "Weight": 1
                            },
                            {
                                "TargetGroupArn": {
                                    "Ref": "TargetGroup2"
                                },
                                "Weight": 1
                            }
                        ]
                    }
                }
            ],
            "Conditions": [
                {
                    "Field": "path-pattern",
                    "Values": [
                        "test"
                    ]
                }
            ],
            "ListenerArn": {
                "Ref": "Listener"
            },
            "Priority": 10
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
