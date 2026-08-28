---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_UpdateCanary.html
---

# UpdateCanary
<a name="API_UpdateCanary"></a>

Updates the configuration of a canary that has already been created.

For multibrowser canaries, you can add or remove browsers by updating the browserConfig list in the update call. For example:
+ To add Firefox to a canary that currently uses Chrome, specify browserConfigs as [CHROME, FIREFOX]
+ To remove Firefox and keep only Chrome, specify browserConfigs as [CHROME]

You can't use this operation to update the tags of an existing canary. To change the tags of an existing canary, use [TagResource](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_TagResource.html).

**Note**
When you use the `dryRunId` field when updating a canary, the only other field you can provide is the `Schedule`. Adding any other field will thrown an exception.

## Request Syntax
<a name="API_UpdateCanary_RequestSyntax"></a>

```
PATCH /canary/{{name}} HTTP/1.1
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
   "DryRunId": "{{string}}",
   "ExecutionRoleArn": "{{string}}",
   "FailureRetentionPeriodInDays": {{number}},
   "ProvisionedResourceCleanup": "{{string}}",
   "RemoveReplicaLocations": [ "{{string}}" ],
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
   "VisualReference": {
      "BaseCanaryRunId": "{{string}}",
      "BaseScreenshots": [
         {
            "IgnoreCoordinates": [ "{{string}}" ],
            "ScreenshotName": "{{string}}"
         }
      ],
      "BrowserType": "{{string}}"
   },
   "VisualReferences": [
      {
         "BaseCanaryRunId": "{{string}}",
         "BaseScreenshots": [
            {
               "IgnoreCoordinates": [ "{{string}}" ],
               "ScreenshotName": "{{string}}"
            }
         ],
         "BrowserType": "{{string}}"
      }
   ],
   "VpcConfig": {
      "Ipv6AllowedForDualStack": {{boolean}},
      "SecurityGroupIds": [ "{{string}}" ],
      "SubnetIds": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_UpdateCanary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-uri-Name"></a>
The name of the canary that you want to update. To find the names of your canaries, use [DescribeCanaries](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html).
You cannot change the name of a canary that has already been created.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[0-9a-z_\-]+$`
Required: Yes

