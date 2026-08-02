---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DescribeJobRun.html
---

# DescribeJobRun
<a name="API_DescribeJobRun"></a>

Displays detailed information about a job run. A job run is a unit of work, such as a Spark jar, PySpark script, or SparkSQL query, that you submit to Amazon EMR on EKS.

## Request Syntax
<a name="API_DescribeJobRun_RequestSyntax"></a>

```
GET /virtualclusters/{{virtualClusterId}}/jobruns/{{jobRunId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeJobRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobRunId](#API_DescribeJobRun_RequestSyntax) **   <a name="emroneks-DescribeJobRun-request-uri-id"></a>
The ID of the job run request.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** [virtualClusterId](#API_DescribeJobRun_RequestSyntax) **   <a name="emroneks-DescribeJobRun-request-uri-virtualClusterId"></a>
The ID of the virtual cluster for which the job run is submitted.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_DescribeJobRun_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeJobRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobRun": {
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
}
```

## Response Elements
<a name="API_DescribeJobRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobRun](#API_DescribeJobRun_ResponseSyntax) **   <a name="emroneks-DescribeJobRun-response-jobRun"></a>
The output displays information about a job run.
Type: [JobRun](API_JobRun.md) object

## Errors
<a name="API_DescribeJobRun_Errors"></a>

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
<a name="API_DescribeJobRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-containers-2020-10-01/DescribeJobRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-containers-2020-10-01/DescribeJobRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/DescribeJobRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-containers-2020-10-01/DescribeJobRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/DescribeJobRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-containers-2020-10-01/DescribeJobRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-containers-2020-10-01/DescribeJobRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-containers-2020-10-01/DescribeJobRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-containers-2020-10-01/DescribeJobRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/DescribeJobRun)
