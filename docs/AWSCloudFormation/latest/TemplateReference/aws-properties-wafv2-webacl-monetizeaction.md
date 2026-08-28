---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-monetizeaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL MonetizeAction
<a name="aws-properties-wafv2-webacl-monetizeaction"></a>

Specifies the monetize action settings for a rule. When AWS WAF applies this action, it returns an HTTP 402 Payment Required response containing pricing information that the requesting client uses to complete payment and gain access to the resource. This is a terminating action-if the client does not complete the 402 payment flow, the request is blocked. This action is available only for web ACLs associated with Amazon CloudFront distributions. You must configure a `MonetizationConfig` on the web ACL or rule group before adding rules that use this action. You cannot use the Monetize action for rate-based rules.

## Syntax
<a name="aws-properties-wafv2-webacl-monetizeaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-monetizeaction-syntax.json"></a>

```
{
  "[PriceMultiplier](#cfn-wafv2-webacl-monetizeaction-pricemultiplier)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-monetizeaction-syntax.yaml"></a>

```
  [PriceMultiplier](#cfn-wafv2-webacl-monetizeaction-pricemultiplier): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-monetizeaction-properties"></a>

`PriceMultiplier`  <a name="cfn-wafv2-webacl-monetizeaction-pricemultiplier"></a>
An integer multiplier applied to the base price defined in the web ACL's `MonetizationConfig`. The effective price for the request is the base price multiplied by this value. Specify as a string. Valid values: 1 to 100.
*Required*: No
*Type*: String
*Pattern*: `^([1-9][0-9]?|100)$`
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
