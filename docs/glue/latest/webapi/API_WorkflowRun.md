---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_WorkflowRun.html
---

# WorkflowRun
<a name="API_WorkflowRun"></a>

A workflow run is an execution of a workflow providing all the runtime information.

## Contents
<a name="API_WorkflowRun_Contents"></a>

 ** CompletedOn **   <a name="Glue-Type-WorkflowRun-CompletedOn"></a>
The date and time when the workflow run completed.
Type: Timestamp
Required: No

 ** ErrorMessage **   <a name="Glue-Type-WorkflowRun-ErrorMessage"></a>
This error message describes any error that may have occurred in starting the workflow run. Currently the only error message is "Concurrent runs exceeded for workflow: `foo`."
Type: String
Required: No

 ** Graph **   <a name="Glue-Type-WorkflowRun-Graph"></a>
The graph representing all the AWS Glue components that belong to the workflow as nodes and directed connections between them as edges.
Type: [WorkflowGraph](API_WorkflowGraph.md) object
Required: No

 ** Name **   <a name="Glue-Type-WorkflowRun-Name"></a>
Name of the workflow that was run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** PreviousRunId **   <a name="Glue-Type-WorkflowRun-PreviousRunId"></a>
The ID of the previous workflow run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** StartedOn **   <a name="Glue-Type-WorkflowRun-StartedOn"></a>
The date and time when the workflow run was started.
Type: Timestamp
Required: No

 ** StartingEventBatchCondition **   <a name="Glue-Type-WorkflowRun-StartingEventBatchCondition"></a>
The batch condition that started the workflow run.
Type: [StartingEventBatchCondition](API_StartingEventBatchCondition.md) object
Required: No

 ** Statistics **   <a name="Glue-Type-WorkflowRun-Statistics"></a>
The statistics of the run.
Type: [WorkflowRunStatistics](API_WorkflowRunStatistics.md) object
Required: No

 ** Status **   <a name="Glue-Type-WorkflowRun-Status"></a>
The status of the workflow run.
Type: String
Valid Values: `RUNNING | COMPLETED | STOPPING | STOPPED | ERROR`
Required: No

 ** WorkflowRunId **   <a name="Glue-Type-WorkflowRun-WorkflowRunId"></a>
The ID of this workflow run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** WorkflowRunProperties **   <a name="Glue-Type-WorkflowRun-WorkflowRunProperties"></a>
The workflow run properties which were set during the run.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_WorkflowRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/WorkflowRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/WorkflowRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/WorkflowRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
