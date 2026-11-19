---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_MetadataConfiguration.html
---

# MetadataConfiguration

Contains the configuration of a single custom metadata field in a knowledge base, including its name, data type, and whether the field is searchable.

## Contents
<a name="API_agent_MetadataConfiguration_Contents"></a>

 ** name **   <a name="bedrock-Type-agent_MetadataConfiguration-name"></a>
The name of the custom metadata field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`
Required: Yes

 ** searchability **   <a name="bedrock-Type-agent_MetadataConfiguration-searchability"></a>
Specifies whether the custom metadata field is searchable. Valid values:
+  `ENABLED` – The field is searchable.
+  `DISABLED` – The field is not searchable.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** type **   <a name="bedrock-Type-agent_MetadataConfiguration-type"></a>
The data type of the custom metadata field. Valid values are `STRING` and `STRING_LIST`.
Type: String
Valid Values: `STRING | STRING_LIST`
Required: Yes

## See Also
<a name="API_agent_MetadataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/MetadataConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/MetadataConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/MetadataConfiguration)
