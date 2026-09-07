---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/aws-dx-dxgw-with-aws-transit-gateway-multi-regions-more-than-3.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS DX – DXGW with AWS Transit Gateway, Multi-Regions (more than 3)
<a name="aws-dx-dxgw-with-aws-transit-gateway-multi-regions-more-than-3"></a>

 **This model is constructed of:**
+  Multiple AWS Regions (more than 3).
+  Dual on-premises data centers.
+  Dual AWS Direct Connect Connections across to independent DX locations per Region.
+  AWS DXGW with AWS Transit Gateway.
+  High scale of VPCs per Region.
+  Full mesh of peering between AWS Transit Gateways.

![Diagram showing AWS DX – DXGW with AWS Transit Gateway, Multi-Regions (more than three)](https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/images/dxgw-with-tg-multi-region.png)

 **Connectivity model attributes:**
+  Lowest operational overhead.
+  AWS DX public VIF is used to access AWS public resources, such as S3, directly over the AWS DX connections.
+  Provide the ability to connect to VPCs and DX connections in other Regions in the future.
+  With AWS Transit Gateway connected to VPCs, full or partial mesh connectivity can be achieved between the VPCs.
+  Inter-Region VPC communication is facilitated by AWS Transit Gateway peering.
+  Offers flexible design options to integrate third-party security and SDWAN virtual appliances with AWS Transit Gateway. See: [Centralized network security for VPC-to-VPC and on-premises to VPC traffic](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-network-security-for-vpc-to-vpc-and-on-premises-to-vpc-traffic.html).

 **Scale considerations:**
+  The number of routes to and from AWS Transit Gateway is limited to the maximum supported number of routes over a Transit VIF (inbound and outbound numbers vary). Refer to the [AWS Direct Connect quotas](https://docs.aws.amazon.com/directconnect/latest/UserGuide/limits.html) for more information about the scale limits. Consider route summarization if needed to reduce the number of routes.
+  Scale up to thousands of VPCs per AWS Transit Gateway over a single BGP session per DXGW (assuming the provided performance by the provisioned AWS DX connections is sufficient).
+  Up to six AWS Transit Gateways can be connected per DXGW.
+  If more than three Regions need to be connected using AWS Transit Gateway, then additional DXGWs are required.
+  Single Transit VIF per AWS DX.
+  Additional AWS DX connections can be added as desired.

 **Other considerations:**
+  Incurs additional AWS Transit Gateway processing cost for data transfer between the on-premises site and AWS.
+  Security groups of a remote VPC cannot be referenced by AWS Transit Gateway (need VPC peering).
+  VPC peering can be used instead of AWS Transit Gateway to facilitate the communication between the VPCs, however, this will add operational complexity to build and manage large number VPC point-to-point peering at scale.

 The following decision tree covers the scalability and communication model considerations:

![Diagram showing scalability and communication model decision tree](https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/images/scalability-communication-model-decision-tree.png)

**Note**
If the selected connection type is VPN, typically at the performance consideration, the decision should be made whether the VPN termination point is AWS VGW or AWS Transit Gateway AWS S2S VPN connection. If not made yet, then you can consider the required communication model between the VPC along with the number of required VPC to be connected to the VPN connection(s) to help you make the decision.
