---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_Actuator.html
---

# Actuator
<a name="API_Actuator"></a>

A signal that represents a vehicle device such as the engine, heater, and door locks. Data from an actuator reports the state of a certain vehicle device.

**Note**
 Updating actuator data can change the state of a device. For example, you can turn on or off the heater by updating its actuator data.

## Contents
<a name="API_Actuator_Contents"></a>

 ** dataType **   <a name="iotfleetwise-Type-Actuator-dataType"></a>
The specified data type of the actuator.
Type: String
Valid Values: `INT8 | UINT8 | INT16 | UINT16 | INT32 | UINT32 | INT64 | UINT64 | BOOLEAN | FLOAT | DOUBLE | STRING | UNIX_TIMESTAMP | INT8_ARRAY | UINT8_ARRAY | INT16_ARRAY | UINT16_ARRAY | INT32_ARRAY | UINT32_ARRAY | INT64_ARRAY | UINT64_ARRAY | BOOLEAN_ARRAY | FLOAT_ARRAY | DOUBLE_ARRAY | STRING_ARRAY | UNIX_TIMESTAMP_ARRAY | UNKNOWN | STRUCT | STRUCT_ARRAY`
Required: Yes

 ** fullyQualifiedName **   <a name="iotfleetwise-Type-Actuator-fullyQualifiedName"></a>
The fully qualified name of the actuator. For example, the fully qualified name of an actuator might be `Vehicle.Front.Left.Door.Lock`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: Yes

 ** allowedValues **   <a name="iotfleetwise-Type-Actuator-allowedValues"></a>
A list of possible values an actuator can take.
Type: Array of strings
Required: No

 ** assignedValue **   <a name="iotfleetwise-Type-Actuator-assignedValue"></a>
 *This member has been deprecated.*
A specified value for the actuator.
Type: String
Required: No

 ** comment **   <a name="iotfleetwise-Type-Actuator-comment"></a>
A comment in addition to the description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** deprecationMessage **   <a name="iotfleetwise-Type-Actuator-deprecationMessage"></a>
The deprecation message for the node or the branch that was moved or deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** description **   <a name="iotfleetwise-Type-Actuator-description"></a>
A brief description of the actuator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** max **   <a name="iotfleetwise-Type-Actuator-max"></a>
The specified possible maximum value of an actuator.
Type: Double
Required: No

 ** min **   <a name="iotfleetwise-Type-Actuator-min"></a>
The specified possible minimum value of an actuator.
Type: Double
Required: No

 ** structFullyQualifiedName **   <a name="iotfleetwise-Type-Actuator-structFullyQualifiedName"></a>
The fully qualified name of the struct node for the actuator if the data type of the actuator is `Struct` or `StructArray`. For example, the struct fully qualified name of an actuator might be `Vehicle.Door.LockStruct`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: No

 ** unit **   <a name="iotfleetwise-Type-Actuator-unit"></a>
The scientific unit for the actuator.
Type: String
Required: No

## See Also
<a name="API_Actuator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/Actuator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/Actuator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/Actuator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
