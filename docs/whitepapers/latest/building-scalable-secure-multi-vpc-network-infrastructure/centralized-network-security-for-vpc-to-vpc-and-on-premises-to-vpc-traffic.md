---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-network-security-for-vpc-to-vpc-and-on-premises-to-vpc-traffic.html
---

# Centralized network security for VPC-to-VPC and on-premises to VPC traffic
<a name="centralized-network-security-for-vpc-to-vpc-and-on-premises-to-vpc-traffic"></a>

There might be scenarios where a customer wants to implement a layer 3-7 ﬁrewall/IPS/IDS within their multi-account environment to inspect traﬃc ﬂows between VPCs (east-west traffic) or between an on-premises data center and a VPC (north-south traffic). This can be achieved diﬀerent ways, depending on use case and requirements. For example, you could incorporate the Gateway Load Balancer, Network Firewall, Transit VPC, or use centralized architectures with Transit Gateways. These scenarios are discussed in the following section.

## Considerations using a centralized network security inspection model
<a name="considerations-using-cnsim"></a>

To reduce costs, you should be selective in what traffic passes via your AWS Network Firewall or Gateway Load Balancer. One way to proceed is to define security zones and inspect traffic between untrusted zones. An untrusted zone can be a remote site managed by a third party, a vendor VPC you don’t control/trust, or a sandbox/dev VPC, which has more relaxed security rules compared to rest of your environment. There are four zones in this example:
+ **Untrusted Zone** — This is for any traffic coming from the ‘VPN to remote untrusted site’ or the third-party vendor VPC.
+ **Production (Prod) Zone** — This contains traffic from the production VPC and on-premises customer DC.
+ **Development (Dev) Zone** —This contains traffic from the two development VPCs.
+ **Security (Sec) Zone** — Contains our firewall components Network Firewall or Gateway Load Balancer.

This setup has four security zones, but you might have more. You can use multiple route tables and blackhole routes to achieve security isolation and optimal traffic flow. Choosing the right set of zones is dependent on your overall Landing Zone design strategy (account structure, VPC design). You can have zones to enable isolation between Business Units (BUs), applications, environments, and so on.

If you want to inspect and filter your VPC-to-VPC, inter-zone traffic, and VPC-on-premises traffic, you can incorporate AWS Network Firewall with Transit Gateway in your centralized architecture. By having the hub-and-spoke model of the AWS Transit Gateway, a centralized deployment model can be achieved. The AWS Network Firewall is deployed in a separate security VPC. A separate security VPC provides a simplified and central approach to manage inspection. Such a VPC architecture gives AWS Network Firewall source and destination IP visibility. Both source and destination IPs are preserved. This security VPC consists of two subnets in each Availability Zone; where one subnet is a dedicated to AWS Transit Gateway attachment and the other subnet is dedicated to the firewall endpoint. The subnets in this VPC should only contain AWS Network Firewall endpoints because Network Firewall can't inspect traffic in the same subnets as the endpoints. When you use Network Firewall to centrally inspect traffic, it can perform deep packet inspection (DPI) on ingress traffic. The DPI pattern is expanded upon in the *Centralized Inbound Inspection* section of this paper.

![A diagram depicting VPC-to-VPC and on-premises to VPC traffic inspection using Transit Gateway and AWS Network Firewall (route table design)](http://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/vpc-traffic-inspection.png)

In the centralized architecture with inspection, the Transit Gateway subnets require a separate VPC route table to ensure the traffic is forwarded to firewall endpoint within the same Availability Zone. For the return traffic, a single VPC route table containing a default route towards the Transit Gateway is configured. Traffic is returned to AWS Transit Gateway in the same Availability Zone after it has been inspected by AWS Network Firewall. This is possible due to the appliance mode feature of the Transit Gateway. The appliance mode feature of the Transit Gateway also helps the AWS Network Firewall to have stateful traffic inspection capability inside the security VPC.

With the appliance mode enabled on a transit gateway, it selects a single network interface using flow hash algorithm for the entire life of the connection. The transit gateway uses the same network interface for the return traffic. This ensures that bidirectional traffic is routed symmetrically—it's routed through the same Availability Zone in the VPC attachment for the life of the flow. For more information on appliance mode, refer to [Stateful appliances and appliance mode](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-appliance-scenario.html#transit-gateway-appliance-support) in the Amazon VPC documentation.

For different deployment options of security VPC with AWS Network Firewall and Transit Gateway, refer to the [Deployment models for AWS Network Firewall](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/) blog post.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
