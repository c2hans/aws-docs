---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_SNOMEDCTConcept.html
---

# SNOMEDCTConcept
<a name="API_SNOMEDCTConcept"></a>

 The SNOMED-CT concepts that the entity could refer to, along with a score indicating the likelihood of the match.

## Contents
<a name="API_SNOMEDCTConcept_Contents"></a>

 ** Code **   <a name="comprehendmedical-Type-SNOMEDCTConcept-Code"></a>
 The numeric ID for the SNOMED-CT concept.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Description **   <a name="comprehendmedical-Type-SNOMEDCTConcept-Description"></a>
 The description of the SNOMED-CT concept.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Score **   <a name="comprehendmedical-Type-SNOMEDCTConcept-Score"></a>
 The level of confidence Comprehend Medical has that the entity should be linked to the identified SNOMED-CT concept.
Type: Float
Required: No

## See Also
<a name="API_SNOMEDCTConcept_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/SNOMEDCTConcept)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/SNOMEDCTConcept)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/SNOMEDCTConcept)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend Medical. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend-medical` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
