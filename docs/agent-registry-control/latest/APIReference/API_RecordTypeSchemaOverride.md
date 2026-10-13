---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_RecordTypeSchemaOverride.html
---

# RecordTypeSchemaOverride
<a name="API_RecordTypeSchemaOverride"></a>

The custom metadata fields for one record type, in addition to the common attributes defined in `defaultSchema`.

## Contents
<a name="API_RecordTypeSchemaOverride_Contents"></a>

 ** recordType **   <a name="agentregistrycontrol-Type-RecordTypeSchemaOverride-recordType"></a>
The record type these fields apply to.
Type: String
Valid Values: `MCP | AGENT | CUSTOM | SKILL | GATEWAY`
Required: Yes

 ** schema **   <a name="agentregistrycontrol-Type-RecordTypeSchemaOverride-schema"></a>
A JSON Schema with the fields for this record type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: Yes

## See Also
<a name="API_RecordTypeSchemaOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RecordTypeSchemaOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RecordTypeSchemaOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RecordTypeSchemaOverride)
