---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/integrate-third-party-services/architecture-3-1.html
---

# Architecture 3.1: Transit Gateway with AWS RAM
<a name="architecture-3-1"></a>

[AWS Resource Access Manager (AWS RAM)](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) helps you share specified AWS resources you own with other AWS accounts. It's a centralized service that provides a consistent experience for sharing different types of AWS resources across multiple accounts. A transit gateway can be shared across accounts with AWS RAM, even if the accounts are in different organizations in AWS Organizations.

Only the transit gateway owner can perform the following operations in AWS RAM:
+ Create a resource share.
+ Update a resource share.
+ View a resource share.
+ View the resources that are shared by your account, across all resource shares.
+ View the principals with whom you are sharing your resources, across all resource shares. This helps you determine who has access to your shared resources.
+ Delete a resource share.
+ Run all APIs for the transit gateway, transit gateway attachments, and transit gateway route tables.

In AWS RAM, your account is the *sharer*, and the third-party account is the *acceptor*. An acceptor cannot create, modify, or delete the transit gateway route tables or their propagations and associations. This configuration gives you, as the owner of the shared transit gateway, a large amount of control and a high level of visibility into its configuration. As a result, third-party service providers might not accept this option because they would have minimal control over the configuration of the transit gateway.

The following architecture diagram shows how you use AWS RAM to share a transit gateway with the third-party service provider. For security, you create a new transit gateway in your account. You connect the new transit gateway to the third-party's VPCs. You use a peering connection to connect the new transit gateway to an existing transit gateway in your account, which is attached to your VPCs. You enable appliance mode on the new transit gateway in order connect with the elastic network interface in the inspection VPC. For more information about the inspection VPC, see [Centralizing network inspection](architecture-3.md#centralized-network-inspection).

![Sharing a transit gateway in your account with a third party by using AWS RAM.](http://docs.aws.amazon.com/prescriptive-guidance/latest/integrate-third-party-services/images/guide-img/80f3a808-d645-486e-82c4-f574fdcf6710/images/004e8c07-7b07-4357-8406-9e6275f4649d.png)
