---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetTaskIdentifier.html
---

# BatchGetTaskIdentifier
<a name="API_BatchGetTaskIdentifier"></a>

The identifiers for a task.

## Contents
<a name="API_BatchGetTaskIdentifier_Contents"></a>

 ** farmId **   <a name="deadlinecloud-Type-BatchGetTaskIdentifier-farmId"></a>
The farm ID of the task.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-BatchGetTaskIdentifier-jobId"></a>
The job ID of the task.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-BatchGetTaskIdentifier-queueId"></a>
The queue ID of the task.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** stepId **   <a name="deadlinecloud-Type-BatchGetTaskIdentifier-stepId"></a>
The step ID of the task.
Type: String
Pattern: `step-[0-9a-f]{32}`
Required: Yes

 ** taskId **   <a name="deadlinecloud-Type-BatchGetTaskIdentifier-taskId"></a>
The task ID.
Type: String
Pattern: `task-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`
Required: Yes

## See Also
<a name="API_BatchGetTaskIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetTaskIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetTaskIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetTaskIdentifier)
