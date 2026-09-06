---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/transit-vpc-option.html
---

# Transit VPC
<a name="transit-vpc-option"></a>

 Building on the Software VPN designs mentioned above, you can create a global transit network on AWS. A transit VPC is a common strategy for connecting multiple, geographically dispersed VPCs and remote networks in order to create a global network transit center. A transit VPC simplifies network management and minimizes the number of connections required to connect multiple VPCs and remote networks. The following figure illustrates this design.

![Diagram showing a transit VPC structure.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/transit-vpc.png)

 Along with providing direct network routing between VPCs and on-premises networks, this design also enables the transit VPC to implement more complex routing rules, such as network address translation between overlapping network ranges, or to add additional network-level packet filtering or inspection. The transit VPC design can be used to support important use cases like, private networking, shared connectivity and cross account AWS usage.

## Additional resources
<a name="additional-resources-16"></a>
+  [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/)
+  [Cisco Catalyst 8000V for SD-WAN & Routing](https://aws.amazon.com/marketplace/pp/prodview-rohvq2cjd4ccg) in AWS Marketplace
