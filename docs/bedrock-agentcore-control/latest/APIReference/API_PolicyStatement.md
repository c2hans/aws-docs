---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_PolicyStatement.html
---

# PolicyStatement
<a name="API_PolicyStatement"></a>

An AgentCore policy statement, which supports plain Cedar policies as well as guardrails definitions.

## Contents
<a name="API_PolicyStatement_Contents"></a>

 ** statement **   <a name="bedrockagentcorecontrol-Type-PolicyStatement-statement"></a>
The body of the AgentCore policy statement. Contains the policy logic, which can be a Cedar policy or a guardrails definition.
Type: String
Length Constraints: Minimum length of 35. Maximum length of 10000.
Required: Yes

## See Also
<a name="API_PolicyStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PolicyStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PolicyStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PolicyStatement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
