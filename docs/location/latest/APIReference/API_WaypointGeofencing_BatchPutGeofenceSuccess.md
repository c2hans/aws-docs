---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchPutGeofenceSuccess.html
---

# BatchPutGeofenceSuccess
<a name="API_WaypointGeofencing_BatchPutGeofenceSuccess"></a>

Contains a summary of each geofence that was successfully stored in a given geofence collection.

## Contents
<a name="API_WaypointGeofencing_BatchPutGeofenceSuccess_Contents"></a>

 ** CreateTime **   <a name="location-Type-WaypointGeofencing_BatchPutGeofenceSuccess-CreateTime"></a>
The timestamp for when the geofence was stored in a geofence collection in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`
Type: Timestamp
Required: Yes

 ** GeofenceId **   <a name="location-Type-WaypointGeofencing_BatchPutGeofenceSuccess-GeofenceId"></a>
The geofence successfully stored in a geofence collection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

 ** UpdateTime **   <a name="location-Type-WaypointGeofencing_BatchPutGeofenceSuccess-UpdateTime"></a>
The timestamp for when the geofence was last updated in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`
Type: Timestamp
Required: Yes

## See Also
<a name="API_WaypointGeofencing_BatchPutGeofenceSuccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointgeofencing-2020-11-19/BatchPutGeofenceSuccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointgeofencing-2020-11-19/BatchPutGeofenceSuccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointgeofencing-2020-11-19/BatchPutGeofenceSuccess)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
