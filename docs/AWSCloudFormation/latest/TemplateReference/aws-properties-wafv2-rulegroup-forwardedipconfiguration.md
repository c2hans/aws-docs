---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-forwardedipconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup ForwardedIPConfiguration
<a name="aws-properties-wafv2-rulegroup-forwardedipconfiguration"></a>

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address that's reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

**Note**
If the specified header isn't present in the request, AWS WAF doesn't apply the rule to the web request at all.

This configuration is used for [GeoMatchStatement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-geomatchstatement), [AsnMatchStatement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-asnmatchstatement), and [RateBasedStatement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-ratebasedstatement). For [IPSetReferenceStatement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-ipsetreferencestatement), use [IPSetForwardedIPConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html#cfn-wafv2-rulegroup-ipsetreferencestatement-ipsetforwardedipconfig) instead.

AWS WAF only evaluates the first IP address found in the specified HTTP header.

## Syntax
<a name="aws-properties-wafv2-rulegroup-forwardedipconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-forwardedipconfiguration-syntax.json"></a>

```
{
  "[FallbackBehavior](#cfn-wafv2-rulegroup-forwardedipconfiguration-fallbackbehavior)" : {{String}},
  "[HeaderName](#cfn-wafv2-rulegroup-forwardedipconfiguration-headername)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-forwardedipconfiguration-syntax.yaml"></a>

```
  [FallbackBehavior](#cfn-wafv2-rulegroup-forwardedipconfiguration-fallbackbehavior): {{String}}
  [HeaderName](#cfn-wafv2-rulegroup-forwardedipconfiguration-headername): {{String}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-forwardedipconfiguration-properties"></a>

`FallbackBehavior`  <a name="cfn-wafv2-rulegroup-forwardedipconfiguration-fallbackbehavior"></a>
The match status to assign to the web request if the request doesn't have a valid IP address in the specified position.
If the specified header isn't present in the request, AWS WAF doesn't apply the rule to the web request at all.
You can specify the following fallback behaviors:
+ `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+ `NO_MATCH` - Treat the web request as not matching the rule statement.
*Required*: Yes
*Type*: String
*Allowed values*: `MATCH | NO_MATCH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HeaderName`  <a name="cfn-wafv2-rulegroup-forwardedipconfiguration-headername"></a>
The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to `X-Forwarded-For`.
If the specified header isn't present in the request, AWS WAF doesn't apply the rule to the web request at all.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+{1,255}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
