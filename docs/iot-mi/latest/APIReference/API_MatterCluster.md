---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_MatterCluster.html
---

# MatterCluster
<a name="API_MatterCluster"></a>

Describe a Matter cluster with an id, and the relevant attributes, commands, and events.

## Contents
<a name="API_MatterCluster_Contents"></a>

 ** attributes **   <a name="managedintegrations-Type-MatterCluster-attributes"></a>
The Matter attributes.
Type: JSON value
Required: No

 ** commands **   <a name="managedintegrations-Type-MatterCluster-commands"></a>
Describe the Matter commands with the Matter command identifier mapped to the command fields.
Type: String to JSON value map
Map Entries: Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 24.
Key Pattern: `0[xX][0-9a-fA-F]+$|^[0-9]+`
Required: No

 ** events **   <a name="managedintegrations-Type-MatterCluster-events"></a>
Describe the Matter events with the Matter event identifier mapped to the event fields.
Type: String to JSON value map
Map Entries: Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 24.
Key Pattern: `0[xX][0-9a-fA-F]+$|^[0-9]+`
Required: No

 ** id **   <a name="managedintegrations-Type-MatterCluster-id"></a>
The cluster id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `0[xX][0-9a-fA-F]+$|^[0-9]+`
Required: No

## See Also
<a name="API_MatterCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/MatterCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/MatterCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/MatterCluster)
