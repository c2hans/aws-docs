---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_SNOMEDCTEntity.html
---

# SNOMEDCTEntity
<a name="API_SNOMEDCTEntity"></a>

 The collection of medical entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence that Comprehend Medical has in the detection and analysis. Attributes and traits of the entity are also returned.

## Contents
<a name="API_SNOMEDCTEntity_Contents"></a>

 ** Attributes **   <a name="comprehendmedical-Type-SNOMEDCTEntity-Attributes"></a>
 An extracted segment of the text that is an attribute of an entity, or otherwise related to an entity, such as the dosage of a medication taken.
Type: Array of [SNOMEDCTAttribute](API_SNOMEDCTAttribute.md) objects
Required: No

 ** BeginOffset **   <a name="comprehendmedical-Type-SNOMEDCTEntity-BeginOffset"></a>
 The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string.
Type: Integer
Required: No

 ** Category **   <a name="comprehendmedical-Type-SNOMEDCTEntity-Category"></a>
 The category of the detected entity. Possible categories are MEDICAL\_CONDITION, ANATOMY, or TEST\_TREATMENT\_PROCEDURE.
Type: String
Valid Values: `MEDICAL_CONDITION | ANATOMY | TEST_TREATMENT_PROCEDURE`
Required: No

 ** EndOffset **   <a name="comprehendmedical-Type-SNOMEDCTEntity-EndOffset"></a>
 The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string.
Type: Integer
Required: No

 ** Id **   <a name="comprehendmedical-Type-SNOMEDCTEntity-Id"></a>
 The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier.
Type: Integer
Required: No

 ** Score **   <a name="comprehendmedical-Type-SNOMEDCTEntity-Score"></a>
 The level of confidence that Comprehend Medical has in the accuracy of the detected entity.
Type: Float
Required: No

 ** SNOMEDCTConcepts **   <a name="comprehendmedical-Type-SNOMEDCTEntity-SNOMEDCTConcepts"></a>
 The SNOMED concepts that the entity could refer to, along with a score indicating the likelihood of the match.
Type: Array of [SNOMEDCTConcept](API_SNOMEDCTConcept.md) objects
Required: No

 ** Text **   <a name="comprehendmedical-Type-SNOMEDCTEntity-Text"></a>
 The segment of input text extracted as this entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: No

 ** Traits **   <a name="comprehendmedical-Type-SNOMEDCTEntity-Traits"></a>
 Contextual information for the entity.
Type: Array of [SNOMEDCTTrait](API_SNOMEDCTTrait.md) objects
Required: No

 ** Type **   <a name="comprehendmedical-Type-SNOMEDCTEntity-Type"></a>
 Describes the specific type of entity with category of entities. Possible types include DX\_NAME, ACUITY, DIRECTION, SYSTEM\_ORGAN\_SITE, TEST\_NAME, TEST\_VALUE, TEST\_UNIT, PROCEDURE\_NAME, or TREATMENT\_NAME.
Type: String
Valid Values: `DX_NAME | TEST_NAME | PROCEDURE_NAME | TREATMENT_NAME`
Required: No

## See Also
<a name="API_SNOMEDCTEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/SNOMEDCTEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/SNOMEDCTEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/SNOMEDCTEntity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend Medical. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend-medical` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
