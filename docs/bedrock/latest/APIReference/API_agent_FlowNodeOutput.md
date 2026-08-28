---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_FlowNodeOutput.html
---

# FlowNodeOutput
<a name="API_agent_FlowNodeOutput"></a>

Contains configurations for an output from a node.

## Contents
<a name="API_agent_FlowNodeOutput_Contents"></a>

 ** name **   <a name="bedrock-Type-agent_FlowNodeOutput-name"></a>
A name for the output that you can reference.
Type: String
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`
Required: Yes

 ** type **   <a name="bedrock-Type-agent_FlowNodeOutput-type"></a>
The data type of the output. If the output doesn't match this type at runtime, a validation error will be thrown.
Type: String
Valid Values: `String | Number | Boolean | Object | Array`
Required: Yes

## See Also
<a name="API_agent_FlowNodeOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/FlowNodeOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/FlowNodeOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/FlowNodeOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
