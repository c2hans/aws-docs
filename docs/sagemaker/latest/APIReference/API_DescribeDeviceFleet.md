---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeDeviceFleet.html
---

# DescribeDeviceFleet
<a name="API_DescribeDeviceFleet"></a>

A description of the fleet the device belongs to.

## Request Syntax
<a name="API_DescribeDeviceFleet_RequestSyntax"></a>

```
{
   "DeviceFleetName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDeviceFleet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeviceFleetName](#API_DescribeDeviceFleet_RequestSyntax) **   <a name="sagemaker-DescribeDeviceFleet-request-DeviceFleetName"></a>
The name of the fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeDeviceFleet_ResponseSyntax"></a>

```
{
   "Description": "string",
   "DeviceFleetArn": "string",
   "DeviceFleetName": "string",
   "IotRoleAlias": "string",
   "OutputConfig": {
      "KmsKeyId": "string",
      "PresetDeploymentConfig": "string",
      "PresetDeploymentType": "string",
      "S3OutputLocation": "string"
   },
   "RoleArn": "string"
}
```

## Response Elements
<a name="API_DescribeDeviceFleet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_DescribeDeviceFleet_ResponseSyntax) **   <a name="sagemaker-DescribeDeviceFleet-response-Description"></a>
A description of the fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.
Pattern: `[-a-zA-Z0-9_.,;:! ]*`

 ** [DeviceFleetArn](#API_DescribeDeviceFleet_ResponseSyntax) **   <a name="sagemaker-DescribeDeviceFleet-response-DeviceFleetArn"></a>
The The Amazon Resource Name (ARN) of the fleet.
Type: String
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:device-fleet/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [DeviceFleetName](#API_DescribeDeviceFleet_ResponseSyntax) **   <a name="sagemaker-DescribeDeviceFleet-response-DeviceFleetName"></a>
The name of the fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [IotRoleAlias](#API_DescribeDeviceFleet_ResponseSyntax) **   <a name="sagemaker-DescribeDeviceFleet-response-IotRoleAlias"></a>
The Amazon Resource Name (ARN) alias created in AWS Internet of Things (IoT).
Type: String
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:rolealias/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [OutputConfig](#API_DescribeDeviceFleet_ResponseSyntax) **   <a name="sagemaker-DescribeDeviceFleet-response-OutputConfig"></a>
The output configuration for storing sampled data.
Type: [EdgeOutputConfig](API_EdgeOutputConfig.md) object

 ** [RoleArn](#API_DescribeDeviceFleet_ResponseSyntax) **   <a name="sagemaker-DescribeDeviceFleet-response-RoleArn"></a>
The Amazon Resource Name (ARN) that has access to AWS Internet of Things (IoT).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

## Errors
<a name="API_DescribeDeviceFleet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDeviceFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeDeviceFleet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeDeviceFleet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeDeviceFleet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeDeviceFleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeDeviceFleet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeDeviceFleet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeDeviceFleet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeDeviceFleet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeDeviceFleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeDeviceFleet)
