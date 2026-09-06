---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_SendMessageContext.html
---

# SendMessageContext
<a name="API_SendMessageContext"></a>

Context object for additional message metadata

## Contents
<a name="API_SendMessageContext_Contents"></a>

 ** approvalAction **   <a name="devopsagent-Type-SendMessageContext-approvalAction"></a>
An approval decision supplied when resuming a paused agent execution. When an agent execution pauses to request approval for an elevated action, SendMessage streams an approval request carrying interrupt identifiers. To resume the paused execution, call SendMessage again with `userActionResponse` set to `"APPROVAL\_ACTION"` and this member populated with those identifiers and the decision (APPROVED or REJECTED). Optional; omit it for messages that are not resuming an approval.
Type: [ApprovalAction](API_ApprovalAction.md) object
Required: No

 ** currentPage **   <a name="devopsagent-Type-SendMessageContext-currentPage"></a>
The current page or view the user is on
Type: String
Required: No

 ** lastMessage **   <a name="devopsagent-Type-SendMessageContext-lastMessage"></a>
The ID of the last message in the conversation
Type: String
Required: No

 ** userActionResponse **   <a name="devopsagent-Type-SendMessageContext-userActionResponse"></a>
Response to a UI prompt (not a text conversation message). Set this to the sentinel value `"APPROVAL\_ACTION"` when the request is resuming a paused execution after an approval decision; in that case the structured decision is provided on the sibling `approvalAction` member. Preserved as a String for backward compatibility: clients that predate the typed approval field may still encode UI-prompt responses as JSON in this field.
Type: String
Required: No

## See Also
<a name="API_SendMessageContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/SendMessageContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/SendMessageContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/SendMessageContext)
