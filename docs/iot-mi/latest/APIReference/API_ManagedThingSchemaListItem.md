---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ManagedThingSchemaListItem.html
---

# ManagedThingSchemaListItem
<a name="API_ManagedThingSchemaListItem"></a>

Structure representing one schema item associated with a managed thing.

## Contents
<a name="API_ManagedThingSchemaListItem_Contents"></a>

 ** CapabilityId **   <a name="managedintegrations-Type-ManagedThingSchemaListItem-CapabilityId"></a>
The id of the capability for a managed thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9./]+(@\d+\.\d+)?`
Required: No

 ** EndpointId **   <a name="managedintegrations-Type-ManagedThingSchemaListItem-EndpointId"></a>
The id of the endpoint for a managed thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`
Required: No

 ** Schema **   <a name="managedintegrations-Type-ManagedThingSchemaListItem-Schema"></a>
The validation schema for one schema item associated with a managed thing.
Type: JSON value
Required: No

## See Also
<a name="API_ManagedThingSchemaListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ManagedThingSchemaListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ManagedThingSchemaListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ManagedThingSchemaListItem)
