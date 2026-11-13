---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-connectedaccountconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup ConnectedAccountConfig
<a name="aws-properties-wafv2-rulegroup-connectedaccountconfig"></a>

A connected account configuration for AI bot monetization. Specifies the connected account that payments settle to and the per-network pricing. Settlement through a connected account is an alternative to the self-managed wallets in `CryptoConfig`; wallet addresses are managed for the connected account rather than configured by you. If the referenced connected account is not active or not enabled for crypto settlement, the `CreateWebACL`, `UpdateWebACL`, `CreateRuleGroup`, or `UpdateRuleGroup` request that includes it is rejected. Specifically, a request that references the account is rejected with `WAFInvalidOperationException` if the account or its crypto settlement capability isn't active, `WAFNonexistentItemException` if the ARN no longer exists, `AccessDeniedException` if you don't have `payments:GetConnectedAccount`, or `WAFInvalidParameterException` if the ARN is invalid or the partition is unsupported. Connected accounts are available only in the commercial AWS partition.

## Syntax
<a name="aws-properties-wafv2-rulegroup-connectedaccountconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-connectedaccountconfig-syntax.json"></a>

```
{
  "[ConnectedAccountArn](#cfn-wafv2-rulegroup-connectedaccountconfig-connectedaccountarn)" : {{String}},
  "[PaymentNetworks](#cfn-wafv2-rulegroup-connectedaccountconfig-paymentnetworks)" : {{[ ConnectedAccountChainConfig, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-connectedaccountconfig-syntax.yaml"></a>

```
  [ConnectedAccountArn](#cfn-wafv2-rulegroup-connectedaccountconfig-connectedaccountarn): {{String}}
  [PaymentNetworks](#cfn-wafv2-rulegroup-connectedaccountconfig-paymentnetworks): {{
    - ConnectedAccountChainConfig}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-connectedaccountconfig-properties"></a>

`ConnectedAccountArn`  <a name="cfn-wafv2-rulegroup-connectedaccountconfig-connectedaccountarn"></a>
The Amazon Resource Name (ARN) of the connected account that payments settle to. You obtain this ARN from Payment preferences > Connected accounts in the AWS Billing and Cost Management console. For more information, see [Managing connected accounts](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-connected-accounts.html). The connected account must be active and enabled for crypto settlement; otherwise the request is rejected. To use a connected account, you must have the `payments:GetConnectedAccount` permission on this ARN.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[a-z]+)*:payments::[0-9]{12}:connectedaccount/[a-zA-Z0-9][a-zA-Z0-9_-]{0,63}-[A-Za-z0-9]{6}$`
*Minimum*: `56`
*Maximum*: `140`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PaymentNetworks`  <a name="cfn-wafv2-rulegroup-connectedaccountconfig-paymentnetworks"></a>
The per-network configurations for the connected account. You can specify 1 to 2 networks. Each entry specifies a blockchain network and the price for each request.
*Required*: Yes
*Type*: Array of [ConnectedAccountChainConfig](aws-properties-wafv2-rulegroup-connectedaccountchainconfig.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
