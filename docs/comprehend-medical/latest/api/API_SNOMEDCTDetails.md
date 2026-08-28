---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_SNOMEDCTDetails.html
---

# SNOMEDCTDetails
<a name="API_SNOMEDCTDetails"></a>

 The information about the revision of the SNOMED-CT ontology in the response. Specifically, the details include the SNOMED-CT edition, language, and version date.

## Contents
<a name="API_SNOMEDCTDetails_Contents"></a>

 ** Edition **   <a name="comprehendmedical-Type-SNOMEDCTDetails-Edition"></a>
 The edition of SNOMED-CT used. The edition used for the InferSNOMEDCT editions is the US edition.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Language **   <a name="comprehendmedical-Type-SNOMEDCTDetails-Language"></a>
 The language used in the SNOMED-CT ontology. All Amazon Comprehend Medical operations are US English (en).
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** VersionDate **   <a name="comprehendmedical-Type-SNOMEDCTDetails-VersionDate"></a>
 The version date of the SNOMED-CT ontology used.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_SNOMEDCTDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/SNOMEDCTDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/SNOMEDCTDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/SNOMEDCTDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend Medical. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend-medical` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
