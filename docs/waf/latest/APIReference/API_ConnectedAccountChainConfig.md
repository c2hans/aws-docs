---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ConnectedAccountChainConfig.html
---

# ConnectedAccountChainConfig
<a name="API_ConnectedAccountChainConfig"></a>

A per-network configuration for a connected account, specifying the blockchain network and the price per request. Unlike `PaymentNetwork`, you do not provide a wallet address; the receiving address is managed for the connected account.

## Contents
<a name="API_ConnectedAccountChainConfig_Contents"></a>

 ** Chain **   <a name="WAF-Type-ConnectedAccountChainConfig-Chain"></a>
The blockchain network for receiving payments through the connected account. Test networks are not supported for connected accounts.
Valid values:
+  `BASE` - Base mainnet.
+  `SOLANA` - Solana mainnet.
Type: String
Valid Values: `BASE | SOLANA`
Required: Yes

 ** Prices **   <a name="WAF-Type-ConnectedAccountChainConfig-Prices"></a>
The price configuration for this network. Currently supports a single price entry in USDC.
Type: Array of [ConnectedAccountPrice](API_ConnectedAccountPrice.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

## See Also
<a name="API_ConnectedAccountChainConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ConnectedAccountChainConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ConnectedAccountChainConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ConnectedAccountChainConfig)
