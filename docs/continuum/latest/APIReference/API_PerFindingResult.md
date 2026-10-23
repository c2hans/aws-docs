---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_PerFindingResult.html
---

# PerFindingResult
<a name="API_PerFindingResult"></a>

Validation's result for one finding within a multi-finding bundle.

## Contents
<a name="API_PerFindingResult_Contents"></a>

 ** exploitable **   <a name="continuum-Type-PerFindingResult-exploitable"></a>
The exploitable.
Type: String
Valid Values: `EXPLOITABLE | NOT_EXPLOITABLE | UNCERTAIN`
Required: Yes

 ** findingId **   <a name="continuum-Type-PerFindingResult-findingId"></a>
The identifier of the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** confidence **   <a name="continuum-Type-PerFindingResult-confidence"></a>
The confidence.
Type: Double
Required: No

 ** exploitArtifact **   <a name="continuum-Type-PerFindingResult-exploitArtifact"></a>
A concrete exploit payload and the effect validation observed from it.
Type: [ValidationExploitArtifact](API_ValidationExploitArtifact.md) object
Required: No

 ** flowVerdicts **   <a name="continuum-Type-PerFindingResult-flowVerdicts"></a>
The flow Verdicts.
Type: Array of [FlowVerdict](API_FlowVerdict.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** reasoningChain **   <a name="continuum-Type-PerFindingResult-reasoningChain"></a>
The reasoning Chain.
Type: Array of [ReasoningStep](API_ReasoningStep.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## See Also
<a name="API_PerFindingResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/PerFindingResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/PerFindingResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/PerFindingResult)
