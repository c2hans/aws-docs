---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-monetizationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup MonetizationConfig
<a name="aws-properties-wafv2-rulegroup-monetizationconfig"></a>

The monetization configuration for a web ACL or rule group. Specifies the cryptocurrency payment networks and currency mode for AI bot monetization. You must provide this configuration when any rule in the web ACL or rule group uses the `Monetize` action.

## Syntax
<a name="aws-properties-wafv2-rulegroup-monetizationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-monetizationconfig-syntax.json"></a>

```
{
  "[CryptoConfig](#cfn-wafv2-rulegroup-monetizationconfig-cryptoconfig)" : {{CryptoConfig}},
  "[CurrencyMode](#cfn-wafv2-rulegroup-monetizationconfig-currencymode)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-monetizationconfig-syntax.yaml"></a>

```
  [CryptoConfig](#cfn-wafv2-rulegroup-monetizationconfig-cryptoconfig): {{
    CryptoConfig}}
  [CurrencyMode](#cfn-wafv2-rulegroup-monetizationconfig-currencymode): {{String}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-monetizationconfig-properties"></a>

`CryptoConfig`  <a name="cfn-wafv2-rulegroup-monetizationconfig-cryptoconfig"></a>
The cryptocurrency payment configuration, including the blockchain networks and wallet addresses where you receive payments.
*Required*: No
*Type*: [CryptoConfig](aws-properties-wafv2-rulegroup-cryptoconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CurrencyMode`  <a name="cfn-wafv2-rulegroup-monetizationconfig-currencymode"></a>
Specifies whether the configuration uses real or test currency. Set to `REAL` to settle payments in USDC on production blockchain networks (Base, Solana). Set to `TEST` to settle on testnet networks (Base Sepolia, Solana Devnet) with tokens that have no monetary value. If not specified, defaults to `REAL`.
*Required*: No
*Type*: String
*Allowed values*: `REAL | TEST`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
