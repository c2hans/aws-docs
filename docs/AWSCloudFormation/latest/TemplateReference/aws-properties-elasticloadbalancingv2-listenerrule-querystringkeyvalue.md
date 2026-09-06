---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listenerrule-querystringkeyvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::ListenerRule QueryStringKeyValue
<a name="aws-properties-elasticloadbalancingv2-listenerrule-querystringkeyvalue"></a>

Information about a key/value pair.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listenerrule-querystringkeyvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listenerrule-querystringkeyvalue-syntax.json"></a>

```
{
  "[Key](#cfn-elasticloadbalancingv2-listenerrule-querystringkeyvalue-key)" : {{String}},
  "[Value](#cfn-elasticloadbalancingv2-listenerrule-querystringkeyvalue-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-querystringkeyvalue-syntax.yaml"></a>

```
  [Key](#cfn-elasticloadbalancingv2-listenerrule-querystringkeyvalue-key): {{String}}
  [Value](#cfn-elasticloadbalancingv2-listenerrule-querystringkeyvalue-value): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listenerrule-querystringkeyvalue-properties"></a>

`Key`  <a name="cfn-elasticloadbalancingv2-listenerrule-querystringkeyvalue-key"></a>
The key. You can omit the key.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-elasticloadbalancingv2-listenerrule-querystringkeyvalue-value"></a>
The value.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
