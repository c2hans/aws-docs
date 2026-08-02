---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateOTAUpdate.html
---

# CreateOTAUpdate
<a name="API_CreateOTAUpdate"></a>

Creates an AWS IoT OTA update on a target group of things or groups.

Requires permission to access the [CreateOTAUpdate](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateOTAUpdate_RequestSyntax"></a>

```
POST /otaUpdates/{{otaUpdateId}} HTTP/1.1
Content-type: application/json

{
   "additionalParameters": {
      "{{string}}" : "{{string}}"
   },
   "awsJobAbortConfig": {
      "abortCriteriaList": [
         {
            "action": "{{string}}",
            "failureType": "{{string}}",
            "minNumberOfExecutedThings": {{number}},
            "thresholdPercentage": {{number}}
         }
      ]
   },
   "awsJobExecutionsRolloutConfig": {
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
   "awsJobPresignedUrlConfig": {
      "expiresInSec": {{number}}
   },
   "awsJobTimeoutConfig": {
      "inProgressTimeoutInMinutes": {{number}}
   },
   "description": "{{string}}",
   "files": [
      {
         "attributes": {
            "{{string}}" : "{{string}}"
         },
         "codeSigning": {
            "awsSignerJobId": "{{string}}",
            "customCodeSigning": {
               "certificateChain": {
                  "certificateName": "{{string}}",
                  "inlineDocument": "{{string}}"
               },
               "hashAlgorithm": "{{string}}",
               "signature": {
                  "inlineDocument": {{blob}}
               },
               "signatureAlgorithm": "{{string}}"
            },
            "startSigningJobParameter": {
               "destination": {
                  "s3Destination": {
                     "bucket": "{{string}}",
                     "prefix": "{{string}}"
                  }
               },
               "signingProfileName": "{{string}}",
               "signingProfileParameter": {
                  "certificateArn": "{{string}}",
                  "certificatePathOnDevice": "{{string}}",
                  "platform": "{{string}}"
               }
            }
         },
         "fileLocation": {
            "s3Location": {
               "bucket": "{{string}}",
               "key": "{{string}}",
               "version": "{{string}}"
            },
            "stream": {
               "fileId": {{number}},
               "streamId": "{{string}}"
            }
         },
         "fileName": "{{string}}",
         "fileType": {{number}},
         "fileVersion": "{{string}}"
      }
   ],
   "protocols": [ "{{string}}" ],
   "roleArn": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "targets": [ "{{string}}" ],
   "targetSelection": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateOTAUpdate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [otaUpdateId](#API_CreateOTAUpdate_RequestSyntax) **   <a name="iot-CreateOTAUpdate-request-uri-otaUpdateId"></a>
The ID of the OTA update to be created.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_CreateOTAUpdate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [additionalParameters](#API_CreateOTAUpdate_RequestSyntax) **   <a name="iot-CreateOTAUpdate-request-additionalParameters"></a>
A list of additional OTA update parameters, which are name-value pairs. They won't be sent to devices as a part of the Job document.
Type: String to string map
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Value Pattern: `[\s\S]*`
Required: No

 ** [awsJobAbortConfig](#API_CreateOTAUpdate_RequestSyntax) **   <a name="iot-CreateOTAUpdate-request-awsJobAbortConfig"></a>
The criteria that determine when and how a job abort takes place.
Type: [AwsJobAbortConfig](API_AwsJobAbortConfig.md) object
Required: No

 ** [awsJobExecutionsRolloutConfig](#API_CreateOTAUpdate_RequestSyntax) **   <a name="iot-CreateOTAUpdate-request-awsJobExecutionsRolloutConfig"></a>
Configuration for the rollout of OTA updates.
Type: [AwsJobExecutionsRolloutConfig](API_AwsJobExecutionsRolloutConfig.md) object
Required: No

 ** [awsJobPresignedUrlConfig](#API_CreateOTAUpdate_RequestSyntax) **   <a name="iot-CreateOTAUpdate-request-awsJobPresignedUrlConfig"></a>
Configuration information for pre-signed URLs.
Type: [AwsJobPresignedUrlConfig](API_AwsJobPresignedUrlConfig.md) object
Required: No

 ** [awsJobTimeoutConfig](#API_CreateOTAUpdate_RequestSyntax) **   <a name="iot-CreateOTAUpdate-request-awsJobTimeoutConfig"></a>
Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to `IN_PROGRESS`. If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to `TIMED_OUT`.
Type: [AwsJobTimeoutConfig](API_AwsJobTimeoutConfig.md) object
Required: No

 ** [description](#API_CreateOTAUpdate_RequestSyntax) **   <a name="iot-CreateOTAUpdate-request-description"></a>
The description of the OTA update.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`
Required: No

 ** [files](#API_CreateOTAUpdate_RequestSyntax) **   <a name="iot-CreateOTAUpdate-request-files"></a>
The files to be streamed by the OTA update.
Type: Array of [OTAUpdateFile](API_OTAUpdateFile.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [protocols](#API_CreateOTAUpdate_RequestSyntax) **   <a name="iot-CreateOTAUpdate-request-protocols"></a>
The protocol used to transfer the OTA update image. Valid values are [HTTP], [MQTT], [HTTP, MQTT]. When both HTTP and MQTT are specified, the target device can choose the protocol.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `MQTT | HTTP`
Required: No

 ** [roleArn](#API_CreateOTAUpdate_RequestSyntax) **   <a name="iot-CreateOTAUpdate-request-roleArn"></a>
The IAM role that grants AWS IoT Core access to the Amazon S3, AWS IoT jobs and AWS Code Signing resources to create an OTA update job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** [tags](#API_CreateOTAUpdate_RequestSyntax) **   <a name="iot-CreateOTAUpdate-request-tags"></a>
Metadata which can be used to manage updates.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [targets](#API_CreateOTAUpdate_RequestSyntax) **   <a name="iot-CreateOTAUpdate-request-targets"></a>
The devices targeted to receive OTA updates.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: Yes

 ** [targetSelection](#API_CreateOTAUpdate_RequestSyntax) **   <a name="iot-CreateOTAUpdate-request-targetSelection"></a>
Specifies whether the update will continue to run (CONTINUOUS), or will be complete after all the things specified as targets have completed the update (SNAPSHOT). If continuous, the update may also be run on a thing when a change is detected in a target. For example, an update will run on a thing when the thing is added to a target group, even after the update was completed by all things originally in the group. Valid values: CONTINUOUS \| SNAPSHOT.
Type: String
Valid Values: `CONTINUOUS | SNAPSHOT`
Required: No

## Response Syntax
<a name="API_CreateOTAUpdate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "awsIotJobArn": "string",
   "awsIotJobId": "string",
   "otaUpdateArn": "string",
   "otaUpdateId": "string",
   "otaUpdateStatus": "string"
}
```

## Response Elements
<a name="API_CreateOTAUpdate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [awsIotJobArn](#API_CreateOTAUpdate_ResponseSyntax) **   <a name="iot-CreateOTAUpdate-response-awsIotJobArn"></a>
The AWS IoT job ARN associated with the OTA update.
Type: String

 ** [awsIotJobId](#API_CreateOTAUpdate_ResponseSyntax) **   <a name="iot-CreateOTAUpdate-response-awsIotJobId"></a>
The AWS IoT job ID associated with the OTA update.
Type: String

 ** [otaUpdateArn](#API_CreateOTAUpdate_ResponseSyntax) **   <a name="iot-CreateOTAUpdate-response-otaUpdateArn"></a>
The OTA update ARN.
Type: String

 ** [otaUpdateId](#API_CreateOTAUpdate_ResponseSyntax) **   <a name="iot-CreateOTAUpdate-response-otaUpdateId"></a>
The OTA update ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`

 ** [otaUpdateStatus](#API_CreateOTAUpdate_ResponseSyntax) **   <a name="iot-CreateOTAUpdate-response-otaUpdateStatus"></a>
The OTA update status.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_COMPLETE | CREATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`

## Errors
<a name="API_CreateOTAUpdate_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

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

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** message **
The message for the exception.
 ** resourceArn **
The ARN of the resource that caused the exception.
 ** resourceId **
The ID of the resource that caused the exception.
HTTP Status Code: 409

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

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_CreateOTAUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateOTAUpdate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateOTAUpdate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateOTAUpdate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateOTAUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateOTAUpdate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateOTAUpdate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateOTAUpdate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateOTAUpdate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateOTAUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateOTAUpdate)
