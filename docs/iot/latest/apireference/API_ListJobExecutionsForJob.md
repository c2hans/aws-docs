---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListJobExecutionsForJob.html
---

# ListJobExecutionsForJob
<a name="API_ListJobExecutionsForJob"></a>

Lists the job executions for a job.

Requires permission to access the [ListJobExecutionsForJob](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListJobExecutionsForJob_RequestSyntax"></a>

```
GET /jobs/{{jobId}}/things?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListJobExecutionsForJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobId](#API_ListJobExecutionsForJob_RequestSyntax) **   <a name="iot-ListJobExecutionsForJob-request-uri-jobId"></a>
The unique identifier you assigned to this job when it was created.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [maxResults](#API_ListJobExecutionsForJob_RequestSyntax) **   <a name="iot-ListJobExecutionsForJob-request-uri-maxResults"></a>
The maximum number of results to be returned per request.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListJobExecutionsForJob_RequestSyntax) **   <a name="iot-ListJobExecutionsForJob-request-uri-nextToken"></a>
The token to retrieve the next set of results.

 ** [status](#API_ListJobExecutionsForJob_RequestSyntax) **   <a name="iot-ListJobExecutionsForJob-request-uri-status"></a>
The status of the job.
Valid Values: `QUEUED | IN_PROGRESS | SUCCEEDED | FAILED | TIMED_OUT | REJECTED | REMOVED | CANCELED`

## Request Body
<a name="API_ListJobExecutionsForJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListJobExecutionsForJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "executionSummaries": [
      {
         "jobExecutionSummary": {
            "executionNumber": number,
            "lastUpdatedAt": number,
            "queuedAt": number,
            "retryAttempt": number,
            "startedAt": number,
            "status": "string"
         },
         "thingArn": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListJobExecutionsForJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [executionSummaries](#API_ListJobExecutionsForJob_ResponseSyntax) **   <a name="iot-ListJobExecutionsForJob-response-executionSummaries"></a>
A list of job execution summaries.
Type: Array of [JobExecutionSummaryForJob](API_JobExecutionSummaryForJob.md) objects

 ** [nextToken](#API_ListJobExecutionsForJob_ResponseSyntax) **   <a name="iot-ListJobExecutionsForJob-response-nextToken"></a>
The token for the next set of results, or **null** if there are no additional results.
Type: String

## Errors
<a name="API_ListJobExecutionsForJob_Errors"></a>

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListJobExecutionsForJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListJobExecutionsForJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListJobExecutionsForJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListJobExecutionsForJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListJobExecutionsForJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListJobExecutionsForJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListJobExecutionsForJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListJobExecutionsForJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListJobExecutionsForJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListJobExecutionsForJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListJobExecutionsForJob)
