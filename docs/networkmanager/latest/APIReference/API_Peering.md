---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_Peering.html
---

# Peering
<a name="API_Peering"></a>

Describes a peering connection.

## Contents
<a name="API_Peering_Contents"></a>

 ** CoreNetworkArn **   <a name="networkmanager-Type-Peering-CoreNetworkArn"></a>
The ARN of a core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

 ** CoreNetworkId **   <a name="networkmanager-Type-Peering-CoreNetworkId"></a>
The ID of the core network for the peering request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: No

 ** CreatedAt **   <a name="networkmanager-Type-Peering-CreatedAt"></a>
The timestamp when the attachment peer was created.
Type: Timestamp
Required: No

 ** EdgeLocation **   <a name="networkmanager-Type-Peering-EdgeLocation"></a>
The edge location for the peer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** LastModificationErrors **   <a name="networkmanager-Type-Peering-LastModificationErrors"></a>
Describes the error associated with the Connect peer request.
Type: Array of [PeeringError](API_PeeringError.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** OwnerAccountId **   <a name="networkmanager-Type-Peering-OwnerAccountId"></a>
The ID of the account owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[\s\S]*`
Required: No

 ** PeeringId **   <a name="networkmanager-Type-Peering-PeeringId"></a>
The ID of the peering attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^peering-([0-9a-f]{8,17})$`
Required: No

 ** PeeringType **   <a name="networkmanager-Type-Peering-PeeringType"></a>
The type of peering. This will be `TRANSIT_GATEWAY`.
Type: String
Valid Values: `TRANSIT_GATEWAY`
Required: No

 ** ResourceArn **   <a name="networkmanager-Type-Peering-ResourceArn"></a>
The resource ARN of the peer.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1500.
Pattern: `[\s\S]*`
Required: No

 ** State **   <a name="networkmanager-Type-Peering-State"></a>
The current state of the peering connection.
Type: String
Valid Values: `CREATING | FAILED | AVAILABLE | DELETING`
Required: No

 ** Tags **   <a name="networkmanager-Type-Peering-Tags"></a>
The list of key-value tags associated with the peering.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_Peering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Peering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Peering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Peering)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
