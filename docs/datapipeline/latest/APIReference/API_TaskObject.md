---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_TaskObject.html
---

# TaskObject
<a name="API_TaskObject"></a>

Contains information about a pipeline task that is assigned to a task runner.

## Contents
<a name="API_TaskObject_Contents"></a>

 ** attemptId **   <a name="DP-Type-TaskObject-attemptId"></a>
The ID of the pipeline task attempt object. AWS Data Pipeline uses this value to track how many times a task is attempted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: No

 ** objects **   <a name="DP-Type-TaskObject-objects"></a>
Connection information for the location where the task runner will publish the output of the task.
Type: String to [PipelineObject](API_PipelineObject.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 1024.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: No

 ** pipelineId **   <a name="DP-Type-TaskObject-pipelineId"></a>
The ID of the pipeline that provided the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: No

 ** taskId **   <a name="DP-Type-TaskObject-taskId"></a>
An internal identifier for the task. This ID is passed to the [SetTaskStatus](API_SetTaskStatus.md) and [ReportTaskProgress](API_ReportTaskProgress.md) actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_TaskObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/TaskObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/TaskObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/TaskObject)
