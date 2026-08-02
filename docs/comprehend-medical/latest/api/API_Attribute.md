---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_Attribute.html
---

# Attribute
<a name="API_Attribute"></a>

 An extracted segment of the text that is an attribute of an entity, or otherwise related to an entity, such as the dosage of a medication taken. It contains information about the attribute such as id, begin and end offset within the input text, and the segment of the input text.

## Contents
<a name="API_Attribute_Contents"></a>

 ** BeginOffset **   <a name="comprehendmedical-Type-Attribute-BeginOffset"></a>
 The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string.
Type: Integer
Required: No

 ** Category **   <a name="comprehendmedical-Type-Attribute-Category"></a>
 The category of attribute.
Type: String
Valid Values: `MEDICATION | MEDICAL_CONDITION | PROTECTED_HEALTH_INFORMATION | TEST_TREATMENT_PROCEDURE | ANATOMY | TIME_EXPRESSION | BEHAVIORAL_ENVIRONMENTAL_SOCIAL`
Required: No

 ** EndOffset **   <a name="comprehendmedical-Type-Attribute-EndOffset"></a>
 The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.
Type: Integer
Required: No

 ** Id **   <a name="comprehendmedical-Type-Attribute-Id"></a>
 The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier.
Type: Integer
Required: No

 ** RelationshipScore **   <a name="comprehendmedical-Type-Attribute-RelationshipScore"></a>
 The level of confidence that Comprehend Medical; has that this attribute is correctly related to this entity.
Type: Float
Required: No

 ** RelationshipType **   <a name="comprehendmedical-Type-Attribute-RelationshipType"></a>
The type of relationship between the entity and attribute. Type for the relationship is `OVERLAP`, indicating that the entity occurred at the same time as the `Date_Expression`.
Type: String
Valid Values: `EVERY | WITH_DOSAGE | ADMINISTERED_VIA | FOR | NEGATIVE | OVERLAP | DOSAGE | ROUTE_OR_MODE | FORM | FREQUENCY | DURATION | STRENGTH | RATE | ACUITY | TEST_VALUE | TEST_UNITS | TEST_UNIT | DIRECTION | SYSTEM_ORGAN_SITE | AMOUNT | USAGE | QUALITY`
Required: No

 ** Score **   <a name="comprehendmedical-Type-Attribute-Score"></a>
 The level of confidence that Comprehend Medical; has that the segment of text is correctly recognized as an attribute.
Type: Float
Required: No

 ** Text **   <a name="comprehendmedical-Type-Attribute-Text"></a>
 The segment of input text extracted as this attribute.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Traits **   <a name="comprehendmedical-Type-Attribute-Traits"></a>
 Contextual information for this attribute.
Type: Array of [Trait](API_Trait.md) objects
Required: No

 ** Type **   <a name="comprehendmedical-Type-Attribute-Type"></a>
 The type of attribute.
Type: String
Valid Values: `NAME | DX_NAME | DOSAGE | ROUTE_OR_MODE | FORM | FREQUENCY | DURATION | GENERIC_NAME | BRAND_NAME | STRENGTH | RATE | ACUITY | TEST_NAME | TEST_VALUE | TEST_UNITS | TEST_UNIT | PROCEDURE_NAME | TREATMENT_NAME | DATE | AGE | CONTACT_POINT | PHONE_OR_FAX | EMAIL | IDENTIFIER | ID | URL | ADDRESS | PROFESSION | SYSTEM_ORGAN_SITE | DIRECTION | QUALITY | QUANTITY | TIME_EXPRESSION | TIME_TO_MEDICATION_NAME | TIME_TO_DX_NAME | TIME_TO_TEST_NAME | TIME_TO_PROCEDURE_NAME | TIME_TO_TREATMENT_NAME | AMOUNT | GENDER | RACE_ETHNICITY | ALLERGIES | TOBACCO_USE | ALCOHOL_CONSUMPTION | REC_DRUG_USE`
Required: No

## See Also
<a name="API_Attribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/Attribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/Attribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/Attribute)
