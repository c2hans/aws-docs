---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_TaskSearchSummary.html
---

# TaskSearchSummary
<a name="API_TaskSearchSummary"></a>

The details of a task search.

## Contents
<a name="API_TaskSearchSummary_Contents"></a>

 ** endedAt **   <a name="deadlinecloud-Type-TaskSearchSummary-endedAt"></a>
The date and time the resource ended running.
Type: Timestamp
Required: No

 ** failureRetryCount **   <a name="deadlinecloud-Type-TaskSearchSummary-failureRetryCount"></a>
The number of times that the task failed and was retried.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** jobId **   <a name="deadlinecloud-Type-TaskSearchSummary-jobId"></a>
The job ID.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: No

 ** latestSessionActionId **   <a name="deadlinecloud-Type-TaskSearchSummary-latestSessionActionId"></a>
The latest session action ID for the task.
Type: String
Pattern: `sessionaction-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`
Required: No

 ** parameters **   <a name="deadlinecloud-Type-TaskSearchSummary-parameters"></a>
The parameters to search for.
Type: String to [TaskParameterValue](API_TaskParameterValue.md) object map
Required: No

 ** queueId **   <a name="deadlinecloud-Type-TaskSearchSummary-queueId"></a>
The queue ID.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: No

 ** runStatus **   <a name="deadlinecloud-Type-TaskSearchSummary-runStatus"></a>
The run status of the task.
Type: String
Valid Values: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`
Required: No

 ** startedAt **   <a name="deadlinecloud-Type-TaskSearchSummary-startedAt"></a>
The date and time the resource started running.
Type: Timestamp
Required: No

 ** stepId **   <a name="deadlinecloud-Type-TaskSearchSummary-stepId"></a>
The step ID.
Type: String
Pattern: `step-[0-9a-f]{32}`
Required: No

 ** targetRunStatus **   <a name="deadlinecloud-Type-TaskSearchSummary-targetRunStatus"></a>
The run status that the task is being updated to.
Type: String
Valid Values: `READY | FAILED | SUCCEEDED | CANCELED | SUSPENDED | PENDING`
Required: No

 ** taskId **   <a name="deadlinecloud-Type-TaskSearchSummary-taskId"></a>
The task ID.
Type: String
Pattern: `task-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-TaskSearchSummary-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-TaskSearchSummary-updatedBy"></a>
The user or system that updated this resource.
Type: String
Required: No

## See Also
<a name="API_TaskSearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/TaskSearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/TaskSearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/TaskSearchSummary)
