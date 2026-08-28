---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_StartJobRun.html
---

# StartJobRun
<a name="API_StartJobRun"></a>

Starts a job run. A job run is a unit of work, such as a Spark jar, PySpark script, or SparkSQL query, that you submit to Amazon EMR on EKS.

## Request Syntax
<a name="API_StartJobRun_RequestSyntax"></a>

```
POST /virtualclusters/{{virtualClusterId}}/jobruns HTTP/1.1
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
      "monitoringConfiguration": {
         "cloudWatchMonitoringConfiguration": {
            "logGroupName": "{{string}}",
            "logStreamNamePrefix": "{{string}}"
         },
         "containerLogRotationConfiguration": {
            "maxFilesToKeep": {{number}},
            "rotationSize": "{{string}}"
         },
         "managedLogs": {
            "allowAWSToRetainLogs": "{{string}}",
            "encryptionKeyArn": "{{string}}"
         },
         "persistentAppUI": "{{string}}",
         "s3MonitoringConfiguration": {
            "encryptionKeyArn": "{{string}}",
            "logUri": "{{string}}"
         }
      }
   },
   "executionRoleArn": "{{string}}",
   "jobDriver": {
      "sparkSqlJobDriver": {
         "entryPoint": "{{string}}",
         "sparkSqlParameters": "{{string}}"
      },
      "sparkSubmitJobDriver": {
         "entryPoint": "{{string}}",
         "entryPointArguments": [ "{{string}}" ],
         "sparkSubmitParameters": "{{string}}"
      }
   },
   "jobTemplateId": "{{string}}",
   "jobTemplateParameters": {
      "{{string}}" : "{{string}}"
   },
   "name": "{{string}}",
   "releaseLabel": "{{string}}",
   "retryPolicyConfiguration": {
      "maxAttempts": {{number}}
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartJobRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [virtualClusterId](#API_StartJobRun_RequestSyntax) **   <a name="emroneks-StartJobRun-request-uri-virtualClusterId"></a>
The virtual cluster ID for which the job run request is submitted.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_StartJobRun_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartJobRun_RequestSyntax) **   <a name="emroneks-StartJobRun-request-clientToken"></a>
The client idempotency token of the job run request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: Yes

 ** [configurationOverrides](#API_StartJobRun_RequestSyntax) **   <a name="emroneks-StartJobRun-request-configurationOverrides"></a>
The configuration overrides for the job run.
Type: [ConfigurationOverrides](API_ConfigurationOverrides.md) object
Required: No

 ** [executionRoleArn](#API_StartJobRun_RequestSyntax) **   <a name="emroneks-StartJobRun-request-executionRoleArn"></a>
The execution role ARN for the job run.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$`
Required: No

 ** [jobDriver](#API_StartJobRun_RequestSyntax) **   <a name="emroneks-StartJobRun-request-jobDriver"></a>
The job driver for the job run.
Type: [JobDriver](API_JobDriver.md) object
Required: No

 ** [jobTemplateId](#API_StartJobRun_RequestSyntax) **   <a name="emroneks-StartJobRun-request-jobTemplateId"></a>
The job template ID to be used to start the job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: No

 ** [jobTemplateParameters](#API_StartJobRun_RequestSyntax) **   <a name="emroneks-StartJobRun-request-jobTemplateParameters"></a>
The values of job template parameters to start a job run.
Type: String to string map
Map Entries: Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 512.
Key Pattern: `[\.\-_\#A-Za-z0-9]+`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `.*\S.*`
Required: No

 ** [name](#API_StartJobRun_RequestSyntax) **   <a name="emroneks-StartJobRun-request-name"></a>
The name of the job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** [releaseLabel](#API_StartJobRun_RequestSyntax) **   <a name="emroneks-StartJobRun-request-releaseLabel"></a>
The Amazon EMR release version to use for the job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/A-Za-z0-9]+`
Required: No

 ** [retryPolicyConfiguration](#API_StartJobRun_RequestSyntax) **   <a name="emroneks-StartJobRun-request-retryPolicyConfiguration"></a>
The retry policy configuration for the job run.
Type: [RetryPolicyConfiguration](API_RetryPolicyConfiguration.md) object
Required: No

 ** [tags](#API_StartJobRun_RequestSyntax) **   <a name="emroneks-StartJobRun-request-tags"></a>
The tags assigned to job runs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.*\S.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_StartJobRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "name": "string",
   "virtualClusterId": "string"
}
```

## Response Elements
<a name="API_StartJobRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_StartJobRun_ResponseSyntax) **   <a name="emroneks-StartJobRun-response-arn"></a>
This output lists the ARN of job run.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):emr-containers:.+:(\d{12}):\/virtualclusters\/[0-9a-zA-Z]+\/jobruns\/[0-9a-zA-Z]+$`

 ** [id](#API_StartJobRun_ResponseSyntax) **   <a name="emroneks-StartJobRun-response-id"></a>
This output displays the started job run ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

 ** [name](#API_StartJobRun_ResponseSyntax) **   <a name="emroneks-StartJobRun-response-name"></a>
This output displays the name of the started job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/#A-Za-z0-9]+`

 ** [virtualClusterId](#API_StartJobRun_ResponseSyntax) **   <a name="emroneks-StartJobRun-response-virtualClusterId"></a>
This output displays the virtual cluster ID for which the job run was submitted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

## Errors
<a name="API_StartJobRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
This is an internal server exception.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

 ** ValidationException **
There are invalid parameters in the client request.
HTTP Status Code: 400

## See Also
<a name="API_StartJobRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-containers-2020-10-01/StartJobRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-containers-2020-10-01/StartJobRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/StartJobRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-containers-2020-10-01/StartJobRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/StartJobRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-containers-2020-10-01/StartJobRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-containers-2020-10-01/StartJobRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-containers-2020-10-01/StartJobRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-containers-2020-10-01/StartJobRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/StartJobRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
