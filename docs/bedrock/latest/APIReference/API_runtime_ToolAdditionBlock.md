---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ToolAdditionBlock.html
---

# ToolAdditionBlock

A content block for adding a tool to the available tool set mid-conversation. Each block references a single tool via its `tool` field. Use within a `system` role message to make a tool available without re-sending the full tool configuration.

## Contents
<a name="API_runtime_ToolAdditionBlock_Contents"></a>

 ** tool **   <a name="bedrock-Type-runtime_ToolAdditionBlock-tool"></a>
A reference to the tool to add to the available tool set.
Type: [ToolReference](API_runtime_ToolReference.md) object
Required: Yes

## See Also
<a name="API_runtime_ToolAdditionBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ToolAdditionBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ToolAdditionBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ToolAdditionBlock)
