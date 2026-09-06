---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_MonetizationConfig.html
---

# MonetizationConfig
<a name="API_MonetizationConfig"></a>

The monetization configuration for a web ACL or rule group. Specifies the cryptocurrency payment networks and currency mode for AI bot monetization. You must provide this configuration when any rule in the web ACL or rule group uses the `Monetize` action.

## Contents
<a name="API_MonetizationConfig_Contents"></a>

 ** CryptoConfig **   <a name="WAF-Type-MonetizationConfig-CryptoConfig"></a>
The cryptocurrency payment configuration, including the blockchain networks and wallet addresses where you receive payments.
Type: [CryptoConfig](API_CryptoConfig.md) object
Required: No

 ** CurrencyMode **   <a name="WAF-Type-MonetizationConfig-CurrencyMode"></a>
Specifies whether the configuration uses real or test currency. Set to `REAL` to settle payments in USDC on production blockchain networks (Base, Solana). Set to `TEST` to settle on testnet networks (Base Sepolia, Solana Devnet) with tokens that have no monetary value. If not specified, defaults to `REAL`.
Type: String
Valid Values: `REAL | TEST`
Required: No

## See Also
<a name="API_MonetizationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/MonetizationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/MonetizationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/MonetizationConfig)
