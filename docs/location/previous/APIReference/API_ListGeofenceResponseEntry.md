---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_ListGeofenceResponseEntry.html
---

# ListGeofenceResponseEntry
<a name="API_ListGeofenceResponseEntry"></a>

Contains a list of geofences stored in a given geofence collection.

**Note**
The returned geometry will always match the geometry format used when the geofence was created.

## Contents
<a name="API_ListGeofenceResponseEntry_Contents"></a>

 ** CreateTime **   <a name="location-Type-ListGeofenceResponseEntry-CreateTime"></a>
The timestamp for when the geofence was stored in a geofence collection in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`
Type: Timestamp
Required: Yes

 ** GeofenceId **   <a name="location-Type-ListGeofenceResponseEntry-GeofenceId"></a>
The geofence identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

 ** Geometry **   <a name="location-Type-ListGeofenceResponseEntry-Geometry"></a>
Contains the geofence geometry details describing the position of the geofence. Can be a circle, a polygon, or a multipolygon.
Type: [GeofenceGeometry](API_GeofenceGeometry.md) object
Required: Yes

 ** Status **   <a name="location-Type-ListGeofenceResponseEntry-Status"></a>
Identifies the state of the geofence. A geofence will hold one of the following states:
+  `ACTIVE` — The geofence has been indexed by the system.
+  `PENDING` — The geofence is being processed by the system.
+  `FAILED` — The geofence failed to be indexed by the system.
+  `DELETED` — The geofence has been deleted from the system index.
+  `DELETING` — The geofence is being deleted from the system index.
Type: String
Required: Yes

 ** UpdateTime **   <a name="location-Type-ListGeofenceResponseEntry-UpdateTime"></a>
The timestamp for when the geofence was last updated in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`
Type: Timestamp
Required: Yes

 ** GeofenceProperties **   <a name="location-Type-ListGeofenceResponseEntry-GeofenceProperties"></a>
User defined properties of the geofence. A property is a key-value pair stored with the geofence and added to any geofence event triggered with that geofence.
Format: `"key" : "value"`
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 3 items.
Key Length Constraints: Minimum length of 1. Maximum length of 20.
Value Length Constraints: Minimum length of 1. Maximum length of 40.
Required: No

## See Also
<a name="API_ListGeofenceResponseEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/ListGeofenceResponseEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/ListGeofenceResponseEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/ListGeofenceResponseEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
