---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CreateCanary.html
---

# CreateCanary
<a name="API_CreateCanary"></a>

Creates a canary. Canaries are scripts that monitor your endpoints and APIs from the outside-in. Canaries help you check the availability and latency of your web services and troubleshoot anomalies by investigating load time data, screenshots of the UI, logs, and metrics. You can set up a canary to run continuously or just once.

Do not use `CreateCanary` to modify an existing canary. Use [UpdateCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_UpdateCanary.html) instead.

To create canaries, you must have the `CloudWatchSyntheticsFullAccess` policy. If you are creating a new IAM role for the canary, you also need the `iam:CreateRole`, `iam:CreatePolicy` and `iam:AttachRolePolicy` permissions. For more information, see [Necessary Roles and Permissions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Roles).

Do not include secrets or proprietary information in your canary names. The canary name makes up part of the Amazon Resource Name (ARN) for the canary, and the ARN is included in outbound calls over the internet. For more information, see [Security Considerations for Synthetics Canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html).

## Request Syntax
<a name="API_CreateCanary_RequestSyntax"></a>

```
POST /canary HTTP/1.1
Content-type: application/json

{
   "AddReplicaLocations": [
      {
         "Location": "{{string}}",
         "VpcConfig": {
            "Ipv6AllowedForDualStack": {{boolean}},
            "SecurityGroupIds": [ "{{string}}" ],
            "SubnetIds": [ "{{string}}" ]
         }
      }
   ],
   "ArtifactConfig": {
      "S3Encryption": {
         "EncryptionMode": "{{string}}",
         "KmsKeyArn": "{{string}}"
      }
   },
   "ArtifactS3Location": "{{string}}",
   "BrowserConfigs": [
      {
         "BrowserType": "{{string}}"
      }
   ],
   "Code": {
      "BlueprintTypes": [ "{{string}}" ],
      "Dependencies": [
         {
            "Reference": "{{string}}",
            "Type": "{{string}}"
         }
      ],
      "Handler": "{{string}}",
      "S3Bucket": "{{string}}",
      "S3Key": "{{string}}",
      "S3Version": "{{string}}",
      "ZipFile": {{blob}}
   },
   "ExecutionRoleArn": "{{string}}",
   "FailureRetentionPeriodInDays": {{number}},
   "Name": "{{string}}",
   "ProvisionedResourceCleanup": "{{string}}",
   "ResourcesToReplicateTags": [ "{{string}}" ],
   "RunConfig": {
      "ActiveTracing": {{boolean}},
      "EnvironmentVariables": {
         "{{string}}" : "{{string}}"
      },
      "EphemeralStorage": {{number}},
      "MemoryInMB": {{number}},
      "TimeoutInSeconds": {{number}}
   },
   "RuntimeVersion": "{{string}}",
   "Schedule": {
      "DurationInSeconds": {{number}},
      "Expression": "{{string}}",
      "RetryConfig": {
         "MaxRetries": {{number}}
      }
   },
   "SuccessRetentionPeriodInDays": {{number}},
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "VpcConfig": {
      "Ipv6AllowedForDualStack": {{boolean}},
      "SecurityGroupIds": [ "{{string}}" ],
      "SubnetIds": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_CreateCanary_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCanary_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AddReplicaLocations](#API_CreateCanary_RequestSyntax) **   <a name="synthetics-CreateCanary-request-AddReplicaLocations"></a>
A list of locations (Amazon Web Services Regions) to add as replicas for the canary. Each location specifies a Region and optional VPC configuration for the replica. You can add up to 50 replica locations.
Type: Array of [AddReplicaLocationInput](API_AddReplicaLocationInput.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** [ArtifactConfig](#API_CreateCanary_RequestSyntax) **   <a name="synthetics-CreateCanary-request-ArtifactConfig"></a>
A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.
Type: [ArtifactConfigInput](API_ArtifactConfigInput.md) object
Required: No

 ** [ArtifactS3Location](#API_CreateCanary_RequestSyntax) **   <a name="synthetics-CreateCanary-request-ArtifactS3Location"></a>
The location in Amazon S3 where Synthetics stores artifacts from the test runs of this canary. Artifacts include the log file, screenshots, and HAR files. The name of the Amazon S3 bucket can't include a period (.).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [BrowserConfigs](#API_CreateCanary_RequestSyntax) **   <a name="synthetics-CreateCanary-request-BrowserConfigs"></a>
CloudWatch Synthetics now supports multibrowser canaries for `syn-nodejs-puppeteer-11.0` and `syn-nodejs-playwright-3.0` runtimes. This feature allows you to run your canaries on both Firefox and Chrome browsers. To create a multibrowser canary, you need to specify the BrowserConfigs with a list of browsers you want to use.
If not specified, `browserConfigs` defaults to Chrome.
Type: Array of [BrowserConfig](API_BrowserConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** [Code](#API_CreateCanary_RequestSyntax) **   <a name="synthetics-CreateCanary-request-Code"></a>
A structure that includes the entry point from which the canary should start running your script. If the script is stored in an Amazon S3 bucket, the bucket name, key, and version are also included.
Type: [CanaryCodeInput](API_CanaryCodeInput.md) object
Required: Yes

 ** [ExecutionRoleArn](#API_CreateCanary_RequestSyntax) **   <a name="synthetics-CreateCanary-request-ExecutionRoleArn"></a>
The ARN of the IAM role to be used to run the canary. This role must already exist, and must include `lambda.amazonaws.com` as a principal in the trust policy. The role must also have the following permissions:
+  `s3:PutObject`
+  `s3:GetBucketLocation`
+  `s3:ListAllMyBuckets`
+  `cloudwatch:PutMetricData`
+  `logs:CreateLogGroup`
+  `logs:CreateLogStream`
+  `logs:PutLogEvents`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [FailureRetentionPeriodInDays](#API_CreateCanary_RequestSyntax) **   <a name="synthetics-CreateCanary-request-FailureRetentionPeriodInDays"></a>
The number of days to retain data about failed runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.
This setting affects the range of information returned by [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html), as well as the range of information displayed in the Synthetics console.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1024.
Required: No

 ** [Name](#API_CreateCanary_RequestSyntax) **   <a name="synthetics-CreateCanary-request-Name"></a>
The name for this canary. Be sure to give it a descriptive name that distinguishes it from other canaries in your account.
Do not include secrets or proprietary information in your canary names. The canary name makes up part of the canary ARN, and the ARN is included in outbound calls over the internet. For more information, see [Security Considerations for Synthetics Canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[0-9a-z_\-]+$`
Required: Yes

 ** [ProvisionedResourceCleanup](#API_CreateCanary_RequestSyntax) **   <a name="synthetics-CreateCanary-request-ProvisionedResourceCleanup"></a>
Specifies whether to also delete the Lambda functions and layers used by this canary when the canary is deleted. If you omit this parameter, the default of `AUTOMATIC` is used, which means that the Lambda functions and layers will be deleted when the canary is deleted.
If the value of this parameter is `OFF`, then the value of the `DeleteLambda` parameter of the [DeleteCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html) operation determines whether the Lambda functions and layers will be deleted.
Type: String
Valid Values: `AUTOMATIC | OFF`
Required: No

 ** [ResourcesToReplicateTags](#API_CreateCanary_RequestSyntax) **   <a name="synthetics-CreateCanary-request-ResourcesToReplicateTags"></a>
To have the tags that you apply to this canary also be applied to the Lambda function that the canary uses, specify this parameter with the value `lambda-function`.
If you specify this parameter and don't specify any tags in the `Tags` parameter, the canary creation fails.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `lambda-function`
Required: No

 ** [RunConfig](#API_CreateCanary_RequestSyntax) **   <a name="synthetics-CreateCanary-request-RunConfig"></a>
A structure that contains the configuration for individual canary runs, such as timeout value and environment variables.
Environment variable keys and values are encrypted at rest using AWS owned AWS KMS keys. However, the environment variables are not encrypted on the client side. Do not store sensitive information in them.
Type: [CanaryRunConfigInput](API_CanaryRunConfigInput.md) object
Required: No

 ** [RuntimeVersion](#API_CreateCanary_RequestSyntax) **   <a name="synthetics-CreateCanary-request-RuntimeVersion"></a>
Specifies the runtime version to use for the canary. For a list of valid runtime versions and more information about runtime versions, see [ Canary Runtime Versions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [Schedule](#API_CreateCanary_RequestSyntax) **   <a name="synthetics-CreateCanary-request-Schedule"></a>
A structure that contains information about how often the canary is to run and when these test runs are to stop.
Type: [CanaryScheduleInput](API_CanaryScheduleInput.md) object
Required: Yes

 ** [SuccessRetentionPeriodInDays](#API_CreateCanary_RequestSyntax) **   <a name="synthetics-CreateCanary-request-SuccessRetentionPeriodInDays"></a>
The number of days to retain data about successful runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.
This setting affects the range of information returned by [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html), as well as the range of information displayed in the Synthetics console.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1024.
Required: No

 ** [Tags](#API_CreateCanary_RequestSyntax) **   <a name="synthetics-CreateCanary-request-Tags"></a>
A list of key-value pairs to associate with the canary. You can associate as many as 50 tags with a canary.
Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only the resources that have certain tag values.
To have the tags that you apply to this canary also be applied to the Lambda function that the canary uses, specify this parameter with the value `lambda-function`.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [VpcConfig](#API_CreateCanary_RequestSyntax) **   <a name="synthetics-CreateCanary-request-VpcConfig"></a>
If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint. For more information, see [ Running a Canary in a VPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html).
Type: [VpcConfigInput](API_VpcConfigInput.md) object
Required: No

## Response Syntax
<a name="API_CreateCanary_ResponseSyntax"></a>

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
<a name="API_CreateCanary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Canary](#API_CreateCanary_ResponseSyntax) **   <a name="synthetics-CreateCanary-response-Canary"></a>
The full details about the canary you have created.
Type: [Canary](API_Canary.md) object

## Errors
<a name="API_CreateCanary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unknown internal error occurred.
HTTP Status Code: 500

 ** RequestEntityTooLargeException **
One of the input resources is larger than is allowed.
HTTP Status Code: 413

 ** ValidationException **
A parameter could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_CreateCanary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/synthetics-2017-10-11/CreateCanary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/synthetics-2017-10-11/CreateCanary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/CreateCanary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/synthetics-2017-10-11/CreateCanary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/CreateCanary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/synthetics-2017-10-11/CreateCanary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/synthetics-2017-10-11/CreateCanary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/synthetics-2017-10-11/CreateCanary)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/synthetics-2017-10-11/CreateCanary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/CreateCanary)
