---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_DevicePosition.html
---

# DevicePosition
<a name="API_DevicePosition"></a>

Contains the device position details.

## Contents
<a name="API_DevicePosition_Contents"></a>

 ** Position **   <a name="location-Type-DevicePosition-Position"></a>
The last known device position.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** ReceivedTime **   <a name="location-Type-DevicePosition-ReceivedTime"></a>
The timestamp for when the tracker resource received the device position in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp
Required: Yes

 ** SampleTime **   <a name="location-Type-DevicePosition-SampleTime"></a>
The timestamp at which the device's position was determined. Uses [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp
Required: Yes

 ** Accuracy **   <a name="location-Type-DevicePosition-Accuracy"></a>
The accuracy of the device position.
Type: [PositionalAccuracy](API_PositionalAccuracy.md) object
Required: No

 ** DeviceId **   <a name="location-Type-DevicePosition-DeviceId"></a>
The device whose position you retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: No

 ** PositionProperties **   <a name="location-Type-DevicePosition-PositionProperties"></a>
The properties associated with the position.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 4 items.
Key Length Constraints: Minimum length of 1. Maximum length of 20.
Value Length Constraints: Minimum length of 1. Maximum length of 150.
Required: No

## See Also
<a name="API_DevicePosition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/DevicePosition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/DevicePosition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/DevicePosition)
