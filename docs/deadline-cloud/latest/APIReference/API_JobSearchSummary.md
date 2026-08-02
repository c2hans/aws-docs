---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_JobSearchSummary.html
---

# JobSearchSummary
<a name="API_JobSearchSummary"></a>

The details of a job search.

## Contents
<a name="API_JobSearchSummary_Contents"></a>

 ** createdAt **   <a name="deadlinecloud-Type-JobSearchSummary-createdAt"></a>
The date and time the resource was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="deadlinecloud-Type-JobSearchSummary-createdBy"></a>
The user or system that created this resource.
Type: String
Required: No

 ** endedAt **   <a name="deadlinecloud-Type-JobSearchSummary-endedAt"></a>
The date and time the resource ended running.
Type: Timestamp
Required: No

 ** jobId **   <a name="deadlinecloud-Type-JobSearchSummary-jobId"></a>
The job ID.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: No

 ** jobParameters **   <a name="deadlinecloud-Type-JobSearchSummary-jobParameters"></a>
The job parameters.
Type: String to [JobParameter](API_JobParameter.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** lifecycleStatus **   <a name="deadlinecloud-Type-JobSearchSummary-lifecycleStatus"></a>
The life cycle status.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | CREATE_COMPLETE | UPLOAD_IN_PROGRESS | UPLOAD_FAILED | UPDATE_IN_PROGRESS | UPDATE_FAILED | UPDATE_SUCCEEDED | ARCHIVED`
Required: No

 ** lifecycleStatusMessage **   <a name="deadlinecloud-Type-JobSearchSummary-lifecycleStatusMessage"></a>
The life cycle status message.
Type: String
Required: No

 ** maxFailedTasksCount **   <a name="deadlinecloud-Type-JobSearchSummary-maxFailedTasksCount"></a>
The number of task failures before the job stops running and is marked as `FAILED`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** maxRetriesPerTask **   <a name="deadlinecloud-Type-JobSearchSummary-maxRetriesPerTask"></a>
The maximum number of retries for a job.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** maxWorkerCount **   <a name="deadlinecloud-Type-JobSearchSummary-maxWorkerCount"></a>
The maximum number of worker hosts that can concurrently process a job. When the `maxWorkerCount` is reached, no more workers will be assigned to process the job, even if the fleets assigned to the job's queue has available workers.
You can't set the `maxWorkerCount` to 0. If you set it to -1, there is no maximum number of workers.
If you don't specify the `maxWorkerCount`, the default is -1.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 2147483647.
Required: No

 ** name **   <a name="deadlinecloud-Type-JobSearchSummary-name"></a>
The job name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** priority **   <a name="deadlinecloud-Type-JobSearchSummary-priority"></a>
The job priority.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** queueId **   <a name="deadlinecloud-Type-JobSearchSummary-queueId"></a>
The queue ID.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: No

 ** sourceJobId **   <a name="deadlinecloud-Type-JobSearchSummary-sourceJobId"></a>
The job ID for the source job.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: No

 ** startedAt **   <a name="deadlinecloud-Type-JobSearchSummary-startedAt"></a>
The date and time the resource started running.
Type: Timestamp
Required: No

 ** targetTaskRunStatus **   <a name="deadlinecloud-Type-JobSearchSummary-targetTaskRunStatus"></a>
The task status to update the job's tasks to.
Type: String
Valid Values: `READY | FAILED | SUCCEEDED | CANCELED | SUSPENDED | PENDING`
Required: No

 ** taskFailureRetryCount **   <a name="deadlinecloud-Type-JobSearchSummary-taskFailureRetryCount"></a>
The total number of times tasks from the job failed and were retried.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** taskRunStatus **   <a name="deadlinecloud-Type-JobSearchSummary-taskRunStatus"></a>
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

 ** taskRunStatusCounts **   <a name="deadlinecloud-Type-JobSearchSummary-taskRunStatusCounts"></a>
The number of tasks running on the job.
Type: String to integer map
Valid Keys: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-JobSearchSummary-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-JobSearchSummary-updatedBy"></a>
The user or system that updated this resource.
Type: String
Required: No

## See Also
<a name="API_JobSearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/JobSearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/JobSearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/JobSearchSummary)
