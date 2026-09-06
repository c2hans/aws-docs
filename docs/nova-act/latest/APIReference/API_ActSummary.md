---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ActSummary.html
---

# ActSummary
<a name="API_ActSummary"></a>

Summary information about an act, including its status and execution timing.

## Contents
<a name="API_ActSummary_Contents"></a>

 ** actId **   <a name="novaact-Type-ActSummary-actId"></a>
The unique identifier of the act.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** sessionId **   <a name="novaact-Type-ActSummary-sessionId"></a>
The unique identifier of the session containing this act.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** startedAt **   <a name="novaact-Type-ActSummary-startedAt"></a>
The timestamp when the act started execution.
Type: Timestamp
Required: Yes

 ** status **   <a name="novaact-Type-ActSummary-status"></a>
The current execution status of the act.
Type: String
Valid Values: `RUNNING | PENDING_CLIENT_ACTION | PENDING_HUMAN_ACTION | SUCCEEDED | FAILED | TIMED_OUT`
Required: Yes

 ** workflowRunId **   <a name="novaact-Type-ActSummary-workflowRunId"></a>
The unique identifier of the workflow run containing this act.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** endedAt **   <a name="novaact-Type-ActSummary-endedAt"></a>
The timestamp when the act completed execution, if applicable.
Type: Timestamp
Required: No

 ** traceLocation **   <a name="novaact-Type-ActSummary-traceLocation"></a>
The location where trace information for this act is stored.
Type: [TraceLocation](API_TraceLocation.md) object
Required: No

## See Also
<a name="API_ActSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/ActSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/ActSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/ActSummary)
