---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetJobRun.html
---

# GetJobRun
<a name="API_GetJobRun"></a>

Displays detailed information about a job run.

## Request Syntax
<a name="API_GetJobRun_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/jobruns/{{jobRunId}}?attempt={{attempt}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetJobRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetJobRun_RequestSyntax) **   <a name="emrserverless-GetJobRun-request-uri-applicationId"></a>
The ID of the application on which the job run is submitted.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** [attempt](#API_GetJobRun_RequestSyntax) **   <a name="emrserverless-GetJobRun-request-uri-attempt"></a>
An optimal parameter that indicates the amount of attempts for the job. If not specified, this value defaults to the attempt of the latest job.
Valid Range: Minimum value of 1.

 ** [jobRunId](#API_GetJobRun_RequestSyntax) **   <a name="emrserverless-GetJobRun-request-uri-jobRunId"></a>
The ID of the job run.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_GetJobRun_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetJobRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobRun": {
      "applicationId": "string",
      "arn": "string",
      "attempt": number,
      "attemptCreatedAt": number,
      "attemptUpdatedAt": number,
      "billedResourceUtilization": {
         "memoryGBHour": number,
         "storageGBHour": number,
         "vCPUHour": number
      },
      "configurationOverrides": {
         "applicationConfiguration": [
            {
               "classification": "string",
               "configurations": [
                  "Configuration"
               ],
               "properties": {
                  "string" : "string"
               }
            }
         ],
         "diskEncryptionConfiguration": {
            "encryptionContext": {
               "string" : "string"
            },
            "encryptionKeyArn": "string"
         },
         "monitoringConfiguration": {
            "cloudWatchLoggingConfiguration": {
               "enabled": boolean,
               "encryptionKeyArn": "string",
               "logGroupName": "string",
               "logStreamNamePrefix": "string",
               "logTypes": {
                  "string" : [ "string" ]
               }
            },
            "managedPersistenceMonitoringConfiguration": {
               "enabled": boolean,
               "encryptionKeyArn": "string"
            },
            "prometheusMonitoringConfiguration": {
               "remoteWriteUrl": "string"
            },
            "s3MonitoringConfiguration": {
               "encryptionKeyArn": "string",
               "logUri": "string"
            }
         }
      },
      "createdAt": number,
      "createdBy": "string",
      "endedAt": number,
      "executionIamPolicy": {
         "policy": "string",
         "policyArns": [ "string" ]
      },
      "executionRole": "string",
      "executionTimeoutMinutes": number,
      "imageConfiguration": {
         "applicationLevelDigestResolution": boolean,
         "imageUri": "string",
         "resolvedImageDigest": "string"
      },
      "jobDriver": { ... },
      "jobRunId": "string",
      "mode": "string",
      "name": "string",
      "networkConfiguration": {
         "securityGroupIds": [ "string" ],
         "subnetIds": [ "string" ]
      },
      "queuedDurationMilliseconds": number,
      "releaseLabel": "string",
      "retryPolicy": {
         "maxAttempts": number,
         "maxFailedAttemptsPerHour": number
      },
      "startedAt": number,
      "state": "string",
      "stateDetails": "string",
      "tags": {
         "string" : "string"
      },
      "totalExecutionDurationSeconds": number,
      "totalResourceUtilization": {
         "memoryGBHour": number,
         "storageGBHour": number,
         "vCPUHour": number
      },
      "updatedAt": number,
      "workerTypeSpecifications": {
         "string" : {
            "imageConfiguration": {
               "applicationLevelDigestResolution": boolean,
               "imageUri": "string",
               "resolvedImageDigest": "string"
            }
         }
      }
   }
}
```

## Response Elements
<a name="API_GetJobRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobRun](#API_GetJobRun_ResponseSyntax) **   <a name="emrserverless-GetJobRun-response-jobRun"></a>
The output displays information about the job run.
Type: [JobRun](API_JobRun.md) object

## Errors
<a name="API_GetJobRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Request processing failed because of an error or failure with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetJobRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-serverless-2021-07-13/GetJobRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-serverless-2021-07-13/GetJobRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/GetJobRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-serverless-2021-07-13/GetJobRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/GetJobRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-serverless-2021-07-13/GetJobRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-serverless-2021-07-13/GetJobRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-serverless-2021-07-13/GetJobRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-serverless-2021-07-13/GetJobRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/GetJobRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
