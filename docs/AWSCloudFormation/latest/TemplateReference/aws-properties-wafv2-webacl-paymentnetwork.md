---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-paymentnetwork.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL PaymentNetwork
<a name="aws-properties-wafv2-webacl-paymentnetwork"></a>

A blockchain payment network configuration for receiving AI bot monetization payments. Specifies the blockchain chain, your wallet address on that chain, and the price per request.

## Syntax
<a name="aws-properties-wafv2-webacl-paymentnetwork-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-paymentnetwork-syntax.json"></a>

```
{
  "[Chain](#cfn-wafv2-webacl-paymentnetwork-chain)" : {{String}},
  "[Prices](#cfn-wafv2-webacl-paymentnetwork-prices)" : {{[ Price, ... ]}},
  "[WalletAddress](#cfn-wafv2-webacl-paymentnetwork-walletaddress)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-paymentnetwork-syntax.yaml"></a>

```
  [Chain](#cfn-wafv2-webacl-paymentnetwork-chain): {{String}}
  [Prices](#cfn-wafv2-webacl-paymentnetwork-prices): {{
    - Price}}
  [WalletAddress](#cfn-wafv2-webacl-paymentnetwork-walletaddress): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-paymentnetwork-properties"></a>

`Chain`  <a name="cfn-wafv2-webacl-paymentnetwork-chain"></a>
The blockchain network for receiving payments. Production networks: `BASE` (Base mainnet), `SOLANA` (Solana mainnet). Test networks: `BASE_SEPOLIA` (Base Sepolia testnet), `SOLANA_DEVNET` (Solana Devnet).
*Required*: Yes
*Type*: String
*Allowed values*: `BASE | SOLANA | BASE_SEPOLIA | SOLANA_DEVNET`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prices`  <a name="cfn-wafv2-webacl-paymentnetwork-prices"></a>
The price configuration for this payment network. Currently supports a single price entry in USDC.
*Required*: Yes
*Type*: Array of [Price](aws-properties-wafv2-webacl-price.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WalletAddress`  <a name="cfn-wafv2-webacl-paymentnetwork-walletaddress"></a>
Your wallet address on the specified blockchain where payments are sent. For EVM chains (Base, Base Sepolia), provide a valid Ethereum address (42 characters including 0x prefix). For Solana chains, provide a valid Base58-encoded public key (32-44 characters).
For EVM addresses, AWS WAF performs EIP-55 checksum validation for typo detection when the address uses a mix of lower and upper case letters. You can bypass this validation by providing the address in all lowercase or all uppercase.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `26`
*Maximum*: `44`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
