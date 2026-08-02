---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ICD10CMConcept.html
---

# ICD10CMConcept
<a name="API_ICD10CMConcept"></a>

 The ICD-10-CM concepts that the entity could refer to, along with a score indicating the likelihood of the match.

## Contents
<a name="API_ICD10CMConcept_Contents"></a>

 ** Code **   <a name="comprehendmedical-Type-ICD10CMConcept-Code"></a>
The ICD-10-CM code that identifies the concept found in the knowledge base from the Centers for Disease Control.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Description **   <a name="comprehendmedical-Type-ICD10CMConcept-Description"></a>
The long description of the ICD-10-CM code in the ontology.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Score **   <a name="comprehendmedical-Type-ICD10CMConcept-Score"></a>
The level of confidence that Amazon Comprehend Medical has that the entity is accurately linked to an ICD-10-CM concept.
Type: Float
Required: No

## See Also
<a name="API_ICD10CMConcept_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/ICD10CMConcept)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/ICD10CMConcept)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/ICD10CMConcept)
