---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_ValidationExecutedProof.html
---

# ValidationExecutedProof
<a name="API_ValidationExecutedProof"></a>

Proof of exploitability the validation agent produced by executing code against the repository under test, with the output that execution produced.

## Contents
<a name="API_ValidationExecutedProof_Contents"></a>

 ** code **   <a name="continuum-Type-ValidationExecutedProof-code"></a>
The code.
Type: [ValidationProofCode](API_ValidationProofCode.md) object
Required: Yes

 ** observedEffect **   <a name="continuum-Type-ValidationExecutedProof-observedEffect"></a>
The observed Effect.
Type: String
Valid Values: `DATA_LEAKED | ERROR_REVEALED | BEHAVIOR_CHANGED | NO_EFFECT`
Required: No

 ** output **   <a name="continuum-Type-ValidationExecutedProof-output"></a>
The output.
Type: [ValidationProofOutput](API_ValidationProofOutput.md) object
Required: No

## See Also
<a name="API_ValidationExecutedProof_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/ValidationExecutedProof)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/ValidationExecutedProof)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/ValidationExecutedProof)
