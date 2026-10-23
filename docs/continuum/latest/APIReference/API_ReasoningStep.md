---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_ReasoningStep.html
---

# ReasoningStep
<a name="API_ReasoningStep"></a>

One step in the validation agent's reasoning chain.

## Contents
<a name="API_ReasoningStep_Contents"></a>

 ** claim **   <a name="continuum-Type-ReasoningStep-claim"></a>
The claim.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: Yes

 ** source **   <a name="continuum-Type-ReasoningStep-source"></a>
The source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** step **   <a name="continuum-Type-ReasoningStep-step"></a>
The step.
Type: Integer
Required: Yes

 ** confidence **   <a name="continuum-Type-ReasoningStep-confidence"></a>
The confidence.
Type: Double
Required: No

## See Also
<a name="API_ReasoningStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/ReasoningStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/ReasoningStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/ReasoningStep)
