---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_MCPServerSigV4AuthorizationConfig.html
---

# MCPServerSigV4AuthorizationConfig
<a name="API_MCPServerSigV4AuthorizationConfig"></a>

Authorization configuration for SigV4-authenticated MCP server.

## Contents
<a name="API_MCPServerSigV4AuthorizationConfig_Contents"></a>

 ** region **   <a name="devopsagent-Type-MCPServerSigV4AuthorizationConfig-region"></a>
AWS region for SigV4 signing. Use '\*' for SigV4a multi-region signing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `(\*|[a-z]{2,4}(-[a-z]+)+-\d+)`
Required: Yes

 ** service **   <a name="devopsagent-Type-MCPServerSigV4AuthorizationConfig-service"></a>
AWS service name for SigV4 signing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** customHeaders **   <a name="devopsagent-Type-MCPServerSigV4AuthorizationConfig-customHeaders"></a>
Custom headers for the SigV4 MCP server.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z0-9-_]+`
Value Length Constraints: Minimum length of 1. Maximum length of 4096.
Value Pattern: `[!-~]([ \t]*[!-~])*`
Required: No

 ** mcpRoleArn **   <a name="devopsagent-Type-MCPServerSigV4AuthorizationConfig-mcpRoleArn"></a>
IAM role ARN to assume for SigV4 signing. Optional — when omitted, credentials are resolved at runtime via a monitor account association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: No

 ** roleArn **   <a name="devopsagent-Type-MCPServerSigV4AuthorizationConfig-roleArn"></a>
Deprecated — use mcpRoleArn instead. IAM role ARN to assume for SigV4 signing.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_MCPServerSigV4AuthorizationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/MCPServerSigV4AuthorizationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/MCPServerSigV4AuthorizationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/MCPServerSigV4AuthorizationConfig)
