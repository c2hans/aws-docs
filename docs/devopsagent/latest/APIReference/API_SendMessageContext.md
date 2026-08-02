---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_SendMessageContext.html
---

# SendMessageContext
<a name="API_SendMessageContext"></a>

Context object for additional message metadata

## Contents
<a name="API_SendMessageContext_Contents"></a>

 ** currentPage **   <a name="devopsagent-Type-SendMessageContext-currentPage"></a>
The current page or view the user is on
Type: String
Required: No

 ** lastMessage **   <a name="devopsagent-Type-SendMessageContext-lastMessage"></a>
The ID of the last message in the conversation
Type: String
Required: No

 ** userActionResponse **   <a name="devopsagent-Type-SendMessageContext-userActionResponse"></a>
Response to a UI prompt (not a text conversation message). Operator App SDK clients set this to the control-string sentinel `"APPROVAL\_ACTION"` when the request is resuming a paused tool call after an operator approval decision; in that case the structured decision context lives on the sibling `approvalAction` member and the chat agent reads from there. Preserved as a String for back-compat: pre-typed-approval clients still encode arbitrary UI-prompt responses as JSON in this field, and the chat agent parses them out during the transition.
Type: String
Required: No

## See Also
<a name="API_SendMessageContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/SendMessageContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/SendMessageContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/SendMessageContext)
