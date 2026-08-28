---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RegisteredRemoteAgentSigV4Details.html
---

# RegisteredRemoteAgentSigV4Details
<a name="API_RegisteredRemoteAgentSigV4Details"></a>

Details specific to a registered SigV4-authenticated remote A2A agent.

## Contents
<a name="API_RegisteredRemoteAgentSigV4Details_Contents"></a>

 ** endpoint **   <a name="devopsagent-Type-RegisteredRemoteAgentSigV4Details-endpoint"></a>
HTTPS endpoint URL for a remote A2A agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?`
Required: Yes

 ** name **   <a name="devopsagent-Type-RegisteredRemoteAgentSigV4Details-name"></a>
Name identifier for a remote A2A agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** region **   <a name="devopsagent-Type-RegisteredRemoteAgentSigV4Details-region"></a>
AWS region identifier or wildcard (\*) for SigV4a multi-region signing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `(\*|[a-z]{2,4}(-[a-z]+)+-\d+)`
Required: Yes

 ** service **   <a name="devopsagent-Type-RegisteredRemoteAgentSigV4Details-service"></a>
The AWS service name for SigV4 signing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** description **   <a name="devopsagent-Type-RegisteredRemoteAgentSigV4Details-description"></a>
Description field
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\p{L}\p{N}\p{P}\p{S}\p{Z}]+`
Required: No

 ** roleArn **   <a name="devopsagent-Type-RegisteredRemoteAgentSigV4Details-roleArn"></a>
AWS IAM role ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: No

## See Also
<a name="API_RegisteredRemoteAgentSigV4Details_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/RegisteredRemoteAgentSigV4Details)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/RegisteredRemoteAgentSigV4Details)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/RegisteredRemoteAgentSigV4Details)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
