---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_SendMessageContentBlockStartEvent.html
---

# SendMessageContentBlockStartEvent
<a name="API_SendMessageContentBlockStartEvent"></a>

Event emitted when a new content block starts

## Contents
<a name="API_SendMessageContentBlockStartEvent_Contents"></a>

 ** id **   <a name="devopsagent-Type-SendMessageContentBlockStartEvent-id"></a>
Block identifier
Type: String
Required: No

 ** index **   <a name="devopsagent-Type-SendMessageContentBlockStartEvent-index"></a>
Zero-based index of the content block
Type: Integer
Required: No

 ** parentId **   <a name="devopsagent-Type-SendMessageContentBlockStartEvent-parentId"></a>
Optional parent block ID for nested content blocks (e.g. subagent tool calls)
Type: String
Required: No

 ** sequenceNumber **   <a name="devopsagent-Type-SendMessageContentBlockStartEvent-sequenceNumber"></a>
Event sequence number
Type: Integer
Required: No

 ** type **   <a name="devopsagent-Type-SendMessageContentBlockStartEvent-type"></a>
The type of content in this block
Type: String
Required: No

## See Also
<a name="API_SendMessageContentBlockStartEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/SendMessageContentBlockStartEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/SendMessageContentBlockStartEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/SendMessageContentBlockStartEvent)
