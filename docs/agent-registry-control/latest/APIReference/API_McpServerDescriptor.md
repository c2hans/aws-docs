---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_McpServerDescriptor.html
---

# McpServerDescriptor
<a name="API_McpServerDescriptor"></a>

Descriptor that defines the content of an MCP (Model Context Protocol) server registry record, including the server definition and its tool definitions. The content is validated against the MCP protocol schema.

## Contents
<a name="API_McpServerDescriptor_Contents"></a>

 ** additionalData **   <a name="agentregistrycontrol-Type-McpServerDescriptor-additionalData"></a>
Additional data associated with the MCP server descriptor, such as tool definitions.
Type: [McpServerAdditionalData](API_McpServerAdditionalData.md) object
Required: No

 ** data **   <a name="agentregistrycontrol-Type-McpServerDescriptor-data"></a>
The MCP server descriptor content, serialized as descriptor payload data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 102400.
Required: No

 ** dataSchemaVersion **   <a name="agentregistrycontrol-Type-McpServerDescriptor-dataSchemaVersion"></a>
The schema version of the descriptor payload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** source **   <a name="agentregistrycontrol-Type-McpServerDescriptor-source"></a>
The optional source configuration used to synchronize the MCP server descriptor content.
Type: [DescriptorSource](API_DescriptorSource.md) object
Required: No

## See Also
<a name="API_McpServerDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vestry-control-plane-2025-12-01/McpServerDescriptor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vestry-control-plane-2025-12-01/McpServerDescriptor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vestry-control-plane-2025-12-01/McpServerDescriptor)
