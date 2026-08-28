---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ActivityTask.html
---

# ActivityTask
<a name="API_ActivityTask"></a>

Unit of work sent to an activity worker.

## Contents
<a name="API_ActivityTask_Contents"></a>

 ** activityId **   <a name="SWF-Type-ActivityTask-activityId"></a>
The unique ID of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** activityType **   <a name="SWF-Type-ActivityTask-activityType"></a>
The type of this activity task.
Type: [ActivityType](API_ActivityType.md) object
Required: Yes

 ** startedEventId **   <a name="SWF-Type-ActivityTask-startedEventId"></a>
The ID of the `ActivityTaskStarted` event recorded in the history.
Type: Long
Required: Yes

 ** taskToken **   <a name="SWF-Type-ActivityTask-taskToken"></a>
The opaque string used as a handle on the task. This token is used by workers to communicate progress and response information back to the system about the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** workflowExecution **   <a name="SWF-Type-ActivityTask-workflowExecution"></a>
The workflow execution that started this activity task.
Type: [WorkflowExecution](API_WorkflowExecution.md) object
Required: Yes

 ** input **   <a name="SWF-Type-ActivityTask-input"></a>
The inputs provided when the activity task was scheduled. The form of the input is user defined and should be meaningful to the activity implementation.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

## See Also
<a name="API_ActivityTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ActivityTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ActivityTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ActivityTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
