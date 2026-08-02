---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/aws-dx-dxgw-with-vgw-single-region.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS DX – DXGW with VGW, Single Region
<a name="aws-dx-dxgw-with-vgw-single-region"></a>

 **This model is constructed of:**
+  Single AWS Region.
+  Dual AWS Direct Connect Connections to independent DX locations.
+  AWS DXGW directly attached to the VPCs using VGW.
+  Optional usage of AWS Transit Gateway for Inter-VPC communication.

![Diagram showing AWS DX – DXGW with VGW, Single AWS Region](http://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/images/dxgw-with-vgw-single-region.png)

 **Connectivity model attributes:**
+  Provides the ability to connect to VPCs and DX connections in other Regions in the future.
+  Offers automated failover with dynamic routing (BGP).
+  With AWS Transit Gateway you can control the desired communication model among the VPCs. For more information, refer to [How transit gateways work](https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html).

 **Scale considerations:**

 Reference [AWS Direct Connect quotas](https://docs.aws.amazon.com/directconnect/latest/UserGuide/limits.html) for more information about other scale limits, such as such number of supported prefixes, number of VIFs per DX connection type (Dedicated, hosted). Some key considerations:
+  The BGP session for a private VIF may advertise up to 100 routes each for IPv4 and IPv6.
+  Up to 20 VPCs can be connected per DXGW over a single BGP session. If more than 20 VPCs are needed, additional DXGWs can be added to facilitate the connectivity at scale, or consider using Transit Gateway integration.
+  Additional AWS Direct Connects can be added as desired.

 **Other considerations:**
+  Does not incur AWS Transit Gateway related processing cost for data transfer between AWS and on-premises networks.
+  Security groups of a remote VPC cannot be referenced over AWS Transit Gateway (need VPC peering).
+  VPC peering can be used instead of AWS Transit Gateway to facilitate the communication between the VPCs, however, this adds operational complexity to build and manage large number VPC point-to-point peering at scale.
+  If Inter-VPC communication is not required, neither AWS Transit Gateway nor VPC peering is required in this connectivity model.
