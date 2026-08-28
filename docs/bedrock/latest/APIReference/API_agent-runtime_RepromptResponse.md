---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RepromptResponse.html
---

# RepromptResponse
<a name="API_agent-runtime_RepromptResponse"></a>

Contains details about the agent's response to reprompt the input.

## Contents
<a name="API_agent-runtime_RepromptResponse_Contents"></a>

 ** source **   <a name="bedrock-Type-agent-runtime_RepromptResponse-source"></a>
Specifies what output is prompting the agent to reprompt the input.
Type: String
Valid Values: `ACTION_GROUP | KNOWLEDGE_BASE | PARSER`
Required: No

 ** text **   <a name="bedrock-Type-agent-runtime_RepromptResponse-text"></a>
The text reprompting the input.
Type: String
Required: No

## See Also
<a name="API_agent-runtime_RepromptResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/RepromptResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/RepromptResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/RepromptResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
