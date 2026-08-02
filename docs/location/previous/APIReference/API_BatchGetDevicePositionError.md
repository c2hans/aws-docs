---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_BatchGetDevicePositionError.html
---

# BatchGetDevicePositionError
<a name="API_BatchGetDevicePositionError"></a>

Contains error details for each device that didn't return a position.

## Contents
<a name="API_BatchGetDevicePositionError_Contents"></a>

 ** DeviceId **   <a name="location-Type-BatchGetDevicePositionError-DeviceId"></a>
The ID of the device that didn't return a position.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

 ** Error **   <a name="location-Type-BatchGetDevicePositionError-Error"></a>
Contains details related to the error code.
Type: [BatchItemError](API_BatchItemError.md) object
Required: Yes

## See Also
<a name="API_BatchGetDevicePositionError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/BatchGetDevicePositionError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/BatchGetDevicePositionError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/BatchGetDevicePositionError)
