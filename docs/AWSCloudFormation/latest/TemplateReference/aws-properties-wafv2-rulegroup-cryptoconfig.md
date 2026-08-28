---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-cryptoconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup CryptoConfig
<a name="aws-properties-wafv2-rulegroup-cryptoconfig"></a>

The cryptocurrency payment configuration for AI bot monetization. Contains the list of blockchain payment networks where you receive payments.

## Syntax
<a name="aws-properties-wafv2-rulegroup-cryptoconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-cryptoconfig-syntax.json"></a>

```
{
  "[PaymentNetworks](#cfn-wafv2-rulegroup-cryptoconfig-paymentnetworks)" : {{[ PaymentNetwork, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-cryptoconfig-syntax.yaml"></a>

```
  [PaymentNetworks](#cfn-wafv2-rulegroup-cryptoconfig-paymentnetworks): {{
    - PaymentNetwork}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-cryptoconfig-properties"></a>

`PaymentNetworks`  <a name="cfn-wafv2-rulegroup-cryptoconfig-paymentnetworks"></a>
The blockchain payment networks configured to receive payments. You can specify 1 to 2 networks. All networks must be in the same environment-either all production networks (Base, Solana) or all test networks (Base Sepolia, Solana Devnet).
*Required*: Yes
*Type*: Array of [PaymentNetwork](aws-properties-wafv2-rulegroup-paymentnetwork.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
