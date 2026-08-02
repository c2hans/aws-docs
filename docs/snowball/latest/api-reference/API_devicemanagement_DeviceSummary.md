---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_DeviceSummary.html
---

# DeviceSummary
<a name="API_devicemanagement_DeviceSummary"></a>

Identifying information about the device.

## Contents
<a name="API_devicemanagement_DeviceSummary_Contents"></a>

 ** associatedWithJob **   <a name="Snowball-Type-devicemanagement_DeviceSummary-associatedWithJob"></a>
The ID of the job used to order the device.
Type: String
Required: No

 ** managedDeviceArn **   <a name="Snowball-Type-devicemanagement_DeviceSummary-managedDeviceArn"></a>
The Amazon Resource Name (ARN) of the device.
Type: String
Required: No

 ** managedDeviceId **   <a name="Snowball-Type-devicemanagement_DeviceSummary-managedDeviceId"></a>
The ID of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** tags **   <a name="Snowball-Type-devicemanagement_DeviceSummary-tags"></a>
Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment.
Type: String to string map
Required: No

## See Also
<a name="API_devicemanagement_DeviceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/DeviceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/DeviceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/DeviceSummary)
