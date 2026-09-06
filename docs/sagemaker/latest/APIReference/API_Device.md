---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Device.html
---

# Device
<a name="API_Device"></a>

Information of a particular device.

## Contents
<a name="API_Device_Contents"></a>

 ** DeviceName **   <a name="sagemaker-Type-Device-DeviceName"></a>
The name of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** Description **   <a name="sagemaker-Type-Device-Description"></a>
Description of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[-a-zA-Z0-9_.,;:! ]*`
Required: No

 ** IotThingName **   <a name="sagemaker-Type-Device-IotThingName"></a>
 AWS Internet of Things (IoT) object name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

## See Also
<a name="API_Device_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Device)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Device)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Device)
