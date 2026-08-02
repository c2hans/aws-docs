---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RegisteredRemoteAgentDetails.html
---

# RegisteredRemoteAgentDetails
<a name="API_RegisteredRemoteAgentDetails"></a>

Details specific to a registered token-based remote A2A agent.

## Contents
<a name="API_RegisteredRemoteAgentDetails_Contents"></a>

 ** authorizationMethod **   <a name="devopsagent-Type-RegisteredRemoteAgentDetails-authorizationMethod"></a>
The authorization method used by the remote agent.
Type: String
Valid Values: `oauth-client-credentials | api-key | bearer-token`
Required: Yes

 ** endpoint **   <a name="devopsagent-Type-RegisteredRemoteAgentDetails-endpoint"></a>
HTTPS endpoint URL for a remote A2A agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?`
Required: Yes

 ** name **   <a name="devopsagent-Type-RegisteredRemoteAgentDetails-name"></a>
Name identifier for a remote A2A agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** apiKeyHeader **   <a name="devopsagent-Type-RegisteredRemoteAgentDetails-apiKeyHeader"></a>
If the remote agent uses API key authentication, the header name.
Type: String
Required: No

 ** description **   <a name="devopsagent-Type-RegisteredRemoteAgentDetails-description"></a>
Description field
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\p{L}\p{N}\p{P}\p{S}\p{Z}]+`
Required: No

## See Also
<a name="API_RegisteredRemoteAgentDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/RegisteredRemoteAgentDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/RegisteredRemoteAgentDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/RegisteredRemoteAgentDetails)
