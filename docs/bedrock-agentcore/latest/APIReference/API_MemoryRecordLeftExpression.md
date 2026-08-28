---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_MemoryRecordLeftExpression.html
---

# MemoryRecordLeftExpression
<a name="API_MemoryRecordLeftExpression"></a>

The left-hand side of a memory record metadata filter expression.

## Contents
<a name="API_MemoryRecordLeftExpression_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** metadataKey **   <a name="BedrockAgentCore-Type-MemoryRecordLeftExpression-metadataKey"></a>
The metadata key to filter on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`
Required: No

## See Also
<a name="API_MemoryRecordLeftExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryRecordLeftExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryRecordLeftExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryRecordLeftExpression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
