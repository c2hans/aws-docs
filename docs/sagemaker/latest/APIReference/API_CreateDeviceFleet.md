---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateDeviceFleet.html
---

# CreateDeviceFleet
<a name="API_CreateDeviceFleet"></a>

Creates a device fleet.

## Request Syntax
<a name="API_CreateDeviceFleet_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "DeviceFleetName": "{{string}}",
   "EnableIotRoleAlias": {{boolean}},
   "OutputConfig": {
      "KmsKeyId": "{{string}}",
      "PresetDeploymentConfig": "{{string}}",
      "PresetDeploymentType": "{{string}}",
      "S3OutputLocation": "{{string}}"
   },
   "RoleArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateDeviceFleet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_CreateDeviceFleet_RequestSyntax) **   <a name="sagemaker-CreateDeviceFleet-request-Description"></a>
A description of the fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.
Pattern: `[-a-zA-Z0-9_.,;:! ]*`
Required: No

 ** [DeviceFleetName](#API_CreateDeviceFleet_RequestSyntax) **   <a name="sagemaker-CreateDeviceFleet-request-DeviceFleetName"></a>
The name of the fleet that the device belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [EnableIotRoleAlias](#API_CreateDeviceFleet_RequestSyntax) **   <a name="sagemaker-CreateDeviceFleet-request-EnableIotRoleAlias"></a>
Whether to create an AWS IoT Role Alias during device fleet creation. The name of the role alias generated will match this pattern: "SageMakerEdge-{DeviceFleetName}".
For example, if your device fleet is called "demo-fleet", the name of the role alias will be "SageMakerEdge-demo-fleet".
Type: Boolean
Required: No

 ** [OutputConfig](#API_CreateDeviceFleet_RequestSyntax) **   <a name="sagemaker-CreateDeviceFleet-request-OutputConfig"></a>
The output configuration for storing sample data collected by the fleet.
Type: [EdgeOutputConfig](API_EdgeOutputConfig.md) object
Required: Yes

 ** [RoleArn](#API_CreateDeviceFleet_RequestSyntax) **   <a name="sagemaker-CreateDeviceFleet-request-RoleArn"></a>
The Amazon Resource Name (ARN) that has access to AWS Internet of Things (IoT).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** [Tags](#API_CreateDeviceFleet_RequestSyntax) **   <a name="sagemaker-CreateDeviceFleet-request-Tags"></a>
Creates tags for the specified fleet.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Elements
<a name="API_CreateDeviceFleet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateDeviceFleet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateDeviceFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateDeviceFleet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateDeviceFleet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateDeviceFleet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateDeviceFleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateDeviceFleet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateDeviceFleet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateDeviceFleet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateDeviceFleet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateDeviceFleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateDeviceFleet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
