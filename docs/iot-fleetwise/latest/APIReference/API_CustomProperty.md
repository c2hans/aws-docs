---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CustomProperty.html
---

# CustomProperty
<a name="API_CustomProperty"></a>

Represents a member of the complex data structure. The data type of the property can be either primitive or another `struct`.

## Contents
<a name="API_CustomProperty_Contents"></a>

 ** dataType **   <a name="iotfleetwise-Type-CustomProperty-dataType"></a>
The data type for the custom property.
Type: String
Valid Values: `INT8 | UINT8 | INT16 | UINT16 | INT32 | UINT32 | INT64 | UINT64 | BOOLEAN | FLOAT | DOUBLE | STRING | UNIX_TIMESTAMP | INT8_ARRAY | UINT8_ARRAY | INT16_ARRAY | UINT16_ARRAY | INT32_ARRAY | UINT32_ARRAY | INT64_ARRAY | UINT64_ARRAY | BOOLEAN_ARRAY | FLOAT_ARRAY | DOUBLE_ARRAY | STRING_ARRAY | UNIX_TIMESTAMP_ARRAY | UNKNOWN | STRUCT | STRUCT_ARRAY`
Required: Yes

 ** fullyQualifiedName **   <a name="iotfleetwise-Type-CustomProperty-fullyQualifiedName"></a>
The fully qualified name of the custom property. For example, the fully qualified name of a custom property might be `ComplexDataTypes.VehicleDataTypes.SVMCamera.FPS`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: Yes

 ** comment **   <a name="iotfleetwise-Type-CustomProperty-comment"></a>
A comment in addition to the description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** dataEncoding **   <a name="iotfleetwise-Type-CustomProperty-dataEncoding"></a>
Indicates whether the property is binary data.
Type: String
Valid Values: `BINARY | TYPED`
Required: No

 ** deprecationMessage **   <a name="iotfleetwise-Type-CustomProperty-deprecationMessage"></a>
The deprecation message for the node or the branch that was moved or deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** description **   <a name="iotfleetwise-Type-CustomProperty-description"></a>
A brief description of the custom property.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** structFullyQualifiedName **   <a name="iotfleetwise-Type-CustomProperty-structFullyQualifiedName"></a>
The fully qualified name of the struct node for the custom property if the data type of the custom property is `Struct` or `StructArray`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: No

## See Also
<a name="API_CustomProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/CustomProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/CustomProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/CustomProperty)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
