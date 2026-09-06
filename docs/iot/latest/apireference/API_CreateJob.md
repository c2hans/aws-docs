---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateJob.html
---

# CreateJob
<a name="API_CreateJob"></a>

Creates a job.

Requires permission to access the [CreateJob](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateJob_RequestSyntax"></a>

```
PUT /jobs/{{jobId}} HTTP/1.1
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
   "documentParameters": {
      "{{string}}" : "{{string}}"
   },
   "documentSource": "{{string}}",
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
   "jobTemplateArn": "{{string}}",
   "namespaceId": "{{string}}",
   "presignedUrlConfig": {
      "expiresInSec": {{number}},
      "roleArn": "{{string}}"
   },
   "schedulingConfig": {
      "endBehavior": "{{string}}",
      "endTime": "{{string}}",
      "maintenanceWindows": [
         {
            "durationInMinutes": {{number}},
            "startTime": "{{string}}"
         }
      ],
      "startTime": "{{string}}"
   },
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "targets": [ "{{string}}" ],
   "targetSelection": "{{string}}",
   "timeoutConfig": {
      "inProgressTimeoutInMinutes": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_CreateJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobId](#API_CreateJob_RequestSyntax) **   <a name="iot-CreateJob-request-uri-jobId"></a>
A job identifier which must be unique for your account. We recommend using a UUID. Alpha-numeric characters, "-" and "\_" are valid for use here.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_CreateJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [abortConfig](#API_CreateJob_RequestSyntax) **   <a name="iot-CreateJob-request-abortConfig"></a>
Allows you to create the criteria to abort a job.
Type: [AbortConfig](API_AbortConfig.md) object
Required: No

 ** [description](#API_CreateJob_RequestSyntax) **   <a name="iot-CreateJob-request-description"></a>
A short text description of the job.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`
Required: No

 ** [destinationPackageVersions](#API_CreateJob_RequestSyntax) **   <a name="iot-CreateJob-request-destinationPackageVersions"></a>
The package version Amazon Resource Names (ARNs) that are installed on the device when the job successfully completes. The package version must be in either the Published or Deprecated state when the job deploys. For more information, see [Package version lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle).
 **Note:**The following Length Constraints relates to a single ARN. Up to 25 package version ARNs are allowed.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:[!-~]+$`
Required: No

 ** [document](#API_CreateJob_RequestSyntax) **   <a name="iot-CreateJob-request-document"></a>
The job document. Required if you don't specify a value for `documentSource`.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** [documentParameters](#API_CreateJob_RequestSyntax) **   <a name="iot-CreateJob-request-documentParameters"></a>
Parameters of an AWS managed template that you can specify to create the job document.
 `documentParameters` can only be used when creating jobs from AWS managed templates. This parameter can't be used with custom job templates or to create jobs from them.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_-]+`
Value Length Constraints: Minimum length of 1. Maximum length of 30720.
Value Pattern: `[^\p{C}]+`
Required: No

 ** [documentSource](#API_CreateJob_RequestSyntax) **   <a name="iot-CreateJob-request-documentSource"></a>
An S3 link, or S3 object URL, to the job document. The link is an Amazon S3 object URL and is required if you don't specify a value for `document`.
For example, `--document-source https://s3.region-code.amazonaws.com/example-firmware/device-firmware.1.0`
For more information, see [Methods for accessing a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-bucket-intro.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1350.
Required: No

 ** [jobExecutionsRetryConfig](#API_CreateJob_RequestSyntax) **   <a name="iot-CreateJob-request-jobExecutionsRetryConfig"></a>
Allows you to create the criteria to retry a job.
Type: [JobExecutionsRetryConfig](API_JobExecutionsRetryConfig.md) object
Required: No

 ** [jobExecutionsRolloutConfig](#API_CreateJob_RequestSyntax) **   <a name="iot-CreateJob-request-jobExecutionsRolloutConfig"></a>
Allows you to create a staged rollout of the job.
Type: [JobExecutionsRolloutConfig](API_JobExecutionsRolloutConfig.md) object
Required: No

 ** [jobTemplateArn](#API_CreateJob_RequestSyntax) **   <a name="iot-CreateJob-request-jobTemplateArn"></a>
The ARN of the job template used to create the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:[!-~]+$`
Required: No

 ** [namespaceId](#API_CreateJob_RequestSyntax) **   <a name="iot-CreateJob-request-namespaceId"></a>
The namespace used to indicate that a job is a customer-managed job.
When you specify a value for this parameter, AWS IoT Core sends jobs notifications to MQTT topics that contain the value in the following format.
 `$aws/things/THING_NAME/jobs/JOB_ID/notify-namespace-NAMESPACE_ID/`
The `namespaceId` feature is only supported by AWS IoT Greengrass at this time. For more information, see [Setting up AWS IoT Greengrass core devices.](https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html)
Type: String
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** [presignedUrlConfig](#API_CreateJob_RequestSyntax) **   <a name="iot-CreateJob-request-presignedUrlConfig"></a>
Configuration information for pre-signed S3 URLs.
Type: [PresignedUrlConfig](API_PresignedUrlConfig.md) object
Required: No

 ** [schedulingConfig](#API_CreateJob_RequestSyntax) **   <a name="iot-CreateJob-request-schedulingConfig"></a>
The configuration that allows you to schedule a job for a future date and time in addition to specifying the end behavior for each job execution.
Type: [SchedulingConfig](API_SchedulingConfig.md) object
Required: No

 ** [tags](#API_CreateJob_RequestSyntax) **   <a name="iot-CreateJob-request-tags"></a>
Metadata which can be used to manage the job.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [targets](#API_CreateJob_RequestSyntax) **   <a name="iot-CreateJob-request-targets"></a>
A list of things and thing groups to which the job should be sent.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Maximum length of 2048.
Required: Yes

 ** [targetSelection](#API_CreateJob_RequestSyntax) **   <a name="iot-CreateJob-request-targetSelection"></a>
Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.
We recommend that you use continuous jobs instead of snapshot jobs for dynamic thing group targets. By using continuous jobs, devices that join the group receive the job execution even after the job has been created.
Type: String
Valid Values: `CONTINUOUS | SNAPSHOT`
Required: No

 ** [timeoutConfig](#API_CreateJob_RequestSyntax) **   <a name="iot-CreateJob-request-timeoutConfig"></a>
Specifies the amount of time each device has to finish its execution of the job. The timer is started when the job execution status is set to `IN_PROGRESS`. If the job execution status is not set to another terminal state before the time expires, it will be automatically set to `TIMED_OUT`.
Type: [TimeoutConfig](API_TimeoutConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateJob_ResponseSyntax"></a>

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
<a name="API_CreateJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_CreateJob_ResponseSyntax) **   <a name="iot-CreateJob-response-description"></a>
The job description.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`

 ** [jobArn](#API_CreateJob_ResponseSyntax) **   <a name="iot-CreateJob-response-jobArn"></a>
The job ARN.
Type: String

 ** [jobId](#API_CreateJob_ResponseSyntax) **   <a name="iot-CreateJob-response-jobId"></a>
The unique identifier you assigned to this job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

## Errors
<a name="API_CreateJob_Errors"></a>

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

## See Also
<a name="API_CreateJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateJob)
