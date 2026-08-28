---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_SessionStorageConfiguration.html
---

# SessionStorageConfiguration
<a name="API_SessionStorageConfiguration"></a>

Configuration for a session storage filesystem mounted into the AgentCore Runtime. Session storage provides persistent storage that is preserved across AgentCore Runtime session invocations.

## Contents
<a name="API_SessionStorageConfiguration_Contents"></a>

 ** mountPath **   <a name="bedrockagentcorecontrol-Type-SessionStorageConfiguration-mountPath"></a>
The mount path for the session storage filesystem inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data`).
Type: String
Length Constraints: Minimum length of 6. Maximum length of 200.
Pattern: `/mnt/[a-zA-Z0-9._-]+/?`
Required: Yes

## See Also
<a name="API_SessionStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/SessionStorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/SessionStorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/SessionStorageConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
