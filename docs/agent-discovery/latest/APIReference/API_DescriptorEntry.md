---
source_url: https://docs.aws.amazon.com/agent-discovery/latest/APIReference/API_DescriptorEntry.html
---

# DescriptorEntry

The content of one descriptor of a record, such as an A2A agent card, an MCP server card, or a skills definition. The content is provided inline (`data`) or as a reference to content hosted at a URL (`source`).

## Contents
<a name="API_DescriptorEntry_Contents"></a>

 ** additionalData **   <a name="agentdiscovery-Type-DescriptorEntry-additionalData"></a>
Nested descriptors, keyed by name, such as the tools of an MCP server.
Type: String to [DescriptorEntry](API_DescriptorEntry.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 32 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** data **   <a name="agentdiscovery-Type-DescriptorEntry-data"></a>
The descriptor content, as a JSON string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** source **   <a name="agentdiscovery-Type-DescriptorEntry-source"></a>
The location of descriptor content that is hosted outside the record.
Type: [DescriptorSource](API_DescriptorSource.md) object
Required: No

 ** version **   <a name="agentdiscovery-Type-DescriptorEntry-version"></a>
The version of the descriptor type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_DescriptorEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-discovery-2022-07-26/DescriptorEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-discovery-2022-07-26/DescriptorEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-discovery-2022-07-26/DescriptorEntry)
