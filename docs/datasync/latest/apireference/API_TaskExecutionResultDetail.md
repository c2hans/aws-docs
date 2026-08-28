---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_TaskExecutionResultDetail.html
---

# TaskExecutionResultDetail
<a name="API_TaskExecutionResultDetail"></a>

Provides detailed information about the result of your AWS DataSync task execution.

## Contents
<a name="API_TaskExecutionResultDetail_Contents"></a>

 ** ErrorCode **   <a name="DataSync-Type-TaskExecutionResultDetail-ErrorCode"></a>
An error that DataSync encountered during your task execution. You can use this information to help [troubleshoot issues](https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html).
Type: String
Required: No

 ** ErrorDetail **   <a name="DataSync-Type-TaskExecutionResultDetail-ErrorDetail"></a>
The detailed description of an error that DataSync encountered during your task execution. You can use this information to help [troubleshoot issues](https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html).
Type: String
Required: No

 ** PrepareDuration **   <a name="DataSync-Type-TaskExecutionResultDetail-PrepareDuration"></a>
The time in milliseconds that your task execution was in the `PREPARING` step. For more information, see [Task execution statuses](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses).
For Enhanced mode tasks, the value is always `0`. For more information, see [How DataSync prepares your data transfer](https://docs.aws.amazon.com/datasync/latest/userguide/how-datasync-transfer-works.html#how-datasync-prepares).
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** PrepareStatus **   <a name="DataSync-Type-TaskExecutionResultDetail-PrepareStatus"></a>
The status of the `PREPARING` step for your task execution. For more information, see [Task execution statuses](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses).
Type: String
Valid Values: `PENDING | SUCCESS | ERROR`
Required: No

 ** TotalDuration **   <a name="DataSync-Type-TaskExecutionResultDetail-TotalDuration"></a>
The time in milliseconds that your task execution ran.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** TransferDuration **   <a name="DataSync-Type-TaskExecutionResultDetail-TransferDuration"></a>
The time in milliseconds that your task execution was in the `TRANSFERRING` step. For more information, see [Task execution statuses](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses).
For Enhanced mode tasks, the value is always `0`. For more information, see [How DataSync transfers your data](https://docs.aws.amazon.com/datasync/latest/userguide/how-datasync-transfer-works.html#how-datasync-transfers).
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** TransferStatus **   <a name="DataSync-Type-TaskExecutionResultDetail-TransferStatus"></a>
The status of the `TRANSFERRING` step for your task execution. For more information, see [Task execution statuses](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses).
Type: String
Valid Values: `PENDING | SUCCESS | ERROR`
Required: No

 ** VerifyDuration **   <a name="DataSync-Type-TaskExecutionResultDetail-VerifyDuration"></a>
The time in milliseconds that your task execution was in the `VERIFYING` step. For more information, see [Task execution statuses](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses).
For Enhanced mode tasks, the value is always `0`. For more information, see [How DataSync verifies your data's integrity](https://docs.aws.amazon.com/datasync/latest/userguide/how-datasync-transfer-works.html#how-verifying-works).
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** VerifyStatus **   <a name="DataSync-Type-TaskExecutionResultDetail-VerifyStatus"></a>
The status of the `VERIFYING` step for your task execution. For more information, see [Task execution statuses](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses).
Type: String
Valid Values: `PENDING | SUCCESS | ERROR`
Required: No

## See Also
<a name="API_TaskExecutionResultDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/TaskExecutionResultDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/TaskExecutionResultDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/TaskExecutionResultDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
