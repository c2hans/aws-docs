---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchDeleteGeofenceError.html
---

# BatchDeleteGeofenceError
<a name="API_WaypointGeofencing_BatchDeleteGeofenceError"></a>

Contains error details for each geofence that failed to delete from the geofence collection.

## Contents
<a name="API_WaypointGeofencing_BatchDeleteGeofenceError_Contents"></a>

 ** Error **   <a name="location-Type-WaypointGeofencing_BatchDeleteGeofenceError-Error"></a>
Contains details associated to the batch error.
Type: [BatchItemError](API_WaypointGeofencing_BatchItemError.md) object
Required: Yes

 ** GeofenceId **   <a name="location-Type-WaypointGeofencing_BatchDeleteGeofenceError-GeofenceId"></a>
The geofence associated with the error message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

## See Also
<a name="API_WaypointGeofencing_BatchDeleteGeofenceError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointgeofencing-2020-11-19/BatchDeleteGeofenceError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointgeofencing-2020-11-19/BatchDeleteGeofenceError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointgeofencing-2020-11-19/BatchDeleteGeofenceError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
