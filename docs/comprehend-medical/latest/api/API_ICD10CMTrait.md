---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ICD10CMTrait.html
---

# ICD10CMTrait
<a name="API_ICD10CMTrait"></a>

Contextual information for the entity. The traits recognized by InferICD10CM are `DIAGNOSIS`, `SIGN`, `SYMPTOM`, and `NEGATION`.

## Contents
<a name="API_ICD10CMTrait_Contents"></a>

 ** Name **   <a name="comprehendmedical-Type-ICD10CMTrait-Name"></a>
Provides a name or contextual description about the trait.
Type: String
Valid Values: `NEGATION | DIAGNOSIS | SIGN | SYMPTOM | PERTAINS_TO_FAMILY | HYPOTHETICAL | LOW_CONFIDENCE`
Required: No

 ** Score **   <a name="comprehendmedical-Type-ICD10CMTrait-Score"></a>
The level of confidence that Comprehend Medical; has that the segment of text is correctly recognized as a trait.
Type: Float
Required: No

## See Also
<a name="API_ICD10CMTrait_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/ICD10CMTrait)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/ICD10CMTrait)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/ICD10CMTrait)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend Medical. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend-medical` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
