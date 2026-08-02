---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/integrate-third-party-services/architecture-3-2.html
---

# Architecture 3.2: Transit Gateway peering
<a name="architecture-3-2"></a>

In this configuration, you deploy two transit gateways, one in your account and another in the third-party account, and you attach them with a peering connection. Because the peering attachment supports static routing, you can associate a route table to the peering attachment, and you can point routes in the transit gateway route tables to the peering attachment route table. This routes traffic between the peered transit gateways.

Because transit gateway peering can be in the same or different AWS Regions, you can now directly peer your transit gateway to a third-party transit gateway and provide connectivity between networks in the same Region.

Compared to the previous option, this configuration gives you less control and visibility over the peered transit gateway deployed in the third-party account. However, this configuration delegates the responsibility of managing VPC attachments to the third party. Third parties might be more accepting of this option because it provides them more control.

The following architecture diagram shows how you create a peering connection between two transit gateways, one new transit gateway in your account and a transit gateway in the third-party account. The third party is responsible for attaching their VPCs to their transit gateway. You also use a peering connection to attach the new transit gateway in your account with an existing transit gateway, which is attached to your VPCs. You enable appliance mode on the new transit gateway in order connect with the elastic network interface in the inspection VPC. For more information about the inspection VPC, see [Centralizing network inspection](architecture-3.md#centralized-network-inspection).

![Creating a peering connection between transit gateways in different AWS accounts.](http://docs.aws.amazon.com/prescriptive-guidance/latest/integrate-third-party-services/images/guide-img/80f3a808-d645-486e-82c4-f574fdcf6710/images/b7d5cb4d-804b-4b8c-ac56-f5f188b9a8d5.png)
