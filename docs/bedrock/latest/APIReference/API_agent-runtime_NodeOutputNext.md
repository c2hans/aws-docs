---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_NodeOutputNext.html
---

# NodeOutputNext
<a name="API_agent-runtime_NodeOutputNext"></a>

Represents the next node that receives output data.

## Contents
<a name="API_agent-runtime_NodeOutputNext_Contents"></a>

 ** inputFieldName **   <a name="bedrock-Type-agent-runtime_NodeOutputNext-inputFieldName"></a>
The name of the input field in the next node that receives the data.
Type: String
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`
Required: Yes

 ** nodeName **   <a name="bedrock-Type-agent-runtime_NodeOutputNext-nodeName"></a>
The name of the next node that receives the output data.
Type: String
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`
Required: Yes

## See Also
<a name="API_agent-runtime_NodeOutputNext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/NodeOutputNext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/NodeOutputNext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/NodeOutputNext)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
