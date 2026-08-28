---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/introduction.html
---

# Introduction
<a name="introduction"></a>

 Amazon VPC provides multiple network connectivity options for you to use, depending on your current network designs and requirements. These connectivity options include using either the internet or an AWS Direct Connect connection as the network backbone and terminating the connection into AWS or user-managed network endpoints. Additionally, with AWS, you can choose how network routing is delivered between Amazon VPC and your networks, leveraging either AWS services or user-managed network equipment and routes. This whitepaper considers the following options with an overview and a high-level comparison of each:
+ [Network-to-Amazon VPC connectivity options](network-to-amazon-vpc-connectivity-options.md)
  +  [AWS Site-to-Site VPN](aws-site-to-site-vpn.md) – Describes establishing a managed IPsec VPN connection from your network equipment on a remote network to Amazon VPC.
  +  [AWS Transit Gateway \+ AWS Site-to-Site VPN](aws-transit-gateway-vpn.md#_AWS_Transit_Gateway) – Describes establishing a managed IPsec VPN connection from your network equipment on a remote network to a regional network hub for Amazon VPCs, using AWS Transit Gateway.
  +  [AWS Direct Connect](aws-direct-connect.md) - Describes establishing a private, logical connection from your remote network to Amazon VPC, using AWS Direct Connect.
  + [AWS Direct Connect \+ AWS Transit Gateway](aws-direct-connect-aws-transit-gateway.md) – Describes establishing a private, logical connection from your remote network to a regional network hub for Amazon VPCs, using AWS Direct Connect and AWS Transit Gateway.
  +  [AWS Direct Connect \+ AWS Site-to-Site VPN](aws-direct-connect-site-to-site-vpn.md) – Describes establishing a private, encrypted connection from your remote network to Amazon VPC, using Direct Connect and AWS Site-to-Site VPN.
  + [AWS Direct Connect \+ AWS Transit Gateway \+ AWS Site-to-Site VPN](aws-direct-connect-aws-transit-gateway-vpn.md) – Describes establishing a private, encrypted connection from your remote network to a regional network hub for Amazon VPCs, using Direct Connect and AWS Transit Gateway.
  +  [Site-to-Site VPN CloudHub](aws-vpn-cloudhub.md) – Describes establishing a hub-and-spoke model for connecting remote branch offices.
  + [Software VPN](software-vpn.md) – Describes establishing a VPN connection from your equipment on a remote network to a user-managed software VPN appliance running inside an Amazon VPC.
  + [AWS Transit Gateway \+ SD-WAN solutions](aws-transit-gateway-sd-wan.md) - Describes the integration of software-defined wide area network (SD-WAN) solutions to interconnect several remote locations to a regional network hub for Amazon VPCs, using the AWS backbone or the internet as a transit network.
+ [Amazon VPC-to-Amazon VPC connectivity options](amazon-vpc-to-amazon-vpc-connectivity-options.md)
  + [VPC peering](vpc-peering.md) – Describes connecting Amazon VPCs within and across regions using the Amazon VPC peering feature.
  +  [AWS Transit Gateway](aws-transit-gateway.md) – Describes connecting Amazon VPCs within and across regions using AWS Transit Gateway in a hub-and-spoke model.
  + [AWS PrivateLink](aws-privatelink.md) – Describes connecting Amazon VPCs with VPC interface endpoints and VPC endpoint services.
  + [Software VPN](software-vpn-1.md) – Describes connecting Amazon VPCs using VPN connections established between user-managed software VPN appliances running inside of each Amazon VPC.
  + [Software VPN-to-AWS Site-to-Site VPN](software-vpn-to-aws-site-to-site-vpn.md) – Describes connecting Amazon VPCs with a VPN connection established between a user-managed software VPN appliance in one Amazon VPC and AWS Site-to-Site VPN attached to the other Amazon VPC.
+ [Software remote access-to-Amazon VPC connectivity options](software-remote-access-to-amazon-vpc-connectivity-options.md)
  + [AWS Client VPN](aws-client-vpn.md) – Describes connecting software remote access to Amazon VPC, leveraging AWS Client VPN.
  + [Software client VPN](software-client-vpn.md) – Describes connecting software remote access to Amazon VPC, leveraging user-managed software VPN appliances.
+ [Transit VPC](transit-vpc-option.md) - Describes establishing a global transit network on AWS using a software VPN in conjunction with an AWS-managed VPN.
+ [AWS Cloud WAN](aws-cloud-wan.md) - Describes establishing a managed wide area network (WAN) to easily build, manage, and monitor global interconnections between resources in Amazon VPCs, datacenters, and remote branches.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
