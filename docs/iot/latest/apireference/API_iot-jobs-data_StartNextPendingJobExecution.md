---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_StartNextPendingJobExecution.html
---

# StartNextPendingJobExecution
<a name="API_iot-jobs-data_StartNextPendingJobExecution"></a>

Gets and starts the next pending (status IN\_PROGRESS or QUEUED) job execution for a thing.

Requires permission to access the [StartNextPendingJobExecution](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iot-jobs-data_StartNextPendingJobExecution_RequestSyntax"></a>

```
PUT /things/{{thingName}}/jobs/$next HTTP/1.1
Content-type: application/json

{
   "statusDetails": {
      "{{string}}" : "{{string}}"
   },
   "stepTimeoutInMinutes": {{number}}
}
```

## URI Request Parameters
<a name="API_iot-jobs-data_StartNextPendingJobExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [thingName](#API_iot-jobs-data_StartNextPendingJobExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_StartNextPendingJobExecution-request-uri-thingName"></a>
The name of the thing associated with the device.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_iot-jobs-data_StartNextPendingJobExecution_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [statusDetails](#API_iot-jobs-data_StartNextPendingJobExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_StartNextPendingJobExecution-request-statusDetails"></a>
A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged.
The maximum length of the value in the name/value pair is 1,024 characters.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9:_-]+`
Value Length Constraints: Minimum length of 1.
Value Pattern: `[^\p{C}]+`
Required: No

 ** [stepTimeoutInMinutes](#API_iot-jobs-data_StartNextPendingJobExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_StartNextPendingJobExecution-request-stepTimeoutInMinutes"></a>
Specifies the amount of time this device has to finish execution of this job. If the job execution status is not set to a terminal state before this timer expires, or before the timer is reset (by calling `UpdateJobExecution`, setting the status to `IN_PROGRESS`, and specifying a new timeout value in field `stepTimeoutInMinutes`) the job execution status will be automatically set to `TIMED_OUT`. Note that setting the step timeout has no effect on the in progress timeout that may have been specified when the job was created (`CreateJob` using field `timeoutConfig`).
Valid values for this parameter range from 1 to 10080 (1 minute to 7 days).
Type: Long
Required: No

## Response Syntax
<a name="API_iot-jobs-data_StartNextPendingJobExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "execution": {
      "approximateSecondsBeforeTimedOut": number,
      "executionNumber": number,
      "jobDocument": "string",
      "jobId": "string",
      "lastUpdatedAt": number,
      "queuedAt": number,
      "startedAt": number,
      "status": "string",
      "statusDetails": {
         "string" : "string"
      },
      "thingName": "string",
      "versionNumber": number
   }
}
```

## Response Elements
<a name="API_iot-jobs-data_StartNextPendingJobExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [execution](#API_iot-jobs-data_StartNextPendingJobExecution_ResponseSyntax) **   <a name="iot-iot-jobs-data_StartNextPendingJobExecution-response-execution"></a>
A JobExecution object.
Type: [JobExecution](API_iot-jobs-data_JobExecution.md) object

## Errors
<a name="API_iot-jobs-data_StartNextPendingJobExecution_Errors"></a>

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
<a name="API_iot-jobs-data_StartNextPendingJobExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-jobs-data-2017-09-29/StartNextPendingJobExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-jobs-data-2017-09-29/StartNextPendingJobExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-jobs-data-2017-09-29/StartNextPendingJobExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-jobs-data-2017-09-29/StartNextPendingJobExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-jobs-data-2017-09-29/StartNextPendingJobExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-jobs-data-2017-09-29/StartNextPendingJobExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-jobs-data-2017-09-29/StartNextPendingJobExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-jobs-data-2017-09-29/StartNextPendingJobExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-jobs-data-2017-09-29/StartNextPendingJobExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-jobs-data-2017-09-29/StartNextPendingJobExecution)
