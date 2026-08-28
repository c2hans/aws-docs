---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_MicrosoftOauth2ProviderConfigOutput.html
---

# MicrosoftOauth2ProviderConfigOutput
<a name="API_MicrosoftOauth2ProviderConfigOutput"></a>

Output configuration for a Microsoft OAuth2 provider.

## Contents
<a name="API_MicrosoftOauth2ProviderConfigOutput_Contents"></a>

 ** oauthDiscovery **   <a name="bedrockagentcorecontrol-Type-MicrosoftOauth2ProviderConfigOutput-oauthDiscovery"></a>
The OAuth2 discovery information for the Microsoft provider.
Type: [Oauth2Discovery](API_Oauth2Discovery.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** clientId **   <a name="bedrockagentcorecontrol-Type-MicrosoftOauth2ProviderConfigOutput-clientId"></a>
The client ID for the Microsoft OAuth2 provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_MicrosoftOauth2ProviderConfigOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/MicrosoftOauth2ProviderConfigOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/MicrosoftOauth2ProviderConfigOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/MicrosoftOauth2ProviderConfigOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
