---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_CustomMetadataSchemaConfiguration.html
---

# CustomMetadataSchemaConfiguration
<a name="API_CustomMetadataSchemaConfiguration"></a>

Configuration that defines a typed metadata schema for a registry. Specify at least one of a default schema or per-record-type schema overrides. You can provide both.

## Contents
<a name="API_CustomMetadataSchemaConfiguration_Contents"></a>

 ** defaultSchema **   <a name="agentregistrycontrol-Type-CustomMetadataSchemaConfiguration-defaultSchema"></a>
The default JSON Schema that applies to record types without a specific override. Supported property types are `string`, `string` with an `enum` constraint, `string` with a `uri` format, and `boolean`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Required: No

 ** recordTypeSchemaOverrides **   <a name="agentregistrycontrol-Type-CustomMetadataSchemaConfiguration-recordTypeSchemaOverrides"></a>
A list of per-record-type schema overrides. When a record's type matches an override, that override's schema is used instead of the default schema for validation. If you don't specify an override for a record type, the default schema applies. If no default schema exists, custom metadata on records of that type is rejected.
Type: Array of [RecordTypeSchemaOverride](API_RecordTypeSchemaOverride.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

## See Also
<a name="API_CustomMetadataSchemaConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/CustomMetadataSchemaConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/CustomMetadataSchemaConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/CustomMetadataSchemaConfiguration)
