---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_SignalDecoder.html
---

# SignalDecoder
<a name="API_SignalDecoder"></a>

Information about a signal decoder.

## Contents
<a name="API_SignalDecoder_Contents"></a>

 ** fullyQualifiedName **   <a name="iotfleetwise-Type-SignalDecoder-fullyQualifiedName"></a>
The fully qualified name of a signal decoder as defined in a vehicle model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: Yes

 ** interfaceId **   <a name="iotfleetwise-Type-SignalDecoder-interfaceId"></a>
The ID of a network interface that specifies what network protocol a vehicle follows.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[-a-zA-Z0-9_.]+`
Required: Yes

 ** type **   <a name="iotfleetwise-Type-SignalDecoder-type"></a>
The network protocol for the vehicle. For example, `CAN_SIGNAL` specifies a protocol that defines how data is communicated between electronic control units (ECUs). `OBD_SIGNAL` specifies a protocol that defines how self-diagnostic data is communicated between ECUs.
Type: String
Valid Values: `CAN_SIGNAL | OBD_SIGNAL | MESSAGE_SIGNAL | CUSTOM_DECODING_SIGNAL`
Required: Yes

 ** canSignal **   <a name="iotfleetwise-Type-SignalDecoder-canSignal"></a>
Information about signal decoder using the Controller Area Network (CAN) protocol.
Type: [CanSignal](API_CanSignal.md) object
Required: No

 ** customDecodingSignal **   <a name="iotfleetwise-Type-SignalDecoder-customDecodingSignal"></a>
Information about a [custom signal decoder](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CustomDecodingSignal.html).
Type: [CustomDecodingSignal](API_CustomDecodingSignal.md) object
Required: No

 ** messageSignal **   <a name="iotfleetwise-Type-SignalDecoder-messageSignal"></a>
The decoding information for a specific message which supports higher order data types.
Type: [MessageSignal](API_MessageSignal.md) object
Required: No

 ** obdSignal **   <a name="iotfleetwise-Type-SignalDecoder-obdSignal"></a>
Information about signal decoder using the on-board diagnostic (OBD) II protocol.
Type: [ObdSignal](API_ObdSignal.md) object
Required: No

## See Also
<a name="API_SignalDecoder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/SignalDecoder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/SignalDecoder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/SignalDecoder)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
