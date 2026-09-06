---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ROS2PrimitiveMessageDefinition.html
---

# ROS2PrimitiveMessageDefinition
<a name="API_ROS2PrimitiveMessageDefinition"></a>

Represents a ROS 2 compliant primitive type message of the complex data structure.

## Contents
<a name="API_ROS2PrimitiveMessageDefinition_Contents"></a>

 ** primitiveType **   <a name="iotfleetwise-Type-ROS2PrimitiveMessageDefinition-primitiveType"></a>
The primitive type (integer, floating point, boolean, etc.) for the ROS 2 primitive message definition.
Type: String
Valid Values: `BOOL | BYTE | CHAR | FLOAT32 | FLOAT64 | INT8 | UINT8 | INT16 | UINT16 | INT32 | UINT32 | INT64 | UINT64 | STRING | WSTRING`
Required: Yes

 ** offset **   <a name="iotfleetwise-Type-ROS2PrimitiveMessageDefinition-offset"></a>
The offset used to calculate the signal value. Combined with scaling, the calculation is `value = raw_value * scaling + offset`.
Type: Double
Required: No

 ** scaling **   <a name="iotfleetwise-Type-ROS2PrimitiveMessageDefinition-scaling"></a>
A multiplier used to decode the message.
Type: Double
Required: No

 ** upperBound **   <a name="iotfleetwise-Type-ROS2PrimitiveMessageDefinition-upperBound"></a>
An optional attribute specifying the upper bound for `STRING` and `WSTRING`.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 2048.
Required: No

## See Also
<a name="API_ROS2PrimitiveMessageDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/ROS2PrimitiveMessageDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/ROS2PrimitiveMessageDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/ROS2PrimitiveMessageDefinition)
