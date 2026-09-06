---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_GetPendingJobExecutions.html
---

# GetPendingJobExecutions
<a name="API_iot-jobs-data_GetPendingJobExecutions"></a>

Gets the list of all jobs for a thing that are not in a terminal status.

Requires permission to access the [GetPendingJobExecutions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iot-jobs-data_GetPendingJobExecutions_RequestSyntax"></a>

```
GET /things/{{thingName}}/jobs HTTP/1.1
```

## URI Request Parameters
<a name="API_iot-jobs-data_GetPendingJobExecutions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [thingName](#API_iot-jobs-data_GetPendingJobExecutions_RequestSyntax) **   <a name="iot-iot-jobs-data_GetPendingJobExecutions-request-uri-thingName"></a>
The name of the thing that is executing the job.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_iot-jobs-data_GetPendingJobExecutions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_iot-jobs-data_GetPendingJobExecutions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "inProgressJobs": [
      {
         "executionNumber": number,
         "jobId": "string",
         "lastUpdatedAt": number,
         "queuedAt": number,
         "startedAt": number,
         "versionNumber": number
      }
   ],
   "queuedJobs": [
      {
         "executionNumber": number,
         "jobId": "string",
         "lastUpdatedAt": number,
         "queuedAt": number,
         "startedAt": number,
         "versionNumber": number
      }
   ]
}
```

## Response Elements
<a name="API_iot-jobs-data_GetPendingJobExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [inProgressJobs](#API_iot-jobs-data_GetPendingJobExecutions_ResponseSyntax) **   <a name="iot-iot-jobs-data_GetPendingJobExecutions-response-inProgressJobs"></a>
A list of JobExecutionSummary objects with status IN\_PROGRESS.
Type: Array of [JobExecutionSummary](API_iot-jobs-data_JobExecutionSummary.md) objects

 ** [queuedJobs](#API_iot-jobs-data_GetPendingJobExecutions_ResponseSyntax) **   <a name="iot-iot-jobs-data_GetPendingJobExecutions-response-queuedJobs"></a>
A list of JobExecutionSummary objects with status QUEUED.
Type: Array of [JobExecutionSummary](API_iot-jobs-data_JobExecutionSummary.md) objects

## Errors
<a name="API_iot-jobs-data_GetPendingJobExecutions_Errors"></a>

 ** CertificateValidationException **
The certificate is invalid.
 ** message **
Additional information about the exception.
HTTP Status Code: 400

 ** InvalidRequestException **
The contents of the request were invalid.
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
The message associated with the exception.
 ** payload **
The payload associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_iot-jobs-data_GetPendingJobExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-jobs-data-2017-09-29/GetPendingJobExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-jobs-data-2017-09-29/GetPendingJobExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-jobs-data-2017-09-29/GetPendingJobExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-jobs-data-2017-09-29/GetPendingJobExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-jobs-data-2017-09-29/GetPendingJobExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-jobs-data-2017-09-29/GetPendingJobExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-jobs-data-2017-09-29/GetPendingJobExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-jobs-data-2017-09-29/GetPendingJobExecutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-jobs-data-2017-09-29/GetPendingJobExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-jobs-data-2017-09-29/GetPendingJobExecutions)
