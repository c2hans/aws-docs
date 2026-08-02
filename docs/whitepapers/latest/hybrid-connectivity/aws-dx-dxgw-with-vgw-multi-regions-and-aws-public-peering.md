---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/aws-dx-dxgw-with-vgw-multi-regions-and-aws-public-peering.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS DX – DXGW with VGW, Multi-Regions, and AWS Public Peering
<a name="aws-dx-dxgw-with-vgw-multi-regions-and-aws-public-peering"></a>

** This model is constructed of: **
+ Multiple on-premises data centers with dual connections to AWS.
+  Dual AWS Direct Connect Connections to independent DX locations.
+  AWS DXGW directly attached to more than 10 VPCs using VGW, up to 20 VPCs using VGW.
+  Optional usage of AWS Transit Gateway for Inter-VPC and Inter-Region communication.

![Diagram showing AWS DX – DXGW with VGW, Multi-Regions, and Public VIF](http://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/images/dxgw-with-vgw-multi-region-public-vif.png)

 **Connectivity model attributes:**
+ AWS DXGW directly attached to more than 10 VPCs using VGW up to 20 VPCs using VGW.
+  AWS DX public VIF is used to access AWS public services, such as Amazon S3, directly over the AWS DX connections.
+  Provide the ability to connect to VPCs and DX connections in other Regions in the future.
+  Inter-VPC and Inter-Region VPC communication facilitated by AWS Transit Gateway and Transit Gateway peering.

 **Scale considerations:**

 Reference [AWS Direct Connect quotas](https://docs.aws.amazon.com/directconnect/latest/UserGuide/limits.html) for more information about other scale limits, such as such number of supported prefixes, number of VIFs per DX connection type (dedicated, hosted). Some key considerations:
+  The BGP session for a private VIF can advertise up to 100 routes each for IPv4 and IPv6.
+  Up to 20 VPCs can be connected per DXGW over a single BGP session on each private VIF, up to 30 private VIFs per DXGW.
+  Additional AWS Direct Connects can be added as desired.

 **Other considerations:**
+  Does not incur AWS Transit Gateway related processing cost for data transfer between AWS and on-premises networks.
+  Security groups of a remote VPC cannot be referenced by AWS Transit Gateway (need VPC peering).
+  VPC peering can be use instead of AWS Transit Gateway to facilitate the communication between the VPCs, however, this will add operational complexity to build and manage large number VPC point-to-point peering at scale.
+  If Inter-VPC communication is not required, neither AWS Transit Gateway nor VPC peering is required in this connectivity model.
