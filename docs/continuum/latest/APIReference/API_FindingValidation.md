---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_FindingValidation.html
---

# FindingValidation
<a name="API_FindingValidation"></a>

A validator's assessment of a finding. Present only when validation actually ran — absent for finding types that are ingested untested, rather than reporting a verdict Continuum did not reach.

## Contents
<a name="API_FindingValidation_Contents"></a>

 ** verdict **   <a name="continuum-Type-FindingValidation-verdict"></a>
A validator's conclusion about whether a finding is real.
Type: String
Valid Values: `TRUE_POSITIVE | FALSE_POSITIVE | BENIGN_TRUE_POSITIVE | NEEDS_REVIEW`
Required: Yes

 ** blockingReason **   <a name="continuum-Type-FindingValidation-blockingReason"></a>
Why a validator rejected a finding. NONE accompanies a true positive.
Type: String
Valid Values: `UNREACHABLE | PROTECTED | MISCLASSIFIED | EXCLUDED | NOT_FEASIBLE | RISK_MITIGATED | NONE`
Required: No

 ** confidence **   <a name="continuum-Type-FindingValidation-confidence"></a>
The confidence.
Type: Double
Required: No

 ** evidence **   <a name="continuum-Type-FindingValidation-evidence"></a>
The evidence.
Type: Array of [FindingEvidence](API_FindingEvidence.md) objects
Array Members: Minimum number of 0 items. Maximum number of 64 items.
Required: No

 ** mitigatingControls **   <a name="continuum-Type-FindingValidation-mitigatingControls"></a>
The mitigating Controls.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** preconditions **   <a name="continuum-Type-FindingValidation-preconditions"></a>
The preconditions.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** rationale **   <a name="continuum-Type-FindingValidation-rationale"></a>
The rationale.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Required: No

 ** severityAdjustment **   <a name="continuum-Type-FindingValidation-severityAdjustment"></a>
A validator's severity conclusion. UNCHANGED means the producer's reported severity stands.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | INFORMATIONAL | UNCHANGED`
Required: No

## See Also
<a name="API_FindingValidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/FindingValidation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/FindingValidation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/FindingValidation)
