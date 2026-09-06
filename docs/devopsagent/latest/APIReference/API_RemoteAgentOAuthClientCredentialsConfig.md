---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RemoteAgentOAuthClientCredentialsConfig.html
---

# RemoteAgentOAuthClientCredentialsConfig
<a name="API_RemoteAgentOAuthClientCredentialsConfig"></a>

OAuth client credentials configuration for remote A2A agent.

## Contents
<a name="API_RemoteAgentOAuthClientCredentialsConfig_Contents"></a>

 ** clientId **   <a name="devopsagent-Type-RemoteAgentOAuthClientCredentialsConfig-clientId"></a>
OAuth client ID for authenticating with the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\u007E]+`
Required: Yes

 ** clientSecret **   <a name="devopsagent-Type-RemoteAgentOAuthClientCredentialsConfig-clientSecret"></a>
OAuth client secret for authenticating with the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\S]+`
Required: Yes

 ** exchangeUrl **   <a name="devopsagent-Type-RemoteAgentOAuthClientCredentialsConfig-exchangeUrl"></a>
OAuth token exchange URL.
Type: String
Pattern: `https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?`
Required: Yes

 ** clientName **   <a name="devopsagent-Type-RemoteAgentOAuthClientCredentialsConfig-clientName"></a>
User friendly OAuth client name specified by end user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\p{L}\p{N}\p{Z}._-]+`
Required: No

 ** exchangeParameters **   <a name="devopsagent-Type-RemoteAgentOAuthClientCredentialsConfig-exchangeParameters"></a>
OAuth token exchange parameters for authenticating with the service.
Type: String to string map
Required: No

 ** scopes **   <a name="devopsagent-Type-RemoteAgentOAuthClientCredentialsConfig-scopes"></a>
OAuth scopes for authentication.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[!#-\[\]-~]+`
Required: No

## See Also
<a name="API_RemoteAgentOAuthClientCredentialsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/RemoteAgentOAuthClientCredentialsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/RemoteAgentOAuthClientCredentialsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/RemoteAgentOAuthClientCredentialsConfig)
