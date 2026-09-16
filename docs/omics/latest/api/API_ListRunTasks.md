---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ListRunTasks.html
---

# ListRunTasks
<a name="API_ListRunTasks"></a>

Returns a list of tasks and status information within their specified run. Use this operation to monitor runs and to identify which specific tasks have failed.

## Request Syntax
<a name="API_ListRunTasks_RequestSyntax"></a>

```
GET /run/{{id}}/task?maxResults={{maxResults}}&startingToken={{startingToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRunTasks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_ListRunTasks_RequestSyntax) **   <a name="omics-ListRunTasks-request-uri-id"></a>
The run's ID.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

 ** [maxResults](#API_ListRunTasks_RequestSyntax) **   <a name="omics-ListRunTasks-request-uri-maxResults"></a>
The maximum number of run tasks to return in one page of results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [startingToken](#API_ListRunTasks_RequestSyntax) **   <a name="omics-ListRunTasks-request-uri-startingToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [status](#API_ListRunTasks_RequestSyntax) **   <a name="omics-ListRunTasks-request-uri-status"></a>
Filter the list by status.
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `PENDING | STARTING | RUNNING | STOPPING | COMPLETED | CANCELLED | FAILED`

## Request Body
<a name="API_ListRunTasks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRunTasks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "cacheHit": boolean,
         "cacheS3Uri": "string",
         "cpus": number,
         "creationTime": "string",
         "gpus": number,
         "instanceType": "string",
         "memory": number,
         "name": "string",
         "startTime": "string",
         "status": "string",
         "stopTime": "string",
         "taskId": "string",
         "uuid": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListRunTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListRunTasks_ResponseSyntax) **   <a name="omics-ListRunTasks-response-items"></a>
A list of tasks.
Type: Array of [TaskListItem](API_TaskListItem.md) objects

 ** [nextToken](#API_ListRunTasks_ResponseSyntax) **   <a name="omics-ListRunTasks-response-nextToken"></a>
A pagination token that's included if more results are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Errors
<a name="API_ListRunTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request cannot be applied to the target resource in its current state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListRunTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/ListRunTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/ListRunTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ListRunTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/ListRunTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ListRunTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/ListRunTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/ListRunTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/ListRunTasks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/ListRunTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ListRunTasks)
