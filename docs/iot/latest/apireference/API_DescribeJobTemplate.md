---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeJobTemplate.html
---

# DescribeJobTemplate
<a name="API_DescribeJobTemplate"></a>

Returns information about a job template.

## Request Syntax
<a name="API_DescribeJobTemplate_RequestSyntax"></a>

```
GET /job-templates/{{jobTemplateId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeJobTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobTemplateId](#API_DescribeJobTemplate_RequestSyntax) **   <a name="iot-DescribeJobTemplate-request-uri-jobTemplateId"></a>
The unique identifier of the job template.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_DescribeJobTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeJobTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "abortConfig": {
      "criteriaList": [
         {
            "action": "string",
            "failureType": "string",
            "minNumberOfExecutedThings": number,
            "thresholdPercentage": number
         }
      ]
   },
   "createdAt": number,
   "description": "string",
   "destinationPackageVersions": [ "string" ],
   "document": "string",
   "documentSource": "string",
   "jobExecutionsRetryConfig": {
      "criteriaList": [
         {
            "failureType": "string",
            "numberOfRetries": number
         }
      ]
   },
   "jobExecutionsRolloutConfig": {
      "exponentialRate": {
         "baseRatePerMinute": number,
         "incrementFactor": number,
         "rateIncreaseCriteria": {
            "numberOfNotifiedThings": number,
            "numberOfSucceededThings": number
         }
      },
      "maximumPerMinute": number
   },
   "jobTemplateArn": "string",
   "jobTemplateId": "string",
   "maintenanceWindows": [
      {
         "durationInMinutes": number,
         "startTime": "string"
      }
   ],
   "presignedUrlConfig": {
      "expiresInSec": number,
      "roleArn": "string"
   },
   "timeoutConfig": {
      "inProgressTimeoutInMinutes": number
   }
}
```

## Response Elements
<a name="API_DescribeJobTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [abortConfig](#API_DescribeJobTemplate_ResponseSyntax) **   <a name="iot-DescribeJobTemplate-response-abortConfig"></a>
The criteria that determine when and how a job abort takes place.
Type: [AbortConfig](API_AbortConfig.md) object

 ** [createdAt](#API_DescribeJobTemplate_ResponseSyntax) **   <a name="iot-DescribeJobTemplate-response-createdAt"></a>
The time, in seconds since the epoch, when the job template was created.
Type: Timestamp

 ** [description](#API_DescribeJobTemplate_ResponseSyntax) **   <a name="iot-DescribeJobTemplate-response-description"></a>
A description of the job template.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`

 ** [destinationPackageVersions](#API_DescribeJobTemplate_ResponseSyntax) **   <a name="iot-DescribeJobTemplate-response-destinationPackageVersions"></a>
The package version Amazon Resource Names (ARNs) that are installed on the device when the job successfully completes. The package version must be in either the Published or Deprecated state when the job deploys. For more information, see [Package version lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle).
 **Note:**The following Length Constraints relates to a single ARN. Up to 25 package version ARNs are allowed.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:[!-~]+$`

 ** [document](#API_DescribeJobTemplate_ResponseSyntax) **   <a name="iot-DescribeJobTemplate-response-document"></a>
The job document.
Type: String
Length Constraints: Maximum length of 32768.

 ** [documentSource](#API_DescribeJobTemplate_ResponseSyntax) **   <a name="iot-DescribeJobTemplate-response-documentSource"></a>
An S3 link to the job document.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1350.

 ** [jobExecutionsRetryConfig](#API_DescribeJobTemplate_ResponseSyntax) **   <a name="iot-DescribeJobTemplate-response-jobExecutionsRetryConfig"></a>
The configuration that determines how many retries are allowed for each failure type for a job.
Type: [JobExecutionsRetryConfig](API_JobExecutionsRetryConfig.md) object

 ** [jobExecutionsRolloutConfig](#API_DescribeJobTemplate_ResponseSyntax) **   <a name="iot-DescribeJobTemplate-response-jobExecutionsRolloutConfig"></a>
Allows you to create a staged rollout of a job.
Type: [JobExecutionsRolloutConfig](API_JobExecutionsRolloutConfig.md) object

 ** [jobTemplateArn](#API_DescribeJobTemplate_ResponseSyntax) **   <a name="iot-DescribeJobTemplate-response-jobTemplateArn"></a>
The ARN of the job template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:[!-~]+$`

 ** [jobTemplateId](#API_DescribeJobTemplate_ResponseSyntax) **   <a name="iot-DescribeJobTemplate-response-jobTemplateId"></a>
The unique identifier of the job template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [maintenanceWindows](#API_DescribeJobTemplate_ResponseSyntax) **   <a name="iot-DescribeJobTemplate-response-maintenanceWindows"></a>
Allows you to configure an optional maintenance window for the rollout of a job document to all devices in the target group for a job.
Type: Array of [MaintenanceWindow](API_MaintenanceWindow.md) objects

 ** [presignedUrlConfig](#API_DescribeJobTemplate_ResponseSyntax) **   <a name="iot-DescribeJobTemplate-response-presignedUrlConfig"></a>
Configuration for pre-signed S3 URLs.
Type: [PresignedUrlConfig](API_PresignedUrlConfig.md) object

 ** [timeoutConfig](#API_DescribeJobTemplate_ResponseSyntax) **   <a name="iot-DescribeJobTemplate-response-timeoutConfig"></a>
Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to `IN_PROGRESS`. If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to `TIMED_OUT`.
Type: [TimeoutConfig](API_TimeoutConfig.md) object

## Errors
<a name="API_DescribeJobTemplate_Errors"></a>

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
<a name="API_DescribeJobTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeJobTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeJobTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeJobTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeJobTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeJobTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeJobTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeJobTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeJobTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeJobTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeJobTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
