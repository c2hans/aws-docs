---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateJobTemplate.html
---

# CreateJobTemplate
<a name="API_CreateJobTemplate"></a>

Creates a job template.

Requires permission to access the [CreateJobTemplate](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateJobTemplate_RequestSyntax"></a>

```
PUT /job-templates/{{jobTemplateId}} HTTP/1.1
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
   "destinationPackageVersions": [ "{{string}}" ],
   "document": "{{string}}",
   "documentSource": "{{string}}",
   "jobArn": "{{string}}",
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
   "maintenanceWindows": [
      {
         "durationInMinutes": {{number}},
         "startTime": "{{string}}"
      }
   ],
   "presignedUrlConfig": {
      "expiresInSec": {{number}},
      "roleArn": "{{string}}"
   },
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "timeoutConfig": {
      "inProgressTimeoutInMinutes": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_CreateJobTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobTemplateId](#API_CreateJobTemplate_RequestSyntax) **   <a name="iot-CreateJobTemplate-request-uri-jobTemplateId"></a>
A unique identifier for the job template. We recommend using a UUID. Alpha-numeric characters, "-", and "\_" are valid for use here.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_CreateJobTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [abortConfig](#API_CreateJobTemplate_RequestSyntax) **   <a name="iot-CreateJobTemplate-request-abortConfig"></a>
The criteria that determine when and how a job abort takes place.
Type: [AbortConfig](API_AbortConfig.md) object
Required: No

 ** [description](#API_CreateJobTemplate_RequestSyntax) **   <a name="iot-CreateJobTemplate-request-description"></a>
A description of the job document.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`
Required: Yes

 ** [destinationPackageVersions](#API_CreateJobTemplate_RequestSyntax) **   <a name="iot-CreateJobTemplate-request-destinationPackageVersions"></a>
The package version Amazon Resource Names (ARNs) that are installed on the device when the job successfully completes. The package version must be in either the Published or Deprecated state when the job deploys. For more information, see [Package version lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle).
 **Note:**The following Length Constraints relates to a single ARN. Up to 25 package version ARNs are allowed.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:[!-~]+$`
Required: No

 ** [document](#API_CreateJobTemplate_RequestSyntax) **   <a name="iot-CreateJobTemplate-request-document"></a>
The job document. Required if you don't specify a value for `documentSource`.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** [documentSource](#API_CreateJobTemplate_RequestSyntax) **   <a name="iot-CreateJobTemplate-request-documentSource"></a>
An S3 link, or S3 object URL, to the job document. The link is an Amazon S3 object URL and is required if you don't specify a value for `document`.
For example, `--document-source https://s3.region-code.amazonaws.com/example-firmware/device-firmware.1.0`
For more information, see [Methods for accessing a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-bucket-intro.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1350.
Required: No

 ** [jobArn](#API_CreateJobTemplate_RequestSyntax) **   <a name="iot-CreateJobTemplate-request-jobArn"></a>
The ARN of the job to use as the basis for the job template.
Type: String
Required: No

 ** [jobExecutionsRetryConfig](#API_CreateJobTemplate_RequestSyntax) **   <a name="iot-CreateJobTemplate-request-jobExecutionsRetryConfig"></a>
Allows you to create the criteria to retry a job.
Type: [JobExecutionsRetryConfig](API_JobExecutionsRetryConfig.md) object
Required: No

 ** [jobExecutionsRolloutConfig](#API_CreateJobTemplate_RequestSyntax) **   <a name="iot-CreateJobTemplate-request-jobExecutionsRolloutConfig"></a>
Allows you to create a staged rollout of a job.
Type: [JobExecutionsRolloutConfig](API_JobExecutionsRolloutConfig.md) object
Required: No

 ** [maintenanceWindows](#API_CreateJobTemplate_RequestSyntax) **   <a name="iot-CreateJobTemplate-request-maintenanceWindows"></a>
Allows you to configure an optional maintenance window for the rollout of a job document to all devices in the target group for a job.
Type: Array of [MaintenanceWindow](API_MaintenanceWindow.md) objects
Required: No

 ** [presignedUrlConfig](#API_CreateJobTemplate_RequestSyntax) **   <a name="iot-CreateJobTemplate-request-presignedUrlConfig"></a>
Configuration for pre-signed S3 URLs.
Type: [PresignedUrlConfig](API_PresignedUrlConfig.md) object
Required: No

 ** [tags](#API_CreateJobTemplate_RequestSyntax) **   <a name="iot-CreateJobTemplate-request-tags"></a>
Metadata that can be used to manage the job template.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [timeoutConfig](#API_CreateJobTemplate_RequestSyntax) **   <a name="iot-CreateJobTemplate-request-timeoutConfig"></a>
Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to `IN_PROGRESS`. If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to `TIMED_OUT`.
Type: [TimeoutConfig](API_TimeoutConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateJobTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobTemplateArn": "string",
   "jobTemplateId": "string"
}
```

## Response Elements
<a name="API_CreateJobTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobTemplateArn](#API_CreateJobTemplate_ResponseSyntax) **   <a name="iot-CreateJobTemplate-response-jobTemplateArn"></a>
The ARN of the job template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:[!-~]+$`

 ** [jobTemplateId](#API_CreateJobTemplate_ResponseSyntax) **   <a name="iot-CreateJobTemplate-response-jobTemplateId"></a>
The unique identifier of the job template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

## Errors
<a name="API_CreateJobTemplate_Errors"></a>

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** resourceId **
A resource with the same name already exists.
HTTP Status Code: 409

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

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateJobTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateJobTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateJobTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateJobTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateJobTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateJobTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateJobTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateJobTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateJobTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateJobTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateJobTemplate)
