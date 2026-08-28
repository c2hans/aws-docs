---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RegisteredMCPServerSigV4Details.html
---

# RegisteredMCPServerSigV4Details
<a name="API_RegisteredMCPServerSigV4Details"></a>

Details specific to a registered SigV4-authenticated MCP server.

## Contents
<a name="API_RegisteredMCPServerSigV4Details_Contents"></a>

 ** endpoint **   <a name="devopsagent-Type-RegisteredMCPServerSigV4Details-endpoint"></a>
MCP server endpoint URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?`
Required: Yes

 ** name **   <a name="devopsagent-Type-RegisteredMCPServerSigV4Details-name"></a>
MCP server name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** region **   <a name="devopsagent-Type-RegisteredMCPServerSigV4Details-region"></a>
AWS region for SigV4 signing. Use '\*' for SigV4a multi-region signing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `(\*|[a-z]{2,4}(-[a-z]+)+-\d+)`
Required: Yes

 ** roleArn **   <a name="devopsagent-Type-RegisteredMCPServerSigV4Details-roleArn"></a>
 *This member has been deprecated.*
IAM role ARN to assume for SigV4 signing.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: Yes

 ** service **   <a name="devopsagent-Type-RegisteredMCPServerSigV4Details-service"></a>
AWS service name for SigV4 signing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** customHeaders **   <a name="devopsagent-Type-RegisteredMCPServerSigV4Details-customHeaders"></a>
Custom headers for the SigV4 MCP server.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z0-9-_]+`
Value Length Constraints: Minimum length of 1. Maximum length of 4096.
Value Pattern: `[!-~]([ \t]*[!-~])*`
Required: No

 ** description **   <a name="devopsagent-Type-RegisteredMCPServerSigV4Details-description"></a>
Optional description for the MCP server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\p{L}\p{N}\p{P}\p{S}\p{Z}]+`
Required: No

 ** mcpRoleArn **   <a name="devopsagent-Type-RegisteredMCPServerSigV4Details-mcpRoleArn"></a>
AWS IAM role ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: No

## See Also
<a name="API_RegisteredMCPServerSigV4Details_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/RegisteredMCPServerSigV4Details)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/RegisteredMCPServerSigV4Details)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/RegisteredMCPServerSigV4Details)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
