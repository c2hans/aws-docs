---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/robust-network-design-control-tower/decentralized-dns.html
---

# Decentralized DNS and Route 53 Profiles
<a name="decentralized-dns"></a>

In a decentralized DNS architecture, organizations create private hosted zones within their respective AWS accounts and directly associate the necessary VPCs. This approach provides the following benefits:
+ Isolation of control
+ Reduced scope in the event of an incident
+ Enhanced operational flexibility, because teams can independently manage their hosted zones and associated VPCs without relying on a centralized authority

## Route 53 Profiles
<a name="route-53-profiles"></a>

Route 53 Profiles streamline the management and sharing of hosted zones, Resolver forwarding rules, and Route 53 DNS firewall rules across different AWS accounts. By managing these resources from a single source, you reduce operational overhead.

You can also associate a hosted zone from other accounts. For example, if you need to configure a private hosted zone that points to your on-premises server, you can create the private hosted zone in a single AWS account and associate it with a Route 53 Profile. If the same hosted zone configuration is required in another account, you can share the Profile with that account and associate the necessary VPCs. This ensures the DNS resolution is handled across multiple accounts without the need to duplicate the hosted zone setup in each account.

The following diagram shows a Route 53 Profile sharing AWS Resource Access Manager (AWS RAM) configuration. Route 53 Profiles can be shared with a single account, an AWS Organizations organizational unit, or across your entire organization.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/robust-network-design-control-tower/images/guide-img/734c65f3-3001-4321-a428-6ffbda3b44b0/images/5d317e49-b056-4121-8c8e-fd7cccaa7a51.png)

The diagram shows the following workflow:

1. The Route 53 Profile is shared from account A to account B.

**Note**
When working with decentralized DNS and Route 53 Profiles, we recommend avoiding duplication of same hosted zone configuration across accounts or VPCs.
