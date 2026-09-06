---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RemoteAgentSigV4ServiceDetails.html
---

# RemoteAgentSigV4ServiceDetails
<a name="API_RemoteAgentSigV4ServiceDetails"></a>

Complete service details for SigV4-authenticated remote A2A agent integration.

## Contents
<a name="API_RemoteAgentSigV4ServiceDetails_Contents"></a>

 ** authorizationConfig **   <a name="devopsagent-Type-RemoteAgentSigV4ServiceDetails-authorizationConfig"></a>
Remote agent SigV4 authorization configuration.
Type: [RemoteAgentSigV4AuthorizationConfig](API_RemoteAgentSigV4AuthorizationConfig.md) object
Required: Yes

 ** endpoint **   <a name="devopsagent-Type-RemoteAgentSigV4ServiceDetails-endpoint"></a>
HTTPS endpoint URL for a remote A2A agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?`
Required: Yes

 ** name **   <a name="devopsagent-Type-RemoteAgentSigV4ServiceDetails-name"></a>
Name identifier for a remote A2A agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** description **   <a name="devopsagent-Type-RemoteAgentSigV4ServiceDetails-description"></a>
Description field
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\p{L}\p{N}\p{P}\p{S}\p{Z}]+`
Required: No

## See Also
<a name="API_RemoteAgentSigV4ServiceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/RemoteAgentSigV4ServiceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/RemoteAgentSigV4ServiceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/RemoteAgentSigV4ServiceDetails)
