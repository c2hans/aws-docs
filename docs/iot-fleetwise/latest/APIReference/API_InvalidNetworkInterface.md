---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_InvalidNetworkInterface.html
---

# InvalidNetworkInterface
<a name="API_InvalidNetworkInterface"></a>

A reason a vehicle network interface isn't valid.

## Contents
<a name="API_InvalidNetworkInterface_Contents"></a>

 ** interfaceId **   <a name="iotfleetwise-Type-InvalidNetworkInterface-interfaceId"></a>
The ID of the interface that isn't valid.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[-a-zA-Z0-9_.]+`
Required: No

 ** reason **   <a name="iotfleetwise-Type-InvalidNetworkInterface-reason"></a>
A message about why the interface isn't valid.
Type: String
Valid Values: `DUPLICATE_NETWORK_INTERFACE | CONFLICTING_NETWORK_INTERFACE | NETWORK_INTERFACE_TO_ADD_ALREADY_EXISTS | CAN_NETWORK_INTERFACE_INFO_IS_NULL | OBD_NETWORK_INTERFACE_INFO_IS_NULL | NETWORK_INTERFACE_TO_REMOVE_ASSOCIATED_WITH_SIGNALS | VEHICLE_MIDDLEWARE_NETWORK_INTERFACE_INFO_IS_NULL | CUSTOM_DECODING_SIGNAL_NETWORK_INTERFACE_INFO_IS_NULL`
Required: No

## See Also
<a name="API_InvalidNetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/InvalidNetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/InvalidNetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/InvalidNetworkInterface)
