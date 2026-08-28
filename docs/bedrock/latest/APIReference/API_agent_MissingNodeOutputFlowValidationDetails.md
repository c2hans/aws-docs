---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_MissingNodeOutputFlowValidationDetails.html
---

# MissingNodeOutputFlowValidationDetails
<a name="API_agent_MissingNodeOutputFlowValidationDetails"></a>

Details about a missing required output in a node.

## Contents
<a name="API_agent_MissingNodeOutputFlowValidationDetails_Contents"></a>

 ** node **   <a name="bedrock-Type-agent_MissingNodeOutputFlowValidationDetails-node"></a>
The name of the node missing the required output.
Type: String
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`
Required: Yes

 ** output **   <a name="bedrock-Type-agent_MissingNodeOutputFlowValidationDetails-output"></a>
The name of the missing output.
Type: String
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`
Required: Yes

## See Also
<a name="API_agent_MissingNodeOutputFlowValidationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/MissingNodeOutputFlowValidationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/MissingNodeOutputFlowValidationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/MissingNodeOutputFlowValidationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
