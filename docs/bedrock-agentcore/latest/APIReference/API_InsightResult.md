---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InsightResult.html
---

# InsightResult
<a name="API_InsightResult"></a>

An insight that groups related failures found across the sessions in a batch evaluation.

## Contents
<a name="API_InsightResult_Contents"></a>

 ** createdAt **   <a name="BedrockAgentCore-Type-InsightResult-createdAt"></a>
The timestamp when the insight was generated.
Type: Timestamp
Required: Yes

 ** description **   <a name="BedrockAgentCore-Type-InsightResult-description"></a>
A description of the failure pattern that the insight represents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-InsightResult-name"></a>
A generated label for the insight. The name is not an identifier and can differ between batch evaluations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** type **   <a name="BedrockAgentCore-Type-InsightResult-type"></a>
The type of insight. `FAILURE` indicates a group of related failures.
Type: String
Valid Values: `FAILURE`
Required: Yes

 ** affectedSessionCount **   <a name="BedrockAgentCore-Type-InsightResult-affectedSessionCount"></a>
The number of distinct sessions affected by the insight.
Type: Integer
Required: No

 ** rootCauses **   <a name="BedrockAgentCore-Type-InsightResult-rootCauses"></a>
The root causes identified for the insight.
Type: Array of [InsightRootCause](API_InsightRootCause.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** sampleSessions **   <a name="BedrockAgentCore-Type-InsightResult-sampleSessions"></a>
A sample of up to 10 sessions affected by the insight. Returned only when the insight has no root causes. Otherwise, sample sessions are returned for each root cause.
Type: Array of [SampleSession](API_SampleSession.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_InsightResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InsightResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InsightResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InsightResult)
