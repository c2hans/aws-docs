---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_NetworkInterface.html
---

# NetworkInterface
<a name="API_NetworkInterface"></a>

Represents a node and its specifications in an in-vehicle communication network. All signal decoders must be associated with a network node.

 To return this information about all the network interfaces specified in a decoder manifest, use the [ListDecoderManifestNetworkInterfaces](API_ListDecoderManifestNetworkInterfaces.md) API operation.

## Contents
<a name="API_NetworkInterface_Contents"></a>

 ** interfaceId **   <a name="iotfleetwise-Type-NetworkInterface-interfaceId"></a>
The ID of the network interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[-a-zA-Z0-9_.]+`
Required: Yes

 ** type **   <a name="iotfleetwise-Type-NetworkInterface-type"></a>
The network protocol for the vehicle. For example, `CAN_SIGNAL` specifies a protocol that defines how data is communicated between electronic control units (ECUs). `OBD_SIGNAL` specifies a protocol that defines how self-diagnostic data is communicated between ECUs.
Type: String
Valid Values: `CAN_INTERFACE | OBD_INTERFACE | VEHICLE_MIDDLEWARE | CUSTOM_DECODING_INTERFACE`
Required: Yes

 ** canInterface **   <a name="iotfleetwise-Type-NetworkInterface-canInterface"></a>
Information about a network interface specified by the Controller Area Network (CAN) protocol.
Type: [CanInterface](API_CanInterface.md) object
Required: No

 ** customDecodingInterface **   <a name="iotfleetwise-Type-NetworkInterface-customDecodingInterface"></a>
Information about a [custom network interface](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CustomDecodingInterface.html).
Type: [CustomDecodingInterface](API_CustomDecodingInterface.md) object
Required: No

 ** obdInterface **   <a name="iotfleetwise-Type-NetworkInterface-obdInterface"></a>
Information about a network interface specified by the on-board diagnostic (OBD) II protocol.
Type: [ObdInterface](API_ObdInterface.md) object
Required: No

 ** vehicleMiddleware **   <a name="iotfleetwise-Type-NetworkInterface-vehicleMiddleware"></a>
The vehicle middleware defined as a type of network interface. Examples of vehicle middleware include `ROS2` and `SOME/IP`.
Type: [VehicleMiddleware](API_VehicleMiddleware.md) object
Required: No

## See Also
<a name="API_NetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/NetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/NetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/NetworkInterface)
