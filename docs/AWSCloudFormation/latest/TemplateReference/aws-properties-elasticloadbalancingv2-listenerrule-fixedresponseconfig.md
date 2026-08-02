---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listenerrule-fixedresponseconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::ListenerRule FixedResponseConfig
<a name="aws-properties-elasticloadbalancingv2-listenerrule-fixedresponseconfig"></a>

Specifies information required when returning a custom HTTP response.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listenerrule-fixedresponseconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listenerrule-fixedresponseconfig-syntax.json"></a>

```
{
  "[ContentType](#cfn-elasticloadbalancingv2-listenerrule-fixedresponseconfig-contenttype)" : {{String}},
  "[MessageBody](#cfn-elasticloadbalancingv2-listenerrule-fixedresponseconfig-messagebody)" : {{String}},
  "[StatusCode](#cfn-elasticloadbalancingv2-listenerrule-fixedresponseconfig-statuscode)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-fixedresponseconfig-syntax.yaml"></a>

```
  [ContentType](#cfn-elasticloadbalancingv2-listenerrule-fixedresponseconfig-contenttype): {{String}}
  [MessageBody](#cfn-elasticloadbalancingv2-listenerrule-fixedresponseconfig-messagebody): {{String}}
  [StatusCode](#cfn-elasticloadbalancingv2-listenerrule-fixedresponseconfig-statuscode): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listenerrule-fixedresponseconfig-properties"></a>

`ContentType`  <a name="cfn-elasticloadbalancingv2-listenerrule-fixedresponseconfig-contenttype"></a>
The content type.
Valid Values: text/plain \| text/css \| text/html \| application/javascript \| application/json
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessageBody`  <a name="cfn-elasticloadbalancingv2-listenerrule-fixedresponseconfig-messagebody"></a>
The message.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusCode`  <a name="cfn-elasticloadbalancingv2-listenerrule-fixedresponseconfig-statuscode"></a>
The HTTP response code (2XX, 4XX, or 5XX).
*Required*: Yes
*Type*: String
*Pattern*: `^(2|4|5)\d\d$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-elasticloadbalancingv2-listenerrule-fixedresponseconfig--examples"></a>

###
<a name="aws-properties-elasticloadbalancingv2-listenerrule-fixedresponseconfig--examples--"></a>

The following example creates a listener rule with an action that returns the specified HTTP response under the specified condition.

#### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-fixedresponseconfig--examples----yaml"></a>

```
myListenerRule:
    Type: AWS::ElasticLoadBalancingV2::ListenerRule
    Properties:
      Actions:
       - Type: fixed-response
         FixedResponseConfig:
           ContentType: text/plain
           MessageBody: "Hello world"
           StatusCode: 200
      Conditions:
       - Field: path-pattern
         Values:
           - /my-path/*
      ListenerArn: !Ref myListener
      Priority: 10
```

#### JSON
<a name="aws-properties-elasticloadbalancingv2-listenerrule-fixedresponseconfig--examples----json"></a>

```
{
    "myListenerRule": {
        "Type": "AWS::ElasticLoadBalancingV2::ListenerRule",
        "Properties": {
            "Actions": [
                {
                    "Type": "fixed-response",
                    "FixedResponseConfig": {
                        "ContentType": "text/plain",
                        "MessageBody": "Hello world",
                        "StatusCode": 200
                    }
                }
            ],
            "Conditions": [
                {
                    "Field": "path-pattern",
                    "Values": [
                        "/my-path/*"
                    ]
                }
            ],
            "ListenerArn": {
                "Ref": "myListener"
            },
            "Priority": 10
        }
    }
}
```
