---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveInstructionConfiguration.html
---

# AgenticRetrieveInstructionConfiguration
<a name="API_agent-runtime_AgenticRetrieveInstructionConfiguration"></a>

The retrieval instruction, identified by its ID and optional version, to apply to this request.

## Contents
<a name="API_agent-runtime_AgenticRetrieveInstructionConfiguration_Contents"></a>

 ** retrievalInstructionId **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveInstructionConfiguration-retrievalInstructionId"></a>
The identifier of the retrieval instruction. The instruction must exist in the caller's account and its status must be ACTIVE.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** version **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveInstructionConfiguration-version"></a>
The version of the retrieval instruction to apply: a version number, or DRAFT for the instruction's current reviewed content. When omitted, DRAFT is used. This default is permanent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 9.
Pattern: `(DRAFT|[1-9][0-9]{0,8})`
Required: No

## See Also
<a name="API_agent-runtime_AgenticRetrieveInstructionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveInstructionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveInstructionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveInstructionConfiguration)
