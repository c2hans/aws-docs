---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ListJobRuns.html
---

# ListJobRuns
<a name="API_ListJobRuns"></a>

Lists job runs based on a set of parameters. A job run is a unit of work, such as a Spark jar, PySpark script, or SparkSQL query, that you submit to Amazon EMR on EKS.

## Request Syntax
<a name="API_ListJobRuns_RequestSyntax"></a>

```
GET /virtualclusters/{{virtualClusterId}}/jobruns?createdAfter={{createdAfter}}&createdBefore={{createdBefore}}&maxResults={{maxResults}}&name={{name}}&nextToken={{nextToken}}&states={{states}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListJobRuns_RequestParameters"></a>

The request uses the following URI parameters.

 ** [createdAfter](#API_ListJobRuns_RequestSyntax) **   <a name="emroneks-ListJobRuns-request-uri-createdAfter"></a>
The date and time after which the job runs were submitted.

 ** [createdBefore](#API_ListJobRuns_RequestSyntax) **   <a name="emroneks-ListJobRuns-request-uri-createdBefore"></a>
The date and time before which the job runs were submitted.

 ** [maxResults](#API_ListJobRuns_RequestSyntax) **   <a name="emroneks-ListJobRuns-request-uri-maxResults"></a>
The maximum number of job runs that can be listed.

 ** [name](#API_ListJobRuns_RequestSyntax) **   <a name="emroneks-ListJobRuns-request-uri-name"></a>
The name of the job run.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/#A-Za-z0-9]+`

 ** [nextToken](#API_ListJobRuns_RequestSyntax) **   <a name="emroneks-ListJobRuns-request-uri-nextToken"></a>
The token for the next set of job runs to return.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [states](#API_ListJobRuns_RequestSyntax) **   <a name="emroneks-ListJobRuns-request-uri-states"></a>
The states of the job run.
Array Members: Maximum number of 10 items.
Valid Values: `PENDING | SUBMITTED | RUNNING | FAILED | CANCELLED | CANCEL_PENDING | COMPLETED`

 ** [virtualClusterId](#API_ListJobRuns_RequestSyntax) **   <a name="emroneks-ListJobRuns-request-uri-virtualClusterId"></a>
The ID of the virtual cluster for which to list the job run.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_ListJobRuns_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListJobRuns_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobRuns": [
      {
         "arn": "string",
         "clientToken": "string",
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
            "monitoringConfiguration": {
               "cloudWatchMonitoringConfiguration": {
                  "logGroupName": "string",
                  "logStreamNamePrefix": "string"
               },
               "containerLogRotationConfiguration": {
                  "maxFilesToKeep": number,
                  "rotationSize": "string"
               },
               "managedLogs": {
                  "allowAWSToRetainLogs": "string",
                  "encryptionKeyArn": "string"
               },
               "persistentAppUI": "string",
               "s3MonitoringConfiguration": {
                  "logUri": "string"
               }
            }
         },
         "createdAt": "string",
         "createdBy": "string",
         "executionRoleArn": "string",
         "failureReason": "string",
         "finishedAt": "string",
         "id": "string",
         "jobDriver": {
            "sparkSqlJobDriver": {
               "entryPoint": "string",
               "sparkSqlParameters": "string"
            },
            "sparkSubmitJobDriver": {
               "entryPoint": "string",
               "entryPointArguments": [ "string" ],
               "sparkSubmitParameters": "string"
            }
         },
         "name": "string",
         "releaseLabel": "string",
         "retryPolicyConfiguration": {
            "maxAttempts": number
         },
         "retryPolicyExecution": {
            "currentAttemptCount": number
         },
         "state": "string",
         "stateDetails": "string",
         "tags": {
            "string" : "string"
         },
         "virtualClusterId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListJobRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobRuns](#API_ListJobRuns_ResponseSyntax) **   <a name="emroneks-ListJobRuns-response-jobRuns"></a>
This output lists information about the specified job runs.
Type: Array of [JobRun](API_JobRun.md) objects

 ** [nextToken](#API_ListJobRuns_ResponseSyntax) **   <a name="emroneks-ListJobRuns-response-nextToken"></a>
This output displays the token for the next set of job runs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

## Errors
<a name="API_ListJobRuns_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
This is an internal server exception.
HTTP Status Code: 500

 ** ValidationException **
There are invalid parameters in the client request.
HTTP Status Code: 400

## See Also
<a name="API_ListJobRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-containers-2020-10-01/ListJobRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-containers-2020-10-01/ListJobRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/ListJobRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-containers-2020-10-01/ListJobRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/ListJobRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-containers-2020-10-01/ListJobRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-containers-2020-10-01/ListJobRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-containers-2020-10-01/ListJobRuns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-containers-2020-10-01/ListJobRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/ListJobRuns)
