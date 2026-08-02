---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ObdSignal.html
---

# ObdSignal
<a name="API_ObdSignal"></a>

Information about signal messages using the on-board diagnostics (OBD) II protocol in a vehicle.

## Contents
<a name="API_ObdSignal_Contents"></a>

 ** byteLength **   <a name="iotfleetwise-Type-ObdSignal-byteLength"></a>
The length of a message.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 8.
Required: Yes

 ** offset **   <a name="iotfleetwise-Type-ObdSignal-offset"></a>
The offset used to calculate the signal value. Combined with scaling, the calculation is `value = raw_value * scaling + offset`.
Type: Double
Required: Yes

 ** pid **   <a name="iotfleetwise-Type-ObdSignal-pid"></a>
The diagnostic code used to request data from a vehicle for this signal.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

 ** pidResponseLength **   <a name="iotfleetwise-Type-ObdSignal-pidResponseLength"></a>
The length of the requested data.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2147483647.
Required: Yes

 ** scaling **   <a name="iotfleetwise-Type-ObdSignal-scaling"></a>
A multiplier used to decode the message.
Type: Double
Required: Yes

 ** serviceMode **   <a name="iotfleetwise-Type-ObdSignal-serviceMode"></a>
The mode of operation (diagnostic service) in a message.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

 ** startByte **   <a name="iotfleetwise-Type-ObdSignal-startByte"></a>
Indicates the beginning of the message.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

 ** bitMaskLength **   <a name="iotfleetwise-Type-ObdSignal-bitMaskLength"></a>
The number of bits to mask in a message.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 8.
Required: No

 ** bitRightShift **   <a name="iotfleetwise-Type-ObdSignal-bitRightShift"></a>
The number of positions to shift bits in the message.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** isSigned **   <a name="iotfleetwise-Type-ObdSignal-isSigned"></a>
Determines whether the message is signed (`true`) or not (`false`). If it's signed, the message can represent both positive and negative numbers. The `isSigned` parameter only applies to the `INTEGER` raw signal type, and it doesn't affect the `FLOATING_POINT` raw signal type. The default value is `false`.
Type: Boolean
Required: No

 ** signalValueType **   <a name="iotfleetwise-Type-ObdSignal-signalValueType"></a>
The value type of the signal. The default value is `INTEGER`.
Type: String
Valid Values: `INTEGER | FLOATING_POINT`
Required: No

## See Also
<a name="API_ObdSignal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/ObdSignal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/ObdSignal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/ObdSignal)
