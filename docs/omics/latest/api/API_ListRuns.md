---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ListRuns.html
---

# ListRuns
<a name="API_ListRuns"></a>

Retrieves a list of runs and returns each run's metadata and status.

 AWS HealthOmics stores a configurable number of runs, as determined by service limits, that are available to the console and API. If the `ListRuns` response doesn't include specific runs that you expected, you can find all run logs in the CloudWatch logs. For more information about viewing the run logs, see [CloudWatch logs](https://docs.aws.amazon.com/omics/latest/dev/monitoring-cloudwatch-logs.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_ListRuns_RequestSyntax"></a>

```
GET /run?batchId={{batchId}}&maxResults={{maxResults}}&name={{name}}&runGroupId={{runGroupId}}&startingToken={{startingToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRuns_RequestParameters"></a>

The request uses the following URI parameters.

 ** [batchId](#API_ListRuns_RequestSyntax) **   <a name="omics-ListRuns-request-uri-batchId"></a>
Filter by batch ID.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [maxResults](#API_ListRuns_RequestSyntax) **   <a name="omics-ListRuns-request-uri-maxResults"></a>
The maximum number of runs to return in one page of results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [name](#API_ListRuns_RequestSyntax) **   <a name="omics-ListRuns-request-uri-name"></a>
Filter the list by run name.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [runGroupId](#API_ListRuns_RequestSyntax) **   <a name="omics-ListRuns-request-uri-runGroupId"></a>
Filter the list by run group ID.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [startingToken](#API_ListRuns_RequestSyntax) **   <a name="omics-ListRuns-request-uri-startingToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [status](#API_ListRuns_RequestSyntax) **   <a name="omics-ListRuns-request-uri-status"></a>
The status of a run.
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `PENDING | STARTING | RUNNING | STOPPING | COMPLETED | DELETED | CANCELLED | FAILED`

## Request Body
<a name="API_ListRuns_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRuns_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "batchId": "string",
         "creationTime": "string",
         "id": "string",
         "name": "string",
         "priority": number,
         "startTime": "string",
         "status": "string",
         "stopTime": "string",
         "storageCapacity": number,
         "storageType": "string",
         "workflowId": "string",
         "workflowName": "string",
         "workflowVersionName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListRuns_ResponseSyntax) **   <a name="omics-ListRuns-response-items"></a>
A list of runs.
Type: Array of [RunListItem](API_RunListItem.md) objects

 ** [nextToken](#API_ListRuns_ResponseSyntax) **   <a name="omics-ListRuns-response-nextToken"></a>
A pagination token that's included if more results are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Errors
<a name="API_ListRuns_Errors"></a>

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
<a name="API_ListRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/ListRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/ListRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ListRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/ListRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ListRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/ListRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/ListRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/ListRuns)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/ListRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ListRuns)
