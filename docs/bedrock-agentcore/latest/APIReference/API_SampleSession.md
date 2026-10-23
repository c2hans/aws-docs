---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SampleSession.html
---

# SampleSession
<a name="API_SampleSession"></a>

A session affected by an insight or root cause. Use the session ID to find the per-session evaluation results in CloudWatch Logs.

## Contents
<a name="API_SampleSession_Contents"></a>

 ** sessionId **   <a name="BedrockAgentCore-Type-SampleSession-sessionId"></a>
The unique identifier of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: Yes

 ** findings **   <a name="BedrockAgentCore-Type-SampleSession-findings"></a>
The failures found in the session that belong to the insight or root cause, up to 10.
Type: Array of [SessionFinding](API_SessionFinding.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** lastSeenAt **   <a name="BedrockAgentCore-Type-SampleSession-lastSeenAt"></a>
The latest timestamp observed for the session in the batch evaluation input.
Type: Timestamp
Required: No

## See Also
<a name="API_SampleSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SampleSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SampleSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SampleSession)
