---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_ValidationSourceAnalysis.html
---

# ValidationSourceAnalysis
<a name="API_ValidationSourceAnalysis"></a>

Proof of exploitability the validation agent produced by reading the repository's source, with nothing built or run. Further members, such as diagram and references, can be added later as optional details.

## Contents
<a name="API_ValidationSourceAnalysis_Contents"></a>

 ** summary **   <a name="continuum-Type-ValidationSourceAnalysis-summary"></a>
The summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: Yes

 ** inferredEffect **   <a name="continuum-Type-ValidationSourceAnalysis-inferredEffect"></a>
The inferred Effect.
Type: String
Valid Values: `DATA_LEAKED | ERROR_REVEALED | BEHAVIOR_CHANGED | NO_EFFECT`
Required: No

## See Also
<a name="API_ValidationSourceAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/ValidationSourceAnalysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/ValidationSourceAnalysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/ValidationSourceAnalysis)
