---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveAppliedInstruction.html
---

# AgenticRetrieveAppliedInstruction
<a name="API_agent-runtime_AgenticRetrieveAppliedInstruction"></a>

The retrieval instruction, identified by its ID and version, that was applied to the request.

## Contents
<a name="API_agent-runtime_AgenticRetrieveAppliedInstruction_Contents"></a>

 ** id **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveAppliedInstruction-id"></a>
The identifier of the retrieval instruction applied.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** version **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveAppliedInstruction-version"></a>
The version that was applied: a version number, or DRAFT. The service reports this version whenever it reports appliedInstruction, including DRAFT when the request did not specify a version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 9.
Pattern: `(DRAFT|[1-9][0-9]{0,8})`
Required: No

## See Also
<a name="API_agent-runtime_AgenticRetrieveAppliedInstruction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveAppliedInstruction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveAppliedInstruction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveAppliedInstruction)
