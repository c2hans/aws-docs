---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_ValidationEvidenceBody.html
---

# ValidationEvidenceBody
<a name="API_ValidationEvidenceBody"></a>

Projected content for a VALIDATION\_EVIDENCE artifact: the validation agent's durable proof of exploitability.

## Contents
<a name="API_ValidationEvidenceBody_Contents"></a>

 ** exploitable **   <a name="continuum-Type-ValidationEvidenceBody-exploitable"></a>
The exploitable.
Type: String
Valid Values: `EXPLOITABLE | NOT_EXPLOITABLE | UNCERTAIN`
Required: Yes

 ** attackFlowsConfirmed **   <a name="continuum-Type-ValidationEvidenceBody-attackFlowsConfirmed"></a>
The attack Flows Confirmed.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** executedProof **   <a name="continuum-Type-ValidationEvidenceBody-executedProof"></a>
Proof of exploitability the validation agent produced by executing code against the repository under test, with the output that execution produced.
Type: [ValidationExecutedProof](API_ValidationExecutedProof.md) object
Required: No

 ** exploitArtifact **   <a name="continuum-Type-ValidationEvidenceBody-exploitArtifact"></a>
A concrete exploit payload and the effect validation observed from it.
Type: [ValidationExploitArtifact](API_ValidationExploitArtifact.md) object
Required: No

 ** flowVerdicts **   <a name="continuum-Type-ValidationEvidenceBody-flowVerdicts"></a>
The flow Verdicts.
Type: Array of [FlowVerdict](API_FlowVerdict.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** perFindingResults **   <a name="continuum-Type-ValidationEvidenceBody-perFindingResults"></a>
The per Finding Results.
Type: Array of [PerFindingResult](API_PerFindingResult.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** sourceAnalysis **   <a name="continuum-Type-ValidationEvidenceBody-sourceAnalysis"></a>
Proof of exploitability the validation agent produced by reading the repository's source, with nothing built or run. Further members, such as diagram and references, can be added later as optional details.
Type: [ValidationSourceAnalysis](API_ValidationSourceAnalysis.md) object
Required: No

 ** terminalStatus **   <a name="continuum-Type-ValidationEvidenceBody-terminalStatus"></a>
The terminal Status.
Type: String
Valid Values: `COMPLETED | FAILED | NO_SOURCE_AVAILABLE | PARTIAL`
Required: No

## See Also
<a name="API_ValidationEvidenceBody_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/ValidationEvidenceBody)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/ValidationEvidenceBody)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/ValidationEvidenceBody)
