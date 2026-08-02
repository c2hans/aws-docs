---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/software-vpn.html
---

# Software VPN
<a name="software-vpn"></a>

 Amazon VPC offers you the flexibility to fully manage both sides of your Amazon VPC connectivity by creating a VPN connection between your remote network and a software VPN appliance running in your Amazon VPC network. This option is recommended if you must manage both ends of the VPN connection, either for compliance purposes or for leveraging gateway devices that are not currently supported by Amazon VPC’s VPN solution. The following figure shows this option.

![AWS Cloud VPC with public and private subnets connecting to customer network via VPN.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/software-site-to-site-vpn.png)

* Software Site-to-Site VPN *

 You can choose from an ecosystem of multiple partners and open-source communities that have produced software VPN appliances that run on Amazon EC2. Along with this choice comes the responsibility that you must manage the software appliance, including configuration, patches, and upgrades.

 Note that this design introduces a potential single point of failure into the network design because the software VPN appliance runs on a single Amazon EC2 instance. For additional information, see [Appendix A: High-Level HA architecture for software VPN instances](appendix-a-high-level-ha-architecture-for-software-vpn-instances.md) Architecture for Software VPN Instances.

## Additional resources
<a name="additional-resources-8"></a>
+  [VPN appliances available in the AWS Marketplace](https://aws.amazon.com/marketplace/search/results/ref%3Dbrs_navgno_search_box?searchTerms=vpn)
+  [Tech Brief - Connecting Cisco ASA to VPC EC2 Instance (IPsec)](https://aws.amazon.com/articles/8800869755706543)
+  [Tech Brief - Connecting Multiple VPCs with EC2 Instances (IPsec)](https://aws.amazon.com/articles/5472675506466066)
+  [Tech Brief - Connecting Multiple VPCs with EC2 Instances (SSL)](https://aws.amazon.com/articles/0639686206802544)
