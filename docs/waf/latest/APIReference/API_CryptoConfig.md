---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_CryptoConfig.html
---

# CryptoConfig
<a name="API_CryptoConfig"></a>

The cryptocurrency payment configuration for AI bot monetization. Contains the list of blockchain payment networks where you receive payments.

## Contents
<a name="API_CryptoConfig_Contents"></a>

 ** PaymentNetworks **   <a name="WAF-Type-CryptoConfig-PaymentNetworks"></a>
The blockchain payment networks configured to receive payments. You can specify 1 to 2 networks. All networks must be in the same environment-either all production networks (Base, Solana) or all test networks (Base Sepolia, Solana Devnet).
Type: Array of [PaymentNetwork](API_PaymentNetwork.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

## See Also
<a name="API_CryptoConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/CryptoConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/CryptoConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/CryptoConfig)
