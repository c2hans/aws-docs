---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_VehicleSummary.html
---

# VehicleSummary
<a name="API_VehicleSummary"></a>

Information about a vehicle.

To return this information about vehicles in your account, you can use the [ListVehicles](API_ListVehicles.md) API operation.

## Contents
<a name="API_VehicleSummary_Contents"></a>

 ** arn **   <a name="iotfleetwise-Type-VehicleSummary-arn"></a>
The Amazon Resource Name (ARN) of the vehicle.
Type: String
Required: Yes

 ** creationTime **   <a name="iotfleetwise-Type-VehicleSummary-creationTime"></a>
The time the vehicle was created in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp
Required: Yes

 ** decoderManifestArn **   <a name="iotfleetwise-Type-VehicleSummary-decoderManifestArn"></a>
The ARN of a decoder manifest associated with the vehicle.
Type: String
Required: Yes

 ** lastModificationTime **   <a name="iotfleetwise-Type-VehicleSummary-lastModificationTime"></a>
The time the vehicle was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp
Required: Yes

 ** modelManifestArn **   <a name="iotfleetwise-Type-VehicleSummary-modelManifestArn"></a>
The ARN of a vehicle model (model manifest) associated with the vehicle.
Type: String
Required: Yes

 ** vehicleName **   <a name="iotfleetwise-Type-VehicleSummary-vehicleName"></a>
The unique ID of the vehicle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

 ** attributes **   <a name="iotfleetwise-Type-VehicleSummary-attributes"></a>
Static information about a vehicle in a key-value pair. For example:
 `"engineType"` : `"1.3 L R2"`
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 150.
Key Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_VehicleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/VehicleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/VehicleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/VehicleSummary)
