---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_TaskExecutionFoldersFailedDetail.html
---

# TaskExecutionFoldersFailedDetail
<a name="API_TaskExecutionFoldersFailedDetail"></a>

The number of directories that DataSync fails to list, prepare, transfer, verify, and delete during your task execution.

**Note**
Applies only to [Enhanced mode tasks](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html).

## Contents
<a name="API_TaskExecutionFoldersFailedDetail_Contents"></a>

 ** Delete **   <a name="DataSync-Type-TaskExecutionFoldersFailedDetail-Delete"></a>
The number of directories that DataSync fails to delete during your task execution.
Type: Long
Required: No

 ** List **   <a name="DataSync-Type-TaskExecutionFoldersFailedDetail-List"></a>
The number of directories that DataSync fails to list during your task execution.
Type: Long
Required: No

 ** Prepare **   <a name="DataSync-Type-TaskExecutionFoldersFailedDetail-Prepare"></a>
The number of directories that DataSync fails to prepare during your task execution.
Type: Long
Required: No

 ** Transfer **   <a name="DataSync-Type-TaskExecutionFoldersFailedDetail-Transfer"></a>
The number of directories that DataSync fails to transfer during your task execution.
Type: Long
Required: No

 ** Verify **   <a name="DataSync-Type-TaskExecutionFoldersFailedDetail-Verify"></a>
The number of directories that DataSync fails to verify during your task execution.
Type: Long
Required: No

## See Also
<a name="API_TaskExecutionFoldersFailedDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/TaskExecutionFoldersFailedDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/TaskExecutionFoldersFailedDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/TaskExecutionFoldersFailedDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
