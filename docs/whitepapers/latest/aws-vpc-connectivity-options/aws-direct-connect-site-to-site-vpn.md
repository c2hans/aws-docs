---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-site-to-site-vpn.html
---

# AWS Direct Connect \+ AWS Site-to-Site VPN
<a name="aws-direct-connect-site-to-site-vpn"></a>

 With [AWS Direct Connect](https://aws.amazon.com/directconnect/) \+ [AWS Site-to-Site VPN](https://aws.amazon.com/vpn/site-to-site-vpn/), you can combine AWS Direct Connect connections with an AWS-managed VPN solution. AWS Direct Connect public VIFs establish a dedicated network connection between your network and public AWS resources such as an AWS Site-to-Site VPN endpoint. Once you establish the connection to the service, you can create IPsec connections to the corresponding Amazon VPC virtual private gateways. The following figure illustrates this option.

![Diagram that shows establishing a connection to the service, then creating IPsec connections.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/aws-direct-connect-and-aws-site-to-site-vpn.png)

This solution combines the benefits of the end-to-end secure IPsec connection with low latency and increased bandwidth of the AWS Direct Connect to provide a more consistent network experience than internet-based VPN connections. A BGP connection session is established between AWS Direct Connect and your router on the public VIF. Another BGP session or a static route will be established between the virtual private gateway and your router on the IPsec VPN tunnels.

## Additional resources
<a name="additional-resources-4"></a>
+  [AWS Direct Connect](https://aws.amazon.com/directconnect/)
+  [AWS Direct Connect virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html)
+  [AWS Site-to-Site VPN User Guide](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
