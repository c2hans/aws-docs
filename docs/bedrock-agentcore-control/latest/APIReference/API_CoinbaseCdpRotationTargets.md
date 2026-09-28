---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CoinbaseCdpRotationTargets.html
---

# CoinbaseCdpRotationTargets
<a name="API_CoinbaseCdpRotationTargets"></a>

Specifies the service-managed Coinbase CDP secrets to rotate.

## Contents
<a name="API_CoinbaseCdpRotationTargets_Contents"></a>

 ** secrets **   <a name="bedrockagentcorecontrol-Type-CoinbaseCdpRotationTargets-secrets"></a>
The secrets to rotate. Specify at least one value. Each secret that you specify is rotated independently.
+  `API_KEY` - The API key that the payment connector uses to call Coinbase CDP. Rotate it as routine maintenance, or if you suspect that it is compromised.
+  `WALLET_SECRET` - The wallet secret that signs transactions. Rotate it only if it is lost or compromised. Coinbase CDP allows one wallet secret per project, so it is replaced in place and signing can be briefly interrupted.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `API_KEY | WALLET_SECRET`
Required: Yes

## See Also
<a name="API_CoinbaseCdpRotationTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CoinbaseCdpRotationTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CoinbaseCdpRotationTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CoinbaseCdpRotationTargets)
