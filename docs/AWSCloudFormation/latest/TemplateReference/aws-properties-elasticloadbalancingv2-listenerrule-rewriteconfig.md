---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listenerrule-rewriteconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::ListenerRule RewriteConfig
<a name="aws-properties-elasticloadbalancingv2-listenerrule-rewriteconfig"></a>

Information about a rewrite transform. This transform matches a pattern and replaces it with the specified string.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listenerrule-rewriteconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listenerrule-rewriteconfig-syntax.json"></a>

```
{
  "[Regex](#cfn-elasticloadbalancingv2-listenerrule-rewriteconfig-regex)" : {{String}},
  "[Replace](#cfn-elasticloadbalancingv2-listenerrule-rewriteconfig-replace)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-rewriteconfig-syntax.yaml"></a>

```
  [Regex](#cfn-elasticloadbalancingv2-listenerrule-rewriteconfig-regex): {{String}}
  [Replace](#cfn-elasticloadbalancingv2-listenerrule-rewriteconfig-replace): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listenerrule-rewriteconfig-properties"></a>

`Regex`  <a name="cfn-elasticloadbalancingv2-listenerrule-rewriteconfig-regex"></a>
The regular expression to match in the input string. The maximum length of the string is 1,024 characters.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Replace`  <a name="cfn-elasticloadbalancingv2-listenerrule-rewriteconfig-replace"></a>
The replacement string to use when rewriting the matched input. The maximum length of the string is 1,024 characters. You can specify capture groups in the regular expression (for example, $1 and $2).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
