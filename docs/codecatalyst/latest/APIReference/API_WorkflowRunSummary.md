---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_WorkflowRunSummary.html
---

# WorkflowRunSummary
<a name="API_WorkflowRunSummary"></a>

Information about a workflow run.

## Contents
<a name="API_WorkflowRunSummary_Contents"></a>

 ** id **   <a name="codecatalyst-Type-WorkflowRunSummary-id"></a>
The system-generated unique ID of the workflow run.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** lastUpdatedTime **   <a name="codecatalyst-Type-WorkflowRunSummary-lastUpdatedTime"></a>
The date and time the workflow was last updated, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6)
Type: Timestamp
Required: Yes

 ** startTime **   <a name="codecatalyst-Type-WorkflowRunSummary-startTime"></a>
The date and time the workflow run began, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6).
Type: Timestamp
Required: Yes

 ** status **   <a name="codecatalyst-Type-WorkflowRunSummary-status"></a>
The status of the workflow run.
Type: String
Valid Values: `SUCCEEDED | FAILED | STOPPED | SUPERSEDED | CANCELLED | NOT_RUN | VALIDATING | PROVISIONING | IN_PROGRESS | STOPPING | ABANDONED`
Required: Yes

 ** workflowId **   <a name="codecatalyst-Type-WorkflowRunSummary-workflowId"></a>
The system-generated unique ID of the workflow.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** workflowName **   <a name="codecatalyst-Type-WorkflowRunSummary-workflowName"></a>
The name of the workflow.
Type: String
Required: Yes

 ** endTime **   <a name="codecatalyst-Type-WorkflowRunSummary-endTime"></a>
The date and time the workflow run ended, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6)
Type: Timestamp
Required: No

 ** statusReasons **   <a name="codecatalyst-Type-WorkflowRunSummary-statusReasons"></a>
The reasons for the workflow run status.
Type: Array of [WorkflowRunStatusReason](API_WorkflowRunStatusReason.md) objects
Required: No

## See Also
<a name="API_WorkflowRunSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/WorkflowRunSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/WorkflowRunSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/WorkflowRunSummary)
