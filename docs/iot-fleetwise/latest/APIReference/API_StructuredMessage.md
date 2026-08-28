---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_StructuredMessage.html
---

# StructuredMessage
<a name="API_StructuredMessage"></a>

The structured message for the message signal. It can be defined with either a `primitiveMessageDefinition`, `structuredMessageListDefinition`, or `structuredMessageDefinition` recursively.

## Contents
<a name="API_StructuredMessage_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** primitiveMessageDefinition **   <a name="iotfleetwise-Type-StructuredMessage-primitiveMessageDefinition"></a>
Represents a primitive type node of the complex data structure.
Type: [PrimitiveMessageDefinition](API_PrimitiveMessageDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** structuredMessageDefinition **   <a name="iotfleetwise-Type-StructuredMessage-structuredMessageDefinition"></a>
Represents a struct type node of the complex data structure.
Type: Array of [StructuredMessageFieldNameAndDataTypePair](API_StructuredMessageFieldNameAndDataTypePair.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: No

 ** structuredMessageListDefinition **   <a name="iotfleetwise-Type-StructuredMessage-structuredMessageListDefinition"></a>
Represents a list type node of the complex data structure.
Type: [StructuredMessageListDefinition](API_StructuredMessageListDefinition.md) object
Required: No

## See Also
<a name="API_StructuredMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/StructuredMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/StructuredMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/StructuredMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
