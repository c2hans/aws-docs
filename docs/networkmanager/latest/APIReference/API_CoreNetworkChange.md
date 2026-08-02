---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CoreNetworkChange.html
---

# CoreNetworkChange
<a name="API_CoreNetworkChange"></a>

Details describing a core network change.

## Contents
<a name="API_CoreNetworkChange_Contents"></a>

 ** Action **   <a name="networkmanager-Type-CoreNetworkChange-Action"></a>
The action to take for a core network.
Type: String
Valid Values: `ADD | MODIFY | REMOVE`
Required: No

 ** Identifier **   <a name="networkmanager-Type-CoreNetworkChange-Identifier"></a>
The resource identifier.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** IdentifierPath **   <a name="networkmanager-Type-CoreNetworkChange-IdentifierPath"></a>
Uniquely identifies the path for a change within the changeset. For example, the `IdentifierPath` for a core network segment change might be `"CORE_NETWORK_SEGMENT/us-east-1/devsegment"`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** NewValues **   <a name="networkmanager-Type-CoreNetworkChange-NewValues"></a>
The new value for a core network
Type: [CoreNetworkChangeValues](API_CoreNetworkChangeValues.md) object
Required: No

 ** PreviousValues **   <a name="networkmanager-Type-CoreNetworkChange-PreviousValues"></a>
The previous values for a core network.
Type: [CoreNetworkChangeValues](API_CoreNetworkChangeValues.md) object
Required: No

 ** Type **   <a name="networkmanager-Type-CoreNetworkChange-Type"></a>
The type of change.
Type: String
Valid Values: `CORE_NETWORK_SEGMENT | NETWORK_FUNCTION_GROUP | CORE_NETWORK_EDGE | ATTACHMENT_MAPPING | ATTACHMENT_ROUTE_PROPAGATION | ATTACHMENT_ROUTE_STATIC | ROUTING_POLICY | ROUTING_POLICY_SEGMENT_ASSOCIATION | ROUTING_POLICY_EDGE_ASSOCIATION | ROUTING_POLICY_ATTACHMENT_ASSOCIATION | CORE_NETWORK_CONFIGURATION | SEGMENTS_CONFIGURATION | SEGMENT_ACTIONS_CONFIGURATION | ATTACHMENT_POLICIES_CONFIGURATION`
Required: No

## See Also
<a name="API_CoreNetworkChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkChange)
