---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_HarnessHookEvent.html
---

# HarnessHookEvent
<a name="API_HarnessHookEvent"></a>

A lifecycle hook event emitted in the invocation stream for visibility into hook decisions.

## Contents
<a name="API_HarnessHookEvent_Contents"></a>

 ** hookEventId **   <a name="BedrockAgentCore-Type-HarnessHookEvent-hookEventId"></a>
The unique identifier for this hook event.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-HarnessHookEvent-name"></a>
The name of the hook that ran.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** type **   <a name="BedrockAgentCore-Type-HarnessHookEvent-type"></a>
The type of lifecycle hook event.
Type: String
Valid Values: `before_tool_call | after_tool_call | before_invocation | after_invocation`
Required: Yes

 ** decision **   <a name="BedrockAgentCore-Type-HarnessHookEvent-decision"></a>
The decision applied to the hook event. This field is present only for blocking Lambda targets.
Type: String
Valid Values: `allow | deny`
Required: No

 ** reason **   <a name="BedrockAgentCore-Type-HarnessHookEvent-reason"></a>
The optional reason for the applied decision.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_HarnessHookEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessHookEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessHookEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessHookEvent)
