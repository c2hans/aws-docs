---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-aws-transit-gateway-vpn.html
---

# AWS Direct Connect \+ AWS Transit Gateway \+ AWS Site-to-Site VPN
<a name="aws-direct-connect-aws-transit-gateway-vpn"></a>

 With [AWS Direct Connect](https://aws.amazon.com/directconnect/) \+ [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) \+ [AWS Site-to-Site VPN](https://aws.amazon.com/vpn/site-to-site-vpn/), you can enable end-to-end IPsec-encrypted connections between your networks and a regional centralized router for Amazon VPCs over a private dedicated connection.

You can use AWS Direct Connect public VIFs to first establish a dedicated network connection between your network to public AWS resources, such as AWS Site-to-Site VPN endpoints. Once this connection is established, you can create an IPsec connection to AWS Transit Gateway. The following figure illustrates this option.

![A diagram showing creating an IPsec connection.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/aws-direct-connect-transit-gateway-site-to-site-vpn-public-vif.png)

![A diagram showing Direct Connect, Transit Gateway, and Site-to-Site VPN.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/aws-direct-connect-and-aws-transit-gateway-and-vpn-with-transit-vif.png)

Consider taking this approach when you want to simplify management and minimize the cost of IPsec VPN connections to multiple Amazon VPCs in the same region, with the low latency and consistent network experience benefits of a private dedicated connection over an internet-based VPN. A BGP session is established between AWS Direct Connect and your router using either the public or the transit VIF. Another BGP session or a static route will be established between AWS Transit Gateway and your router on the IPsec VPN tunnel.

## Additional resources
<a name="additional-resources-5"></a>
+  [AWS Direct Connect virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html)
+  [Transit gateway VPN attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-attachments.html)
+  [Requirements for customer gateway devices](https://docs.aws.amazon.com/vpc/latest/adminguide/Introduction.html#CGRequirements)
+  [Customer gateway devices tested with Amazon VPC](https://docs.aws.amazon.com/vpc/latest/adminguide/Introduction.html#DevicesTested)
+  [AWS Site-to-Site VPN – Private IP VPN with AWS Direct Connect](https://docs.aws.amazon.com/vpn/latest/s2svpn/private-ip-dx.html)
