---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listenerrule-hostheaderconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::ListenerRule HostHeaderConfig
<a name="aws-properties-elasticloadbalancingv2-listenerrule-hostheaderconfig"></a>

Information about a host header condition.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listenerrule-hostheaderconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listenerrule-hostheaderconfig-syntax.json"></a>

```
{
  "[RegexValues](#cfn-elasticloadbalancingv2-listenerrule-hostheaderconfig-regexvalues)" : {{[ String, ... ]}},
  "[Values](#cfn-elasticloadbalancingv2-listenerrule-hostheaderconfig-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-hostheaderconfig-syntax.yaml"></a>

```
  [RegexValues](#cfn-elasticloadbalancingv2-listenerrule-hostheaderconfig-regexvalues): {{
    - String}}
  [Values](#cfn-elasticloadbalancingv2-listenerrule-hostheaderconfig-values): {{
    - String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listenerrule-hostheaderconfig-properties"></a>

`RegexValues`  <a name="cfn-elasticloadbalancingv2-listenerrule-hostheaderconfig-regexvalues"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-elasticloadbalancingv2-listenerrule-hostheaderconfig-values"></a>
The host names. The maximum length of each string is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: \* (matches 0 or more characters) and ? (matches exactly 1 character). You must include at least one "." character. You can include only alphabetical characters after the final "." character.
If you specify multiple strings, the condition is satisfied if one of the strings matches the host name.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-elasticloadbalancingv2-listenerrule-hostheaderconfig--examples"></a>

###
<a name="aws-properties-elasticloadbalancingv2-listenerrule-hostheaderconfig--examples--"></a>

This example creates a listener rule with an action that forwards requests destined for the specified domain and subdomain to the specified target group.

#### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-hostheaderconfig--examples----yaml"></a>

```
myHostHeaderListenerRule:
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
<a name="aws-properties-elasticloadbalancingv2-listenerrule-hostheaderconfig--examples----json"></a>

```
{
    "myHostHeaderListenerRule": {
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
