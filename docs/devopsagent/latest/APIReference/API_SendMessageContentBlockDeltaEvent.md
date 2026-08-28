---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_SendMessageContentBlockDeltaEvent.html
---

# SendMessageContentBlockDeltaEvent
<a name="API_SendMessageContentBlockDeltaEvent"></a>

Event emitted for each incremental content delta within a content block

## Contents
<a name="API_SendMessageContentBlockDeltaEvent_Contents"></a>

 ** delta **   <a name="devopsagent-Type-SendMessageContentBlockDeltaEvent-delta"></a>
The incremental content delta
Type: [SendMessageContentBlockDelta](API_SendMessageContentBlockDelta.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** index **   <a name="devopsagent-Type-SendMessageContentBlockDeltaEvent-index"></a>
Zero-based index of the content block
Type: Integer
Required: No

 ** sequenceNumber **   <a name="devopsagent-Type-SendMessageContentBlockDeltaEvent-sequenceNumber"></a>
Event sequence number
Type: Integer
Required: No

## See Also
<a name="API_SendMessageContentBlockDeltaEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/SendMessageContentBlockDeltaEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/SendMessageContentBlockDeltaEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/SendMessageContentBlockDeltaEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
