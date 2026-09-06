---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TaskRun.html
---

# TaskRun
<a name="API_TaskRun"></a>

The sampling parameters that are associated with the machine learning transform.

## Contents
<a name="API_TaskRun_Contents"></a>

 ** CompletedOn **   <a name="Glue-Type-TaskRun-CompletedOn"></a>
The last point in time that the requested task run was completed.
Type: Timestamp
Required: No

 ** ErrorString **   <a name="Glue-Type-TaskRun-ErrorString"></a>
The list of error strings associated with this task run.
Type: String
Required: No

 ** ExecutionTime **   <a name="Glue-Type-TaskRun-ExecutionTime"></a>
The amount of time (in seconds) that the task run consumed resources.
Type: Integer
Required: No

 ** LastModifiedOn **   <a name="Glue-Type-TaskRun-LastModifiedOn"></a>
The last point in time that the requested task run was updated.
Type: Timestamp
Required: No

 ** LogGroupName **   <a name="Glue-Type-TaskRun-LogGroupName"></a>
The names of the log group for secure logging, associated with this task run.
Type: String
Required: No

 ** Properties **   <a name="Glue-Type-TaskRun-Properties"></a>
Specifies configuration properties associated with this task run.
Type: [TaskRunProperties](API_TaskRunProperties.md) object
Required: No

 ** StartedOn **   <a name="Glue-Type-TaskRun-StartedOn"></a>
The date and time that this task run started.
Type: Timestamp
Required: No

 ** Status **   <a name="Glue-Type-TaskRun-Status"></a>
The current status of the requested task run.
Type: String
Valid Values: `STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED | TIMEOUT`
Required: No

 ** TaskRunId **   <a name="Glue-Type-TaskRun-TaskRunId"></a>
The unique identifier for this task run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** TransformId **   <a name="Glue-Type-TaskRun-TransformId"></a>
The unique identifier for the transform.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_TaskRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TaskRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TaskRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TaskRun)
