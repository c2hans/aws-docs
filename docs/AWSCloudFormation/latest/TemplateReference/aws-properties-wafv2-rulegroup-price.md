---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-price.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup Price
<a name="aws-properties-wafv2-rulegroup-price"></a>

The price per request for a payment network, specifying the amount and cryptocurrency.

## Syntax
<a name="aws-properties-wafv2-rulegroup-price-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-price-syntax.json"></a>

```
{
  "[Amount](#cfn-wafv2-rulegroup-price-amount)" : {{String}},
  "[Currency](#cfn-wafv2-rulegroup-price-currency)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-price-syntax.yaml"></a>

```
  [Amount](#cfn-wafv2-rulegroup-price-amount): {{String}}
  [Currency](#cfn-wafv2-rulegroup-price-currency): {{String}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-price-properties"></a>

`Amount`  <a name="cfn-wafv2-rulegroup-price-amount"></a>
The price per request as a decimal string in the specified currency. Minimum: 0.001. Maximum: 999999999.999. Supports up to 3 decimal places.
*Required*: Yes
*Type*: String
*Pattern*: `^([1-9][0-9]*(\.[0-9]{1,3})?|0\.([1-9][0-9]{0,2}|0[1-9][0-9]?|00[1-9]))$`
*Minimum*: `1`
*Maximum*: `13`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Currency`  <a name="cfn-wafv2-rulegroup-price-currency"></a>
The cryptocurrency for payment. Currently only `USDC` is supported.
*Required*: Yes
*Type*: String
*Allowed values*: `USDC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
