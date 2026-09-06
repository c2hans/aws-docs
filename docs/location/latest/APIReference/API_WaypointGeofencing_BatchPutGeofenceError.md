---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchPutGeofenceError.html
---

# BatchPutGeofenceError
<a name="API_WaypointGeofencing_BatchPutGeofenceError"></a>

Contains error details for each geofence that failed to be stored in a given geofence collection.

## Contents
<a name="API_WaypointGeofencing_BatchPutGeofenceError_Contents"></a>

 ** Error **   <a name="location-Type-WaypointGeofencing_BatchPutGeofenceError-Error"></a>
Contains details associated to the batch error.
Type: [BatchItemError](API_WaypointGeofencing_BatchItemError.md) object
Required: Yes

 ** GeofenceId **   <a name="location-Type-WaypointGeofencing_BatchPutGeofenceError-GeofenceId"></a>
The geofence associated with the error message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

## See Also
<a name="API_WaypointGeofencing_BatchPutGeofenceError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointgeofencing-2020-11-19/BatchPutGeofenceError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointgeofencing-2020-11-19/BatchPutGeofenceError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointgeofencing-2020-11-19/BatchPutGeofenceError)
