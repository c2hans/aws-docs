---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListRuns.html
---

# ListRuns
<a name="API_ListRuns"></a>

Gets information about runs, given an AWS Device Farm project ARN.

## Request Syntax
<a name="API_ListRuns_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRuns_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_ListRuns_RequestSyntax) **   <a name="devicefarm-ListRuns-request-arn"></a>
The Amazon Resource Name (ARN) of the project for which you want to list runs.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [nextToken](#API_ListRuns_RequestSyntax) **   <a name="devicefarm-ListRuns-request-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListRuns_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "runs": [
      {
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
   ]
}
```

## Response Elements
<a name="API_ListRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRuns_ResponseSyntax) **   <a name="devicefarm-ListRuns-response-nextToken"></a>
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

 ** [runs](#API_ListRuns_ResponseSyntax) **   <a name="devicefarm-ListRuns-response-runs"></a>
Information about the runs.
Type: Array of [Run](API_Run.md) objects

## Errors
<a name="API_ListRuns_Errors"></a>

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
<a name="API_ListRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListRuns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListRuns)
