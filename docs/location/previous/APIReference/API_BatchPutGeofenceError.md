---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_BatchPutGeofenceError.html
---

# BatchPutGeofenceError
<a name="API_BatchPutGeofenceError"></a>

Contains error details for each geofence that failed to be stored in a given geofence collection.

## Contents
<a name="API_BatchPutGeofenceError_Contents"></a>

 ** Error **   <a name="location-Type-BatchPutGeofenceError-Error"></a>
Contains details associated to the batch error.
Type: [BatchItemError](API_BatchItemError.md) object
Required: Yes

 ** GeofenceId **   <a name="location-Type-BatchPutGeofenceError-GeofenceId"></a>
The geofence associated with the error message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

## See Also
<a name="API_BatchPutGeofenceError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/BatchPutGeofenceError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/BatchPutGeofenceError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/BatchPutGeofenceError)
