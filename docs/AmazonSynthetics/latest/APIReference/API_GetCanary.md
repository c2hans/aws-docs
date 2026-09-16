---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanary.html
---

# GetCanary
<a name="API_GetCanary"></a>

Retrieves complete information about one canary. You must specify the name of the canary that you want. To get a list of canaries and their names, use [DescribeCanaries](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html).

## Request Syntax
<a name="API_GetCanary_RequestSyntax"></a>

```
GET /canary/{{name}}?dryRunId={{DryRunId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCanary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DryRunId](#API_GetCanary_RequestSyntax) **   <a name="synthetics-GetCanary-request-uri-DryRunId"></a>
The DryRunId associated with an existing canary’s dry run. You can use this DryRunId to retrieve information about the dry run.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

 ** [name](#API_GetCanary_RequestSyntax) **   <a name="synthetics-GetCanary-request-uri-Name"></a>
The name of the canary that you want details for.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[0-9a-z_\-]+$`
Required: Yes

## Request Body
<a name="API_GetCanary_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCanary_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Canary": {
      "ArtifactConfig": {
         "S3Encryption": {
            "EncryptionMode": "string",
            "KmsKeyArn": "string"
         }
      },
      "ArtifactS3Location": "string",
      "BrowserConfigs": [
         {
            "BrowserType": "string"
         }
      ],
      "Code": {
         "BlueprintTypes": [ "string" ],
         "Dependencies": [
            {
               "Reference": "string",
               "Type": "string"
            }
         ],
         "Handler": "string",
         "SourceLocationArn": "string"
      },
      "DryRunConfig": {
         "DryRunId": "string",
         "LastDryRunExecutionStatus": "string"
      },
      "EngineArn": "string",
      "EngineConfigs": [
         {
            "BrowserType": "string",
            "EngineArn": "string"
         }
      ],
      "ExecutionRoleArn": "string",
      "FailureRetentionPeriodInDays": number,
      "Id": "string",
      "MultiLocationConfig": {
         "LocationType": "string",
         "PrimaryLocation": "string",
         "Replicas": [
            {
               "CanaryState": "string",
               "LastModified": number,
               "Location": "string",
               "ReplicationStatus": {
                  "State": "string",
                  "StateReason": "string",
                  "StateReasonCode": "string"
               },
               "VpcConfig": {
                  "Ipv6AllowedForDualStack": boolean,
                  "SecurityGroupIds": [ "string" ],
                  "SubnetIds": [ "string" ],
                  "VpcId": "string"
               }
            }
         ],
         "ReplicationState": "string"
      },
      "Name": "string",
      "ProvisionedResourceCleanup": "string",
      "RunConfig": {
         "ActiveTracing": boolean,
         "EphemeralStorage": number,
         "MemoryInMB": number,
         "TimeoutInSeconds": number
      },
      "RuntimeVersion": "string",
      "Schedule": {
         "DurationInSeconds": number,
         "Expression": "string",
         "RetryConfig": {
            "MaxRetries": number
         }
      },
      "Status": {
         "State": "string",
         "StateReason": "string",
         "StateReasonCode": "string"
      },
      "SuccessRetentionPeriodInDays": number,
      "Tags": {
         "string" : "string"
      },
      "Timeline": {
         "Created": number,
         "LastModified": number,
         "LastStarted": number,
         "LastStopped": number
      },
      "VisualReference": {
         "BaseCanaryRunId": "string",
         "BaseScreenshots": [
            {
               "IgnoreCoordinates": [ "string" ],
               "ScreenshotName": "string"
            }
         ],
         "BrowserType": "string"
      },
      "VisualReferences": [
         {
            "BaseCanaryRunId": "string",
            "BaseScreenshots": [
               {
                  "IgnoreCoordinates": [ "string" ],
                  "ScreenshotName": "string"
               }
            ],
            "BrowserType": "string"
         }
      ],
      "VpcConfig": {
         "Ipv6AllowedForDualStack": boolean,
         "SecurityGroupIds": [ "string" ],
         "SubnetIds": [ "string" ],
         "VpcId": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetCanary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Canary](#API_GetCanary_ResponseSyntax) **   <a name="synthetics-GetCanary-response-Canary"></a>
A structure that contains the full information about the canary.
Type: [Canary](API_Canary.md) object

## Errors
<a name="API_GetCanary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unknown internal error occurred.
HTTP Status Code: 500

 ** ValidationException **
A parameter could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_GetCanary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/synthetics-2017-10-11/GetCanary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/synthetics-2017-10-11/GetCanary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/GetCanary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/synthetics-2017-10-11/GetCanary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/GetCanary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/synthetics-2017-10-11/GetCanary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/synthetics-2017-10-11/GetCanary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/synthetics-2017-10-11/GetCanary)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/synthetics-2017-10-11/GetCanary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/GetCanary)
