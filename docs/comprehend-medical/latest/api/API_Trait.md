---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_Trait.html
---

# Trait
<a name="API_Trait"></a>

 Provides contextual information about the extracted entity.

## Contents
<a name="API_Trait_Contents"></a>

 ** Name **   <a name="comprehendmedical-Type-Trait-Name"></a>
 Provides a name or contextual description about the trait.
Type: String
Valid Values: `SIGN | SYMPTOM | DIAGNOSIS | NEGATION | PERTAINS_TO_FAMILY | HYPOTHETICAL | LOW_CONFIDENCE | PAST_HISTORY | FUTURE`
Required: No

 ** Score **   <a name="comprehendmedical-Type-Trait-Score"></a>
 The level of confidence that Comprehend Medical; has in the accuracy of this trait.
Type: Float
Required: No

## See Also
<a name="API_Trait_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/Trait)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/Trait)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/Trait)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend Medical. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend-medical` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
