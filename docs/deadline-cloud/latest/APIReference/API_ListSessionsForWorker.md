---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListSessionsForWorker.html
---

# ListSessionsForWorker
<a name="API_ListSessionsForWorker"></a>

Lists sessions for a worker.

## Request Syntax
<a name="API_ListSessionsForWorker_RequestSyntax"></a>

```
GET /2023-10-12/farms/{{farmId}}/fleets/{{fleetId}}/workers/{{workerId}}/sessions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSessionsForWorker_RequestParameters"></a>

The request uses the following URI parameters.

 ** [farmId](#API_ListSessionsForWorker_RequestSyntax) **   <a name="deadlinecloud-ListSessionsForWorker-request-uri-farmId"></a>
The farm ID for the session.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** [fleetId](#API_ListSessionsForWorker_RequestSyntax) **   <a name="deadlinecloud-ListSessionsForWorker-request-uri-fleetId"></a>
The fleet ID for the session.
Pattern: `fleet-[0-9a-f]{32}`
Required: Yes

 ** [maxResults](#API_ListSessionsForWorker_RequestSyntax) **   <a name="deadlinecloud-ListSessionsForWorker-request-uri-maxResults"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListSessionsForWorker_RequestSyntax) **   <a name="deadlinecloud-ListSessionsForWorker-request-uri-nextToken"></a>
The token for the next set of results, or `null` to start from the beginning.
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [workerId](#API_ListSessionsForWorker_RequestSyntax) **   <a name="deadlinecloud-ListSessionsForWorker-request-uri-workerId"></a>
The worker ID for the session.
Pattern: `worker-[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_ListSessionsForWorker_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSessionsForWorker_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "sessions": [
      {
         "endedAt": "string",
         "jobId": "string",
         "lifecycleStatus": "string",
         "queueId": "string",
         "sessionId": "string",
         "startedAt": "string",
         "targetLifecycleStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSessionsForWorker_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSessionsForWorker_ResponseSyntax) **   <a name="deadlinecloud-ListSessionsForWorker-response-nextToken"></a>
The token for the next set of results, or `null` to start from the beginning.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [sessions](#API_ListSessionsForWorker_ResponseSyntax) **   <a name="deadlinecloud-ListSessionsForWorker-response-sessions"></a>
The sessions in the response.
Type: Array of [WorkerSessionSummary](API_WorkerSessionSummary.md) objects

## Errors
<a name="API_ListSessionsForWorker_Errors"></a>

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
<a name="API_ListSessionsForWorker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/ListSessionsForWorker)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/ListSessionsForWorker)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ListSessionsForWorker)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/ListSessionsForWorker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ListSessionsForWorker)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/ListSessionsForWorker)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/ListSessionsForWorker)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/ListSessionsForWorker)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/ListSessionsForWorker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ListSessionsForWorker)
