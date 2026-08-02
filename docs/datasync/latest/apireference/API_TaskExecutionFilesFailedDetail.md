---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_TaskExecutionFilesFailedDetail.html
---

# TaskExecutionFilesFailedDetail
<a name="API_TaskExecutionFilesFailedDetail"></a>

The number of files or objects that DataSync fails to prepare, transfer, verify, and delete during your task execution.

**Note**
Applies only to [Enhanced mode tasks](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html).

## Contents
<a name="API_TaskExecutionFilesFailedDetail_Contents"></a>

 ** Delete **   <a name="DataSync-Type-TaskExecutionFilesFailedDetail-Delete"></a>
The number of files or objects that DataSync fails to delete during your task execution.
Type: Long
Required: No

 ** Prepare **   <a name="DataSync-Type-TaskExecutionFilesFailedDetail-Prepare"></a>
The number of files or objects that DataSync fails to prepare during your task execution.
Type: Long
Required: No

 ** Transfer **   <a name="DataSync-Type-TaskExecutionFilesFailedDetail-Transfer"></a>
The number of files or objects that DataSync fails to transfer during your task execution.
Type: Long
Required: No

 ** Verify **   <a name="DataSync-Type-TaskExecutionFilesFailedDetail-Verify"></a>
The number of files or objects that DataSync fails to verify during your task execution.
Type: Long
Required: No

## See Also
<a name="API_TaskExecutionFilesFailedDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/TaskExecutionFilesFailedDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/TaskExecutionFilesFailedDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/TaskExecutionFilesFailedDetail)
