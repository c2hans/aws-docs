---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/software-vpn-to-aws-site-to-site-vpn.html
---

# Software VPN-to-AWS Site-to-Site VPN
<a name="software-vpn-to-aws-site-to-site-vpn"></a>

 Amazon VPC provides the flexibility to combine the AWS managed VPN and software VPN options to connect multiple VPCs. With this design, you can create secure VPN tunnels between a software VPN appliance and a virtual private gateway, allowing instances in each VPC to seamlessly connect to each other using private IP addresses. This option uses a virtual private gateway in one Amazon VPC and a combination of an internet gateway and software VPN appliance in another Amazon VPC, as shown in the following figure.

![Diagram that shows software VPN to AWS Site-to-Site VPN VPC-to-VPC Routing.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/software-vpn-to-site-to-site-vpn-vpc-routing.png)

 Note that this design introduces a potential single point of failure into the network design. For additional information, see [Appendix A: High-Level HA architecture for software VPN instances](appendix-a-high-level-ha-architecture-for-software-vpn-instances.md).

## Additional resources
<a name="additional-resources-11"></a>
+  [VPN appliances available from the AWS Marketplace](https://aws.amazon.com/marketplace/search/results/ref%3Dbrs_navgno_search_box?searchTerms=vpn)
+  [AWS Site-to-Site VPN User Guide](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
+  [Requirements for customer gateway devices](https://docs.aws.amazon.com/vpc/latest/adminguide/Introduction.html#CGRequirements)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
