---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-ratelimitja4fingerprint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup RateLimitJA4Fingerprint
<a name="aws-properties-wafv2-rulegroup-ratelimitja4fingerprint"></a>

Use the request's JA4 fingerprint derived from the TLS Client Hello of an incoming request as an aggregate key. If you use a single JA4 fingerprint as your custom key, then each value fully defines an aggregation instance.

## Syntax
<a name="aws-properties-wafv2-rulegroup-ratelimitja4fingerprint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-ratelimitja4fingerprint-syntax.json"></a>

```
{
  "[FallbackBehavior](#cfn-wafv2-rulegroup-ratelimitja4fingerprint-fallbackbehavior)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-ratelimitja4fingerprint-syntax.yaml"></a>

```
  [FallbackBehavior](#cfn-wafv2-rulegroup-ratelimitja4fingerprint-fallbackbehavior): {{String}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-ratelimitja4fingerprint-properties"></a>

`FallbackBehavior`  <a name="cfn-wafv2-rulegroup-ratelimitja4fingerprint-fallbackbehavior"></a>
The match status to assign to the web request if there is insufficient TSL Client Hello information to compute the JA4 fingerprint.
You can specify the following fallback behaviors:
+ `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+ `NO_MATCH` - Treat the web request as not matching the rule statement.
*Required*: Yes
*Type*: String
*Allowed values*: `MATCH | NO_MATCH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
