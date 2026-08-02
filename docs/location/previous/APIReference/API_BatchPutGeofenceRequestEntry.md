---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_BatchPutGeofenceRequestEntry.html
---

# BatchPutGeofenceRequestEntry
<a name="API_BatchPutGeofenceRequestEntry"></a>

Contains geofence geometry details.

## Contents
<a name="API_BatchPutGeofenceRequestEntry_Contents"></a>

 ** GeofenceId **   <a name="location-Type-BatchPutGeofenceRequestEntry-GeofenceId"></a>
The identifier for the geofence to be stored in a given geofence collection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

 ** Geometry **   <a name="location-Type-BatchPutGeofenceRequestEntry-Geometry"></a>
Contains the details to specify the position of the geofence. Can be a circle, a polygon, or a multipolygon. `Polygon` and `MultiPolygon` geometries can be defined using their respective parameters, or encoded in Geobuf format using the `Geobuf` parameter. Including multiple geometry types in the same request will return a validation error.
The geofence `Polygon` and `MultiPolygon` formats support a maximum of 1,000 total vertices. The `Geobuf` format supports a maximum of 100,000 vertices.
Type: [GeofenceGeometry](API_GeofenceGeometry.md) object
Required: Yes

 ** GeofenceProperties **   <a name="location-Type-BatchPutGeofenceRequestEntry-GeofenceProperties"></a>
Associates one of more properties with the geofence. A property is a key-value pair stored with the geofence and added to any geofence event triggered with that geofence.
Format: `"key" : "value"`
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 3 items.
Key Length Constraints: Minimum length of 1. Maximum length of 20.
Value Length Constraints: Minimum length of 1. Maximum length of 40.
Required: No

## See Also
<a name="API_BatchPutGeofenceRequestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/BatchPutGeofenceRequestEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/BatchPutGeofenceRequestEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/BatchPutGeofenceRequestEntry)
