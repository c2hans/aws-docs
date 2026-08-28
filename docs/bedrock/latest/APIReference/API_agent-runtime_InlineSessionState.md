---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InlineSessionState.html
---

# InlineSessionState
<a name="API_agent-runtime_InlineSessionState"></a>

 Contains parameters that specify various attributes that persist across a session or prompt. You can define session state attributes as key-value pairs when writing a [Lambda function](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html) for an action group or pass them when making an `InvokeInlineAgent` request. Use session state attributes to control and provide conversational context for your inline agent and to help customize your agent's behavior. For more information, see [Control session context](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html)

## Contents
<a name="API_agent-runtime_InlineSessionState_Contents"></a>

 ** conversationHistory **   <a name="bedrock-Type-agent-runtime_InlineSessionState-conversationHistory"></a>
 Contains the conversation history that persist across sessions.
Type: [ConversationHistory](API_agent-runtime_ConversationHistory.md) object
Required: No

 ** files **   <a name="bedrock-Type-agent-runtime_InlineSessionState-files"></a>
 Contains information about the files used by code interpreter.
Type: Array of [InputFile](API_agent-runtime_InputFile.md) objects
Required: No

 ** invocationId **   <a name="bedrock-Type-agent-runtime_InlineSessionState-invocationId"></a>
 The identifier of the invocation of an action. This value must match the `invocationId` returned in the `InvokeInlineAgent` response for the action whose results are provided in the `returnControlInvocationResults` field. For more information, see [Return control to the agent developer](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-returncontrol.html).
Type: String
Required: No

 ** promptSessionAttributes **   <a name="bedrock-Type-agent-runtime_InlineSessionState-promptSessionAttributes"></a>
 Contains attributes that persist across a session and the values of those attributes.
Type: String to string map
Required: No

 ** returnControlInvocationResults **   <a name="bedrock-Type-agent-runtime_InlineSessionState-returnControlInvocationResults"></a>
 Contains information about the results from the action group invocation. For more information, see [Return control to the agent developer](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-returncontrol.html).
If you include this field in the `sessionState` field, the `inputText` field will be ignored.
Type: Array of [InvocationResultMember](API_agent-runtime_InvocationResultMember.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** sessionAttributes **   <a name="bedrock-Type-agent-runtime_InlineSessionState-sessionAttributes"></a>
 Contains attributes that persist across a session and the values of those attributes.
Type: String to string map
Required: No

## See Also
<a name="API_agent-runtime_InlineSessionState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/InlineSessionState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/InlineSessionState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/InlineSessionState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
