---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-connectedaccountchainconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup ConnectedAccountChainConfig
<a name="aws-properties-wafv2-rulegroup-connectedaccountchainconfig"></a>

A per-network configuration for a connected account, specifying the blockchain network and the price per request. Unlike `PaymentNetwork`, you do not provide a wallet address; the receiving address is managed for the connected account.

## Syntax
<a name="aws-properties-wafv2-rulegroup-connectedaccountchainconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-connectedaccountchainconfig-syntax.json"></a>

```
{
  "[Chain](#cfn-wafv2-rulegroup-connectedaccountchainconfig-chain)" : {{String}},
  "[Prices](#cfn-wafv2-rulegroup-connectedaccountchainconfig-prices)" : {{[ ConnectedAccountPrice, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-connectedaccountchainconfig-syntax.yaml"></a>

```
  [Chain](#cfn-wafv2-rulegroup-connectedaccountchainconfig-chain): {{String}}
  [Prices](#cfn-wafv2-rulegroup-connectedaccountchainconfig-prices): {{
    - ConnectedAccountPrice}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-connectedaccountchainconfig-properties"></a>

`Chain`  <a name="cfn-wafv2-rulegroup-connectedaccountchainconfig-chain"></a>
The blockchain network for receiving payments through the connected account. Test networks are not supported for connected accounts.
Valid values:
+ `BASE` - Base mainnet.
+ `SOLANA` - Solana mainnet.
*Required*: Yes
*Type*: String
*Allowed values*: `BASE | SOLANA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prices`  <a name="cfn-wafv2-rulegroup-connectedaccountchainconfig-prices"></a>
The price configuration for this network. Currently supports a single price entry in USDC.
*Required*: Yes
*Type*: Array of [ConnectedAccountPrice](aws-properties-wafv2-rulegroup-connectedaccountprice.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
