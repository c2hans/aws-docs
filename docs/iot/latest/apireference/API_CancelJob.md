---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CancelJob.html
---

# CancelJob
<a name="API_CancelJob"></a>

Cancels a job.

Requires permission to access the [CancelJob](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CancelJob_RequestSyntax"></a>

```
PUT /jobs/{{jobId}}/cancel?force={{force}} HTTP/1.1
Content-type: application/json

{
   "comment": "{{string}}",
   "reasonCode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CancelJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [force](#API_CancelJob_RequestSyntax) **   <a name="iot-CancelJob-request-uri-force"></a>
(Optional) If `true` job executions with status "IN\_PROGRESS" and "QUEUED" are canceled, otherwise only job executions with status "QUEUED" are canceled. The default is `false`.
Canceling a job which is "IN\_PROGRESS", will cause a device which is executing the job to be unable to update the job execution status. Use caution and ensure that each device executing a job which is canceled is able to recover to a valid state.

 ** [jobId](#API_CancelJob_RequestSyntax) **   <a name="iot-CancelJob-request-uri-jobId"></a>
The unique identifier you assigned to this job when it was created.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_CancelJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [comment](#API_CancelJob_RequestSyntax) **   <a name="iot-CancelJob-request-comment"></a>
An optional comment string describing why the job was canceled.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`
Required: No

 ** [reasonCode](#API_CancelJob_RequestSyntax) **   <a name="iot-CancelJob-request-reasonCode"></a>
(Optional)A reason code string that explains why the job was canceled.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\p{Upper}\p{Digit}_]+`
Required: No

## Response Syntax
<a name="API_CancelJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "description": "string",
   "jobArn": "string",
   "jobId": "string"
}
```

## Response Elements
<a name="API_CancelJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_CancelJob_ResponseSyntax) **   <a name="iot-CancelJob-response-description"></a>
A short text description of the job.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`

 ** [jobArn](#API_CancelJob_ResponseSyntax) **   <a name="iot-CancelJob-response-jobArn"></a>
The job ARN.
Type: String

 ** [jobId](#API_CancelJob_ResponseSyntax) **   <a name="iot-CancelJob-response-jobId"></a>
The unique identifier you assigned to this job when it was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

## Errors
<a name="API_CancelJob_Errors"></a>

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit has been exceeded.
 ** message **
The message for the exception.
HTTP Status Code: 410

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
<a name="API_CancelJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CancelJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CancelJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CancelJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CancelJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CancelJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CancelJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CancelJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CancelJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CancelJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CancelJob)
