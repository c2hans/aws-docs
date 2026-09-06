---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_Device.html
---

# Device
<a name="API_Device"></a>

Describes a device.

## Contents
<a name="API_Device_Contents"></a>

 ** AWSLocation **   <a name="networkmanager-Type-Device-AWSLocation"></a>
The AWS location of the device.
Type: [AWSLocation](API_AWSLocation.md) object
Required: No

 ** CreatedAt **   <a name="networkmanager-Type-Device-CreatedAt"></a>
The date and time that the site was created.
Type: Timestamp
Required: No

 ** Description **   <a name="networkmanager-Type-Device-Description"></a>
The description of the device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** DeviceArn **   <a name="networkmanager-Type-Device-DeviceArn"></a>
The Amazon Resource Name (ARN) of the device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

 ** DeviceId **   <a name="networkmanager-Type-Device-DeviceId"></a>
The ID of the device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** GlobalNetworkId **   <a name="networkmanager-Type-Device-GlobalNetworkId"></a>
The ID of the global network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** Location **   <a name="networkmanager-Type-Device-Location"></a>
The site location.
Type: [Location](API_Location.md) object
Required: No

 ** Model **   <a name="networkmanager-Type-Device-Model"></a>
The device model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** SerialNumber **   <a name="networkmanager-Type-Device-SerialNumber"></a>
The device serial number.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** SiteId **   <a name="networkmanager-Type-Device-SiteId"></a>
The site ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** State **   <a name="networkmanager-Type-Device-State"></a>
The device state.
Type: String
Valid Values: `PENDING | AVAILABLE | DELETING | UPDATING`
Required: No

 ** Tags **   <a name="networkmanager-Type-Device-Tags"></a>
The tags for the device.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** Type **   <a name="networkmanager-Type-Device-Type"></a>
The device type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** Vendor **   <a name="networkmanager-Type-Device-Vendor"></a>
The device vendor.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_Device_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Device)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Device)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Device)
