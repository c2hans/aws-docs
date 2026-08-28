---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchUpdateTaskItem.html
---

# BatchUpdateTaskItem
<a name="API_BatchUpdateTaskItem"></a>

The details of a task to update in a batch update operation.

## Contents
<a name="API_BatchUpdateTaskItem_Contents"></a>

 ** farmId **   <a name="deadlinecloud-Type-BatchUpdateTaskItem-farmId"></a>
The farm ID of the task to update.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-BatchUpdateTaskItem-jobId"></a>
The job ID of the task to update.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-BatchUpdateTaskItem-queueId"></a>
The queue ID of the task to update.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** stepId **   <a name="deadlinecloud-Type-BatchUpdateTaskItem-stepId"></a>
The step ID of the task to update.
Type: String
Pattern: `step-[0-9a-f]{32}`
Required: Yes

 ** targetRunStatus **   <a name="deadlinecloud-Type-BatchUpdateTaskItem-targetRunStatus"></a>
The run status with which to start the task.
Type: String
Valid Values: `READY | FAILED | SUCCEEDED | CANCELED | SUSPENDED | PENDING`
Required: Yes

 ** taskId **   <a name="deadlinecloud-Type-BatchUpdateTaskItem-taskId"></a>
The task ID of the task to update.
Type: String
Pattern: `task-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`
Required: Yes

## See Also
<a name="API_BatchUpdateTaskItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchUpdateTaskItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchUpdateTaskItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchUpdateTaskItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
