---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AssociateTargetsWithJob.html
---

# AssociateTargetsWithJob
<a name="API_AssociateTargetsWithJob"></a>

Associates a group with a continuous job. The following criteria must be met:
+ The job must have been created with the `targetSelection` field set to "CONTINUOUS".
+ The job status must currently be "IN\_PROGRESS".
+ The total number of targets associated with a job must not exceed 100.

Requires permission to access the [AssociateTargetsWithJob](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_AssociateTargetsWithJob_RequestSyntax"></a>

```
POST /jobs/{{jobId}}/targets?namespaceId={{namespaceId}} HTTP/1.1
Content-type: application/json

{
   "comment": "{{string}}",
   "targets": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_AssociateTargetsWithJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobId](#API_AssociateTargetsWithJob_RequestSyntax) **   <a name="iot-AssociateTargetsWithJob-request-uri-jobId"></a>
The unique identifier you assigned to this job when it was created.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [namespaceId](#API_AssociateTargetsWithJob_RequestSyntax) **   <a name="iot-AssociateTargetsWithJob-request-uri-namespaceId"></a>
The namespace used to indicate that a job is a customer-managed job.
When you specify a value for this parameter, AWS IoT Core sends jobs notifications to MQTT topics that contain the value in the following format.
 `$aws/things/THING_NAME/jobs/JOB_ID/notify-namespace-NAMESPACE_ID/`
The `namespaceId` feature is only supported by AWS IoT Greengrass at this time. For more information, see [Setting up AWS IoT Greengrass core devices.](https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html)
Pattern: `[a-zA-Z0-9_-]+`

## Request Body
<a name="API_AssociateTargetsWithJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [comment](#API_AssociateTargetsWithJob_RequestSyntax) **   <a name="iot-AssociateTargetsWithJob-request-comment"></a>
An optional comment string describing why the job was associated with the targets.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`
Required: No

 ** [targets](#API_AssociateTargetsWithJob_RequestSyntax) **   <a name="iot-AssociateTargetsWithJob-request-targets"></a>
A list of thing group ARNs that define the targets of the job.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_AssociateTargetsWithJob_ResponseSyntax"></a>

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
<a name="API_AssociateTargetsWithJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_AssociateTargetsWithJob_ResponseSyntax) **   <a name="iot-AssociateTargetsWithJob-response-description"></a>
A short text description of the job.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`

 ** [jobArn](#API_AssociateTargetsWithJob_ResponseSyntax) **   <a name="iot-AssociateTargetsWithJob-response-jobArn"></a>
An ARN identifying the job.
Type: String

 ** [jobId](#API_AssociateTargetsWithJob_ResponseSyntax) **   <a name="iot-AssociateTargetsWithJob-response-jobId"></a>
The unique identifier you assigned to this job when it was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

## Errors
<a name="API_AssociateTargetsWithJob_Errors"></a>

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
<a name="API_AssociateTargetsWithJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/AssociateTargetsWithJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/AssociateTargetsWithJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AssociateTargetsWithJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/AssociateTargetsWithJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AssociateTargetsWithJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/AssociateTargetsWithJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/AssociateTargetsWithJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/AssociateTargetsWithJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/AssociateTargetsWithJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AssociateTargetsWithJob)
