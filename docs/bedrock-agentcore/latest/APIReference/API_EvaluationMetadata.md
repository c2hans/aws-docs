---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_EvaluationMetadata.html
---

# EvaluationMetadata
<a name="API_EvaluationMetadata"></a>

Metadata for the evaluation, including session-specific ground truth data.

## Contents
<a name="API_EvaluationMetadata_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** sessionMetadata **   <a name="BedrockAgentCore-Type-EvaluationMetadata-sessionMetadata"></a>
A list of session metadata entries containing ground truth data and test scenario identifiers for specific sessions.
Type: Array of [SessionMetadataShape](API_SessionMetadataShape.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Required: No

## See Also
<a name="API_EvaluationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluationMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluationMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluationMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
