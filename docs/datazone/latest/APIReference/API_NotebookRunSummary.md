---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_NotebookRunSummary.html
---

# NotebookRunSummary
<a name="API_NotebookRunSummary"></a>

The summary of a notebook run in Amazon SageMaker Unified Studio.

## Contents
<a name="API_NotebookRunSummary_Contents"></a>

 ** domainId **   <a name="datazone-Type-NotebookRunSummary-domainId"></a>
The identifier of the Amazon SageMaker Unified Studio domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-NotebookRunSummary-id"></a>
The identifier of the notebook run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** notebookId **   <a name="datazone-Type-NotebookRunSummary-notebookId"></a>
The identifier of the notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** owningProjectId **   <a name="datazone-Type-NotebookRunSummary-owningProjectId"></a>
The identifier of the project that owns the notebook run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** status **   <a name="datazone-Type-NotebookRunSummary-status"></a>
The status of the notebook run.
Type: String
Valid Values: `QUEUED | STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED`
Required: Yes

 ** completedAt **   <a name="datazone-Type-NotebookRunSummary-completedAt"></a>
The timestamp of when the notebook run completed.
Type: Timestamp
Required: No

 ** createdAt **   <a name="datazone-Type-NotebookRunSummary-createdAt"></a>
The timestamp of when the notebook run was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="datazone-Type-NotebookRunSummary-createdBy"></a>
The identifier of the user who created the notebook run.
Type: String
Required: No

 ** scheduleId **   <a name="datazone-Type-NotebookRunSummary-scheduleId"></a>
The identifier of the schedule associated with the notebook run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** startedAt **   <a name="datazone-Type-NotebookRunSummary-startedAt"></a>
The timestamp of when the notebook run started executing.
Type: Timestamp
Required: No

 ** triggerSource **   <a name="datazone-Type-NotebookRunSummary-triggerSource"></a>
The source that triggered the notebook run.
Type: [TriggerSource](API_TriggerSource.md) object
Required: No

 ** updatedAt **   <a name="datazone-Type-NotebookRunSummary-updatedAt"></a>
The timestamp of when the notebook run was last updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="datazone-Type-NotebookRunSummary-updatedBy"></a>
The identifier of the user who last updated the notebook run.
Type: String
Required: No

## See Also
<a name="API_NotebookRunSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/NotebookRunSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/NotebookRunSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/NotebookRunSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
