---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RemoteAgentBearerTokenConfig.html
---

# RemoteAgentBearerTokenConfig
<a name="API_RemoteAgentBearerTokenConfig"></a>

Bearer token configuration for remote A2A agent (RFC 6750).

## Contents
<a name="API_RemoteAgentBearerTokenConfig_Contents"></a>

 ** tokenName **   <a name="devopsagent-Type-RemoteAgentBearerTokenConfig-tokenName"></a>
User friendly bearer token name specified by end user.
Type: String
Pattern: `[a-zA-Z0-9_\s-]+`
Required: Yes

 ** tokenValue **   <a name="devopsagent-Type-RemoteAgentBearerTokenConfig-tokenValue"></a>
Bearer token value in alphanumeric for authenticating with the service.
Type: String
Pattern: `[\S]+`
Required: Yes

 ** authorizationHeader **   <a name="devopsagent-Type-RemoteAgentBearerTokenConfig-authorizationHeader"></a>
HTTP header name to send the bearer token in requests to the service. Defaults to 'Authorization' per RFC 6750.
Type: String
Pattern: `[a-zA-Z0-9-]+`
Required: No

## See Also
<a name="API_RemoteAgentBearerTokenConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/RemoteAgentBearerTokenConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/RemoteAgentBearerTokenConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/RemoteAgentBearerTokenConfig)
