---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetMLTaskRun.html
---

# GetMLTaskRun
<a name="API_GetMLTaskRun"></a>

Gets details for a specific task run on a machine learning transform. Machine learning task runs are asynchronous tasks that AWS Glue runs on your behalf as part of various machine learning workflows. You can check the stats of any task run by calling `GetMLTaskRun` with the `TaskRunID` and its parent transform's `TransformID`.

## Request Syntax
<a name="API_GetMLTaskRun_RequestSyntax"></a>

```
{
   "TaskRunId": "{{string}}",
   "TransformId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMLTaskRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TaskRunId](#API_GetMLTaskRun_RequestSyntax) **   <a name="Glue-GetMLTaskRun-request-TaskRunId"></a>
The unique identifier of the task run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [TransformId](#API_GetMLTaskRun_RequestSyntax) **   <a name="Glue-GetMLTaskRun-request-TransformId"></a>
The unique identifier of the machine learning transform.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetMLTaskRun_ResponseSyntax"></a>

```
{
   "CompletedOn": number,
   "ErrorString": "string",
   "ExecutionTime": number,
   "LastModifiedOn": number,
   "LogGroupName": "string",
   "Properties": {
      "ExportLabelsTaskRunProperties": {
         "OutputS3Path": "string"
      },
      "FindMatchesTaskRunProperties": {
         "JobId": "string",
         "JobName": "string",
         "JobRunId": "string"
      },
      "ImportLabelsTaskRunProperties": {
         "InputS3Path": "string",
         "Replace": boolean
      },
      "LabelingSetGenerationTaskRunProperties": {
         "OutputS3Path": "string"
      },
      "TaskType": "string"
   },
   "StartedOn": number,
   "Status": "string",
   "TaskRunId": "string",
   "TransformId": "string"
}
```

## Response Elements
<a name="API_GetMLTaskRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CompletedOn](#API_GetMLTaskRun_ResponseSyntax) **   <a name="Glue-GetMLTaskRun-response-CompletedOn"></a>
The date and time when this task run was completed.
Type: Timestamp

 ** [ErrorString](#API_GetMLTaskRun_ResponseSyntax) **   <a name="Glue-GetMLTaskRun-response-ErrorString"></a>
The error strings that are associated with the task run.
Type: String

 ** [ExecutionTime](#API_GetMLTaskRun_ResponseSyntax) **   <a name="Glue-GetMLTaskRun-response-ExecutionTime"></a>
The amount of time (in seconds) that the task run consumed resources.
Type: Integer

 ** [LastModifiedOn](#API_GetMLTaskRun_ResponseSyntax) **   <a name="Glue-GetMLTaskRun-response-LastModifiedOn"></a>
The date and time when this task run was last modified.
Type: Timestamp

 ** [LogGroupName](#API_GetMLTaskRun_ResponseSyntax) **   <a name="Glue-GetMLTaskRun-response-LogGroupName"></a>
The names of the log groups that are associated with the task run.
Type: String

 ** [Properties](#API_GetMLTaskRun_ResponseSyntax) **   <a name="Glue-GetMLTaskRun-response-Properties"></a>
The list of properties that are associated with the task run.
Type: [TaskRunProperties](API_TaskRunProperties.md) object

 ** [StartedOn](#API_GetMLTaskRun_ResponseSyntax) **   <a name="Glue-GetMLTaskRun-response-StartedOn"></a>
The date and time when this task run started.
Type: Timestamp

 ** [Status](#API_GetMLTaskRun_ResponseSyntax) **   <a name="Glue-GetMLTaskRun-response-Status"></a>
The status for this task run.
Type: String
Valid Values: `STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED | TIMEOUT`

 ** [TaskRunId](#API_GetMLTaskRun_ResponseSyntax) **   <a name="Glue-GetMLTaskRun-response-TaskRunId"></a>
The unique run identifier associated with this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [TransformId](#API_GetMLTaskRun_ResponseSyntax) **   <a name="Glue-GetMLTaskRun-response-TransformId"></a>
The unique identifier of the task run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_GetMLTaskRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetMLTaskRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetMLTaskRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetMLTaskRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetMLTaskRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetMLTaskRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetMLTaskRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetMLTaskRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetMLTaskRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetMLTaskRun)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetMLTaskRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetMLTaskRun)
