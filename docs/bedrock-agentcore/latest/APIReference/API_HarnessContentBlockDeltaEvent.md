---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_HarnessContentBlockDeltaEvent.html
---

# HarnessContentBlockDeltaEvent
<a name="API_HarnessContentBlockDeltaEvent"></a>

Event containing a delta update to a content block.

## Contents
<a name="API_HarnessContentBlockDeltaEvent_Contents"></a>

 ** contentBlockIndex **   <a name="BedrockAgentCore-Type-HarnessContentBlockDeltaEvent-contentBlockIndex"></a>
The index of the content block being updated.
Type: Integer
Required: Yes

 ** delta **   <a name="BedrockAgentCore-Type-HarnessContentBlockDeltaEvent-delta"></a>
The delta payload.
Type: [HarnessContentBlockDelta](API_HarnessContentBlockDelta.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_HarnessContentBlockDeltaEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessContentBlockDeltaEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessContentBlockDeltaEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessContentBlockDeltaEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
