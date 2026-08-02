---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_WorkflowRunSummary.html
---

# WorkflowRunSummary
<a name="API_WorkflowRunSummary"></a>

Summary information about a workflow run, including execution status and timing.

## Contents
<a name="API_WorkflowRunSummary_Contents"></a>

 ** startedAt **   <a name="novaact-Type-WorkflowRunSummary-startedAt"></a>
The timestamp when the workflow run started execution.
Type: Timestamp
Required: Yes

 ** status **   <a name="novaact-Type-WorkflowRunSummary-status"></a>
The current execution status of the workflow run.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | TIMED_OUT | DELETING`
Required: Yes

 ** workflowRunArn **   <a name="novaact-Type-WorkflowRunSummary-workflowRunArn"></a>
The Amazon Resource Name (ARN) of the workflow run.
Type: String
Pattern: `arn:(aws|aws-cn|aws-us-gov):nova-act:[a-z0-9-]+:[0-9]{12}:workflow-definition/[a-zA-Z0-9_-]{1,40}/workflow-run/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** workflowRunId **   <a name="novaact-Type-WorkflowRunSummary-workflowRunId"></a>
The unique identifier of the workflow run.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** endedAt **   <a name="novaact-Type-WorkflowRunSummary-endedAt"></a>
The timestamp when the workflow run completed execution, if applicable.
Type: Timestamp
Required: No

 ** traceLocation **   <a name="novaact-Type-WorkflowRunSummary-traceLocation"></a>
The location where trace information for this workflow run is stored.
Type: [TraceLocation](API_TraceLocation.md) object
Required: No

## See Also
<a name="API_WorkflowRunSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/WorkflowRunSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/WorkflowRunSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/WorkflowRunSummary)
