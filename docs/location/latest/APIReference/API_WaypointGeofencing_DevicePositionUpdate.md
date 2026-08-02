---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_DevicePositionUpdate.html
---

# DevicePositionUpdate
<a name="API_WaypointGeofencing_DevicePositionUpdate"></a>

## Contents
<a name="API_WaypointGeofencing_DevicePositionUpdate_Contents"></a>

 ** DeviceId **   <a name="location-Type-WaypointGeofencing_DevicePositionUpdate-DeviceId"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

 ** Position **   <a name="location-Type-WaypointGeofencing_DevicePositionUpdate-Position"></a>

Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** SampleTime **   <a name="location-Type-WaypointGeofencing_DevicePositionUpdate-SampleTime"></a>

Type: Timestamp
Required: Yes

 ** Accuracy **   <a name="location-Type-WaypointGeofencing_DevicePositionUpdate-Accuracy"></a>

Type: [PositionalAccuracy](API_WaypointGeofencing_PositionalAccuracy.md) object
Required: No

 ** PositionProperties **   <a name="location-Type-WaypointGeofencing_DevicePositionUpdate-PositionProperties"></a>

Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 4 items.
Key Length Constraints: Minimum length of 1. Maximum length of 20.
Value Length Constraints: Minimum length of 1. Maximum length of 150.
Required: No

## See Also
<a name="API_WaypointGeofencing_DevicePositionUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointgeofencing-2020-11-19/DevicePositionUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointgeofencing-2020-11-19/DevicePositionUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointgeofencing-2020-11-19/DevicePositionUpdate)
