---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_UnmappedAttribute.html
---

# UnmappedAttribute
<a name="API_UnmappedAttribute"></a>

 An attribute that was extracted, but Comprehend Medical; was unable to relate to an entity.

## Contents
<a name="API_UnmappedAttribute_Contents"></a>

 ** Attribute **   <a name="comprehendmedical-Type-UnmappedAttribute-Attribute"></a>
 The specific attribute that has been extracted but not mapped to an entity.
Type: [Attribute](API_Attribute.md) object
Required: No

 ** Type **   <a name="comprehendmedical-Type-UnmappedAttribute-Type"></a>
 The type of the unmapped attribute, could be one of the following values: "MEDICATION", "MEDICAL\_CONDITION", "ANATOMY", "TEST\_AND\_TREATMENT\_PROCEDURE" or "PROTECTED\_HEALTH\_INFORMATION".
Type: String
Valid Values: `MEDICATION | MEDICAL_CONDITION | PROTECTED_HEALTH_INFORMATION | TEST_TREATMENT_PROCEDURE | ANATOMY | TIME_EXPRESSION | BEHAVIORAL_ENVIRONMENTAL_SOCIAL`
Required: No

## See Also
<a name="API_UnmappedAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/UnmappedAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/UnmappedAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/UnmappedAttribute)
