---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_SNOMEDCTAttribute.html
---

# SNOMEDCTAttribute
<a name="API_SNOMEDCTAttribute"></a>

 The extracted attributes that relate to an entity. An extracted segment of the text that is an attribute of an entity, or otherwise related to an entity, such as the dosage of a medication taken.

## Contents
<a name="API_SNOMEDCTAttribute_Contents"></a>

 ** BeginOffset **   <a name="comprehendmedical-Type-SNOMEDCTAttribute-BeginOffset"></a>
 The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string.
Type: Integer
Required: No

 ** Category **   <a name="comprehendmedical-Type-SNOMEDCTAttribute-Category"></a>
 The category of the detected attribute. Possible categories include MEDICAL\_CONDITION, ANATOMY, and TEST\_TREATMENT\_PROCEDURE.
Type: String
Valid Values: `MEDICAL_CONDITION | ANATOMY | TEST_TREATMENT_PROCEDURE`
Required: No

 ** EndOffset **   <a name="comprehendmedical-Type-SNOMEDCTAttribute-EndOffset"></a>
 The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.
Type: Integer
Required: No

 ** Id **   <a name="comprehendmedical-Type-SNOMEDCTAttribute-Id"></a>
 The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier.
Type: Integer
Required: No

 ** RelationshipScore **   <a name="comprehendmedical-Type-SNOMEDCTAttribute-RelationshipScore"></a>
 The level of confidence that Comprehend Medical has that this attribute is correctly related to this entity.
Type: Float
Required: No

 ** RelationshipType **   <a name="comprehendmedical-Type-SNOMEDCTAttribute-RelationshipType"></a>
 The type of relationship that exists between the entity and the related attribute.
Type: String
Valid Values: `ACUITY | QUALITY | TEST_VALUE | TEST_UNITS | DIRECTION | SYSTEM_ORGAN_SITE | TEST_UNIT`
Required: No

 ** Score **   <a name="comprehendmedical-Type-SNOMEDCTAttribute-Score"></a>
 The level of confidence that Comprehend Medical has that the segment of text is correctly recognized as an attribute.
Type: Float
Required: No

 ** SNOMEDCTConcepts **   <a name="comprehendmedical-Type-SNOMEDCTAttribute-SNOMEDCTConcepts"></a>
 The SNOMED-CT concepts specific to an attribute, along with a score indicating the likelihood of the match.
Type: Array of [SNOMEDCTConcept](API_SNOMEDCTConcept.md) objects
Required: No

 ** Text **   <a name="comprehendmedical-Type-SNOMEDCTAttribute-Text"></a>
 The segment of input text extracted as this attribute.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Traits **   <a name="comprehendmedical-Type-SNOMEDCTAttribute-Traits"></a>
 Contextual information for an attribute. Examples include signs, symptoms, diagnosis, and negation.
Type: Array of [SNOMEDCTTrait](API_SNOMEDCTTrait.md) objects
Required: No

 ** Type **   <a name="comprehendmedical-Type-SNOMEDCTAttribute-Type"></a>
 The type of attribute. Possible types include DX\_NAME, ACUITY, DIRECTION, SYSTEM\_ORGAN\_SITE,TEST\_NAME, TEST\_VALUE, TEST\_UNIT, PROCEDURE\_NAME, and TREATMENT\_NAME.
Type: String
Valid Values: `ACUITY | QUALITY | DIRECTION | SYSTEM_ORGAN_SITE | TEST_VALUE | TEST_UNIT`
Required: No

## See Also
<a name="API_SNOMEDCTAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/SNOMEDCTAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/SNOMEDCTAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/SNOMEDCTAttribute)
