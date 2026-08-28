---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/aws-hybrid-connectivity-services.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS hybrid connectivity services
<a name="aws-hybrid-connectivity-services"></a>

 AWS hybrid connectivity services provide highly scalable, highly available networking components. They play an essential role in building hybrid networking solutions. At the time of this whitepaper writing, there are three primary service endpoints:
+  **AWS Virtual Private Gateway (VGW)** is a regional, highly redundant service that provides IP routing and forwarding at the VPC level, acting as the gateway for the VPC to communicate with your customer gateway devices. VGW can terminate AWS S2S VPN connections and AWS Direct Connect Private VIFs.
+  **AWS Transit Gateway** (**TGW)** is a regional, highly available and scalable service that enables you to connect multiple VPCs with each other, as well as your on-premises networks over Site-to-Site VPN and/or Direct Connect using a single centralized gateway. Conceptually, an AWS Transit Gateway acts as a highly available and redundant virtual cloud router. AWS Transit Gateway supports equal cost multi-path (ECMP) routing over multiple Direct Connect connections, VPN tunnels, or TGW Connect peers. Transit Gateways can peer to each other, both in the same region and cross-region, allowing their connected resources to communicate over the peering links. For more details, see [AWS Transit Gateway scenarios](https://docs.aws.amazon.com/vpc/latest/tgw/TGW_Scenarios.html).
+  **AWS Cloud WAN** provides a central dashboard for making connections between your branch offices, data centers, and Amazon VPCs—building a global network with only a few clicks. You use network policies to automate network management and security tasks in one location. For more details, see the [AWS Cloud WAN documentation](https://docs.aws.amazon.com/vpc/latest/cloudwan/what-is-cloudwan.html).
+  **Direct Connect Gateway (DXGW)** is a globally available service that distributes routing information across its connections, behaving similarly to BGP route reflectors in a traditional network. Data does not pass through a DXGW – it only handles the routing information. You can create a DXGW in any AWS Region and access it from all other AWS Regions. You can connect Direct Connect VIFs to a DXGW, then associate the DXGW with either VGWs (using private VIFs) or an AWS Transit Gateway (using transit VIFs). See [Direct Connect gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html) for more information. You do not need to create multiple DXGWs for redundancy as it is a globally availability service. However, you might choose to use multiple DXGWs to separate routing domains, for example, a production and a testing network you want to keep completely isolated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
