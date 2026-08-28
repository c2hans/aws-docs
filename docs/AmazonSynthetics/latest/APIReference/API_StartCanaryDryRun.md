---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_StartCanaryDryRun.html
---

# StartCanaryDryRun
<a name="API_StartCanaryDryRun"></a>

Use this operation to start a dry run for a canary that has already been created

## Request Syntax
<a name="API_StartCanaryDryRun_RequestSyntax"></a>

```
POST /canary/{{name}}/dry-run/start HTTP/1.1
Content-type: application/json

{
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
   "ProvisionedResourceCleanup": "{{string}}",
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
<a name="API_StartCanaryDryRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_StartCanaryDryRun_RequestSyntax) **   <a name="synthetics-StartCanaryDryRun-request-uri-Name"></a>
The name of the canary that you want to dry run. To find canary names, use [DescribeCanaries](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html).
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[0-9a-z_\-]+$`
Required: Yes

## Request Body
<a name="API_StartCanaryDryRun_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ArtifactConfig](#API_StartCanaryDryRun_RequestSyntax) **   <a name="synthetics-StartCanaryDryRun-request-ArtifactConfig"></a>
A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.
Type: [ArtifactConfigInput](API_ArtifactConfigInput.md) object
Required: No

 ** [ArtifactS3Location](#API_StartCanaryDryRun_RequestSyntax) **   <a name="synthetics-StartCanaryDryRun-request-ArtifactS3Location"></a>
The location in Amazon S3 where Synthetics stores artifacts from the test runs of this canary. Artifacts include the log file, screenshots, and HAR files. The name of the Amazon S3 bucket can't include a period (.).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [BrowserConfigs](#API_StartCanaryDryRun_RequestSyntax) **   <a name="synthetics-StartCanaryDryRun-request-BrowserConfigs"></a>
A structure that specifies the browser type to use for a canary run. CloudWatch Synthetics supports running canaries on both `CHROME` and `FIREFOX` browsers.
If not specified, `browserConfigs` defaults to Chrome.
Type: Array of [BrowserConfig](API_BrowserConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** [Code](#API_StartCanaryDryRun_RequestSyntax) **   <a name="synthetics-StartCanaryDryRun-request-Code"></a>
Use this structure to input your script code for the canary. This structure contains the Lambda handler with the location where the canary should start running the script. If the script is stored in an Amazon S3 bucket, the bucket name, key, and version are also included. If the script was passed into the canary directly, the script code is contained in the value of `Zipfile`.
If you are uploading your canary scripts with an Amazon S3 bucket, your zip file should include your script in a certain folder structure.
+ For Node.js canaries, the folder structure must be `nodejs/node_modules/myCanaryFilename.js ` For more information, see [Packaging your Node.js canary files](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_WritingCanary_Nodejs.html#CloudWatch_Synthetics_Canaries_package)
+ For Python canaries, the folder structure must be `python/myCanaryFilename.py ` or `python/myFolder/myCanaryFilename.py ` For more information, see [Packaging your Python canary files](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_WritingCanary_Python.html#CloudWatch_Synthetics_Canaries_WritingCanary_Python_package)
Type: [CanaryCodeInput](API_CanaryCodeInput.md) object
Required: No

 ** [ExecutionRoleArn](#API_StartCanaryDryRun_RequestSyntax) **   <a name="synthetics-StartCanaryDryRun-request-ExecutionRoleArn"></a>
The ARN of the IAM role to be used to run the canary. This role must already exist, and must include `lambda.amazonaws.com` as a principal in the trust policy. The role must also have the following permissions:
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** [FailureRetentionPeriodInDays](#API_StartCanaryDryRun_RequestSyntax) **   <a name="synthetics-StartCanaryDryRun-request-FailureRetentionPeriodInDays"></a>
The number of days to retain data about failed runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.
This setting affects the range of information returned by [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html), as well as the range of information displayed in the Synthetics console.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1024.
Required: No

 ** [ProvisionedResourceCleanup](#API_StartCanaryDryRun_RequestSyntax) **   <a name="synthetics-StartCanaryDryRun-request-ProvisionedResourceCleanup"></a>
Specifies whether to also delete the Lambda functions and layers used by this canary when the canary is deleted. If you omit this parameter, the default of `AUTOMATIC` is used, which means that the Lambda functions and layers will be deleted when the canary is deleted.
If the value of this parameter is `OFF`, then the value of the `DeleteLambda` parameter of the [DeleteCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html) operation determines whether the Lambda functions and layers will be deleted.
Type: String
Valid Values: `AUTOMATIC | OFF`
Required: No

 ** [RunConfig](#API_StartCanaryDryRun_RequestSyntax) **   <a name="synthetics-StartCanaryDryRun-request-RunConfig"></a>
A structure that contains input information for a canary run.
Type: [CanaryRunConfigInput](API_CanaryRunConfigInput.md) object
Required: No

 ** [RuntimeVersion](#API_StartCanaryDryRun_RequestSyntax) **   <a name="synthetics-StartCanaryDryRun-request-RuntimeVersion"></a>
Specifies the runtime version to use for the canary. For a list of valid runtime versions and for more information about runtime versions, see [ Canary Runtime Versions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [SuccessRetentionPeriodInDays](#API_StartCanaryDryRun_RequestSyntax) **   <a name="synthetics-StartCanaryDryRun-request-SuccessRetentionPeriodInDays"></a>
The number of days to retain data about successful runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.
This setting affects the range of information returned by [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html), as well as the range of information displayed in the Synthetics console.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1024.
Required: No

 ** [VisualReference](#API_StartCanaryDryRun_RequestSyntax) **   <a name="synthetics-StartCanaryDryRun-request-VisualReference"></a>
An object that specifies what screenshots to use as a baseline for visual monitoring by this canary. It can optionally also specify parts of the screenshots to ignore during the visual monitoring comparison.
Visual monitoring is supported only on canaries running the **syn-puppeteer-node-3.2** runtime or later. For more information, see [ Visual monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_SyntheticsLogger_VisualTesting.html) and [ Visual monitoring blueprint](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Blueprints_VisualTesting.html)
Type: [VisualReferenceInput](API_VisualReferenceInput.md) object
Required: No

 ** [VisualReferences](#API_StartCanaryDryRun_RequestSyntax) **   <a name="synthetics-StartCanaryDryRun-request-VisualReferences"></a>
A list of visual reference configurations for the canary, one for each browser type that the canary is configured to run on. Visual references are used for visual monitoring comparisons.
 `syn-nodejs-puppeteer-11.0` and above, and `syn-nodejs-playwright-3.0` and above, only supports `visualReferences`. `visualReference` field is not supported.
Versions older than `syn-nodejs-puppeteer-11.0` supports both `visualReference` and `visualReferences` for backward compatibility. It is recommended to use `visualReferences` for consistency and future compatibility.
Type: Array of [VisualReferenceInput](API_VisualReferenceInput.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** [VpcConfig](#API_StartCanaryDryRun_RequestSyntax) **   <a name="synthetics-StartCanaryDryRun-request-VpcConfig"></a>
If this canary is to test an endpoint in a VPC, this structure contains information about the subnets and security groups of the VPC endpoint. For more information, see [ Running a Canary in a VPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html).
Type: [VpcConfigInput](API_VpcConfigInput.md) object
Required: No

## Response Syntax
<a name="API_StartCanaryDryRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DryRunConfig": {
      "DryRunId": "string",
      "LastDryRunExecutionStatus": "string"
   }
}
```

## Response Elements
<a name="API_StartCanaryDryRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DryRunConfig](#API_StartCanaryDryRun_ResponseSyntax) **   <a name="synthetics-StartCanaryDryRun-response-DryRunConfig"></a>
Returns the dry run configurations for a canary.
Type: [DryRunConfigOutput](API_DryRunConfigOutput.md) object

## Errors
<a name="API_StartCanaryDryRun_Errors"></a>

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

 ** ResourceNotFoundException **
One of the specified resources was not found.
HTTP Status Code: 404

 ** ValidationException **
A parameter could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_StartCanaryDryRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/synthetics-2017-10-11/StartCanaryDryRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/synthetics-2017-10-11/StartCanaryDryRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/StartCanaryDryRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/synthetics-2017-10-11/StartCanaryDryRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/StartCanaryDryRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/synthetics-2017-10-11/StartCanaryDryRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/synthetics-2017-10-11/StartCanaryDryRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/synthetics-2017-10-11/StartCanaryDryRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/synthetics-2017-10-11/StartCanaryDryRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/StartCanaryDryRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
