---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RegisterDevices.html
---

# RegisterDevices
<a name="API_RegisterDevices"></a>

Register devices.

## Request Syntax
<a name="API_RegisterDevices_RequestSyntax"></a>

```
{
   "DeviceFleetName": "{{string}}",
   "Devices": [
      {
         "Description": "{{string}}",
         "DeviceName": "{{string}}",
         "IotThingName": "{{string}}"
      }
   ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_RegisterDevices_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeviceFleetName](#API_RegisterDevices_RequestSyntax) **   <a name="sagemaker-RegisterDevices-request-DeviceFleetName"></a>
The name of the fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [Devices](#API_RegisterDevices_RequestSyntax) **   <a name="sagemaker-RegisterDevices-request-Devices"></a>
A list of devices to register with SageMaker Edge Manager.
Type: Array of [Device](API_Device.md) objects
Required: Yes

 ** [Tags](#API_RegisterDevices_RequestSyntax) **   <a name="sagemaker-RegisterDevices-request-Tags"></a>
The tags associated with devices.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Elements
<a name="API_RegisterDevices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RegisterDevices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_RegisterDevices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/RegisterDevices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/RegisterDevices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RegisterDevices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/RegisterDevices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RegisterDevices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/RegisterDevices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/RegisterDevices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/RegisterDevices)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/RegisterDevices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RegisterDevices)
