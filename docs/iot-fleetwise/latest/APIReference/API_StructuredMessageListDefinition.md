---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_StructuredMessageListDefinition.html
---

# StructuredMessageListDefinition
<a name="API_StructuredMessageListDefinition"></a>

Represents a list type node of the complex data structure.

## Contents
<a name="API_StructuredMessageListDefinition_Contents"></a>

 ** listType **   <a name="iotfleetwise-Type-StructuredMessageListDefinition-listType"></a>
The type of list of the structured message list definition.
Type: String
Valid Values: `FIXED_CAPACITY | DYNAMIC_UNBOUNDED_CAPACITY | DYNAMIC_BOUNDED_CAPACITY`
Required: Yes

 ** memberType **   <a name="iotfleetwise-Type-StructuredMessageListDefinition-memberType"></a>
The member type of the structured message list definition.
Type: [StructuredMessage](API_StructuredMessage.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** name **   <a name="iotfleetwise-Type-StructuredMessageListDefinition-name"></a>
The name of the structured message list definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Required: Yes

 ** capacity **   <a name="iotfleetwise-Type-StructuredMessageListDefinition-capacity"></a>
The capacity of the structured message list definition when the list type is `FIXED_CAPACITY` or `DYNAMIC_BOUNDED_CAPACITY`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

## See Also
<a name="API_StructuredMessageListDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/StructuredMessageListDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/StructuredMessageListDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/StructuredMessageListDefinition)
