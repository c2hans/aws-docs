---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_WorkflowRunStatistics.html
---

# WorkflowRunStatistics
<a name="API_WorkflowRunStatistics"></a>

Workflow run statistics provides statistics about the workflow run.

## Contents
<a name="API_WorkflowRunStatistics_Contents"></a>

 ** ErroredActions **   <a name="Glue-Type-WorkflowRunStatistics-ErroredActions"></a>
Indicates the count of job runs in the ERROR state in the workflow run.
Type: Integer
Required: No

 ** FailedActions **   <a name="Glue-Type-WorkflowRunStatistics-FailedActions"></a>
Total number of Actions that have failed.
Type: Integer
Required: No

 ** RunningActions **   <a name="Glue-Type-WorkflowRunStatistics-RunningActions"></a>
Total number Actions in running state.
Type: Integer
Required: No

 ** StoppedActions **   <a name="Glue-Type-WorkflowRunStatistics-StoppedActions"></a>
Total number of Actions that have stopped.
Type: Integer
Required: No

 ** SucceededActions **   <a name="Glue-Type-WorkflowRunStatistics-SucceededActions"></a>
Total number of Actions that have succeeded.
Type: Integer
Required: No

 ** TimeoutActions **   <a name="Glue-Type-WorkflowRunStatistics-TimeoutActions"></a>
Total number of Actions that timed out.
Type: Integer
Required: No

 ** TotalActions **   <a name="Glue-Type-WorkflowRunStatistics-TotalActions"></a>
Total number of Actions in the workflow run.
Type: Integer
Required: No

 ** WaitingActions **   <a name="Glue-Type-WorkflowRunStatistics-WaitingActions"></a>
Indicates the count of job runs in WAITING state in the workflow run.
Type: Integer
Required: No

## See Also
<a name="API_WorkflowRunStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/WorkflowRunStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/WorkflowRunStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/WorkflowRunStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
