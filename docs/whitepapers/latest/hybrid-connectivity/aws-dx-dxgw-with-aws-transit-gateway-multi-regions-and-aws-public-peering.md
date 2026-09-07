---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/aws-dx-dxgw-with-aws-transit-gateway-multi-regions-and-aws-public-peering.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS DX – DXGW with AWS Transit Gateway, Multi-Regions, and AWS Public Peering
<a name="aws-dx-dxgw-with-aws-transit-gateway-multi-regions-and-aws-public-peering"></a>

** This model is constructed of: **
+  Multiple AWS Regions.
+  Dual AWS Direct Connect Connections to independent DX locations.
+  Single on-premises data center with dual connections to AWS.
+  AWS DXGW with AWS Transit Gateway.
+  High scale of VPCs per Region.

![Diagram showing AWS DX – DXGW with AWS Transit Gateway, Multi-Regions, and AWS Public VIF](https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/images/dxgw-with-tg-multi-region-public-peering.png)

 **Connectivity model attributes:**
+  AWS DX public VIF is used to access AWS public resources such as S3 directly over the AWS DX connections.
+  Provide the ability to connect to VPCs and/or DX connections in other Regions in the future.
+  With AWS Transit Gateway connected to VPCs, full or partial mesh connectivity can be achieved between the VPCs.
+  Inter-VPC and Inter-Region VPC communication facilitated by AWS Transit Gateway peering.
+  Offers flexible design options to integrate third-party security and SDWAN virtual appliances with AWS Transit Gateway. See: [Centralized network security for VPC-to-VPC and on-premises to VPC traffic](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-network-security-for-vpc-to-vpc-and-on-premises-to-vpc-traffic.html).

 **Scale considerations:**
+  The number of routes to and from AWS Transit Gateway is limited to the maximum supported number of routes over a Transit VIF (inbound and outbound numbers vary). Refer to the [AWS Direct Connect quotas](https://docs.aws.amazon.com/directconnect/latest/UserGuide/limits.html) for more information about the scale limits and supported number of routes and VIFs.
+  Scale up to thousands of VPCs per AWS Transit Gateway over a single BGP session.
+  Single Transit VIF per AWS DX.
+  Additional AWS DX connections can be added as desired.

 **Other considerations:**
+  Incurs additional AWS Transit Gateway processing costs for data transfer between AWS and on-premises site.
+  Security groups of a remote VPC cannot be referenced by AWS Transit Gateway (need VPC peering).
+  VPC peering can be use instead of AWS Transit Gateway to facilitate the communication between the VPCs, however, this will add operational complexity to build and manage large number VPC point-to-point peering at scale.
