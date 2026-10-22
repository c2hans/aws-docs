---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_RetrievalInstructionSummary.html
---

# RetrievalInstructionSummary
<a name="API_agent_RetrievalInstructionSummary"></a>

A summary of a retrieval instruction, without the content.

## Contents
<a name="API_agent_RetrievalInstructionSummary_Contents"></a>

 ** createdAt **   <a name="bedrock-Type-agent_RetrievalInstructionSummary-createdAt"></a>
When you created the retrieval instruction.
Type: Timestamp
Required: Yes

 ** lastTransitionStatus **   <a name="bedrock-Type-agent_RetrievalInstructionSummary-lastTransitionStatus"></a>
The outcome or in-progress state of the most recent create or update of the retrieval instruction.
Type: String
Valid Values: `CREATING | UPDATING | CREATE_SUCCESSFUL | CREATE_FAILED | UPDATE_SUCCESSFUL | UPDATE_FAILED`
Required: Yes

 ** name **   <a name="bedrock-Type-agent_RetrievalInstructionSummary-name"></a>
The name of the retrieval instruction.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `([0-9a-zA-Z][_-]?){1,100}`
Required: Yes

 ** retrievalInstructionArn **   <a name="bedrock-Type-agent_RetrievalInstructionSummary-retrievalInstructionArn"></a>
The ARN of the retrieval instruction.
Type: String
Pattern: `arn:aws(-cn|-us-gov|-eusc|-iso(-[b-f])?)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:retrieval-instruction/[a-z0-9]{10}`
Required: Yes

 ** retrievalInstructionId **   <a name="bedrock-Type-agent_RetrievalInstructionSummary-retrievalInstructionId"></a>
The identifier of the retrieval instruction.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `[a-z0-9]{10}`
Required: Yes

 ** status **   <a name="bedrock-Type-agent_RetrievalInstructionSummary-status"></a>
Whether the instruction can be used. Only ACTIVE is resolvable at retrieval time.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_RetrievalInstructionSummary-updatedAt"></a>
When the retrieval instruction was last updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="bedrock-Type-agent_RetrievalInstructionSummary-description"></a>
A description of the retrieval instruction.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

## See Also
<a name="API_agent_RetrievalInstructionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/RetrievalInstructionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/RetrievalInstructionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/RetrievalInstructionSummary)
