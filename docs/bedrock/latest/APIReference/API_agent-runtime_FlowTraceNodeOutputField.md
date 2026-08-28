---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_FlowTraceNodeOutputField.html
---

# FlowTraceNodeOutputField
<a name="API_agent-runtime_FlowTraceNodeOutputField"></a>

Contains information about a field in the output from a node. For more information, see [Track each step in your prompt flow by viewing its trace in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-trace.html).

## Contents
<a name="API_agent-runtime_FlowTraceNodeOutputField_Contents"></a>

 ** content **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeOutputField-content"></a>
The content of the node output.
Type: [FlowTraceNodeOutputContent](API_agent-runtime_FlowTraceNodeOutputContent.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** nodeOutputName **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeOutputField-nodeOutputName"></a>
The name of the node output.
Type: String
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}`
Required: Yes

 ** next **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeOutputField-next"></a>
The next node that receives output data from this field.
Type: Array of [FlowTraceNodeOutputNext](API_agent-runtime_FlowTraceNodeOutputNext.md) objects
Required: No

 ** type **   <a name="bedrock-Type-agent-runtime_FlowTraceNodeOutputField-type"></a>
The data type of the output field for compatibility validation.
Type: String
Valid Values: `String | Number | Boolean | Object | Array`
Required: No

## See Also
<a name="API_agent-runtime_FlowTraceNodeOutputField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowTraceNodeOutputField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowTraceNodeOutputField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowTraceNodeOutputField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
