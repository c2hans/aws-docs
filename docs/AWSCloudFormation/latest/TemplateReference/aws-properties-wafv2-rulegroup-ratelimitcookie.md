---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-ratelimitcookie.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup RateLimitCookie
<a name="aws-properties-wafv2-rulegroup-ratelimitcookie"></a>

Specifies a cookie as an aggregate key for a rate-based rule. Each distinct value in the cookie contributes to the aggregation instance. If you use a single cookie as your custom key, then each value fully defines an aggregation instance.

## Syntax
<a name="aws-properties-wafv2-rulegroup-ratelimitcookie-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-ratelimitcookie-syntax.json"></a>

```
{
  "[Name](#cfn-wafv2-rulegroup-ratelimitcookie-name)" : {{String}},
  "[TextTransformations](#cfn-wafv2-rulegroup-ratelimitcookie-texttransformations)" : {{[ TextTransformation, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-ratelimitcookie-syntax.yaml"></a>

```
  [Name](#cfn-wafv2-rulegroup-ratelimitcookie-name): {{String}}
  [TextTransformations](#cfn-wafv2-rulegroup-ratelimitcookie-texttransformations): {{
    - TextTransformation}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-ratelimitcookie-properties"></a>

`Name`  <a name="cfn-wafv2-rulegroup-ratelimitcookie-name"></a>
The name of the cookie to use.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextTransformations`  <a name="cfn-wafv2-rulegroup-ratelimitcookie-texttransformations"></a>
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. Text transformations are used in rule match statements, to transform the `FieldToMatch` request component before inspecting it, and they're used in rate-based rule statements, to transform request components before using them as custom aggregation keys. If you specify one or more transformations to apply, AWS WAF performs all transformations on the specified content, starting from the lowest priority setting, and then uses the transformed component contents.
*Required*: Yes
*Type*: Array of [TextTransformation](aws-properties-wafv2-rulegroup-texttransformation.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
