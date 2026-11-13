---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-monetizationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL MonetizationConfig
<a name="aws-properties-wafv2-webacl-monetizationconfig"></a>

The monetization configuration for a web ACL or rule group. Specifies the payment settlement options (self-managed crypto wallets in `CryptoConfig`, a connected account in `ConnectedAccountConfigs`, or both) and the currency mode for artificial intelligence (AI) bot monetization. You must provide this configuration when any rule in the web ACL or rule group uses the `Monetize` action.

## Syntax
<a name="aws-properties-wafv2-webacl-monetizationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-monetizationconfig-syntax.json"></a>

```
{
  "[ConnectedAccountConfigs](#cfn-wafv2-webacl-monetizationconfig-connectedaccountconfigs)" : {{[ ConnectedAccountConfig, ... ]}},
  "[CryptoConfig](#cfn-wafv2-webacl-monetizationconfig-cryptoconfig)" : {{CryptoConfig}},
  "[CurrencyMode](#cfn-wafv2-webacl-monetizationconfig-currencymode)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-monetizationconfig-syntax.yaml"></a>

```
  [ConnectedAccountConfigs](#cfn-wafv2-webacl-monetizationconfig-connectedaccountconfigs): {{
    - ConnectedAccountConfig}}
  [CryptoConfig](#cfn-wafv2-webacl-monetizationconfig-cryptoconfig): {{
    CryptoConfig}}
  [CurrencyMode](#cfn-wafv2-webacl-monetizationconfig-currencymode): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-monetizationconfig-properties"></a>

`ConnectedAccountConfigs`  <a name="cfn-wafv2-webacl-monetizationconfig-connectedaccountconfigs"></a>
The connected account configurations for settling AI bot payments through a connected account with a supported third-party payment provider (Stripe), as an alternative to the self-managed wallets in `CryptoConfig`. You can provide `CryptoConfig`, `ConnectedAccountConfigs`, or both; however, a given blockchain network (chain) can be used by only one of them. Currently supports exactly one connected account.
*Required*: No
*Type*: Array of [ConnectedAccountConfig](aws-properties-wafv2-webacl-connectedaccountconfig.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CryptoConfig`  <a name="cfn-wafv2-webacl-monetizationconfig-cryptoconfig"></a>
The cryptocurrency payment configuration, including the blockchain networks and wallet addresses where you receive payments.
*Required*: No
*Type*: [CryptoConfig](aws-properties-wafv2-webacl-cryptoconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CurrencyMode`  <a name="cfn-wafv2-webacl-monetizationconfig-currencymode"></a>
Specifies whether the configuration uses real or test currency. If not specified, defaults to `REAL`. Connected account configurations support production settlement only; `TEST` is not supported when `ConnectedAccountConfigs` is present.
Valid values:
+ `REAL` - Settle payments in USDC on production blockchain networks (Base, Solana).
+ `TEST` - Settle on testnet networks (Base Sepolia, Solana Devnet) with tokens that have no monetary value.
*Required*: No
*Type*: String
*Allowed values*: `REAL | TEST`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
