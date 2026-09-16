---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeJob.html
---

# DescribeJob
<a name="API_DescribeJob"></a>

Describes a job.

Requires permission to access the [DescribeJob](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeJob_RequestSyntax"></a>

```
GET /jobs/{{jobId}}?beforeSubstitution={{beforeSubstitution}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [beforeSubstitution](#API_DescribeJob_RequestSyntax) **   <a name="iot-DescribeJob-request-uri-beforeSubstitution"></a>
Provides a view of the job document before and after the substitution parameters have been resolved with their exact values.

 ** [jobId](#API_DescribeJob_RequestSyntax) **   <a name="iot-DescribeJob-request-uri-jobId"></a>
The unique identifier you assigned to this job when it was created.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_DescribeJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "documentSource": "string",
   "job": {
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
      "comment": "string",
      "completedAt": number,
      "createdAt": number,
      "description": "string",
      "destinationPackageVersions": [ "string" ],
      "documentParameters": {
         "string" : "string"
      },
      "forceCanceled": boolean,
      "isConcurrent": boolean,
      "jobArn": "string",
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
      "jobId": "string",
      "jobProcessDetails": {
         "numberOfCanceledThings": number,
         "numberOfFailedThings": number,
         "numberOfInProgressThings": number,
         "numberOfQueuedThings": number,
         "numberOfRejectedThings": number,
         "numberOfRemovedThings": number,
         "numberOfSucceededThings": number,
         "numberOfTimedOutThings": number,
         "processingTargets": [ "string" ]
      },
      "jobTemplateArn": "string",
      "lastUpdatedAt": number,
      "namespaceId": "string",
      "presignedUrlConfig": {
         "expiresInSec": number,
         "roleArn": "string"
      },
      "reasonCode": "string",
      "scheduledJobRollouts": [
         {
            "startTime": "string"
         }
      ],
      "schedulingConfig": {
         "endBehavior": "string",
         "endTime": "string",
         "maintenanceWindows": [
            {
               "durationInMinutes": number,
               "startTime": "string"
            }
         ],
         "startTime": "string"
      },
      "status": "string",
      "targets": [ "string" ],
      "targetSelection": "string",
      "timeoutConfig": {
         "inProgressTimeoutInMinutes": number
      }
   }
}
```

## Response Elements
<a name="API_DescribeJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [documentSource](#API_DescribeJob_ResponseSyntax) **   <a name="iot-DescribeJob-response-documentSource"></a>
An S3 link to the job document.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1350.

 ** [job](#API_DescribeJob_ResponseSyntax) **   <a name="iot-DescribeJob-response-job"></a>
Information about the job.
Type: [Job](API_Job.md) object

## Errors
<a name="API_DescribeJob_Errors"></a>

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
<a name="API_DescribeJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeJob)
