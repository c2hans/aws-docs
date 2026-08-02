---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listenerrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::ListenerRule
<a name="aws-resource-elasticloadbalancingv2-listenerrule"></a>

Specifies a listener rule. The listener must be associated with an Application Load Balancer. Each rule consists of a priority, one or more actions, and one or more conditions.

For more information, see [Quotas for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html) in the *User Guide for Application Load Balancers*.

## Syntax
<a name="aws-resource-elasticloadbalancingv2-listenerrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elasticloadbalancingv2-listenerrule-syntax.json"></a>

```
{
  "Type" : "AWS::ElasticLoadBalancingV2::ListenerRule",
  "Properties" : {
      "[Actions](#cfn-elasticloadbalancingv2-listenerrule-actions)" : {{[ Action, ... ]}},
      "[Conditions](#cfn-elasticloadbalancingv2-listenerrule-conditions)" : {{[ RuleCondition, ... ]}},
      "[ListenerArn](#cfn-elasticloadbalancingv2-listenerrule-listenerarn)" : {{String}},
      "[Priority](#cfn-elasticloadbalancingv2-listenerrule-priority)" : {{Integer}},
      "[Tags](#cfn-elasticloadbalancingv2-listenerrule-tags)" : {{[ Tag, ... ]}},
      "[Transforms](#cfn-elasticloadbalancingv2-listenerrule-transforms)" : {{[ Transform, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-elasticloadbalancingv2-listenerrule-syntax.yaml"></a>

```
Type: AWS::ElasticLoadBalancingV2::ListenerRule
Properties:
  [Actions](#cfn-elasticloadbalancingv2-listenerrule-actions): {{
    - Action}}
  [Conditions](#cfn-elasticloadbalancingv2-listenerrule-conditions): {{
    - RuleCondition}}
  [ListenerArn](#cfn-elasticloadbalancingv2-listenerrule-listenerarn): {{String}}
  [Priority](#cfn-elasticloadbalancingv2-listenerrule-priority): {{Integer}}
  [Tags](#cfn-elasticloadbalancingv2-listenerrule-tags): {{
    - Tag}}
  [Transforms](#cfn-elasticloadbalancingv2-listenerrule-transforms): {{
    - Transform}}
