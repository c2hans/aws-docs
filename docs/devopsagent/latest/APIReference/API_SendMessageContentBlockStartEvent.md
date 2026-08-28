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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
