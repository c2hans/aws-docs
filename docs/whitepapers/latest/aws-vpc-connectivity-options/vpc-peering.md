---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/vpc-peering.html
---

# VPC peering
<a name="vpc-peering"></a>

 A VPC peering connection is a networking connection between two VPCs that enables routing using each VPC’s private IP addresses as if they were in the same network. VPC peering connections can be created between your own VPCs or with a VPC in another AWS account. VPC peering also supports inter-region peering.

 Traffic using inter-region VPC Peering always stays on the global AWS backbone and never traverses the public internet, thereby reducing threat vectors, such as common exploits and DDoS attacks.

![Diagram that shows VPC-to-VPC Peering](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/vpc-to-vpc-peering.png)

 AWS uses the existing infrastructure of a VPC to create VPC peering connections and does not rely on a separate piece of physical hardware. Therefore, they do not introduce a potential single point of failure or network bandwidth bottleneck between VPCs. Additionally, VPC routing tables, security groups, and network access control lists can be leveraged to control which subnets or instances are able to utilize the VPC peering connection.

 Amazon VPCs do not support transitive peering, meaning that you can’t communicate two VPCs that are not directly peered using a third VPC as transit. If you want all of your VPCs to communicate with each other using VPC peering, you will need to create 1:1 VPC peering connections between each of them. Alternatively, you can use AWS Transit Gateway or AWS Cloud WAN to act as a network transit hub.

 Both IPv4 and IPv6 traffic is supported in VPC peering connections. However, two VPCs cannot be peered if their primary IPv4 CIDR block overlaps, regardless of the secondary IPv4 or IPv6 CIDR blocks used. Take this into account when assigning the primary CIDR block to your VPCs if you plan to use VPC peering between them.

## Additional resources
<a name="additional-resources-8"></a>
+  [Amazon VPC peering](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-peering.html)
+  [What is VPC peering?](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html)
