---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ConnectedAccountConfig.html
---

# ConnectedAccountConfig
<a name="API_ConnectedAccountConfig"></a>

A connected account configuration for AI bot monetization. Specifies the connected account that payments settle to and the per-network pricing. Settlement through a connected account is an alternative to the self-managed wallets in `CryptoConfig`; wallet addresses are managed for the connected account rather than configured by you. If the referenced connected account is not active or not enabled for crypto settlement, the `CreateWebACL`, `UpdateWebACL`, `CreateRuleGroup`, or `UpdateRuleGroup` request that includes it is rejected. Specifically, a request that references the account is rejected with `WAFInvalidOperationException` if the account or its crypto settlement capability isn't active, `WAFNonexistentItemException` if the ARN no longer exists, `AccessDeniedException` if you don't have `payments:GetConnectedAccount`, or `WAFInvalidParameterException` if the ARN is invalid or the partition is unsupported. Connected accounts are available only in the commercial AWS partition.

## Contents
<a name="API_ConnectedAccountConfig_Contents"></a>

 ** ConnectedAccountArn **   <a name="WAF-Type-ConnectedAccountConfig-ConnectedAccountArn"></a>
The Amazon Resource Name (ARN) of the connected account that payments settle to. You obtain this ARN from Payment preferences > Connected accounts in the AWS Billing and Cost Management console. For more information, see [Managing connected accounts](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-connected-accounts.html). The connected account must be active and enabled for crypto settlement; otherwise the request is rejected. To use a connected account, you must have the `payments:GetConnectedAccount` permission on this ARN.
Type: String
Length Constraints: Minimum length of 56. Maximum length of 140.
Pattern: `^arn:aws(-[a-z]+)*:payments::[0-9]{12}:connectedaccount/[a-zA-Z0-9][a-zA-Z0-9_-]{0,63}-[A-Za-z0-9]{6}$`
Required: Yes

 ** PaymentNetworks **   <a name="WAF-Type-ConnectedAccountConfig-PaymentNetworks"></a>
The per-network configurations for the connected account. You can specify 1 to 2 networks. Each entry specifies a blockchain network and the price for each request.
Type: Array of [ConnectedAccountChainConfig](API_ConnectedAccountChainConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

## See Also
<a name="API_ConnectedAccountConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ConnectedAccountConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ConnectedAccountConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ConnectedAccountConfig)
