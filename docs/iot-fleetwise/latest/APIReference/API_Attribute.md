---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_Attribute.html
---

# Attribute
<a name="API_Attribute"></a>

A signal that represents static information about the vehicle, such as engine type or manufacturing date.

## Contents
<a name="API_Attribute_Contents"></a>

 ** dataType **   <a name="iotfleetwise-Type-Attribute-dataType"></a>
The specified data type of the attribute.
Type: String
Valid Values: `INT8 | UINT8 | INT16 | UINT16 | INT32 | UINT32 | INT64 | UINT64 | BOOLEAN | FLOAT | DOUBLE | STRING | UNIX_TIMESTAMP | INT8_ARRAY | UINT8_ARRAY | INT16_ARRAY | UINT16_ARRAY | INT32_ARRAY | UINT32_ARRAY | INT64_ARRAY | UINT64_ARRAY | BOOLEAN_ARRAY | FLOAT_ARRAY | DOUBLE_ARRAY | STRING_ARRAY | UNIX_TIMESTAMP_ARRAY | UNKNOWN | STRUCT | STRUCT_ARRAY`
Required: Yes

 ** fullyQualifiedName **   <a name="iotfleetwise-Type-Attribute-fullyQualifiedName"></a>
The fully qualified name of the attribute. For example, the fully qualified name of an attribute might be `Vehicle.Body.Engine.Type`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: Yes

 ** allowedValues **   <a name="iotfleetwise-Type-Attribute-allowedValues"></a>
A list of possible values an attribute can be assigned.
Type: Array of strings
Required: No

 ** assignedValue **   <a name="iotfleetwise-Type-Attribute-assignedValue"></a>
 *This member has been deprecated.*
A specified value for the attribute.
Type: String
Required: No

 ** comment **   <a name="iotfleetwise-Type-Attribute-comment"></a>
A comment in addition to the description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** defaultValue **   <a name="iotfleetwise-Type-Attribute-defaultValue"></a>
The default value of the attribute.
Type: String
Required: No

 ** deprecationMessage **   <a name="iotfleetwise-Type-Attribute-deprecationMessage"></a>
The deprecation message for the node or the branch that was moved or deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** description **   <a name="iotfleetwise-Type-Attribute-description"></a>
A brief description of the attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** max **   <a name="iotfleetwise-Type-Attribute-max"></a>
The specified possible maximum value of the attribute.
Type: Double
Required: No

 ** min **   <a name="iotfleetwise-Type-Attribute-min"></a>
The specified possible minimum value of the attribute.
Type: Double
Required: No

 ** unit **   <a name="iotfleetwise-Type-Attribute-unit"></a>
The scientific unit for the attribute.
Type: String
Required: No

## See Also
<a name="API_Attribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/Attribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/Attribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/Attribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