```

## Properties
<a name="aws-resource-elasticloadbalancingv2-listenerrule-properties"></a>

`Actions`  <a name="cfn-elasticloadbalancingv2-listenerrule-actions"></a>
The actions.
The rule must include exactly one of the following types of actions: `forward`, `fixed-response`, or `redirect`, and it must be the last action to be performed. If the rule is for an HTTPS listener, it can also optionally include an authentication action.
*Required*: Yes
*Type*: Array of [Action](aws-properties-elasticloadbalancingv2-listenerrule-action.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Conditions`  <a name="cfn-elasticloadbalancingv2-listenerrule-conditions"></a>
The conditions.
The rule can optionally include up to one of each of the following conditions: `http-request-method`, `host-header`, `path-pattern`, and `source-ip`. A rule can also optionally include one or more of each of the following conditions: `http-header` and `query-string`.
*Required*: Yes
*Type*: Array of [RuleCondition](aws-properties-elasticloadbalancingv2-listenerrule-rulecondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ListenerArn`  <a name="cfn-elasticloadbalancingv2-listenerrule-listenerarn"></a>
The Amazon Resource Name (ARN) of the listener.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Priority`  <a name="cfn-elasticloadbalancingv2-listenerrule-priority"></a>
The rule priority. A listener can't have multiple rules with the same priority.
If you try to reorder rules by updating their priorities, do not specify a new priority if an existing rule already uses this priority, as this can cause an error. If you need to reuse a priority with a different rule, you must remove it as a priority first, and then specify it in a subsequent update.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `50000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-elasticloadbalancingv2-listenerrule-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-elasticloadbalancingv2-listenerrule-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Transforms`  <a name="cfn-elasticloadbalancingv2-listenerrule-transforms"></a>
Property description not available.
*Required*: No
*Type*: Array of [Transform](aws-properties-elasticloadbalancingv2-listenerrule-transform.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-elasticloadbalancingv2-listenerrule-return-values"></a>

### Ref
<a name="aws-resource-elasticloadbalancingv2-listenerrule-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the listener rule.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-elasticloadbalancingv2-listenerrule-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-elasticloadbalancingv2-listenerrule-return-values-fn--getatt-fn--getatt"></a>

`IsDefault`  <a name="IsDefault-fn::getatt"></a>
Indicates whether this is the default rule.

`RuleArn`  <a name="RuleArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the rule.

## Examples
<a name="aws-resource-elasticloadbalancingv2-listenerrule--examples"></a>

You can define rules for your listener in addition to the default action. Each rule must specify an action and a condition.

**Topics**
+ [Forward action with a host-header condition](#aws-resource-elasticloadbalancingv2-listenerrule--examples--Forward_action_with_a_host-header_condition)
+ [Fixed-response action with a source-ip condition](#aws-resource-elasticloadbalancingv2-listenerrule--examples--Fixed-response_action_with_a_source-ip_condition)
+ [Redirect action with an http-header condition](#aws-resource-elasticloadbalancingv2-listenerrule--examples--Redirect_action_with_an_http-header_condition)

### Forward action with a host-header condition
<a name="aws-resource-elasticloadbalancingv2-listenerrule--examples--Forward_action_with_a_host-header_condition"></a>

The following example creates a rule with a `forward` action and a `host-header` condition.

#### YAML
<a name="aws-resource-elasticloadbalancingv2-listenerrule--examples--Forward_action_with_a_host-header_condition--yaml"></a>

```
myForwardListenerRule:
   Type: 'AWS::ElasticLoadBalancingV2::ListenerRule'
   Properties:
     ListenerArn: !Ref myListener
     Priority: 10
     Conditions:
       - Field: host-header
         Values:
           - example.com
           - www.example.com
     Actions:
       - Type: forward
         TargetGroupArn: !Ref myTargetGroup
```

#### JSON
<a name="aws-resource-elasticloadbalancingv2-listenerrule--examples--Forward_action_with_a_host-header_condition--json"></a>

```
{
    "myForwardListenerRule": {
        "Type": "AWS::ElasticLoadBalancingV2::ListenerRule",
        "Properties": {
            "ListenerArn": {
                "Ref": "myListener"
            },
            "Priority": 10,
            "Conditions": [
                {
                    "Field": "host-header",
                    "Values": [
                        "example.com",
                        "www.example.com"
                    ]
                }
            ],
            "Actions": [
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

### Fixed-response action with a source-ip condition
<a name="aws-resource-elasticloadbalancingv2-listenerrule--examples--Fixed-response_action_with_a_source-ip_condition"></a>

The following example creates a rule with a `fixed-response` action and a `source-ip` condition.

#### YAML
<a name="aws-resource-elasticloadbalancingv2-listenerrule--examples--Fixed-response_action_with_a_source-ip_condition--yaml"></a>

```
myFixedResponseListenerRule:
   Type: 'AWS::ElasticLoadBalancingV2::ListenerRule'
   Properties:
     ListenerArn: !Ref myListener
     Priority: 20
     Conditions:
       - Field: source-ip
         SourceIpConfig:
           Values:
             - 192.168.1.0/24
             - 10.0.0.0/16
     Actions:
       - Type: fixed-response
         FixedResponseConfig:
           StatusCode: 403
           ContentType: text/plain
           MessageBody: "Access denied"
```

#### JSON
<a name="aws-resource-elasticloadbalancingv2-listenerrule--examples--Fixed-response_action_with_a_source-ip_condition--json"></a>

```
{
    "myFixedResponseListenerRule": {
        "Type": "AWS::ElasticLoadBalancingV2::ListenerRule",
        "Properties": {
            "ListenerArn": {
                "Ref": "myListener"
            },
            "Priority": 20,
            "Conditions": [
                {
                    "Field": "source-ip",
                    "SourceIpConfig": {
                        "Values": [
                            "192.168.1.0/24",
                            "10.0.0.0/16"
                        ]
                    }
                }
            ],
            "Actions": [
                {
                    "Type": "fixed-response",
                    "FixedResponseConfig": {
                        "StatusCode": 403,
                        "ContentType": "text/plain",
                        "MessageBody": "Access denied"
                    }
                }
            ]
        }
    }
}
```

### Redirect action with an http-header condition
<a name="aws-resource-elasticloadbalancingv2-listenerrule--examples--Redirect_action_with_an_http-header_condition"></a>

The following example creates a rule with a `redirect` action and an `http-header` condition.

#### YAML
<a name="aws-resource-elasticloadbalancingv2-listenerrule--examples--Redirect_action_with_an_http-header_condition--yaml"></a>

```
myRedirectListenerRule:
   Type: 'AWS::ElasticLoadBalancingV2::ListenerRule'
   Properties:
     ListenerArn: !Ref myListener
     Priority: 30
     Conditions:
       - Field: http-header
         HttpHeaderConfig:
           HttpHeaderName: User-Agent
           Values:
             - "*Mobile*"
             - "*Android*"
             - "*iPhone*"
     Actions:
       - Type: redirect
         RedirectConfig:
           Host: m.example.com
           StatusCode: HTTP_302
```

#### JSON
<a name="aws-resource-elasticloadbalancingv2-listenerrule--examples--Redirect_action_with_an_http-header_condition--json"></a>

```
{
    "myRedirectListenerRule": {
        "Type": "AWS::ElasticLoadBalancingV2::ListenerRule",
        "Properties": {
            "ListenerArn": {
                "Ref": "myListener"
            },
            "Priority": 30,
            "Conditions": [
                {
                    "Field": "http-header",
                    "HttpHeaderConfig": {
                        "HttpHeaderName": "User-Agent",
                        "Values": [
                            "*Mobile*",
                            "*Android*",
                            "*iPhone*"
                        ]
                    }
                }
            ],
            "Actions": [
                {
                    "Type": "redirect",
                    "RedirectConfig": {
                        "Host": "m.example.com",
                        "StatusCode": "HTTP_302"
                    }
                }
            ]
        }
    }
}
```

## See also
<a name="aws-resource-elasticloadbalancingv2-listenerrule--seealso"></a>
+ [CreateRule](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateRule.html) in the *Elastic Load Balancing API Reference (version 2015-12-01)*
+ [Listener Rules](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#listener-rules) in the *User Guide for Application Load Balancers*
