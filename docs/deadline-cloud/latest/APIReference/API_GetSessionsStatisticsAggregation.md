---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetSessionsStatisticsAggregation.html
---

# GetSessionsStatisticsAggregation
<a name="API_GetSessionsStatisticsAggregation"></a>

Gets a set of statistics for queues or farms. Before you can call the `GetSessionStatisticsAggregation` operation, you must first call the `StartSessionsStatisticsAggregation` operation. Statistics are available for 1 hour after you call the `StartSessionsStatisticsAggregation` operation.

## Request Syntax
<a name="API_GetSessionsStatisticsAggregation_RequestSyntax"></a>

```
GET /2023-10-12/farms/{{farmId}}/sessions-statistics-aggregation?aggregationId={{aggregationId}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSessionsStatisticsAggregation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [aggregationId](#API_GetSessionsStatisticsAggregation_RequestSyntax) **   <a name="deadlinecloud-GetSessionsStatisticsAggregation-request-uri-aggregationId"></a>
The identifier returned by the `StartSessionsStatisticsAggregation` operation that identifies the aggregated statistics.
Pattern: `[0-9a-f]{32}`
Required: Yes

 ** [farmId](#API_GetSessionsStatisticsAggregation_RequestSyntax) **   <a name="deadlinecloud-GetSessionsStatisticsAggregation-request-uri-farmId"></a>
The identifier of the farm to include in the statistics. This should be the same as the farm ID used in the call to the `StartSessionsStatisticsAggregation` operation.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** [maxResults](#API_GetSessionsStatisticsAggregation_RequestSyntax) **   <a name="deadlinecloud-GetSessionsStatisticsAggregation-request-uri-maxResults"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_GetSessionsStatisticsAggregation_RequestSyntax) **   <a name="deadlinecloud-GetSessionsStatisticsAggregation-request-uri-nextToken"></a>
The token for the next set of results, or `null` to start from the beginning.
Length Constraints: Minimum length of 0. Maximum length of 4096.

## Request Body
<a name="API_GetSessionsStatisticsAggregation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSessionsStatisticsAggregation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "statistics": [
      {
         "aggregationEndTime": "string",
         "aggregationStartTime": "string",
         "costInUsd": {
            "avg": number,
            "max": number,
            "min": number,
            "sum": number
         },
         "count": number,
         "fleetId": "string",
         "instanceType": "string",
         "jobId": "string",
         "jobName": "string",
         "licenseProduct": "string",
         "queueId": "string",
         "runtimeInSeconds": {
            "avg": number,
            "max": number,
            "min": number,
            "sum": number
         },
         "usageType": "string",
         "userId": "string"
      }
   ],
   "status": "string",
   "statusMessage": "string"
}
```

## Response Elements
<a name="API_GetSessionsStatisticsAggregation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetSessionsStatisticsAggregation_ResponseSyntax) **   <a name="deadlinecloud-GetSessionsStatisticsAggregation-response-nextToken"></a>
If Deadline Cloud returns `nextToken`, then there are more results available. The value of `nextToken` is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then `nextToken` is set to `null`. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 `ValidationException` error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [statistics](#API_GetSessionsStatisticsAggregation_ResponseSyntax) **   <a name="deadlinecloud-GetSessionsStatisticsAggregation-response-statistics"></a>
The statistics for the specified fleets or queues.
Type: Array of [Statistics](API_Statistics.md) objects

 ** [status](#API_GetSessionsStatisticsAggregation_ResponseSyntax) **   <a name="deadlinecloud-GetSessionsStatisticsAggregation-response-status"></a>
The status of the aggregated results. An aggregation may fail or time out if the results are too large. If this happens, you can call the `StartSessionsStatisticsAggregation` operation after you reduce the aggregation time frame, reduce the number of queues or fleets in the aggregation, or increase the period length.
If you call the `StartSessionsStatisticsAggregation ` operation when the status is `IN_PROGRESS`, you will receive a `ThrottlingException`.
Type: String
Valid Values: `IN_PROGRESS | TIMEOUT | FAILED | COMPLETED`

 ** [statusMessage](#API_GetSessionsStatisticsAggregation_ResponseSyntax) **   <a name="deadlinecloud-GetSessionsStatisticsAggregation-response-statusMessage"></a>
A message that describes the status.
Type: String

## Errors
<a name="API_GetSessionsStatisticsAggregation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
 ** context **
Information about the resources in use when the exception was thrown.
HTTP Status Code: 403

 ** InternalServerErrorException **
Deadline Cloud can't process your request right now. Try again later.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** context **
Information about the resources in use when the exception was thrown.
 ** resourceId **
The identifier of the resource that couldn't be found.
 ** resourceType **
The type of the resource that couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a request rate quota.
 ** context **
Information about the resources in use when the exception was thrown.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service that is being throttled.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** context **
Information about the resources in use when the exception was thrown.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_GetSessionsStatisticsAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetSessionsStatisticsAggregation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/GetSessionsStatisticsAggregation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetSessionsStatisticsAggregation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetSessionsStatisticsAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetSessionsStatisticsAggregation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetSessionsStatisticsAggregation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetSessionsStatisticsAggregation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetSessionsStatisticsAggregation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetSessionsStatisticsAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetSessionsStatisticsAggregation)
