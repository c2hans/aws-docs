---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ScheduleRun.html
---

# ScheduleRun
<a name="API_ScheduleRun"></a>

Schedules a run.

## Request Syntax
<a name="API_ScheduleRun_RequestSyntax"></a>

```
{
   "appArn": "{{string}}",
   "configuration": {
      "auxiliaryApps": [ "{{string}}" ],
      "billingMethod": "{{string}}",
      "customerArtifactPaths": {
         "androidPaths": [ "{{string}}" ],
         "deviceHostPaths": [ "{{string}}" ],
         "iosPaths": [ "{{string}}" ]
      },
      "deviceProxy": {
         "host": "{{string}}",
         "port": {{number}}
      },
      "environmentVariables": [
         {
            "name": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "executionRoleArn": "{{string}}",
      "extraDataPackageArn": "{{string}}",
      "insightsTypes": [ "{{string}}" ],
      "locale": "{{string}}",
      "location": {
         "latitude": {{number}},
         "longitude": {{number}}
      },
      "networkProfileArn": "{{string}}",
      "radios": {
         "bluetooth": {{boolean}},
         "gps": {{boolean}},
         "nfc": {{boolean}},
         "wifi": {{boolean}}
      },
      "vpceConfigurationArns": [ "{{string}}" ]
   },
   "devicePoolArn": "{{string}}",
   "deviceSelectionConfiguration": {
      "filters": [
         {
            "attribute": "{{string}}",
            "operator": "{{string}}",
            "values": [ "{{string}}" ]
         }
      ],
      "maxDevices": {{number}}
   },
   "executionConfiguration": {
      "accountsCleanup": {{boolean}},
      "appPackagesCleanup": {{boolean}},
      "jobTimeoutMinutes": {{number}},
      "skipAppResign": {{boolean}},
      "videoCapture": {{boolean}}
   },
   "name": "{{string}}",
   "projectArn": "{{string}}",
   "test": {
      "filter": "{{string}}",
      "parameters": {
         "{{string}}" : "{{string}}"
      },
      "testPackageArn": "{{string}}",
      "testSpecArn": "{{string}}",
      "type": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ScheduleRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [appArn](#API_ScheduleRun_RequestSyntax) **   <a name="devicefarm-ScheduleRun-request-appArn"></a>
The ARN of an application package to run tests against, created with [CreateUpload](API_CreateUpload.md). See [ListUploads](API_ListUploads.md).
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** [configuration](#API_ScheduleRun_RequestSyntax) **   <a name="devicefarm-ScheduleRun-request-configuration"></a>
Information about the settings for the run to be scheduled.
Type: [ScheduleRunConfiguration](API_ScheduleRunConfiguration.md) object
Required: No

 ** [devicePoolArn](#API_ScheduleRun_RequestSyntax) **   <a name="devicefarm-ScheduleRun-request-devicePoolArn"></a>
The ARN of the device pool for the run to be scheduled.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** [deviceSelectionConfiguration](#API_ScheduleRun_RequestSyntax) **   <a name="devicefarm-ScheduleRun-request-deviceSelectionConfiguration"></a>
The filter criteria used to dynamically select a set of devices for a test run and the maximum number of devices to be included in the run.
Either ** `devicePoolArn` ** or ** `deviceSelectionConfiguration` ** is required in a request.
Type: [DeviceSelectionConfiguration](API_DeviceSelectionConfiguration.md) object
Required: No

 ** [executionConfiguration](#API_ScheduleRun_RequestSyntax) **   <a name="devicefarm-ScheduleRun-request-executionConfiguration"></a>
Specifies configuration information about a test run, such as the execution timeout (in minutes).
Type: [ExecutionConfiguration](API_ExecutionConfiguration.md) object
Required: No

 ** [name](#API_ScheduleRun_RequestSyntax) **   <a name="devicefarm-ScheduleRun-request-name"></a>
The name for the run to be scheduled.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [projectArn](#API_ScheduleRun_RequestSyntax) **   <a name="devicefarm-ScheduleRun-request-projectArn"></a>
The ARN of the project for the run to be scheduled.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [test](#API_ScheduleRun_RequestSyntax) **   <a name="devicefarm-ScheduleRun-request-test"></a>
Information about the test for the run to be scheduled.
Type: [ScheduleRunTest](API_ScheduleRunTest.md) object
Required: Yes

## Response Syntax
<a name="API_ScheduleRun_ResponseSyntax"></a>

```
{
   "run": {
      "appUpload": "string",
      "arn": "string",
      "billingMethod": "string",
      "completedJobs": number,
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
      "customerArtifactPaths": {
         "androidPaths": [ "string" ],
         "deviceHostPaths": [ "string" ],
         "iosPaths": [ "string" ]
      },
      "deviceMinutes": {
         "metered": number,
         "total": number,
         "unmetered": number
      },
      "devicePoolArn": "string",
      "deviceProxy": {
         "host": "string",
         "port": number
      },
      "deviceSelectionResult": {
         "filters": [
            {
               "attribute": "string",
               "operator": "string",
               "values": [ "string" ]
            }
         ],
         "matchedDevicesCount": number,
         "maxDevices": number
      },
      "environmentVariables": [
         {
            "name": "string",
            "value": "string"
         }
      ],
      "eventCount": number,
      "executionRoleArn": "string",
      "insights": {
         "jobReport": {
            "jobDetailsUrl": "string",
            "message": "string",
            "metrics": {
               "averageJobExecutionDurationSeconds": number,
               "jobsErrored": number,
               "jobsFailed": number,
               "jobsPassed": number,
               "jobsPassedPercentage": number,
               "jobsSkipped": number,
               "jobsStopped": number,
               "jobsTotal": number,
               "medianJobExecutionDurationSeconds": number,
               "totalJobExecutionDurationSeconds": number
            }
         },
         "status": "string"
      },
      "insightsTypes": [ "string" ],
      "jobTimeoutMinutes": number,
      "locale": "string",
      "location": {
         "latitude": number,
         "longitude": number
      },
      "message": "string",
      "name": "string",
      "networkProfile": {
         "arn": "string",
         "description": "string",
         "downlinkBandwidthBits": number,
         "downlinkDelayMs": number,
         "downlinkJitterMs": number,
         "downlinkLossPercent": number,
         "name": "string",
         "type": "string",
         "uplinkBandwidthBits": number,
         "uplinkDelayMs": number,
         "uplinkJitterMs": number,
         "uplinkLossPercent": number
      },
      "parsingResultUrl": "string",
      "platform": "string",
      "radios": {
         "bluetooth": boolean,
         "gps": boolean,
         "nfc": boolean,
         "wifi": boolean
      },
      "result": "string",
      "resultCode": "string",
      "seed": number,
      "skipAppResign": boolean,
      "started": number,
      "status": "string",
      "stopped": number,
      "testSpecArn": "string",
      "totalJobs": number,
      "type": "string",
      "vpcConfig": {
         "securityGroupIds": [ "string" ],
         "subnetIds": [ "string" ],
         "vpcId": "string"
      },
      "webUrl": "string"
   }
}
```

## Response Elements
<a name="API_ScheduleRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [run](#API_ScheduleRun_ResponseSyntax) **   <a name="devicefarm-ScheduleRun-response-run"></a>
Information about the scheduled run.
Type: [Run](API_Run.md) object

## Errors
<a name="API_ScheduleRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** IdempotencyException **
An entity with the same name already exists.
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
<a name="API_ScheduleRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ScheduleRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ScheduleRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ScheduleRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ScheduleRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ScheduleRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ScheduleRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ScheduleRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ScheduleRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ScheduleRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ScheduleRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
