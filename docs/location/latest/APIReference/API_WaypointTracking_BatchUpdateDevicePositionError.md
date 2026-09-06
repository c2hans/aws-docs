---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_BatchUpdateDevicePositionError.html
---

# BatchUpdateDevicePositionError
<a name="API_WaypointTracking_BatchUpdateDevicePositionError"></a>

Contains error details for each device that failed to update its position.

## Contents
<a name="API_WaypointTracking_BatchUpdateDevicePositionError_Contents"></a>

 ** DeviceId **   <a name="location-Type-WaypointTracking_BatchUpdateDevicePositionError-DeviceId"></a>
The device associated with the failed location update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

 ** Error **   <a name="location-Type-WaypointTracking_BatchUpdateDevicePositionError-Error"></a>
Contains details related to the error code such as the error code and error message.
Type: [BatchItemError](API_WaypointTracking_BatchItemError.md) object
Required: Yes

 ** SampleTime **   <a name="location-Type-WaypointTracking_BatchUpdateDevicePositionError-SampleTime"></a>
The timestamp at which the device position was determined. Uses [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp
Required: Yes

## See Also
<a name="API_WaypointTracking_BatchUpdateDevicePositionError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointtracking-2020-11-19/BatchUpdateDevicePositionError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointtracking-2020-11-19/BatchUpdateDevicePositionError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointtracking-2020-11-19/BatchUpdateDevicePositionError)
