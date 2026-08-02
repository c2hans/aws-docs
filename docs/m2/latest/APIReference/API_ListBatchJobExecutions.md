---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_ListBatchJobExecutions.html
---

# ListBatchJobExecutions
<a name="API_ListBatchJobExecutions"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Lists historical, current, and scheduled batch job executions for a specific application.

## Request Syntax
<a name="API_ListBatchJobExecutions_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/batch-job-executions?executionIds={{executionIds}}&jobName={{jobName}}&maxResults={{maxResults}}&nextToken={{nextToken}}&startedAfter={{startedAfter}}&startedBefore={{startedBefore}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListBatchJobExecutions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_ListBatchJobExecutions_RequestSyntax) **   <a name="m2-ListBatchJobExecutions-request-uri-applicationId"></a>
The unique identifier of the application.
Pattern: `\S{1,80}`
Required: Yes

 ** [executionIds](#API_ListBatchJobExecutions_RequestSyntax) **   <a name="m2-ListBatchJobExecutions-request-uri-executionIds"></a>
The unique identifier of each batch job execution.
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `\S{1,80}`

 ** [jobName](#API_ListBatchJobExecutions_RequestSyntax) **   <a name="m2-ListBatchJobExecutions-request-uri-jobName"></a>
The name of each batch job execution.
Pattern: `\S{1,100}`

 ** [maxResults](#API_ListBatchJobExecutions_RequestSyntax) **   <a name="m2-ListBatchJobExecutions-request-uri-maxResults"></a>
The maximum number of batch job executions to return.
Valid Range: Minimum value of 1. Maximum value of 2000.

 ** [nextToken](#API_ListBatchJobExecutions_RequestSyntax) **   <a name="m2-ListBatchJobExecutions-request-uri-nextToken"></a>
A pagination token to control the number of batch job executions displayed in the list.
Pattern: `\S{1,2000}`

 ** [startedAfter](#API_ListBatchJobExecutions_RequestSyntax) **   <a name="m2-ListBatchJobExecutions-request-uri-startedAfter"></a>
The time after which the batch job executions started.

 ** [startedBefore](#API_ListBatchJobExecutions_RequestSyntax) **   <a name="m2-ListBatchJobExecutions-request-uri-startedBefore"></a>
The time before the batch job executions started.

 ** [status](#API_ListBatchJobExecutions_RequestSyntax) **   <a name="m2-ListBatchJobExecutions-request-uri-status"></a>
The status of the batch job executions.
Valid Values: `Submitting | Holding | Dispatching | Running | Cancelling | Cancelled | Succeeded | Failed | Purged | Succeeded With Warning`

## Request Body
<a name="API_ListBatchJobExecutions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBatchJobExecutions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "batchJobExecutions": [
      {
         "applicationId": "string",
         "batchJobIdentifier": { ... },
         "endTime": number,
         "executionId": "string",
         "jobId": "string",
         "jobName": "string",
         "jobType": "string",
         "returnCode": "string",
         "startTime": number,
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBatchJobExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [batchJobExecutions](#API_ListBatchJobExecutions_ResponseSyntax) **   <a name="m2-ListBatchJobExecutions-response-batchJobExecutions"></a>
Returns a list of batch job executions for an application.
Type: Array of [BatchJobExecutionSummary](API_BatchJobExecutionSummary.md) objects

 ** [nextToken](#API_ListBatchJobExecutions_ResponseSyntax) **   <a name="m2-ListBatchJobExecutions-response-nextToken"></a>
A pagination token that's returned when the response doesn't contain all batch job executions.
Type: String
Pattern: `\S{1,2000}`

## Errors
<a name="API_ListBatchJobExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The account or role doesn't have the right permissions to make the request.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** resourceId **
The ID of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ThrottlingException **
The number of requests made exceeds the limit.
 ** quotaCode **
The identifier of the throttled request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
 ** serviceCode **
The identifier of the service that the throttled request was made to.
HTTP Status Code: 429

 ** ValidationException **
One or more parameters provided in the request is not valid.
 ** fieldList **
The list of fields that failed service validation.
 ** reason **
The reason why it failed service validation.
HTTP Status Code: 400

## See Also
<a name="API_ListBatchJobExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/ListBatchJobExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/ListBatchJobExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/ListBatchJobExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/ListBatchJobExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/ListBatchJobExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/ListBatchJobExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/ListBatchJobExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/ListBatchJobExecutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/ListBatchJobExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/ListBatchJobExecutions)
