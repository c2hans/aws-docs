---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_DevicePositionUpdate.html
---

# DevicePositionUpdate
<a name="API_DevicePositionUpdate"></a>

Contains the position update details for a device.

## Contents
<a name="API_DevicePositionUpdate_Contents"></a>

 ** DeviceId **   <a name="location-Type-DevicePositionUpdate-DeviceId"></a>
The device associated to the position update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

 ** Position **   <a name="location-Type-DevicePositionUpdate-Position"></a>
The latest device position defined in [WGS 84](https://earth-info.nga.mil/index.php?dir=wgs84&action=wgs84) format: `[X or longitude, Y or latitude]`.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** SampleTime **   <a name="location-Type-DevicePositionUpdate-SampleTime"></a>
The timestamp at which the device's position was determined. Uses [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`
Type: Timestamp
Required: Yes

 ** Accuracy **   <a name="location-Type-DevicePositionUpdate-Accuracy"></a>
The accuracy of the device position.
Type: [PositionalAccuracy](API_PositionalAccuracy.md) object
Required: No

 ** PositionProperties **   <a name="location-Type-DevicePositionUpdate-PositionProperties"></a>
Associates one of more properties with the position update. A property is a key-value pair stored with the position update and added to any geofence event the update may trigger.
Format: `"key" : "value"`
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 4 items.
Key Length Constraints: Minimum length of 1. Maximum length of 20.
Value Length Constraints: Minimum length of 1. Maximum length of 150.
Required: No

## See Also
<a name="API_DevicePositionUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/DevicePositionUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/DevicePositionUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/DevicePositionUpdate)
