---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_OnBehalfOfAuthenticationConfig.html
---

# OnBehalfOfAuthenticationConfig
<a name="API_OnBehalfOfAuthenticationConfig"></a>

Specifies the client authentication method to use for the on-behalf-of token exchange.

## Contents
<a name="API_OnBehalfOfAuthenticationConfig_Contents"></a>

 ** clientAuthenticationMethod **   <a name="bedrockagentcorecontrol-Type-OnBehalfOfAuthenticationConfig-clientAuthenticationMethod"></a>
The client authentication method to use during the on-behalf-of token exchange. The `NO_CLIENT` option omits the `clientId` and `clientSecret` during the on-behalf-of token exchange with the identity provider.
Type: String
Valid Values: `NO_CLIENT`
Required: Yes

## See Also
<a name="API_OnBehalfOfAuthenticationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/OnBehalfOfAuthenticationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/OnBehalfOfAuthenticationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/OnBehalfOfAuthenticationConfig)
