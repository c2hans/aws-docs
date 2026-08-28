---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/hybrid-network-connections.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Hybrid network connections
<a name="hybrid-network-connections"></a>

 There are several ways to connect between your on-premises equipment and AWS. This whitepaper is focused on how these different ways can be combined into overall architectures, however, a brief overview of the different options (AWS Direct Connect, Site-to-Site Virtual Private Network, and Transit Gateway Connect) are provided.

## AWS Direct Connect
<a name="aws-direct-connect"></a>

 AWS Direct Connect is a service that establishes a dedicated network connection from your premises to AWS. See [AWS Direct Connect](https://aws.amazon.com/directconnect/) for details.

 There are two types of AWS Direct Connect connections: dedicated and hosted. A dedicated connection is a direct link between an AWS device and your on-premises device, whereas a hosted connection is supported by an AWS Partner who can handle connection details for you. See [AWS Direct Connect connections](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithConnections.html) for more information.

 A Direct Connect connection uses Virtual Interfaces (VIFs) to isolate different traffic flows. Multiple VIFs can use the same Direct Connect link, separated by VLAN (802.1q) tags. There are three types of VIFs that provide connectivity to the AWS network. See [AWS Direct Connect virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html) for more details. The three types are:
+  **Private VIF:** A private VIF is a private connection between your device and your resources inside AWS. These terminate inside AWS on either a Virtual Private Gateway (VGW) directly (that supports a single VPC) or via a Direct Connect Gateway that then connects to multiple VGWs.
+  **Public VIF:** A public VIF enables connectivity to any public AWS resources, such as S3, DynamoDB, and public EC2 IP ranges. While a public VIF does not have direct access to the internet, any Amazon public resource can reach it (including other customers’ public EC2 instances), which customers should consider during security planning.
+  **Transit VIF:** A transit VIF is a private connection between your device and an AWS Transit Gateway, via a Direct Connect Gateway. Transit VIFs are now supported on links with speeds of less than 1 Gbps - see [the launch announcement](https://aws.amazon.com/about-aws/whats-new/2022/08/aws-direct-connect-expands-transit-gateway-support-connection-speeds/) for details.

**Note**
Hosted Virtual Interface (Hosted VIF) is a type of Private VIF where the VIF is assigned to a different AWS account than the AWS account which owns the AWS Direct Connect connection (which can include an AWS Direct Connect partner). AWS no longer allows new partners to offer this model. For more information, see [Creating a hosted virtual interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/createhostedvirtualinterface.html).

![Diagram showing AWS Direct Connect Private and Public VIFs](http://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/images/private-public-vifs.png)

## Site-to-Site Virtual Private Network (VPN)
<a name="site-to-site-virtual-private-network-vpn"></a>

 A site-to-site VPN enables two networks to communicate securely and can be used over an untrusted transport, such as the internet. Customers can establish VPN connections between on-premises sites and Amazon Virtual Private Clouds (Amazon VPC) via two options:
+  **AWS Managed Site-to-Site VPN (AWS S2S VPN):** This is a fully managed and highly available VPN service, using IPSec. See [What is AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) for more information. You can optionally enable acceleration for your Site-to-Site VPN connection. See [Accelerated Site-to-Site VPN connections](https://docs.aws.amazon.com/vpn/latest/s2svpn/accelerated-vpn.html) for more information. S2S VPN can also use Direct Connect transit VIFs to avoid having the traffic traverse the internet, lowering costs and allowing the use of private IP addresses. For details, see [Private IP VPN with AWS Direct Connect](https://docs.aws.amazon.com/vpn/latest/s2svpn/private-ip-dx.html).
+  **Software Site-to-Site VPN (Customer-managed VPN):** With this VPN connectivity option, you are responsible for provisioning and managing the entire VPN solution, typically by running VPN software on an EC2 instance. For more information, see [Software Site-to-Site VPN](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/software-site-to-site-vpn.html).

 Both options require support on the customer gateway device to terminate the on-premises end of the VPN tunnels. This device can be a physical device or a software appliance. For more information about network devices tested by AWS, refer to the list of [tested customer gateway devices](https://docs.aws.amazon.com/vpn/latest/s2svpn/your-cgw.html).

## Transit Gateway Connect (TGW Connect)
<a name="transit-gateway-connect"></a>

 Transit Gateway Connect uses GRE tunnels between an AWS Transit Gateway and an on-premises gateway device. BGP is used on top of TGW Connect to enable dynamic routing. Note that TGW Connect is not encrypted. For more information, see [Transit Gateway Connect](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-connect.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