## Request Body
<a name="API_UpdateCanary_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AddReplicaLocations](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-AddReplicaLocations"></a>
A list of locations (Amazon Web Services Regions) to add as replicas for the canary. Each location specifies a Region and optional VPC configuration for the replica. You can add up to 50 replica locations.
Type: Array of [AddReplicaLocationInput](API_AddReplicaLocationInput.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** [ArtifactConfig](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-ArtifactConfig"></a>
A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.
Type: [ArtifactConfigInput](API_ArtifactConfigInput.md) object
Required: No

 ** [ArtifactS3Location](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-ArtifactS3Location"></a>
The location in Amazon S3 where Synthetics stores artifacts from the test runs of this canary. Artifacts include the log file, screenshots, and HAR files. The name of the Amazon S3 bucket can't include a period (.).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [BrowserConfigs](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-BrowserConfigs"></a>
A structure that specifies the browser type to use for a canary run. CloudWatch Synthetics supports running canaries on both `CHROME` and `FIREFOX` browsers.
If not specified, `browserConfigs` defaults to Chrome.
Type: Array of [BrowserConfig](API_BrowserConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** [Code](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-Code"></a>
A structure that includes the entry point from which the canary should start running your script. If the script is stored in an Amazon S3 bucket, the bucket name, key, and version are also included.
Type: [CanaryCodeInput](API_CanaryCodeInput.md) object
Required: No

 ** [DryRunId](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-DryRunId"></a>
Update the existing canary using the updated configurations from the DryRun associated with the DryRunId.
When you use the `dryRunId` field when updating a canary, the only other field you can provide is the `Schedule`. Adding any other field will thrown an exception.
Type: String
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** [ExecutionRoleArn](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-ExecutionRoleArn"></a>
The ARN of the IAM role to be used to run the canary. This role must already exist, and must include `lambda.amazonaws.com` as a principal in the trust policy. The role must also have the following permissions:
+  `s3:PutObject`
+  `s3:GetBucketLocation`
+  `s3:ListAllMyBuckets`
+  `cloudwatch:PutMetricData`
+  `logs:CreateLogGroup`
+  `logs:CreateLogStream`
+  `logs:CreateLogStream`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** [FailureRetentionPeriodInDays](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-FailureRetentionPeriodInDays"></a>
The number of days to retain data about failed runs of this canary.
This setting affects the range of information returned by [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html), as well as the range of information displayed in the Synthetics console.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1024.
Required: No

 ** [ProvisionedResourceCleanup](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-ProvisionedResourceCleanup"></a>
Specifies whether to also delete the Lambda functions and layers used by this canary when the canary is deleted.
If the value of this parameter is `OFF`, then the value of the `DeleteLambda` parameter of the [DeleteCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html) operation determines whether the Lambda functions and layers will be deleted.
Type: String
Valid Values: `AUTOMATIC | OFF`
Required: No

 ** [RemoveReplicaLocations](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-RemoveReplicaLocations"></a>
A list of locations (Amazon Web Services Regions) to remove as replicas for the canary. You must specify at least one location to remove. All replicas can be removed in a single API call and you cannot remove the primary location.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-{0,1}[0-9]{0,1}$`
Required: No

 ** [RunConfig](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-RunConfig"></a>
A structure that contains the timeout value that is used for each individual run of the canary.
Environment variable keys and values are encrypted at rest using AWS owned AWS KMS keys. However, the environment variables are not encrypted on the client side. Do not store sensitive information in them.
Type: [CanaryRunConfigInput](API_CanaryRunConfigInput.md) object
Required: No

 ** [RuntimeVersion](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-RuntimeVersion"></a>
Specifies the runtime version to use for the canary. For a list of valid runtime versions and for more information about runtime versions, see [ Canary Runtime Versions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [Schedule](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-Schedule"></a>
A structure that contains information about how often the canary is to run, and when these runs are to stop.
Type: [CanaryScheduleInput](API_CanaryScheduleInput.md) object
Required: No

 ** [SuccessRetentionPeriodInDays](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-SuccessRetentionPeriodInDays"></a>
The number of days to retain data about successful runs of this canary.
This setting affects the range of information returned by [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html), as well as the range of information displayed in the Synthetics console.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1024.
Required: No

 ** [VisualReference](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-VisualReference"></a>
Defines the screenshots to use as the baseline for comparisons during visual monitoring comparisons during future runs of this canary. If you omit this parameter, no changes are made to any baseline screenshots that the canary might be using already.
Visual monitoring is supported only on canaries running the **syn-puppeteer-node-3.2** runtime or later. For more information, see [ Visual monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_SyntheticsLogger_VisualTesting.html) and [ Visual monitoring blueprint](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Blueprints_VisualTesting.html)
Type: [VisualReferenceInput](API_VisualReferenceInput.md) object
Required: No

 ** [VisualReferences](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-VisualReferences"></a>
A list of visual reference configurations for the canary, one for each browser type that the canary is configured to run on. Visual references are used for visual monitoring comparisons.
 `syn-nodejs-puppeteer-11.0` and above, and `syn-nodejs-playwright-3.0` and above, only supports `visualReferences`. `visualReference` field is not supported.
Versions older than `syn-nodejs-puppeteer-11.0` supports both `visualReference` and `visualReferences` for backward compatibility. It is recommended to use `visualReferences` for consistency and future compatibility.
For multibrowser visual monitoring, you can update the baseline for all configured browsers in a single update call by specifying a list of VisualReference objects, one per browser. Each VisualReference object maps to a specific browser configuration, allowing you to manage visual baselines for multiple browsers simultaneously.
For single configuration canaries using Chrome browser (default browser), use visualReferences for `syn-nodejs-puppeteer-11.0` and above, and `syn-nodejs-playwright-3.0` and above canaries. The browserType in the visualReference object is not mandatory.
Type: Array of [VisualReferenceInput](API_VisualReferenceInput.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** [VpcConfig](#API_UpdateCanary_RequestSyntax) **   <a name="synthetics-UpdateCanary-request-VpcConfig"></a>
If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint. For more information, see [ Running a Canary in a VPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html).
Type: [VpcConfigInput](API_VpcConfigInput.md) object
Required: No

## Response Syntax
<a name="API_UpdateCanary_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateCanary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateCanary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform this operation on this resource.
HTTP Status Code: 403

 ** ConflictException **
A conflicting operation is already in progress.
HTTP Status Code: 409

 ** InternalServerException **
An unknown internal error occurred.
HTTP Status Code: 500

 ** RequestEntityTooLargeException **
One of the input resources is larger than is allowed.
HTTP Status Code: 413

 ** ResourceNotFoundException **
One of the specified resources was not found.
HTTP Status Code: 404

 ** ValidationException **
A parameter could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_UpdateCanary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/synthetics-2017-10-11/UpdateCanary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/synthetics-2017-10-11/UpdateCanary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/UpdateCanary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/synthetics-2017-10-11/UpdateCanary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/UpdateCanary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/synthetics-2017-10-11/UpdateCanary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/synthetics-2017-10-11/UpdateCanary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/synthetics-2017-10-11/UpdateCanary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/synthetics-2017-10-11/UpdateCanary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/UpdateCanary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
