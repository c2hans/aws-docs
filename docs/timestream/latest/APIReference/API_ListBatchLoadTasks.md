---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_ListBatchLoadTasks.html
---

# ListBatchLoadTasks
<a name="API_ListBatchLoadTasks"></a>

Provides a list of batch load tasks, along with the name, status, when the task is resumable until, and other details. See [code sample](https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.list-batch-load-tasks.html) for details.

## Request Syntax
<a name="API_ListBatchLoadTasks_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TaskStatus": "{{string}}"
}
```

## Request Parameters
<a name="API_ListBatchLoadTasks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListBatchLoadTasks_RequestSyntax) **   <a name="timestream-ListBatchLoadTasks-request-MaxResults"></a>
The total number of items to return in the output. If the total number of items available is more than the value specified, a NextToken is provided in the output. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListBatchLoadTasks_RequestSyntax) **   <a name="timestream-ListBatchLoadTasks-request-NextToken"></a>
A token to specify where to start paginating. This is the NextToken from a previously truncated response.
Type: String
Required: No

 ** [TaskStatus](#API_ListBatchLoadTasks_RequestSyntax) **   <a name="timestream-ListBatchLoadTasks-request-TaskStatus"></a>
Status of the batch load task.
Type: String
Valid Values: `CREATED | IN_PROGRESS | FAILED | SUCCEEDED | PROGRESS_STOPPED | PENDING_RESUME`
Required: No

## Response Syntax
<a name="API_ListBatchLoadTasks_ResponseSyntax"></a>

```
{
   "BatchLoadTasks": [
      {
         "CreationTime": number,
         "DatabaseName": "string",
         "LastUpdatedTime": number,
         "ResumableUntil": number,
         "TableName": "string",
         "TaskId": "string",
         "TaskStatus": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListBatchLoadTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BatchLoadTasks](#API_ListBatchLoadTasks_ResponseSyntax) **   <a name="timestream-ListBatchLoadTasks-response-BatchLoadTasks"></a>
A list of batch load task details.
Type: Array of [BatchLoadTask](API_BatchLoadTask.md) objects

 ** [NextToken](#API_ListBatchLoadTasks_ResponseSyntax) **   <a name="timestream-ListBatchLoadTasks-response-NextToken"></a>
A token to specify where to start paginating. Provide the next ListBatchLoadTasksRequest.
Type: String

## Errors
<a name="API_ListBatchLoadTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
 Timestream was unable to fully process this request because of an internal server error.
HTTP Status Code: 500

 ** InvalidEndpointException **
The requested endpoint was not valid.
HTTP Status Code: 400

 ** ThrottlingException **
 Too many requests were made by a user and they exceeded the service quotas. The request was throttled.
HTTP Status Code: 400

 ** ValidationException **
 An invalid or malformed request.
HTTP Status Code: 400

## See Also
<a name="API_ListBatchLoadTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-write-2018-11-01/ListBatchLoadTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-write-2018-11-01/ListBatchLoadTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/ListBatchLoadTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-write-2018-11-01/ListBatchLoadTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/ListBatchLoadTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-write-2018-11-01/ListBatchLoadTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-write-2018-11-01/ListBatchLoadTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-write-2018-11-01/ListBatchLoadTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-write-2018-11-01/ListBatchLoadTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/ListBatchLoadTasks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
