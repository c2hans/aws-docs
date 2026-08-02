---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ObdInterface.html
---

# ObdInterface
<a name="API_ObdInterface"></a>

A network interface that specifies the on-board diagnostic (OBD) II network protocol.

## Contents
<a name="API_ObdInterface_Contents"></a>

 ** name **   <a name="iotfleetwise-Type-ObdInterface-name"></a>
The name of the interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.]+`
Required: Yes

 ** requestMessageId **   <a name="iotfleetwise-Type-ObdInterface-requestMessageId"></a>
The ID of the message requesting vehicle data.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

 ** dtcRequestIntervalSeconds **   <a name="iotfleetwise-Type-ObdInterface-dtcRequestIntervalSeconds"></a>
The maximum number message requests per diagnostic trouble code per second.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** hasTransmissionEcu **   <a name="iotfleetwise-Type-ObdInterface-hasTransmissionEcu"></a>
Whether the vehicle has a transmission control module (TCM).
Type: Boolean
Required: No

 ** obdStandard **   <a name="iotfleetwise-Type-ObdInterface-obdStandard"></a>
The standard OBD II PID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** pidRequestIntervalSeconds **   <a name="iotfleetwise-Type-ObdInterface-pidRequestIntervalSeconds"></a>
The maximum number message requests per second.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** useExtendedIds **   <a name="iotfleetwise-Type-ObdInterface-useExtendedIds"></a>
Whether to use extended IDs in the message.
Type: Boolean
Required: No

## See Also
<a name="API_ObdInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/ObdInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/ObdInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/ObdInterface)
