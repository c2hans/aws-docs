---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetTaskItem.html
---

# BatchGetTaskItem
<a name="API_BatchGetTaskItem"></a>

The details of a task returned in a batch get operation.

## Contents
<a name="API_BatchGetTaskItem_Contents"></a>

 ** createdAt **   <a name="deadlinecloud-Type-BatchGetTaskItem-createdAt"></a>
The date and time the resource was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="deadlinecloud-Type-BatchGetTaskItem-createdBy"></a>
The user or system that created this resource.
Type: String
Required: Yes

 ** farmId **   <a name="deadlinecloud-Type-BatchGetTaskItem-farmId"></a>
The farm ID of the task.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-BatchGetTaskItem-jobId"></a>
The job ID of the task.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-BatchGetTaskItem-queueId"></a>
The queue ID of the task.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** runStatus **   <a name="deadlinecloud-Type-BatchGetTaskItem-runStatus"></a>
The run status of the task.
Type: String
Valid Values: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`
Required: Yes

 ** stepId **   <a name="deadlinecloud-Type-BatchGetTaskItem-stepId"></a>
The step ID of the task.
Type: String
Pattern: `step-[0-9a-f]{32}`
Required: Yes

 ** taskId **   <a name="deadlinecloud-Type-BatchGetTaskItem-taskId"></a>
The task ID.
Type: String
Pattern: `task-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`
Required: Yes

 ** endedAt **   <a name="deadlinecloud-Type-BatchGetTaskItem-endedAt"></a>
The date and time the resource ended running.
Type: Timestamp
Required: No

 ** failureRetryCount **   <a name="deadlinecloud-Type-BatchGetTaskItem-failureRetryCount"></a>
The number of times the task failed and was retried.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** latestSessionActionId **   <a name="deadlinecloud-Type-BatchGetTaskItem-latestSessionActionId"></a>
The latest session action for the task.
Type: String
Pattern: `sessionaction-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`
Required: No

 ** parameters **   <a name="deadlinecloud-Type-BatchGetTaskItem-parameters"></a>
The parameters for the task.
Type: String to [TaskParameterValue](API_TaskParameterValue.md) object map
Required: No

 ** startedAt **   <a name="deadlinecloud-Type-BatchGetTaskItem-startedAt"></a>
The date and time the resource started running.
Type: Timestamp
Required: No

 ** targetRunStatus **   <a name="deadlinecloud-Type-BatchGetTaskItem-targetRunStatus"></a>
The run status with which to start the task.
Type: String
Valid Values: `READY | FAILED | SUCCEEDED | CANCELED | SUSPENDED | PENDING`
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-BatchGetTaskItem-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-BatchGetTaskItem-updatedBy"></a>
The user or system that updated this resource.
Type: String
Required: No

## See Also
<a name="API_BatchGetTaskItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetTaskItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetTaskItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetTaskItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
