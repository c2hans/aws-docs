---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_MatterEndpoint.html
---

# MatterEndpoint
<a name="API_MatterEndpoint"></a>

Structure describing a managed thing.

## Contents
<a name="API_MatterEndpoint_Contents"></a>

 ** clusters **   <a name="managedintegrations-Type-MatterEndpoint-clusters"></a>
A list of Matter clusters for a managed thing.
Type: Array of [MatterCluster](API_MatterCluster.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** id **   <a name="managedintegrations-Type-MatterEndpoint-id"></a>
The Matter endpoint id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`
Required: No

## See Also
<a name="API_MatterEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/MatterEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/MatterEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/MatterEndpoint)
