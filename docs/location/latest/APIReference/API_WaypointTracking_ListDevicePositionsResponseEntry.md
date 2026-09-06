---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ListDevicePositionsResponseEntry.html
---

# ListDevicePositionsResponseEntry
<a name="API_WaypointTracking_ListDevicePositionsResponseEntry"></a>

Contains the tracker resource details.

## Contents
<a name="API_WaypointTracking_ListDevicePositionsResponseEntry_Contents"></a>

 ** DeviceId **   <a name="location-Type-WaypointTracking_ListDevicePositionsResponseEntry-DeviceId"></a>
The ID of the device for this position.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

 ** Position **   <a name="location-Type-WaypointTracking_ListDevicePositionsResponseEntry-Position"></a>
The last known device position. Empty if no positions currently stored.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** SampleTime **   <a name="location-Type-WaypointTracking_ListDevicePositionsResponseEntry-SampleTime"></a>
The timestamp at which the device position was determined. Uses [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp
Required: Yes

 ** Accuracy **   <a name="location-Type-WaypointTracking_ListDevicePositionsResponseEntry-Accuracy"></a>
The accuracy of the device position.
Type: [PositionalAccuracy](API_WaypointTracking_PositionalAccuracy.md) object
Required: No

 ** PositionProperties **   <a name="location-Type-WaypointTracking_ListDevicePositionsResponseEntry-PositionProperties"></a>
The properties associated with the position.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 4 items.
Key Length Constraints: Minimum length of 1. Maximum length of 20.
Value Length Constraints: Minimum length of 1. Maximum length of 150.
Required: No

## See Also
<a name="API_WaypointTracking_ListDevicePositionsResponseEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointtracking-2020-11-19/ListDevicePositionsResponseEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointtracking-2020-11-19/ListDevicePositionsResponseEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointtracking-2020-11-19/ListDevicePositionsResponseEntry)
