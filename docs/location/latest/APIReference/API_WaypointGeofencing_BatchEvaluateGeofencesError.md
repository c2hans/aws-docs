---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchEvaluateGeofencesError.html
---

# BatchEvaluateGeofencesError
<a name="API_WaypointGeofencing_BatchEvaluateGeofencesError"></a>

Contains error details for each device that failed to evaluate its position against the geofences in a given geofence collection.

## Contents
<a name="API_WaypointGeofencing_BatchEvaluateGeofencesError_Contents"></a>

 ** DeviceId **   <a name="location-Type-WaypointGeofencing_BatchEvaluateGeofencesError-DeviceId"></a>
The device associated with the position evaluation error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

 ** Error **   <a name="location-Type-WaypointGeofencing_BatchEvaluateGeofencesError-Error"></a>
Contains details associated to the batch error.
Type: [BatchItemError](API_WaypointGeofencing_BatchItemError.md) object
Required: Yes

 ** SampleTime **   <a name="location-Type-WaypointGeofencing_BatchEvaluateGeofencesError-SampleTime"></a>
Specifies a timestamp for when the error occurred in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`
Type: Timestamp
Required: Yes

## See Also
<a name="API_WaypointGeofencing_BatchEvaluateGeofencesError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointgeofencing-2020-11-19/BatchEvaluateGeofencesError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointgeofencing-2020-11-19/BatchEvaluateGeofencesError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointgeofencing-2020-11-19/BatchEvaluateGeofencesError)
