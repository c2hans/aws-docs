---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_RetrievalInstructionFailureReason.html
---

# RetrievalInstructionFailureReason
<a name="API_agent_RetrievalInstructionFailureReason"></a>

One reason the most recent create or update did not succeed. code drives programmatic branching (fix the text, fix the configuration, or retry); message carries the specific cause.

## Contents
<a name="API_agent_RetrievalInstructionFailureReason_Contents"></a>

 ** code **   <a name="bedrock-Type-agent_RetrievalInstructionFailureReason-code"></a>
Stable, machine-readable classification by fault attribution. Valid values:
+ CONTENT\_REJECTED – The review rejected the named field's content; revise the text and resubmit.
+ CLIENT\_ERROR – The review could not run for a customer-side reason, for example the customer managed AWS KMS key could not be used; fix the configuration and resubmit.
+ INTERNAL\_ERROR – The review could not complete due to a service fault; retry the create or update.
New values may be added over time; your client should tolerate values it does not recognize and treat them as a failure.
Type: String
Valid Values: `CONTENT_REJECTED | CLIENT_ERROR | INTERNAL_ERROR`
Required: Yes

 ** message **   <a name="bedrock-Type-agent_RetrievalInstructionFailureReason-message"></a>
Human-readable explanation of the specific cause. Never contains the customer's own text.
Type: String
Required: Yes

 ** fieldName **   <a name="bedrock-Type-agent_RetrievalInstructionFailureReason-fieldName"></a>
The instruction field this entry is about. Present on review rejections of a specific field; absent when the failure applies to the whole review, because a client-side execution failure or a service fault has no single field.
Type: String
Valid Values: `RETRIEVAL_GUIDANCE | PERSONA | ANSWER_FORMAT | ANSWER_POLICY`
Required: No

## See Also
<a name="API_agent_RetrievalInstructionFailureReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/RetrievalInstructionFailureReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/RetrievalInstructionFailureReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/RetrievalInstructionFailureReason)
