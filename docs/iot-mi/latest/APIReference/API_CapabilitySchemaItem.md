---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CapabilitySchemaItem.html
---

# CapabilitySchemaItem
<a name="API_CapabilitySchemaItem"></a>

Structure representing a capability schema item that defines the functionality and features supported by a managed thing.

## Contents
<a name="API_CapabilitySchemaItem_Contents"></a>

 ** CapabilityId **   <a name="managedintegrations-Type-CapabilitySchemaItem-CapabilityId"></a>
The unique identifier of the capability defined in the schema.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 128.
Pattern: `[a-zA-Z0-9.]+@(\d+\.\d+(\.\d+)?|\$latest)`
Required: Yes

 ** ExtrinsicId **   <a name="managedintegrations-Type-CapabilitySchemaItem-ExtrinsicId"></a>
The external identifier for the capability, used when referencing the capability outside of the AWS ecosystem.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `0[xX][0-9a-fA-F]+$|^[0-9]+`
Required: Yes

 ** ExtrinsicVersion **   <a name="managedintegrations-Type-CapabilitySchemaItem-ExtrinsicVersion"></a>
The version of the external capability definition, used to track compatibility with external systems.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: Yes

 ** Format **   <a name="managedintegrations-Type-CapabilitySchemaItem-Format"></a>
The format of the capability schema, which defines how the schema is structured and interpreted.
Type: String
Valid Values: `AWS | ZCL | CONNECTOR`
Required: Yes

 ** Schema **   <a name="managedintegrations-Type-CapabilitySchemaItem-Schema"></a>
The actual schema definition that describes the capability's properties, actions, and events.
Type: JSON value
Required: Yes

## See Also
<a name="API_CapabilitySchemaItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CapabilitySchemaItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CapabilitySchemaItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CapabilitySchemaItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
