---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_RxNormConcept.html
---

# RxNormConcept
<a name="API_RxNormConcept"></a>

The RxNorm concept that the entity could refer to, along with a score indicating the likelihood of the match.

## Contents
<a name="API_RxNormConcept_Contents"></a>

 ** Code **   <a name="comprehendmedical-Type-RxNormConcept-Code"></a>
RxNorm concept ID, also known as the RxCUI.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Description **   <a name="comprehendmedical-Type-RxNormConcept-Description"></a>
The description of the RxNorm concept.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Score **   <a name="comprehendmedical-Type-RxNormConcept-Score"></a>
The level of confidence that Amazon Comprehend Medical has that the entity is accurately linked to the reported RxNorm concept.
Type: Float
Required: No

## See Also
<a name="API_RxNormConcept_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/RxNormConcept)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/RxNormConcept)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/RxNormConcept)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend Medical. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend-medical` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
