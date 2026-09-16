---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchUpdateJobItem.html
---

# BatchUpdateJobItem
<a name="API_BatchUpdateJobItem"></a>

The details of a job to update in a batch update operation.

## Contents
<a name="API_BatchUpdateJobItem_Contents"></a>

 ** farmId **   <a name="deadlinecloud-Type-BatchUpdateJobItem-farmId"></a>
The farm ID of the job to update.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-BatchUpdateJobItem-jobId"></a>
The job ID of the job to update.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-BatchUpdateJobItem-queueId"></a>
The queue ID of the job to update.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** description **   <a name="deadlinecloud-Type-BatchUpdateJobItem-description"></a>
The description of the job to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** lifecycleStatus **   <a name="deadlinecloud-Type-BatchUpdateJobItem-lifecycleStatus"></a>
The status of a job in its lifecycle. When you change the status of the job to `ARCHIVED`, the job can't be scheduled or archived.
An archived job and its steps and tasks are deleted after 120 days. The job can't be recovered.
Type: String
Valid Values: `ARCHIVED`
Required: No

 ** maxFailedTasksCount **   <a name="deadlinecloud-Type-BatchUpdateJobItem-maxFailedTasksCount"></a>
The number of task failures before the job stops running and is marked as `FAILED`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** maxRetriesPerTask **   <a name="deadlinecloud-Type-BatchUpdateJobItem-maxRetriesPerTask"></a>
The maximum number of retries per failed tasks.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** maxWorkerCount **   <a name="deadlinecloud-Type-BatchUpdateJobItem-maxWorkerCount"></a>
The maximum number of worker hosts that can concurrently process a job.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 2147483647.
Required: No

 ** name **   <a name="deadlinecloud-Type-BatchUpdateJobItem-name"></a>
The name of the job to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** priority **   <a name="deadlinecloud-Type-BatchUpdateJobItem-priority"></a>
The job priority to update.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** targetTaskRunStatus **   <a name="deadlinecloud-Type-BatchUpdateJobItem-targetTaskRunStatus"></a>
The task status to update the job's tasks to.
Type: String
Valid Values: `READY | FAILED | SUCCEEDED | CANCELED | SUSPENDED | PENDING`
Required: No

## See Also
<a name="API_BatchUpdateJobItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchUpdateJobItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchUpdateJobItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchUpdateJobItem)
