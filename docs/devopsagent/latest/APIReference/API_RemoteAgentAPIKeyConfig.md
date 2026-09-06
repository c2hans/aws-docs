---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RemoteAgentAPIKeyConfig.html
---

# RemoteAgentAPIKeyConfig
<a name="API_RemoteAgentAPIKeyConfig"></a>

API key configuration for remote A2A agent.

## Contents
<a name="API_RemoteAgentAPIKeyConfig_Contents"></a>

 ** apiKeyHeader **   <a name="devopsagent-Type-RemoteAgentAPIKeyConfig-apiKeyHeader"></a>
HTTP header name to send the API key in requests to the service.
Type: String
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

 ** apiKeyName **   <a name="devopsagent-Type-RemoteAgentAPIKeyConfig-apiKeyName"></a>
User friendly API key name specified by end user.
Type: String
Pattern: `[a-zA-Z0-9_\s-]+`
Required: Yes

 ** apiKeyValue **   <a name="devopsagent-Type-RemoteAgentAPIKeyConfig-apiKeyValue"></a>
API key value for authenticating with the service.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[!-~]([ \t]*[!-~])*`
Required: Yes

## See Also
<a name="API_RemoteAgentAPIKeyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/RemoteAgentAPIKeyConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/RemoteAgentAPIKeyConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/RemoteAgentAPIKeyConfig)
