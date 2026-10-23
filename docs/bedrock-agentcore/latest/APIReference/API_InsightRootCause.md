---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InsightRootCause.html
---

# InsightRootCause
<a name="API_InsightRootCause"></a>

A root cause that contributes to an insight.

## Contents
<a name="API_InsightRootCause_Contents"></a>

 ** explanation **   <a name="BedrockAgentCore-Type-InsightRootCause-explanation"></a>
An explanation of how the root cause leads to the failures in the insight.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-InsightRootCause-name"></a>
A generated label for the root cause.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** affectedSessionCount **   <a name="BedrockAgentCore-Type-InsightRootCause-affectedSessionCount"></a>
The number of distinct sessions affected by the root cause. A session can be affected by more than one root cause of the same insight.
Type: Integer
Required: No

 ** sampleSessions **   <a name="BedrockAgentCore-Type-InsightRootCause-sampleSessions"></a>
A sample of up to 10 sessions affected by the root cause.
Type: Array of [SampleSession](API_SampleSession.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** suggestedFix **   <a name="BedrockAgentCore-Type-InsightRootCause-suggestedFix"></a>
A suggested change to the agent that addresses the root cause.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.
Required: No

## See Also
<a name="API_InsightRootCause_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InsightRootCause)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InsightRootCause)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InsightRootCause)
