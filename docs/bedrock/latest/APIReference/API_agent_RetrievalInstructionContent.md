---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_RetrievalInstructionContent.html
---

# RetrievalInstructionContent
<a name="API_agent_RetrievalInstructionContent"></a>

The instruction content, as a set of named fields. Every field is optional; at least one must be present. Service-side validation enforces per-field and aggregate size limits.

## Contents
<a name="API_agent_RetrievalInstructionContent_Contents"></a>

 ** answerFormat **   <a name="bedrock-Type-agent_RetrievalInstructionContent-answerFormat"></a>
How the answer is structured, including how sources are cited.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** answerPolicy **   <a name="bedrock-Type-agent_RetrievalInstructionContent-answerPolicy"></a>
Whether and how to answer: how strongly an answer must be supported, and what to do with questions outside scope.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** persona **   <a name="bedrock-Type-agent_RetrievalInstructionContent-persona"></a>
Who the assistant is: identity, tone and language.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** retrievalGuidance **   <a name="bedrock-Type-agent_RetrievalInstructionContent-retrievalGuidance"></a>
How to interpret and decompose the question, and what to prioritise when searching.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_agent_RetrievalInstructionContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/RetrievalInstructionContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/RetrievalInstructionContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/RetrievalInstructionContent)
