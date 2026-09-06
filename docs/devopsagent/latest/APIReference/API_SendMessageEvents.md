---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_SendMessageEvents.html
---

# SendMessageEvents
<a name="API_SendMessageEvents"></a>

Event stream for chat message responses using the content block model. Events follow a lifecycle: responseCreated -> responseInProgress -> (contentBlockStart/contentBlockDelta/contentBlockStop events) -> responseCompleted\|responseFailed SendMessage always uses content block mode — legacy per-field events (outputTextDelta, functionCallArgumentsDelta, etc.) are not emitted.

## Contents
<a name="API_SendMessageEvents_Contents"></a>

 ** contentBlockDelta **   <a name="devopsagent-Type-SendMessageEvents-contentBlockDelta"></a>
Emitted for each incremental content delta within a content block
Type: [SendMessageContentBlockDeltaEvent](API_SendMessageContentBlockDeltaEvent.md) object
Required: No

 ** contentBlockStart **   <a name="devopsagent-Type-SendMessageEvents-contentBlockStart"></a>
Emitted when a new content block starts
Type: [SendMessageContentBlockStartEvent](API_SendMessageContentBlockStartEvent.md) object
Required: No

 ** contentBlockStop **   <a name="devopsagent-Type-SendMessageEvents-contentBlockStop"></a>
Emitted when a content block is complete
Type: [SendMessageContentBlockStopEvent](API_SendMessageContentBlockStopEvent.md) object
Required: No

 ** heartbeat **   <a name="devopsagent-Type-SendMessageEvents-heartbeat"></a>
Heartbeat event sent periodically to keep the connection alive during idle periods
Type: [SendMessageHeartbeatEvent](API_SendMessageHeartbeatEvent.md) object
Required: No

 ** responseCompleted **   <a name="devopsagent-Type-SendMessageEvents-responseCompleted"></a>
Emitted when the response completes successfully
Type: [SendMessageResponseCompletedEvent](API_SendMessageResponseCompletedEvent.md) object
Required: No

 ** responseCreated **   <a name="devopsagent-Type-SendMessageEvents-responseCreated"></a>
Emitted when the response is created
Type: [SendMessageResponseCreatedEvent](API_SendMessageResponseCreatedEvent.md) object
Required: No

 ** responseFailed **   <a name="devopsagent-Type-SendMessageEvents-responseFailed"></a>
Emitted when the response fails
Type: [SendMessageResponseFailedEvent](API_SendMessageResponseFailedEvent.md) object
Required: No

 ** responseInProgress **   <a name="devopsagent-Type-SendMessageEvents-responseInProgress"></a>
Emitted while the response is being generated
Type: [SendMessageResponseInProgressEvent](API_SendMessageResponseInProgressEvent.md) object
Required: No

 ** summary **   <a name="devopsagent-Type-SendMessageEvents-summary"></a>
Emitted to provide a summary of agent actions
Type: [SendMessageSummaryEvent](API_SendMessageSummaryEvent.md) object
Required: No

## See Also
<a name="API_SendMessageEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/SendMessageEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/SendMessageEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/SendMessageEvents)
