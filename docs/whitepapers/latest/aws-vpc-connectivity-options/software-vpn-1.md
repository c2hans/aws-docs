---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/software-vpn-1.html
---

# Software VPN
<a name="software-vpn-1"></a>

 Amazon VPC provides network routing flexibility. This includes the ability to create secure VPN tunnels between two or more software VPN appliances to connect multiple VPCs into a larger virtual private network so that instances in each VPC can seamlessly connect to each other using private IP addresses. This option is recommended when you want to manage both ends of the VPN connection using your preferred VPN software provider. This option uses an internet gateway attached to each VPC to facilitate communication between the software VPN appliances.

![Diagram showing an internet gateway attached to each VPC.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/software-site-to-site-vpn-vpc-to-vpc-routing.png)

 You can choose from an ecosystem of multiple partners and open source communities that have produced software VPN appliances that run on Amazon EC2. Along with this choice comes the responsibility for you to manage the software appliance including configuration, patches, and upgrades.

 Note that this design introduces a potential single point of failure into the network design as the software VPN appliance runs on a single Amazon EC2 instance. For additional information, see [Appendix A: High-Level HA architecture for software VPN instances](appendix-a-high-level-ha-architecture-for-software-vpn-instances.md).

## Additional resources
<a name="additional-resources-10"></a>
+  [VPN appliances available from the AWS Marketplace](https://aws.amazon.com/marketplace/search/results/ref%3Dbrs_navgno_search_box?searchTerms=vpn)
+  [Tech Brief - Connecting Multiple VPCs with EC2 Instances (IPsec)](https://aws.amazon.com/articles/5472675506466066)
+  [Tech Brief - Connecting Multiple VPCs with EC2 Instances (SSL)](https://aws.amazon.com/articles/0639686206802544)
