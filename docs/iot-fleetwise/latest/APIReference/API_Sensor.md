---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_Sensor.html
---

# Sensor
<a name="API_Sensor"></a>

An input component that reports the environmental condition of a vehicle.

**Note**
You can collect data about fluid levels, temperatures, vibrations, or battery voltage from sensors.

## Contents
<a name="API_Sensor_Contents"></a>

 ** dataType **   <a name="iotfleetwise-Type-Sensor-dataType"></a>
The specified data type of the sensor.
Type: String
Valid Values: `INT8 | UINT8 | INT16 | UINT16 | INT32 | UINT32 | INT64 | UINT64 | BOOLEAN | FLOAT | DOUBLE | STRING | UNIX_TIMESTAMP | INT8_ARRAY | UINT8_ARRAY | INT16_ARRAY | UINT16_ARRAY | INT32_ARRAY | UINT32_ARRAY | INT64_ARRAY | UINT64_ARRAY | BOOLEAN_ARRAY | FLOAT_ARRAY | DOUBLE_ARRAY | STRING_ARRAY | UNIX_TIMESTAMP_ARRAY | UNKNOWN | STRUCT | STRUCT_ARRAY`
Required: Yes

 ** fullyQualifiedName **   <a name="iotfleetwise-Type-Sensor-fullyQualifiedName"></a>
The fully qualified name of the sensor. For example, the fully qualified name of a sensor might be `Vehicle.Body.Engine.Battery`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: Yes

 ** allowedValues **   <a name="iotfleetwise-Type-Sensor-allowedValues"></a>
A list of possible values a sensor can take.
Type: Array of strings
Required: No

 ** comment **   <a name="iotfleetwise-Type-Sensor-comment"></a>
A comment in addition to the description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** deprecationMessage **   <a name="iotfleetwise-Type-Sensor-deprecationMessage"></a>
The deprecation message for the node or the branch that was moved or deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** description **   <a name="iotfleetwise-Type-Sensor-description"></a>
A brief description of a sensor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** max **   <a name="iotfleetwise-Type-Sensor-max"></a>
The specified possible maximum value of the sensor.
Type: Double
Required: No

 ** min **   <a name="iotfleetwise-Type-Sensor-min"></a>
The specified possible minimum value of the sensor.
Type: Double
Required: No

 ** structFullyQualifiedName **   <a name="iotfleetwise-Type-Sensor-structFullyQualifiedName"></a>
The fully qualified name of the struct node for a sensor if the data type of the actuator is `Struct` or `StructArray`. For example, the struct fully qualified name of a sensor might be `Vehicle.ADAS.CameraStruct`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: No

 ** unit **   <a name="iotfleetwise-Type-Sensor-unit"></a>
The scientific unit of measurement for data collected by the sensor.
Type: String
Required: No

## See Also
<a name="API_Sensor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/Sensor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/Sensor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/Sensor)
