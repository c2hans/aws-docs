---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetMLTaskRuns.html
---

# GetMLTaskRuns
<a name="API_GetMLTaskRuns"></a>

Gets a list of runs for a machine learning transform. Machine learning task runs are asynchronous tasks that AWS Glue runs on your behalf as part of various machine learning workflows. You can get a sortable, filterable list of machine learning task runs by calling `GetMLTaskRuns` with their parent transform's `TransformID` and other optional parameters as documented in this section.

This operation returns a list of historic runs and must be paginated.

## Request Syntax
<a name="API_GetMLTaskRuns_RequestSyntax"></a>

```
{
   "Filter": {
      "StartedAfter": {{number}},
      "StartedBefore": {{number}},
      "Status": "{{string}}",
      "TaskRunType": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Sort": {
      "Column": "{{string}}",
      "SortDirection": "{{string}}"
   },
   "TransformId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMLTaskRuns_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_GetMLTaskRuns_RequestSyntax) **   <a name="Glue-GetMLTaskRuns-request-Filter"></a>
The filter criteria, in the `TaskRunFilterCriteria` structure, for the task run.
Type: [TaskRunFilterCriteria](API_TaskRunFilterCriteria.md) object
Required: No

 ** [MaxResults](#API_GetMLTaskRuns_RequestSyntax) **   <a name="Glue-GetMLTaskRuns-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetMLTaskRuns_RequestSyntax) **   <a name="Glue-GetMLTaskRuns-request-NextToken"></a>
A token for pagination of the results. The default is empty.
Type: String
Required: No

 ** [Sort](#API_GetMLTaskRuns_RequestSyntax) **   <a name="Glue-GetMLTaskRuns-request-Sort"></a>
The sorting criteria, in the `TaskRunSortCriteria` structure, for the task run.
Type: [TaskRunSortCriteria](API_TaskRunSortCriteria.md) object
Required: No

 ** [TransformId](#API_GetMLTaskRuns_RequestSyntax) **   <a name="Glue-GetMLTaskRuns-request-TransformId"></a>
The unique identifier of the machine learning transform.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetMLTaskRuns_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TaskRuns": [
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
   ]
}
```

## Response Elements
<a name="API_GetMLTaskRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetMLTaskRuns_ResponseSyntax) **   <a name="Glue-GetMLTaskRuns-response-NextToken"></a>
A pagination token, if more results are available.
Type: String

 ** [TaskRuns](#API_GetMLTaskRuns_ResponseSyntax) **   <a name="Glue-GetMLTaskRuns-response-TaskRuns"></a>
A list of task runs that are associated with the transform.
Type: Array of [TaskRun](API_TaskRun.md) objects

## Errors
<a name="API_GetMLTaskRuns_Errors"></a>

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
<a name="API_GetMLTaskRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetMLTaskRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetMLTaskRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetMLTaskRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetMLTaskRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetMLTaskRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetMLTaskRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetMLTaskRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetMLTaskRuns)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetMLTaskRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetMLTaskRuns)
