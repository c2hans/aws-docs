---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListJobs.html
---

# ListJobs
<a name="API_ListJobs"></a>

Gets information about jobs for a given test run.

## Request Syntax
<a name="API_ListJobs_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_ListJobs_RequestSyntax) **   <a name="devicefarm-ListJobs-request-arn"></a>
The run's Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [nextToken](#API_ListJobs_RequestSyntax) **   <a name="devicefarm-ListJobs-request-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListJobs_ResponseSyntax"></a>

```
{
   "jobs": [
      {
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobs](#API_ListJobs_ResponseSyntax) **   <a name="devicefarm-ListJobs-response-jobs"></a>
Information about the jobs.
Type: Array of [Job](API_Job.md) objects

 ** [nextToken](#API_ListJobs_ResponseSyntax) **   <a name="devicefarm-ListJobs-response-nextToken"></a>
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

## Errors
<a name="API_ListJobs_Errors"></a>

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
<a name="API_ListJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListJobs)
