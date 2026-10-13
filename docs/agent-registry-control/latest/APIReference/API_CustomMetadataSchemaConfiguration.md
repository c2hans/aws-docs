---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_CustomMetadataSchemaConfiguration.html
---

# CustomMetadataSchemaConfiguration
<a name="API_CustomMetadataSchemaConfiguration"></a>

The custom metadata fields that records in the registry can carry. `defaultSchema` defines the common attributes for every record type, and `recordTypeSchemaOverrides` adds fields for individual record types.

## Contents
<a name="API_CustomMetadataSchemaConfiguration_Contents"></a>

 ** defaultSchema **   <a name="agentregistrycontrol-Type-CustomMetadataSchemaConfiguration-defaultSchema"></a>
A JSON Schema with the common attributes: fields that records of every record type can carry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: No

 ** recordTypeSchemaOverrides **   <a name="agentregistrycontrol-Type-CustomMetadataSchemaConfiguration-recordTypeSchemaOverrides"></a>
The fields for individual record types. Records of a record type can carry the common attributes defined in `defaultSchema` plus that record type's fields.
Type: Array of [RecordTypeSchemaOverride](API_RecordTypeSchemaOverride.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_CustomMetadataSchemaConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/CustomMetadataSchemaConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/CustomMetadataSchemaConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/CustomMetadataSchemaConfiguration)
