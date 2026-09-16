---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_StepSummary.html
---

# StepSummary
<a name="API_StepSummary"></a>

The details for a step.

## Contents
<a name="API_StepSummary_Contents"></a>

 ** createdAt **   <a name="deadlinecloud-Type-StepSummary-createdAt"></a>
The date and time the resource was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="deadlinecloud-Type-StepSummary-createdBy"></a>
The user or system that created this resource.
Type: String
Required: Yes

 ** lifecycleStatus **   <a name="deadlinecloud-Type-StepSummary-lifecycleStatus"></a>
The life cycle status.
Type: String
Valid Values: `CREATE_COMPLETE | UPDATE_IN_PROGRESS | UPDATE_FAILED | UPDATE_SUCCEEDED`
Required: Yes

 ** name **   <a name="deadlinecloud-Type-StepSummary-name"></a>
The name of the step.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** stepId **   <a name="deadlinecloud-Type-StepSummary-stepId"></a>
The step ID.
Type: String
Pattern: `step-[0-9a-f]{32}`
Required: Yes

 ** taskRunStatus **   <a name="deadlinecloud-Type-StepSummary-taskRunStatus"></a>
The task run status for the job.
+  `PENDING`–pending and waiting for resources.
+  `READY`–ready to process.
+  `ASSIGNED`–assigned and will run next on a worker.
+  `SCHEDULED`–scheduled to run on a worker.
+  `INTERRUPTING`–being interrupted.
+  `RUNNING`–running on a worker.
+  `SUSPENDED`–the task is suspended.
+  `CANCELED`–the task has been canceled.
+  `FAILED`–the task has failed.
+  `SUCCEEDED`–the task has succeeded.
Type: String
Valid Values: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`
Required: Yes

 ** taskRunStatusCounts **   <a name="deadlinecloud-Type-StepSummary-taskRunStatusCounts"></a>
The number of tasks running on the job.
Type: String to integer map
Valid Keys: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`
Required: Yes

 ** dependencyCounts **   <a name="deadlinecloud-Type-StepSummary-dependencyCounts"></a>
The number of dependencies for the step.
Type: [DependencyCounts](API_DependencyCounts.md) object
Required: No

 ** endedAt **   <a name="deadlinecloud-Type-StepSummary-endedAt"></a>
The date and time the resource ended running.
Type: Timestamp
Required: No

 ** lifecycleStatusMessage **   <a name="deadlinecloud-Type-StepSummary-lifecycleStatusMessage"></a>
A message that describes the lifecycle of the step.
Type: String
Required: No

 ** startedAt **   <a name="deadlinecloud-Type-StepSummary-startedAt"></a>
The date and time the resource started running.
Type: Timestamp
Required: No

 ** targetTaskRunStatus **   <a name="deadlinecloud-Type-StepSummary-targetTaskRunStatus"></a>
The task status to update the job's tasks to.
Type: String
Valid Values: `READY | FAILED | SUCCEEDED | CANCELED | SUSPENDED | PENDING`
Required: No

 ** taskFailureRetryCount **   <a name="deadlinecloud-Type-StepSummary-taskFailureRetryCount"></a>
The total number of times tasks from the step failed and were retried.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-StepSummary-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-StepSummary-updatedBy"></a>
The user or system that updated this resource.
Type: String
Required: No

## See Also
<a name="API_StepSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/StepSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/StepSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/StepSummary)
