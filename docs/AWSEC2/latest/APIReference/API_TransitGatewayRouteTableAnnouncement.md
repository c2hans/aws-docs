---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayRouteTableAnnouncement.html
---

# TransitGatewayRouteTableAnnouncement
<a name="API_TransitGatewayRouteTableAnnouncement"></a>

Describes a transit gateway route table announcement.

## Contents
<a name="API_TransitGatewayRouteTableAnnouncement_Contents"></a>

 ** announcementDirection **
The direction for the route table announcement.
Type: String
Valid Values: `outgoing | incoming`
Required: No

 ** coreNetworkId **
The ID of the core network for the transit gateway route table announcement.
Type: String
Required: No

 ** creationTime **
The timestamp when the transit gateway route table announcement was created.
Type: Timestamp
Required: No

 ** peerCoreNetworkId **
The ID of the core network ID for the peer.
Type: String
Required: No

 ** peeringAttachmentId **
The ID of the peering attachment.
Type: String
Required: No

 ** peerTransitGatewayId **
The ID of the peer transit gateway.
Type: String
Required: No

 ** state **
The state of the transit gateway announcement.
Type: String
Valid Values: `available | pending | failing | failed | deleting | deleted`
Required: No

 ** TagSet.N **
The key-value pairs associated with the route table announcement.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** transitGatewayId **
The ID of the transit gateway.
Type: String
Required: No

 ** transitGatewayRouteTableAnnouncementId **
The ID of the transit gateway route table announcement.
Type: String
Required: No

 ** transitGatewayRouteTableId **
The ID of the transit gateway route table.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayRouteTableAnnouncement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayRouteTableAnnouncement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayRouteTableAnnouncement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayRouteTableAnnouncement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
