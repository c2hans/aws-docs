---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ToolSpec.html
---

# ToolSpec
<a name="API_ToolSpec"></a>

Specification for a tool that acts can invoke, including its name, description, and input schema.

## Contents
<a name="API_ToolSpec_Contents"></a>

 ** description **   <a name="novaact-Type-ToolSpec-description"></a>
A description of what the tool does and how it should be used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: Yes

 ** inputSchema **   <a name="novaact-Type-ToolSpec-inputSchema"></a>
The JSON schema that defines the expected input format for the tool.
Type: [ToolInputSchema](API_ToolInputSchema.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** name **   <a name="novaact-Type-ToolSpec-name"></a>
The unique name of the tool that acts will use to invoke it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## See Also
<a name="API_ToolSpec_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/ToolSpec)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/ToolSpec)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/ToolSpec)
