---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CanSignal.html
---

# CanSignal
<a name="API_CanSignal"></a>

Information about a single controller area network (CAN) signal and the messages it receives and transmits.

## Contents
<a name="API_CanSignal_Contents"></a>

 ** factor **   <a name="iotfleetwise-Type-CanSignal-factor"></a>
A multiplier used to decode the CAN message.
Type: Double
Required: Yes

 ** isBigEndian **   <a name="iotfleetwise-Type-CanSignal-isBigEndian"></a>
Whether the byte ordering of a CAN message is big-endian.
Type: Boolean
Required: Yes

 ** isSigned **   <a name="iotfleetwise-Type-CanSignal-isSigned"></a>
Determines whether the message is signed (`true`) or not (`false`). If it's signed, the message can represent both positive and negative numbers. The `isSigned` parameter only applies to the `INTEGER` raw signal type, and it doesn't affect the `FLOATING_POINT` raw signal type.
Type: Boolean
Required: Yes

 ** length **   <a name="iotfleetwise-Type-CanSignal-length"></a>
How many bytes of data are in the message.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

 ** messageId **   <a name="iotfleetwise-Type-CanSignal-messageId"></a>
The ID of the message.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

 ** offset **   <a name="iotfleetwise-Type-CanSignal-offset"></a>
The offset used to calculate the signal value. Combined with factor, the calculation is `value = raw_value * factor + offset`.
Type: Double
Required: Yes

 ** startBit **   <a name="iotfleetwise-Type-CanSignal-startBit"></a>
Indicates the beginning of the CAN signal. This should always be the least significant bit (LSB).
This value might be different from the value in a DBC file. For little endian signals, `startBit` is the same value as in the DBC file. For big endian signals in a DBC file, the start bit is the most significant bit (MSB). You will have to calculate the LSB instead and pass it as the `startBit`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

 ** name **   <a name="iotfleetwise-Type-CanSignal-name"></a>
The name of the signal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.]+`
Required: No

 ** signalValueType **   <a name="iotfleetwise-Type-CanSignal-signalValueType"></a>
The value type of the signal. The default value is `INTEGER`.
Type: String
Valid Values: `INTEGER | FLOATING_POINT`
Required: No

## See Also
<a name="API_CanSignal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/CanSignal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/CanSignal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/CanSignal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
