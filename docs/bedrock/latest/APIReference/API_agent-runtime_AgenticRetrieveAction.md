---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveAction.html
---

# AgenticRetrieveAction
<a name="API_agent-runtime_AgenticRetrieveAction"></a>

An action taken during agentic retrieval.

## Contents
<a name="API_agent-runtime_AgenticRetrieveAction_Contents"></a>

 ** fullDocumentExpansion **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveAction-fullDocumentExpansion"></a>
Details of a full document expansion action.
Type: [AgenticRetrieveFullDocExpansionDetails](API_agent-runtime_AgenticRetrieveFullDocExpansionDetails.md) object
Required: No

 ** memoryRetrieve **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveAction-memoryRetrieve"></a>
The details of a long-term memory retrieval that the agent chose to perform.
Type: [AgenticRetrieveMemoryRetrieveDetails](API_agent-runtime_AgenticRetrieveMemoryRetrieveDetails.md) object
Required: No

 ** retrieve **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveAction-retrieve"></a>
Details of the retrieve action.
Type: [AgenticRetrieveActionDetails](API_agent-runtime_AgenticRetrieveActionDetails.md) object
Required: No

## See Also
<a name="API_agent-runtime_AgenticRetrieveAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
