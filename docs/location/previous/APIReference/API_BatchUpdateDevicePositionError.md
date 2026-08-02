---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_BatchUpdateDevicePositionError.html
---

# BatchUpdateDevicePositionError
<a name="API_BatchUpdateDevicePositionError"></a>

Contains error details for each device that failed to update its position.

## Contents
<a name="API_BatchUpdateDevicePositionError_Contents"></a>

 ** DeviceId **   <a name="location-Type-BatchUpdateDevicePositionError-DeviceId"></a>
The device associated with the failed location update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

 ** Error **   <a name="location-Type-BatchUpdateDevicePositionError-Error"></a>
Contains details related to the error code such as the error code and error message.
Type: [BatchItemError](API_BatchItemError.md) object
Required: Yes

 ** SampleTime **   <a name="location-Type-BatchUpdateDevicePositionError-SampleTime"></a>
The timestamp at which the device position was determined. Uses [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp
Required: Yes

## See Also
<a name="API_BatchUpdateDevicePositionError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/BatchUpdateDevicePositionError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/BatchUpdateDevicePositionError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/BatchUpdateDevicePositionError)
