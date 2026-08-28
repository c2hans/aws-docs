---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-vpn-cloudhub.html
---

# Site-to-Site VPN CloudHub
<a name="aws-vpn-cloudhub"></a>

 Building on the AWS managed VPN options described previously, you can securely communicate from one site to another using the Site-to-Site VPN CloudHub. The Site-to-Site VPN CloudHub operates on a simple hub-and-spoke model that you can use with or without a VPC. Use this approach if you have multiple branch offices and existing internet connections and would like to implement a convenient, potentially low-cost hub-and-spoke model for primary or backup connectivity between these remote offices.

 The following figure shows the Site-to-Site VPN CloudHub architecture, with lines indicating network traffic between remote sites being routed over their Site-to-Site VPN connections.

![VPC with EC2 instances connecting through Virtual Private Gateway to multiple customer networks via IPsec VPN.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/aws-vpn-cloudhub.png)

* Site-to-Site VPN CloudHub *

 Site-to-Site VPN CloudHub uses an Amazon VPC virtual private gateway with multiple customer gateways, each using unique BGP autonomous system numbers (ASNs). The remote sites must not have overlapping IP ranges. Your gateways advertise the appropriate routes (BGP prefixes) over their VPN connections. These routing advertisements are received and re-advertised to each BGP peer so that each site can send data to and receive data from the other sites.

## Additional resources
<a name="additional-resources-6"></a>
+  [Providing secure communication between sites using VPN CloudHub](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPN_CloudHub.html)
+  [AWS Site-to-Site VPN User Guide](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
+  [Requirements for customer gateway devices](https://docs.aws.amazon.com/vpc/latest/adminguide/Introduction.html#CGRequirements)
+  [Customer gateway devices tested with Amazon VPC](https://docs.aws.amazon.com/vpc/latest/adminguide/Introduction.html#DevicesTested)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
