---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchPutGeofenceRequestEntry.html
---

# BatchPutGeofenceRequestEntry
<a name="API_WaypointGeofencing_BatchPutGeofenceRequestEntry"></a>

Contains geofence geometry details.

## Contents
<a name="API_WaypointGeofencing_BatchPutGeofenceRequestEntry_Contents"></a>

 ** GeofenceId **   <a name="location-Type-WaypointGeofencing_BatchPutGeofenceRequestEntry-GeofenceId"></a>
The identifier for the geofence to be stored in a given geofence collection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

 ** Geometry **   <a name="location-Type-WaypointGeofencing_BatchPutGeofenceRequestEntry-Geometry"></a>
Contains the details to specify the position of the geofence. Can be a polygon, a circle or a polygon encoded in Geobuf format. Including multiple selections will return a validation error.
The [ geofence polygon](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_GeofenceGeometry.html) format supports a maximum of 1,000 vertices. The [Geofence geobuf](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_GeofenceGeometry.html) format supports a maximum of 100,000 vertices.
Type: [GeofenceGeometry](API_WaypointGeofencing_GeofenceGeometry.md) object
Required: Yes

 ** GeofenceProperties **   <a name="location-Type-WaypointGeofencing_BatchPutGeofenceRequestEntry-GeofenceProperties"></a>
Associates one of more properties with the geofence. A property is a key-value pair stored with the geofence and added to any geofence event triggered with that geofence.
Format: `"key" : "value"`
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 3 items.
Key Length Constraints: Minimum length of 1. Maximum length of 20.
Value Length Constraints: Minimum length of 1. Maximum length of 40.
Required: No

## See Also
<a name="API_WaypointGeofencing_BatchPutGeofenceRequestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointgeofencing-2020-11-19/BatchPutGeofenceRequestEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointgeofencing-2020-11-19/BatchPutGeofenceRequestEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointgeofencing-2020-11-19/BatchPutGeofenceRequestEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
