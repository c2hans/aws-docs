---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_FunctionSchema.html
---

# FunctionSchema
<a name="API_agent-runtime_FunctionSchema"></a>

 Contains details about the function schema for the action group or the JSON or YAML-formatted payload defining the schema.

## Contents
<a name="API_agent-runtime_FunctionSchema_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** functions **   <a name="bedrock-Type-agent-runtime_FunctionSchema-functions"></a>
 A list of functions that each define an action in the action group.
Type: Array of [FunctionDefinition](API_agent-runtime_FunctionDefinition.md) objects
Required: No

## See Also
<a name="API_agent-runtime_FunctionSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FunctionSchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FunctionSchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FunctionSchema)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
