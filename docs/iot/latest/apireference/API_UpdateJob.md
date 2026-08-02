---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateJob.html
---

# UpdateJob
<a name="API_UpdateJob"></a>

Updates supported fields of the specified job.

Requires permission to access the [UpdateJob](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateJob_RequestSyntax"></a>

```
PATCH /jobs/{{jobId}}?namespaceId={{namespaceId}} HTTP/1.1
Content-type: application/json

{
   "abortConfig": {
      "criteriaList": [
         {
            "action": "{{string}}",
            "failureType": "{{string}}",
            "minNumberOfExecutedThings": {{number}},
            "thresholdPercentage": {{number}}
         }
      ]
   },
   "description": "{{string}}",
   "jobExecutionsRetryConfig": {
      "criteriaList": [
         {
            "failureType": "{{string}}",
            "numberOfRetries": {{number}}
         }
      ]
   },
   "jobExecutionsRolloutConfig": {
      "exponentialRate": {
         "baseRatePerMinute": {{number}},
         "incrementFactor": {{number}},
         "rateIncreaseCriteria": {
            "numberOfNotifiedThings": {{number}},
            "numberOfSucceededThings": {{number}}
         }
      },
      "maximumPerMinute": {{number}}
   },
   "presignedUrlConfig": {
      "expiresInSec": {{number}},
      "roleArn": "{{string}}"
   },
   "timeoutConfig": {
      "inProgressTimeoutInMinutes": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobId](#API_UpdateJob_RequestSyntax) **   <a name="iot-UpdateJob-request-uri-jobId"></a>
The ID of the job to be updated.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [namespaceId](#API_UpdateJob_RequestSyntax) **   <a name="iot-UpdateJob-request-uri-namespaceId"></a>
The namespace used to indicate that a job is a customer-managed job.
When you specify a value for this parameter, AWS IoT Core sends jobs notifications to MQTT topics that contain the value in the following format.
 `$aws/things/THING_NAME/jobs/JOB_ID/notify-namespace-NAMESPACE_ID/`
The `namespaceId` feature is only supported by AWS IoT Greengrass at this time. For more information, see [Setting up AWS IoT Greengrass core devices.](https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html)
Pattern: `[a-zA-Z0-9_-]+`

## Request Body
<a name="API_UpdateJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [abortConfig](#API_UpdateJob_RequestSyntax) **   <a name="iot-UpdateJob-request-abortConfig"></a>
Allows you to create criteria to abort a job.
Type: [AbortConfig](API_AbortConfig.md) object
Required: No

 ** [description](#API_UpdateJob_RequestSyntax) **   <a name="iot-UpdateJob-request-description"></a>
A short text description of the job.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`
Required: No

 ** [jobExecutionsRetryConfig](#API_UpdateJob_RequestSyntax) **   <a name="iot-UpdateJob-request-jobExecutionsRetryConfig"></a>
Allows you to create the criteria to retry a job.
Type: [JobExecutionsRetryConfig](API_JobExecutionsRetryConfig.md) object
Required: No

 ** [jobExecutionsRolloutConfig](#API_UpdateJob_RequestSyntax) **   <a name="iot-UpdateJob-request-jobExecutionsRolloutConfig"></a>
Allows you to create a staged rollout of the job.
Type: [JobExecutionsRolloutConfig](API_JobExecutionsRolloutConfig.md) object
Required: No

 ** [presignedUrlConfig](#API_UpdateJob_RequestSyntax) **   <a name="iot-UpdateJob-request-presignedUrlConfig"></a>
Configuration information for pre-signed S3 URLs.
Type: [PresignedUrlConfig](API_PresignedUrlConfig.md) object
Required: No

 ** [timeoutConfig](#API_UpdateJob_RequestSyntax) **   <a name="iot-UpdateJob-request-timeoutConfig"></a>
Specifies the amount of time each device has to finish its execution of the job. The timer is started when the job execution status is set to `IN_PROGRESS`. If the job execution status is not set to another terminal state before the time expires, it will be automatically set to `TIMED_OUT`.
Type: [TimeoutConfig](API_TimeoutConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdateJob_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateJob_Errors"></a>

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
<a name="API_UpdateJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateJob)
