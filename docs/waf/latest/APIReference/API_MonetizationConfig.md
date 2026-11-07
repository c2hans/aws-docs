---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_MonetizationConfig.html
---

# MonetizationConfig
<a name="API_MonetizationConfig"></a>

The monetization configuration for a web ACL or rule group. Specifies the payment settlement options (self-managed crypto wallets in `CryptoConfig`, a connected account in `ConnectedAccountConfigs`, or both) and the currency mode for artificial intelligence (AI) bot monetization. You must provide this configuration when any rule in the web ACL or rule group uses the `Monetize` action.

## Contents
<a name="API_MonetizationConfig_Contents"></a>

 ** ConnectedAccountConfigs **   <a name="WAF-Type-MonetizationConfig-ConnectedAccountConfigs"></a>
The connected account configurations for settling AI bot payments through a connected account with a supported third-party payment provider (Stripe), as an alternative to the self-managed wallets in `CryptoConfig`. You can provide `CryptoConfig`, `ConnectedAccountConfigs`, or both; however, a given blockchain network (chain) can be used by only one of them. Currently supports exactly one connected account.
Type: Array of [ConnectedAccountConfig](API_ConnectedAccountConfig.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** CryptoConfig **   <a name="WAF-Type-MonetizationConfig-CryptoConfig"></a>
The cryptocurrency payment configuration, including the blockchain networks and wallet addresses where you receive payments.
Type: [CryptoConfig](API_CryptoConfig.md) object
Required: No

 ** CurrencyMode **   <a name="WAF-Type-MonetizationConfig-CurrencyMode"></a>
Specifies whether the configuration uses real or test currency. If not specified, defaults to `REAL`. Connected account configurations support production settlement only; `TEST` is not supported when `ConnectedAccountConfigs` is present.
Valid values:
+  `REAL` - Settle payments in USDC on production blockchain networks (Base, Solana).
+  `TEST` - Settle on testnet networks (Base Sepolia, Solana Devnet) with tokens that have no monetary value.
Type: String
Valid Values: `REAL | TEST`
Required: No

## See Also
<a name="API_MonetizationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/MonetizationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/MonetizationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/MonetizationConfig)
