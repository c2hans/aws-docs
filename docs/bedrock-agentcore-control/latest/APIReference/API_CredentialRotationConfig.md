---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CredentialRotationConfig.html
---

# CredentialRotationConfig
<a name="API_CredentialRotationConfig"></a>

Specifies the service-managed credentials to rotate. Provide the member that matches the payment connector's `type`.

## Contents
<a name="API_CredentialRotationConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** coinbaseCDP **   <a name="bedrockagentcorecontrol-Type-CredentialRotationConfig-coinbaseCDP"></a>
The credentials to rotate for a Coinbase CDP payment connector.
Type: [CoinbaseCdpRotationTargets](API_CoinbaseCdpRotationTargets.md) object
Required: No

## See Also
<a name="API_CredentialRotationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CredentialRotationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CredentialRotationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CredentialRotationConfig)
