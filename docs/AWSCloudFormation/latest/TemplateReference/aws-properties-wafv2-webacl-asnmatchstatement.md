---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-asnmatchstatement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL AsnMatchStatement
<a name="aws-properties-wafv2-webacl-asnmatchstatement"></a>

A rule statement that inspects web traffic based on the Autonomous System Number (ASN) associated with the request's IP address.

For additional details, see [ASN match rule statement](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-asn-match.html) in the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html).

## Syntax
<a name="aws-properties-wafv2-webacl-asnmatchstatement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-asnmatchstatement-syntax.json"></a>

```
{
  "[AsnList](#cfn-wafv2-webacl-asnmatchstatement-asnlist)" : {{[ Integer, ... ]}},
  "[ForwardedIPConfig](#cfn-wafv2-webacl-asnmatchstatement-forwardedipconfig)" : {{ForwardedIPConfiguration}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-asnmatchstatement-syntax.yaml"></a>

```
  [AsnList](#cfn-wafv2-webacl-asnmatchstatement-asnlist): {{
    - Integer}}
  [ForwardedIPConfig](#cfn-wafv2-webacl-asnmatchstatement-forwardedipconfig): {{
    ForwardedIPConfiguration}}
```

## Properties
<a name="aws-properties-wafv2-webacl-asnmatchstatement-properties"></a>

`AsnList`  <a name="cfn-wafv2-webacl-asnmatchstatement-asnlist"></a>
Contains one or more Autonomous System Numbers (ASNs). ASNs are unique identifiers assigned to large internet networks managed by organizations such as internet service providers, enterprises, universities, or government agencies.
*Required*: No
*Type*: Array of Integer
*Minimum*: `0`
*Maximum*: `4294967295`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ForwardedIPConfig`  <a name="cfn-wafv2-webacl-asnmatchstatement-forwardedipconfig"></a>
The configuration for inspecting IP addresses to match against an ASN in an HTTP header that you specify, instead of using the IP address that's reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.
*Required*: No
*Type*: [ForwardedIPConfiguration](aws-properties-wafv2-webacl-forwardedipconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
