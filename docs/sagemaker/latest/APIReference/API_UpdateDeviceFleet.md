---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateDeviceFleet.html
---

# UpdateDeviceFleet
<a name="API_UpdateDeviceFleet"></a>

Updates a fleet of devices.

## Request Syntax
<a name="API_UpdateDeviceFleet_RequestSyntax"></a>

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
   "RoleArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateDeviceFleet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateDeviceFleet_RequestSyntax) **   <a name="sagemaker-UpdateDeviceFleet-request-Description"></a>
Description of the fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.
Pattern: `[-a-zA-Z0-9_.,;:! ]*`
Required: No

 ** [DeviceFleetName](#API_UpdateDeviceFleet_RequestSyntax) **   <a name="sagemaker-UpdateDeviceFleet-request-DeviceFleetName"></a>
The name of the fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [EnableIotRoleAlias](#API_UpdateDeviceFleet_RequestSyntax) **   <a name="sagemaker-UpdateDeviceFleet-request-EnableIotRoleAlias"></a>
Whether to create an AWS IoT Role Alias during device fleet creation. The name of the role alias generated will match this pattern: "SageMakerEdge-{DeviceFleetName}".
For example, if your device fleet is called "demo-fleet", the name of the role alias will be "SageMakerEdge-demo-fleet".
Type: Boolean
Required: No

 ** [OutputConfig](#API_UpdateDeviceFleet_RequestSyntax) **   <a name="sagemaker-UpdateDeviceFleet-request-OutputConfig"></a>
Output configuration for storing sample data collected by the fleet.
Type: [EdgeOutputConfig](API_EdgeOutputConfig.md) object
Required: Yes

 ** [RoleArn](#API_UpdateDeviceFleet_RequestSyntax) **   <a name="sagemaker-UpdateDeviceFleet-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the device.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

## Response Elements
<a name="API_UpdateDeviceFleet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateDeviceFleet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

## See Also
<a name="API_UpdateDeviceFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateDeviceFleet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateDeviceFleet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateDeviceFleet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateDeviceFleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateDeviceFleet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateDeviceFleet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateDeviceFleet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateDeviceFleet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateDeviceFleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateDeviceFleet)
