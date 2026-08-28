---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_RxNormEntity.html
---

# RxNormEntity
<a name="API_RxNormEntity"></a>

The collection of medical entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence that Amazon Comprehend Medical has in the detection and analysis. Attributes and traits of the entity are also returned.

## Contents
<a name="API_RxNormEntity_Contents"></a>

 ** Attributes **   <a name="comprehendmedical-Type-RxNormEntity-Attributes"></a>
The extracted attributes that relate to the entity. The attributes recognized by InferRxNorm are `DOSAGE`, `DURATION`, `FORM`, `FREQUENCY`, `RATE`, `ROUTE_OR_MODE`, and `STRENGTH`.
Type: Array of [RxNormAttribute](API_RxNormAttribute.md) objects
Required: No

 ** BeginOffset **   <a name="comprehendmedical-Type-RxNormEntity-BeginOffset"></a>
The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string.
Type: Integer
Required: No

 ** Category **   <a name="comprehendmedical-Type-RxNormEntity-Category"></a>
The category of the entity.
Type: String
Valid Values: `MEDICATION`
Required: No

 ** EndOffset **   <a name="comprehendmedical-Type-RxNormEntity-EndOffset"></a>
The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string.
Type: Integer
Required: No

 ** Id **   <a name="comprehendmedical-Type-RxNormEntity-Id"></a>
The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier.
Type: Integer
Required: No

 ** RxNormConcepts **   <a name="comprehendmedical-Type-RxNormEntity-RxNormConcepts"></a>
 The RxNorm concepts that the entity could refer to, along with a score indicating the likelihood of the match.
Type: Array of [RxNormConcept](API_RxNormConcept.md) objects
Required: No

 ** Score **   <a name="comprehendmedical-Type-RxNormEntity-Score"></a>
The level of confidence that Amazon Comprehend Medical has in the accuracy of the detected entity.
Type: Float
Required: No

 ** Text **   <a name="comprehendmedical-Type-RxNormEntity-Text"></a>
The segment of input text extracted from which the entity was detected.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: No

 ** Traits **   <a name="comprehendmedical-Type-RxNormEntity-Traits"></a>
 Contextual information for the entity.
Type: Array of [RxNormTrait](API_RxNormTrait.md) objects
Required: No

 ** Type **   <a name="comprehendmedical-Type-RxNormEntity-Type"></a>
Describes the specific type of entity.
Type: String
Valid Values: `BRAND_NAME | GENERIC_NAME`
Required: No

## See Also
<a name="API_RxNormEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/RxNormEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/RxNormEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/RxNormEntity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend Medical. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend-medical` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
