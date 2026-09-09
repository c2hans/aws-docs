---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GetDeviceFleetReport.html
---

# GetDeviceFleetReport
<a name="API_GetDeviceFleetReport"></a>

Describes a fleet.

## Request Syntax
<a name="API_GetDeviceFleetReport_RequestSyntax"></a>

```
{
   "DeviceFleetName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDeviceFleetReport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeviceFleetName](#API_GetDeviceFleetReport_RequestSyntax) **   <a name="sagemaker-GetDeviceFleetReport-request-DeviceFleetName"></a>
The name of the fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_GetDeviceFleetReport_ResponseSyntax"></a>

```
{
   "AgentVersions": [
      {
         "AgentCount": number,
         "Version": "string"
      }
   ],
   "Description": "string",
   "DeviceFleetArn": "string",
   "DeviceFleetName": "string",
   "DeviceStats": {
      "ConnectedDeviceCount": number,
      "RegisteredDeviceCount": number
   },
   "ModelStats": [
      {
         "ActiveDeviceCount": number,
         "ConnectedDeviceCount": number,
         "ModelName": "string",
         "ModelVersion": "string",
         "OfflineDeviceCount": number,
         "SamplingDeviceCount": number
      }
   ],
   "OutputConfig": {
      "KmsKeyId": "string",
      "PresetDeploymentConfig": "string",
      "PresetDeploymentType": "string",
      "S3OutputLocation": "string"
   }
}
```

## Response Elements
<a name="API_GetDeviceFleetReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AgentVersions](#API_GetDeviceFleetReport_ResponseSyntax) **   <a name="sagemaker-GetDeviceFleetReport-response-AgentVersions"></a>
The versions of Edge Manager agent deployed on the fleet.
Type: Array of [AgentVersion](API_AgentVersion.md) objects

 ** [Description](#API_GetDeviceFleetReport_ResponseSyntax) **   <a name="sagemaker-GetDeviceFleetReport-response-Description"></a>
Description of the fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.
Pattern: `[-a-zA-Z0-9_.,;:! ]*`

 ** [DeviceFleetArn](#API_GetDeviceFleetReport_ResponseSyntax) **   <a name="sagemaker-GetDeviceFleetReport-response-DeviceFleetArn"></a>
The Amazon Resource Name (ARN) of the device.
Type: String
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:device-fleet/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [DeviceFleetName](#API_GetDeviceFleetReport_ResponseSyntax) **   <a name="sagemaker-GetDeviceFleetReport-response-DeviceFleetName"></a>
The name of the fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [DeviceStats](#API_GetDeviceFleetReport_ResponseSyntax) **   <a name="sagemaker-GetDeviceFleetReport-response-DeviceStats"></a>
Status of devices.
Type: [DeviceStats](API_DeviceStats.md) object

 ** [ModelStats](#API_GetDeviceFleetReport_ResponseSyntax) **   <a name="sagemaker-GetDeviceFleetReport-response-ModelStats"></a>
Status of model on device.
Type: Array of [EdgeModelStat](API_EdgeModelStat.md) objects

 ** [OutputConfig](#API_GetDeviceFleetReport_ResponseSyntax) **   <a name="sagemaker-GetDeviceFleetReport-response-OutputConfig"></a>
The output configuration for storing sample data collected by the fleet.
Type: [EdgeOutputConfig](API_EdgeOutputConfig.md) object

## Errors
<a name="API_GetDeviceFleetReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetDeviceFleetReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/GetDeviceFleetReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/GetDeviceFleetReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/GetDeviceFleetReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/GetDeviceFleetReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/GetDeviceFleetReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/GetDeviceFleetReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/GetDeviceFleetReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/GetDeviceFleetReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/GetDeviceFleetReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/GetDeviceFleetReport)
