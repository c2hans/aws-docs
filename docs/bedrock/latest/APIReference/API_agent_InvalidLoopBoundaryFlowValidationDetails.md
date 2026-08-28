---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_InvalidLoopBoundaryFlowValidationDetails.html
---

# InvalidLoopBoundaryFlowValidationDetails
<a name="API_agent_InvalidLoopBoundaryFlowValidationDetails"></a>

Details about a flow that contains connections that violate loop boundary rules.

## Contents
<a name="API_agent_InvalidLoopBoundaryFlowValidationDetails_Contents"></a>

 ** connection **   <a name="bedrock-Type-agent_InvalidLoopBoundaryFlowValidationDetails-connection"></a>
The name of the connection that violates loop boundary rules.
Type: String
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,100}`
Required: Yes

 ** source **   <a name="bedrock-Type-agent_InvalidLoopBoundaryFlowValidationDetails-source"></a>
The source node of the connection that violates DoWhile loop boundary rules.
Type: String
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`
Required: Yes

 ** target **   <a name="bedrock-Type-agent_InvalidLoopBoundaryFlowValidationDetails-target"></a>
The target node of the connection that violates DoWhile loop boundary rules.
Type: String
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`
Required: Yes

## See Also
<a name="API_agent_InvalidLoopBoundaryFlowValidationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/InvalidLoopBoundaryFlowValidationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/InvalidLoopBoundaryFlowValidationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/InvalidLoopBoundaryFlowValidationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
