---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListJobExecutionsForThing.html
---

# ListJobExecutionsForThing
<a name="API_ListJobExecutionsForThing"></a>

Lists the job executions for the specified thing.

Requires permission to access the [ListJobExecutionsForThing](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListJobExecutionsForThing_RequestSyntax"></a>

```
GET /things/{{thingName}}/jobs?jobId={{jobId}}&maxResults={{maxResults}}&namespaceId={{namespaceId}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListJobExecutionsForThing_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobId](#API_ListJobExecutionsForThing_RequestSyntax) **   <a name="iot-ListJobExecutionsForThing-request-uri-jobId"></a>
The unique identifier you assigned to this job when it was created.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [maxResults](#API_ListJobExecutionsForThing_RequestSyntax) **   <a name="iot-ListJobExecutionsForThing-request-uri-maxResults"></a>
The maximum number of results to be returned per request.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [namespaceId](#API_ListJobExecutionsForThing_RequestSyntax) **   <a name="iot-ListJobExecutionsForThing-request-uri-namespaceId"></a>
The namespace used to indicate that a job is a customer-managed job.
When you specify a value for this parameter, AWS IoT Core sends jobs notifications to MQTT topics that contain the value in the following format.
 `$aws/things/THING_NAME/jobs/JOB_ID/notify-namespace-NAMESPACE_ID/`
The `namespaceId` feature is only supported by AWS IoT Greengrass at this time. For more information, see [Setting up AWS IoT Greengrass core devices.](https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html)
Pattern: `[a-zA-Z0-9_-]+`

 ** [nextToken](#API_ListJobExecutionsForThing_RequestSyntax) **   <a name="iot-ListJobExecutionsForThing-request-uri-nextToken"></a>
The token to retrieve the next set of results.

 ** [status](#API_ListJobExecutionsForThing_RequestSyntax) **   <a name="iot-ListJobExecutionsForThing-request-uri-status"></a>
An optional filter that lets you search for jobs that have the specified status.
Valid Values: `QUEUED | IN_PROGRESS | SUCCEEDED | FAILED | TIMED_OUT | REJECTED | REMOVED | CANCELED`

 ** [thingName](#API_ListJobExecutionsForThing_RequestSyntax) **   <a name="iot-ListJobExecutionsForThing-request-uri-thingName"></a>
The thing name.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_ListJobExecutionsForThing_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListJobExecutionsForThing_ResponseSyntax"></a>

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
         "jobId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListJobExecutionsForThing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [executionSummaries](#API_ListJobExecutionsForThing_ResponseSyntax) **   <a name="iot-ListJobExecutionsForThing-response-executionSummaries"></a>
A list of job execution summaries.
Type: Array of [JobExecutionSummaryForThing](API_JobExecutionSummaryForThing.md) objects

 ** [nextToken](#API_ListJobExecutionsForThing_ResponseSyntax) **   <a name="iot-ListJobExecutionsForThing-response-nextToken"></a>
The token for the next set of results, or **null** if there are no additional results.
Type: String

## Errors
<a name="API_ListJobExecutionsForThing_Errors"></a>

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
<a name="API_ListJobExecutionsForThing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListJobExecutionsForThing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListJobExecutionsForThing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListJobExecutionsForThing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListJobExecutionsForThing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListJobExecutionsForThing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListJobExecutionsForThing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListJobExecutionsForThing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListJobExecutionsForThing)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListJobExecutionsForThing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListJobExecutionsForThing)
