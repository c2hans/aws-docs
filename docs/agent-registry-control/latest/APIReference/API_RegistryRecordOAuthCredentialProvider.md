---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_RegistryRecordOAuthCredentialProvider.html
---

# RegistryRecordOAuthCredentialProvider

The configuration for an OAuth 2.0 credential provider that authenticates requests to a registry record's source.

## Contents
<a name="API_RegistryRecordOAuthCredentialProvider_Contents"></a>

 ** providerArn **   <a name="agentregistrycontrol-Type-RegistryRecordOAuthCredentialProvider-providerArn"></a>
The Amazon Resource Name (ARN) of the OAuth 2.0 credential provider resource in Amazon Bedrock AgentCore Identity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:.*`
Required: Yes

 ** customParameters **   <a name="agentregistrycontrol-Type-RegistryRecordOAuthCredentialProvider-customParameters"></a>
Additional parameters to include in the OAuth 2.0 token request.
Type: String to string map
Required: No

 ** grantType **   <a name="agentregistrycontrol-Type-RegistryRecordOAuthCredentialProvider-grantType"></a>
The OAuth 2.0 grant type used to obtain access tokens. A GitHub skill source requires `AUTHORIZATION_CODE`. Other sources, such as MCP server and A2A agent card sources, use `CLIENT_CREDENTIALS`. A GitHub source takes exactly one OAuth credential provider, in the registry's AWS account and Region. Only an IAM role or IAM user in the account that owns the registry can set, synchronize, or reauthorize it, and the caller needs `bedrock-agentcore:GetWorkloadAccessTokenForUserId` and `bedrock-agentcore:GetResourceOauth2Token` on the registry's workload identity, `registry-` followed by the registry ID.
Type: String
Valid Values: `CLIENT_CREDENTIALS | AUTHORIZATION_CODE`
Required: No

 ** returnUrl **   <a name="agentregistrycontrol-Type-RegistryRecordOAuthCredentialProvider-returnUrl"></a>
The URL that the user's browser returns to after the user approves access on GitHub, for the `AUTHORIZATION_CODE` grant. There, your application completes the authorization by calling the Amazon Bedrock AgentCore Identity `CompleteResourceTokenAuth` operation with the `userId` from `authorizationData`. If you omit it, the user returns to the AWS Agent Registry console, which completes the authorization when the user is signed in as the IAM principal that made the request. A request that joins an authorization already in progress uses the return URL of the request that started it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\w+:(\/?\/?)[^\s]+`
Required: No

 ** scopes **   <a name="agentregistrycontrol-Type-RegistryRecordOAuthCredentialProvider-scopes"></a>
The OAuth 2.0 scopes to request when obtaining access tokens.
Type: Array of strings
Required: No

## See Also
<a name="API_RegistryRecordOAuthCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryRecordOAuthCredentialProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryRecordOAuthCredentialProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryRecordOAuthCredentialProvider)
