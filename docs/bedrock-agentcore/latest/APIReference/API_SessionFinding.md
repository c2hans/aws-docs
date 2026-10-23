---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SessionFinding.html
---

# SessionFinding
<a name="API_SessionFinding"></a>

A failure found in a session.

## Contents
<a name="API_SessionFinding_Contents"></a>

 ** description **   <a name="BedrockAgentCore-Type-SessionFinding-description"></a>
A description of the failure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** category **   <a name="BedrockAgentCore-Type-SessionFinding-category"></a>
The category of the failure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** confidence **   <a name="BedrockAgentCore-Type-SessionFinding-confidence"></a>
The confidence that the finding is a failure, from 0 to 1.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** targetId **   <a name="BedrockAgentCore-Type-SessionFinding-targetId"></a>
The identifier or name of the location in the session where the failure was found, interpreted according to `targetType`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** targetType **   <a name="BedrockAgentCore-Type-SessionFinding-targetType"></a>
The type of location that `targetId` refers to.
Type: String
Valid Values: `SPAN_ID | TRACE_ID | SPAN_NAME`
Required: No

## See Also
<a name="API_SessionFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SessionFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SessionFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SessionFinding)
