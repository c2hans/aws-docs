---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_StopJob.html
---

# StopJob
<a name="API_StopJob"></a>

Initiates a stop request for the current job. AWS Device Farm immediately stops the job on the device where tests have not started. You are not billed for this device. On the device where tests have started, setup suite and teardown suite tests run to completion on the device. You are billed for setup, teardown, and any tests that were in progress or already completed.

## Request Syntax
<a name="API_StopJob_RequestSyntax"></a>

```
{
   "arn": "{{string}}"
}
```

## Request Parameters
<a name="API_StopJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_StopJob_RequestSyntax) **   <a name="devicefarm-StopJob-request-arn"></a>
Represents the Amazon Resource Name (ARN) of the Device Farm job to stop.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

## Response Syntax
<a name="API_StopJob_ResponseSyntax"></a>

```
{
   "job": {
      "arn": "string",
      "counters": {
         "errored": number,
         "failed": number,
         "passed": number,
         "skipped": number,
         "stopped": number,
         "total": number,
         "warned": number
      },
      "created": number,
      "device": {
         "arn": "string",
         "availability": "string",
         "carrier": "string",
         "cpu": {
            "architecture": "string",
            "clock": number,
            "frequency": "string"
         },
         "fleetName": "string",
         "fleetType": "string",
         "formFactor": "string",
         "heapSize": number,
         "image": "string",
         "instances": [
            {
               "arn": "string",
               "deviceArn": "string",
               "instanceProfile": {
                  "arn": "string",
                  "description": "string",
                  "excludeAppPackagesFromCleanup": [ "string" ],
                  "name": "string",
                  "packageCleanup": boolean,
                  "rebootAfterUse": boolean
               },
               "labels": [ "string" ],
               "status": "string",
               "udid": "string"
            }
         ],
         "manufacturer": "string",
         "memory": number,
         "model": "string",
         "modelId": "string",
         "name": "string",
         "os": "string",
         "platform": "string",
         "radio": "string",
         "remoteAccessEnabled": boolean,
         "remoteDebugEnabled": boolean,
         "resolution": {
            "height": number,
            "width": number
         }
      },
      "deviceMinutes": {
         "metered": number,
         "total": number,
         "unmetered": number
      },
      "insights": {
         "status": "string",
         "testReport": {
            "message": "string",
            "metrics": {
               "medianTestExecutionDurationSeconds": number,
               "testsErrored": number,
               "testsFailed": number,
               "testsOther": number,
               "testsPassed": number,
               "testsPassedPercentage": number,
               "testsSkipped": number,
               "testsTotal": number,
               "totalTestExecutionDurationSeconds": number
            },
            "testDetailsUrl": "string"
         }
      },
      "instanceArn": "string",
      "message": "string",
      "name": "string",
      "result": "string",
      "started": number,
      "status": "string",
      "stopped": number,
      "type": "string",
      "videoCapture": boolean,
      "videoEndpoint": "string"
   }
}
```

## Response Elements
<a name="API_StopJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [job](#API_StopJob_ResponseSyntax) **   <a name="devicefarm-StopJob-response-job"></a>
The job that was stopped.
Type: [Job](API_Job.md) object

## Errors
<a name="API_StopJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit was exceeded.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** ServiceAccountException **
There was a problem with the service account.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_StopJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/StopJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/StopJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/StopJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/StopJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/StopJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/StopJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/StopJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/StopJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/StopJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/StopJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
