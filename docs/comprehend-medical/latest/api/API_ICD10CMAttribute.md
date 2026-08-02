---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ICD10CMAttribute.html
---

# ICD10CMAttribute
<a name="API_ICD10CMAttribute"></a>

The detected attributes that relate to an entity. This includes an extracted segment of the text that is an attribute of an entity, or otherwise related to an entity. InferICD10CM detects the following attributes: `Direction`, `System, Organ or Site`, and `Acuity`.

## Contents
<a name="API_ICD10CMAttribute_Contents"></a>

 ** BeginOffset **   <a name="comprehendmedical-Type-ICD10CMAttribute-BeginOffset"></a>
The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string.
Type: Integer
Required: No

 ** Category **   <a name="comprehendmedical-Type-ICD10CMAttribute-Category"></a>
The category of attribute. Can be either of `DX_NAME` or `TIME_EXPRESSION`.
Type: String
Valid Values: `DX_NAME | TIME_EXPRESSION`
Required: No

 ** EndOffset **   <a name="comprehendmedical-Type-ICD10CMAttribute-EndOffset"></a>
The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.
Type: Integer
Required: No

 ** Id **   <a name="comprehendmedical-Type-ICD10CMAttribute-Id"></a>
The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier.
Type: Integer
Required: No

 ** RelationshipScore **   <a name="comprehendmedical-Type-ICD10CMAttribute-RelationshipScore"></a>
The level of confidence that Amazon Comprehend Medical has that this attribute is correctly related to this entity.
Type: Float
Required: No

 ** RelationshipType **   <a name="comprehendmedical-Type-ICD10CMAttribute-RelationshipType"></a>
The type of relationship between the entity and attribute. Type for the relationship can be either of `OVERLAP` or `SYSTEM_ORGAN_SITE`.
Type: String
Valid Values: `OVERLAP | SYSTEM_ORGAN_SITE | QUALITY`
Required: No

 ** Score **   <a name="comprehendmedical-Type-ICD10CMAttribute-Score"></a>
The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as an attribute.
Type: Float
Required: No

 ** Text **   <a name="comprehendmedical-Type-ICD10CMAttribute-Text"></a>
The segment of input text which contains the detected attribute.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Traits **   <a name="comprehendmedical-Type-ICD10CMAttribute-Traits"></a>
The contextual information for the attribute. The traits recognized by InferICD10CM are `DIAGNOSIS`, `SIGN`, `SYMPTOM`, and `NEGATION`.
Type: Array of [ICD10CMTrait](API_ICD10CMTrait.md) objects
Required: No

 ** Type **   <a name="comprehendmedical-Type-ICD10CMAttribute-Type"></a>
The type of attribute. InferICD10CM detects entities of the type `DX_NAME`.
Type: String
Valid Values: `ACUITY | DIRECTION | SYSTEM_ORGAN_SITE | QUALITY | QUANTITY | TIME_TO_DX_NAME | TIME_EXPRESSION`
Required: No

## See Also
<a name="API_ICD10CMAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/ICD10CMAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/ICD10CMAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/ICD10CMAttribute)
