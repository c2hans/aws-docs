---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ToolReference.html
---

# ToolReference

A reference to a tool in the tool configuration. Used with `ToolAdditionBlock` and `ToolRemovalBlock` to identify which tool to add or remove mid-conversation.

## Contents
<a name="API_runtime_ToolReference_Contents"></a>

 ** name **   <a name="bedrock-Type-runtime_ToolReference-name"></a>
The name of the tool. Must match the name of a tool declared in the top-level tool configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** serverName **   <a name="bedrock-Type-runtime_ToolReference-serverName"></a>
The name of the MCP server that provides the tool. Required when referencing an MCP tool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** type **   <a name="bedrock-Type-runtime_ToolReference-type"></a>
The type of tool reference.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_runtime_ToolReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ToolReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ToolReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ToolReference)
