---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Tool.html
---

# Tool
<a name="API_runtime_Tool"></a>

Information about a tool that you can use with the Converse API. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_runtime_Tool_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cachePoint **   <a name="bedrock-Type-runtime_Tool-cachePoint"></a>
CachePoint to include in the tool configuration.
Type: [CachePointBlock](API_runtime_CachePointBlock.md) object
Required: No

 ** systemTool **   <a name="bedrock-Type-runtime_Tool-systemTool"></a>
Specifies the system-defined tool that you want use.
Type: [SystemTool](API_runtime_SystemTool.md) object
Required: No

 ** toolSpec **   <a name="bedrock-Type-runtime_Tool-toolSpec"></a>
The specfication for the tool.
Type: [ToolSpecification](API_runtime_ToolSpecification.md) object
Required: No

## See Also
<a name="API_runtime_Tool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/Tool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/Tool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/Tool)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
