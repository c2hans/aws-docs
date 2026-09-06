---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RemoteAgentSigV4AuthorizationConfig.html
---

# RemoteAgentSigV4AuthorizationConfig
<a name="API_RemoteAgentSigV4AuthorizationConfig"></a>

SigV4 authorization configuration for remote A2A agent.

## Contents
<a name="API_RemoteAgentSigV4AuthorizationConfig_Contents"></a>

 ** region **   <a name="devopsagent-Type-RemoteAgentSigV4AuthorizationConfig-region"></a>
AWS region identifier or wildcard (\*) for SigV4a multi-region signing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `(\*|[a-z]{2,4}(-[a-z]+)+-\d+)`
Required: Yes

 ** service **   <a name="devopsagent-Type-RemoteAgentSigV4AuthorizationConfig-service"></a>
The AWS service name for SigV4 signing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** roleArn **   <a name="devopsagent-Type-RemoteAgentSigV4AuthorizationConfig-roleArn"></a>
AWS IAM role ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: No

## See Also
<a name="API_RemoteAgentSigV4AuthorizationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/RemoteAgentSigV4AuthorizationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/RemoteAgentSigV4AuthorizationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/RemoteAgentSigV4AuthorizationConfig)
