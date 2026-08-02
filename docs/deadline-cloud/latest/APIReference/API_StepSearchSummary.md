---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_StepSearchSummary.html
---

# StepSearchSummary
<a name="API_StepSearchSummary"></a>

The details of a step search.

## Contents
<a name="API_StepSearchSummary_Contents"></a>

 ** createdAt **   <a name="deadlinecloud-Type-StepSearchSummary-createdAt"></a>
The date and time the resource was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="deadlinecloud-Type-StepSearchSummary-createdBy"></a>
The user or system that created this resource.
Type: String
Required: No

 ** endedAt **   <a name="deadlinecloud-Type-StepSearchSummary-endedAt"></a>
The date and time the resource ended running.
Type: Timestamp
Required: No

 ** jobId **   <a name="deadlinecloud-Type-StepSearchSummary-jobId"></a>
The job ID.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: No

 ** lifecycleStatus **   <a name="deadlinecloud-Type-StepSearchSummary-lifecycleStatus"></a>
The life cycle status.
Type: String
Valid Values: `CREATE_COMPLETE | UPDATE_IN_PROGRESS | UPDATE_FAILED | UPDATE_SUCCEEDED`
Required: No

 ** lifecycleStatusMessage **   <a name="deadlinecloud-Type-StepSearchSummary-lifecycleStatusMessage"></a>
The life cycle status message.
Type: String
Required: No

 ** name **   <a name="deadlinecloud-Type-StepSearchSummary-name"></a>
The step name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** parameterSpace **   <a name="deadlinecloud-Type-StepSearchSummary-parameterSpace"></a>
The parameters and combination expressions for the search.
Type: [ParameterSpace](API_ParameterSpace.md) object
Required: No

 ** queueId **   <a name="deadlinecloud-Type-StepSearchSummary-queueId"></a>
The queue ID.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: No

 ** startedAt **   <a name="deadlinecloud-Type-StepSearchSummary-startedAt"></a>
The date and time the resource started running.
Type: Timestamp
Required: No

 ** stepId **   <a name="deadlinecloud-Type-StepSearchSummary-stepId"></a>
The step ID.
Type: String
Pattern: `step-[0-9a-f]{32}`
Required: No

 ** targetTaskRunStatus **   <a name="deadlinecloud-Type-StepSearchSummary-targetTaskRunStatus"></a>
The task status to update the job's tasks to.
Type: String
Valid Values: `READY | FAILED | SUCCEEDED | CANCELED | SUSPENDED | PENDING`
Required: No

 ** taskFailureRetryCount **   <a name="deadlinecloud-Type-StepSearchSummary-taskFailureRetryCount"></a>
The total number of times tasks from the step failed and were retried.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** taskRunStatus **   <a name="deadlinecloud-Type-StepSearchSummary-taskRunStatus"></a>
The task run status for the job.
+  `PENDING`–pending and waiting for resources.
+  `READY`–ready to be processed.
+  `ASSIGNED`–assigned and will run next on a worker.
+  `SCHEDULED`–scheduled to be run on a worker.
+  `INTERRUPTING`–being interrupted.
+  `RUNNING`–running on a worker.
+  `SUSPENDED`–the task is suspended.
+  `CANCELED`–the task has been canceled.
+  `FAILED`–the task has failed.
+  `SUCCEEDED`–the task has succeeded.
Type: String
Valid Values: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`
Required: No

 ** taskRunStatusCounts **   <a name="deadlinecloud-Type-StepSearchSummary-taskRunStatusCounts"></a>
The number of tasks running on the job.
Type: String to integer map
Valid Keys: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-StepSearchSummary-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-StepSearchSummary-updatedBy"></a>
The user or system that updated this resource.
Type: String
Required: No

## See Also
<a name="API_StepSearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/StepSearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/StepSearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/StepSearchSummary)
