---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetJobItem.html
---

# BatchGetJobItem
<a name="API_BatchGetJobItem"></a>

The details of a job returned in a batch get operation.

## Contents
<a name="API_BatchGetJobItem_Contents"></a>

 ** createdAt **   <a name="deadlinecloud-Type-BatchGetJobItem-createdAt"></a>
The date and time the resource was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="deadlinecloud-Type-BatchGetJobItem-createdBy"></a>
The user or system that created this resource.
Type: String
Required: Yes

 ** farmId **   <a name="deadlinecloud-Type-BatchGetJobItem-farmId"></a>
The farm ID of the job.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-BatchGetJobItem-jobId"></a>
The job ID.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** lifecycleStatus **   <a name="deadlinecloud-Type-BatchGetJobItem-lifecycleStatus"></a>
The life cycle status of the job.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | CREATE_COMPLETE | UPLOAD_IN_PROGRESS | UPLOAD_FAILED | UPDATE_IN_PROGRESS | UPDATE_FAILED | UPDATE_SUCCEEDED | ARCHIVED`
Required: Yes

 ** lifecycleStatusMessage **   <a name="deadlinecloud-Type-BatchGetJobItem-lifecycleStatusMessage"></a>
A message that communicates the status of the life cycle.
Type: String
Required: Yes

 ** name **   <a name="deadlinecloud-Type-BatchGetJobItem-name"></a>
The name of the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** priority **   <a name="deadlinecloud-Type-BatchGetJobItem-priority"></a>
The job priority.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-BatchGetJobItem-queueId"></a>
The queue ID of the job.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** attachments **   <a name="deadlinecloud-Type-BatchGetJobItem-attachments"></a>
The attachments for the job.
Type: [Attachments](API_Attachments.md) object
Required: No

 ** description **   <a name="deadlinecloud-Type-BatchGetJobItem-description"></a>
The description of the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** endedAt **   <a name="deadlinecloud-Type-BatchGetJobItem-endedAt"></a>
The date and time the resource ended running.
Type: Timestamp
Required: No

 ** maxFailedTasksCount **   <a name="deadlinecloud-Type-BatchGetJobItem-maxFailedTasksCount"></a>
The number of task failures before the job stops running and is marked as `FAILED`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** maxRetriesPerTask **   <a name="deadlinecloud-Type-BatchGetJobItem-maxRetriesPerTask"></a>
The maximum number of retries per failed tasks.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** maxWorkerCount **   <a name="deadlinecloud-Type-BatchGetJobItem-maxWorkerCount"></a>
The maximum number of worker hosts that can concurrently process a job.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 2147483647.
Required: No

 ** parameters **   <a name="deadlinecloud-Type-BatchGetJobItem-parameters"></a>
The parameters for the job.
Type: String to [JobParameter](API_JobParameter.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** sourceJobId **   <a name="deadlinecloud-Type-BatchGetJobItem-sourceJobId"></a>
The job ID for the source job.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: No

 ** startedAt **   <a name="deadlinecloud-Type-BatchGetJobItem-startedAt"></a>
The date and time the resource started running.
Type: Timestamp
Required: No

 ** storageProfileId **   <a name="deadlinecloud-Type-BatchGetJobItem-storageProfileId"></a>
The storage profile ID associated with the job.
Type: String
Pattern: `sp-[0-9a-f]{32}`
Required: No

 ** targetTaskRunStatus **   <a name="deadlinecloud-Type-BatchGetJobItem-targetTaskRunStatus"></a>
The task status to start with on the job.
Type: String
Valid Values: `READY | FAILED | SUCCEEDED | CANCELED | SUSPENDED | PENDING`
Required: No

 ** taskFailureRetryCount **   <a name="deadlinecloud-Type-BatchGetJobItem-taskFailureRetryCount"></a>
The number of times that tasks failed and were retried.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** taskRunStatus **   <a name="deadlinecloud-Type-BatchGetJobItem-taskRunStatus"></a>
The task run status for the job.
Type: String
Valid Values: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`
Required: No

 ** taskRunStatusCounts **   <a name="deadlinecloud-Type-BatchGetJobItem-taskRunStatusCounts"></a>
The number of tasks for each run status for the job.
Type: String to integer map
Valid Keys: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-BatchGetJobItem-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-BatchGetJobItem-updatedBy"></a>
The user or system that updated this resource.
Type: String
Required: No

## See Also
<a name="API_BatchGetJobItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetJobItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetJobItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetJobItem)
