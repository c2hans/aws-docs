---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_TaskSummary.html
---

# TaskSummary
<a name="API_TaskSummary"></a>

The details of a task.

## Contents
<a name="API_TaskSummary_Contents"></a>

 ** createdAt **   <a name="deadlinecloud-Type-TaskSummary-createdAt"></a>
The date and time the resource was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="deadlinecloud-Type-TaskSummary-createdBy"></a>
The user or system that created this resource.
Type: String
Required: Yes

 ** runStatus **   <a name="deadlinecloud-Type-TaskSummary-runStatus"></a>
The run status of the task.
Type: String
Valid Values: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`
Required: Yes

 ** taskId **   <a name="deadlinecloud-Type-TaskSummary-taskId"></a>
The task ID.
Type: String
Pattern: `task-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`
Required: Yes

 ** endedAt **   <a name="deadlinecloud-Type-TaskSummary-endedAt"></a>
The date and time the resource ended running.
Type: Timestamp
Required: No

 ** failureRetryCount **   <a name="deadlinecloud-Type-TaskSummary-failureRetryCount"></a>
The number of times that the task failed and was retried.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** latestSessionActionId **   <a name="deadlinecloud-Type-TaskSummary-latestSessionActionId"></a>
The latest session action ID for the task.
Type: String
Pattern: `sessionaction-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`
Required: No

 ** parameters **   <a name="deadlinecloud-Type-TaskSummary-parameters"></a>
The task parameters.
Type: String to [TaskParameterValue](API_TaskParameterValue.md) object map
Required: No

 ** startedAt **   <a name="deadlinecloud-Type-TaskSummary-startedAt"></a>
The date and time the resource started running.
Type: Timestamp
Required: No

 ** targetRunStatus **   <a name="deadlinecloud-Type-TaskSummary-targetRunStatus"></a>
The run status on which the started.
Type: String
Valid Values: `READY | FAILED | SUCCEEDED | CANCELED | SUSPENDED | PENDING`
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-TaskSummary-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-TaskSummary-updatedBy"></a>
The user or system that updated this resource.
Type: String
Required: No

## See Also
<a name="API_TaskSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/TaskSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/TaskSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/TaskSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
