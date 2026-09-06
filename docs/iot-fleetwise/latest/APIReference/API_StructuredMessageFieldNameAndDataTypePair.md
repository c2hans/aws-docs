---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_StructuredMessageFieldNameAndDataTypePair.html
---

# StructuredMessageFieldNameAndDataTypePair
<a name="API_StructuredMessageFieldNameAndDataTypePair"></a>

Represents a `StructureMessageName` to `DataType` map element.

## Contents
<a name="API_StructuredMessageFieldNameAndDataTypePair_Contents"></a>

 ** dataType **   <a name="iotfleetwise-Type-StructuredMessageFieldNameAndDataTypePair-dataType"></a>
The data type.
Type: [StructuredMessage](API_StructuredMessage.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** fieldName **   <a name="iotfleetwise-Type-StructuredMessageFieldNameAndDataTypePair-fieldName"></a>
The field name of the structured message. It determines how a data value is referenced in the target language.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Required: Yes

## See Also
<a name="API_StructuredMessageFieldNameAndDataTypePair_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/StructuredMessageFieldNameAndDataTypePair)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/StructuredMessageFieldNameAndDataTypePair)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/StructuredMessageFieldNameAndDataTypePair)
