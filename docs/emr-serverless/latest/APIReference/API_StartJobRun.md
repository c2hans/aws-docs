---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_StartJobRun.html
---

# StartJobRun
<a name="API_StartJobRun"></a>

Starts a job run.

## Request Syntax
<a name="API_StartJobRun_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/jobruns HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "configurationOverrides": {
      "applicationConfiguration": [
         {
            "classification": "{{string}}",
            "configurations": [
               "Configuration"
            ],
            "properties": {
               "{{string}}" : "{{string}}"
            }
         }
      ],
      "diskEncryptionConfiguration": {
         "encryptionContext": {
            "{{string}}" : "{{string}}"
         },
         "encryptionKeyArn": "{{string}}"
      },
      "monitoringConfiguration": {
         "cloudWatchLoggingConfiguration": {
            "enabled": {{boolean}},
            "encryptionKeyArn": "{{string}}",
            "logGroupName": "{{string}}",
            "logStreamNamePrefix": "{{string}}",
            "logTypes": {
               "{{string}}" : [ "{{string}}" ]
            }
         },
         "managedPersistenceMonitoringConfiguration": {
            "enabled": {{boolean}},
            "encryptionKeyArn": "{{string}}"
         },
         "prometheusMonitoringConfiguration": {
            "remoteWriteUrl": "{{string}}"
         },
         "s3MonitoringConfiguration": {
            "encryptionKeyArn": "{{string}}",
            "logUri": "{{string}}"
         }
      }
   },
   "executionIamPolicy": {
      "policy": "{{string}}",
      "policyArns": [ "{{string}}" ]
   },
   "executionRoleArn": "{{string}}",
   "executionTimeoutMinutes": {{number}},
   "jobDriver": { ... },
   "mode": "{{string}}",
   "name": "{{string}}",
   "retryPolicy": {
      "maxAttempts": {{number}},
      "maxFailedAttemptsPerHour": {{number}}
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartJobRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_StartJobRun_RequestSyntax) **   <a name="emrserverless-StartJobRun-request-uri-applicationId"></a>
The ID of the application on which to run the job.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_StartJobRun_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartJobRun_RequestSyntax) **   <a name="emrserverless-StartJobRun-request-clientToken"></a>
The client idempotency token of the job run to start. Its value must be unique for each request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._-]+`
Required: Yes

 ** [configurationOverrides](#API_StartJobRun_RequestSyntax) **   <a name="emrserverless-StartJobRun-request-configurationOverrides"></a>
The configuration overrides for the job run.
Type: [ConfigurationOverrides](API_ConfigurationOverrides.md) object
Required: No

 ** [executionIamPolicy](#API_StartJobRun_RequestSyntax) **   <a name="emrserverless-StartJobRun-request-executionIamPolicy"></a>
You can pass an optional IAM policy. The resulting job IAM role permissions will be an intersection of this policy and the policy associated with your job execution role.
Type: [JobRunExecutionIamPolicy](API_JobRunExecutionIamPolicy.md) object
Required: No

 ** [executionRoleArn](#API_StartJobRun_RequestSyntax) **   <a name="emrserverless-StartJobRun-request-executionRoleArn"></a>
The execution role ARN for the job run.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):iam::([0-9]{12}):(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)`
Required: Yes

 ** [executionTimeoutMinutes](#API_StartJobRun_RequestSyntax) **   <a name="emrserverless-StartJobRun-request-executionTimeoutMinutes"></a>
The maximum duration, in minutes, for the job run. If the job run exceeds this duration, Amazon EMR Serverless cancels it automatically.
For BATCH mode job runs, the maximum value is 10080 minutes (7 days) starting with Amazon EMR release 7.11. Setting a value of 0 to disable the timeout is no longer supported for BATCH mode job runs.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000.
Required: No

 ** [jobDriver](#API_StartJobRun_RequestSyntax) **   <a name="emrserverless-StartJobRun-request-jobDriver"></a>
The job driver for the job run.
Type: [JobDriver](API_JobDriver.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [mode](#API_StartJobRun_RequestSyntax) **   <a name="emrserverless-StartJobRun-request-mode"></a>
The mode of the job run when it starts.
Type: String
Valid Values: `BATCH | STREAMING`
Required: No

 ** [name](#API_StartJobRun_RequestSyntax) **   <a name="emrserverless-StartJobRun-request-name"></a>
The optional job run name. This doesn't have to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** [retryPolicy](#API_StartJobRun_RequestSyntax) **   <a name="emrserverless-StartJobRun-request-retryPolicy"></a>
The retry policy when job run starts.
Type: [RetryPolicy](API_RetryPolicy.md) object
Required: No

 ** [tags](#API_StartJobRun_RequestSyntax) **   <a name="emrserverless-StartJobRun-request-tags"></a>
The tags assigned to the job run.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[A-Za-z0-9 /_.:=+@-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[A-Za-z0-9 /_.:=+@-]*`
Required: No

## Response Syntax
<a name="API_StartJobRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationId": "string",
   "arn": "string",
   "jobRunId": "string"
}
```

## Response Elements
<a name="API_StartJobRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationId](#API_StartJobRun_ResponseSyntax) **   <a name="emrserverless-StartJobRun-response-applicationId"></a>
This output displays the application ID on which the job run was submitted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

 ** [arn](#API_StartJobRun_ResponseSyntax) **   <a name="emrserverless-StartJobRun-response-arn"></a>
This output displays the ARN of the job run..
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `arn:(aws[a-zA-Z0-9-]*):emr-serverless:.+:(\d{12}):\/applications\/[0-9a-zA-Z]+\/jobruns\/[0-9a-zA-Z]+`

 ** [jobRunId](#API_StartJobRun_ResponseSyntax) **   <a name="emrserverless-StartJobRun-response-jobRunId"></a>
The output contains the ID of the started job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

## Errors
<a name="API_StartJobRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
HTTP Status Code: 409

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
<a name="API_StartJobRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-serverless-2021-07-13/StartJobRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-serverless-2021-07-13/StartJobRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/StartJobRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-serverless-2021-07-13/StartJobRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/StartJobRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-serverless-2021-07-13/StartJobRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-serverless-2021-07-13/StartJobRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-serverless-2021-07-13/StartJobRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-serverless-2021-07-13/StartJobRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/StartJobRun)
