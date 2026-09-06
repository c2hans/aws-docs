---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-teradata-vantagecloud-aws/reference-architectures.html
---

# Reference architectures
<a name="reference-architectures"></a>

The following supported connectivity options can help you connect to Teradata VantageCloud Enterprise:
+ AWS Transit Gateway enables Cloud-to-cloud connections.
+ AWS Site-to-Site VPN enables On-premises-to-cloud connections and cloud-to-cloud connections.
+ AWS PrivateLink enables cloud-to-cloud connections.
+ AWS Direct Connect enables on-premises-to-cloud connections.

You can use Direct Connect (recommended option) and Site-to-Site VPN to connect your on-premises environment to Teradata VantageCloud Enterprise. Transit Gateway (recommended option), PrivateLink, and Site-to-Site VPN are the supported options for connecting your AWS account to Teradata VantageCloud Enterprise.

## VPC connection options
<a name="vpc-connection-options"></a>

Teradata supports the following virtual private connection (VPC) connection options.

|
|
| Connection | Typical use case | Description |
| --- |--- |--- |
| Transit Gateway | Connecting a VPC in your AWS account to a VPC in a Teradata AWS account<br />Connecting to multiple sites and multiple appliances from a VPC in your AWS account to a VPC in a Teradata AWS account | A good option if you require scaling and a single point of control while working with multiple AWS sites for Teradata, especially in a hybrid setup<br />Offers more control when managing network traffic<br />Doesn't support inter-Region connectivity |
| Site-to-Site VPN | Connecting a VPC in your AWS account to a VPC in a Teradata AWS account<br />Connecting an on-premises data center to a VPC in a Teradata AWS account<br />Vantage must initiate a connection to one or more applications\* in your VPC | Bidirectional connection initiation<br />IP address abstraction that prevents the need for IP address planning |
| PrivateLink | Connecting a VPC in your AWS account to a VPC in a Teradata AWS account<br />Vantage must not initiate communication with any application\* in your VPC | Unidirectional connection initiation<br />Requires set up and maintenance of one reverse PrivateLink endpoint if LDAP is needed (from a Teradata VPC to your VPC)<br />Number of PrivateLink endpoints required varies based on applications\* |
| Direct Connect | Connecting an on-premises data center to a VPC in a Teradata AWS account | Dependency on ISP for implementation |

\*Application examples include another Teradata instance, [Teradata QueryGrid](https://www.teradata.com/Products/Ecosystem-Management/IntelliSphere/QueryGrid), other data sources, an LDAP server, or a Kerberos server.

## Transit Gateway architecture
<a name="architecture-transit-gateway"></a>

A network architecture based on [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/faqs/) connects VPCs and on-premises networks through a central hub. This approach simplifies the network architecture and eliminates the need for complex peering connections.

You can use Transit Gateway to establish the following types of connections:
+ Teradata VantageCloud to Teradata VantageCloud Enterprise
+ Your VPC to Teradata VantageCloud Enterprise

Transit Gateway is owned and managed by you. The Transit Gateway-to-Teradata VantageCloud Enterprise VPC connection and data egress add additional costs that you're responsible for.

The following diagram shows how you can connect your data center to a VPC in your AWS account by using either Direct Connect or a VPN. You can use Transit Gateway to shut down the connection from your data center.

**Note**
VPCs for Teradata VantageCloud Enterprise deployments that are managed by Teradata are attached to Transit Gateway in your AWS account.

## Site-to-site VPN architecture
<a name="architecture-site-to-site-vpn"></a>

A single [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) connection is included with a subscription to Teradata VantageCloud Enterprise. This type of connection is also known as an [AWS managed VPN](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-site-to-site-vpn.html) connection. The connection can support up to 1.25 gigabits (Gb) per second. Network egress fees apply as VPN traffic is routed over the internet.

Both hybrid and multi-cloud to AWS managed VPN options are supported. For Amazon VPC-to-Amazon VPC VPN connectivity, you can set up a software VPN. For more information, see [Software VPN-to-AWS Site-to-Site VPN](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/software-vpn-to-aws-site-to-site-vpn.html) in the AWS Whitepaper documentation.

The following diagram shows a Site-to-Site VPN architecture that supports two VPN configurations. You can connect a Site-to-Site VPN from your data center to Teradata VantageCloud Enterprise VPCs. You can also connect a Site-to-Site VPN from your AWS account to the Teradata VantageCloud Enterprise VPCs.

## PrivateLink architecture
<a name="private-link-architecture"></a>

[AWS PrivateLink](https://aws.amazon.com/privatelink/?privatelink-blogs.sort-by=item.additionalFields.createdDate&privatelink-blogs.sort-order=desc) provides connectivity between VPCs. You can access Teradata VantageCloud Enterprise over private IP addresses from your virtual network while keeping the data flow on the secure backbone network of AWS. Data never traverses the public internet. This significantly reduces exposure to common security threats.

PrivateLink allows only unidirectional network connectivity. Applications that require a connection to be initiated from both endpoints require two PrivateLink connections.

The following diagram shows a PrivateLink architecture where a private endpoint in an AWS account uses PrivateLink to connect to Teradata Vantage SQL Engine nodes. A private endpoint in the AWS account also uses PrivateLink to connect to a Teradata Viewpoint server. In the diagram, LDAP is configured with two PrivateLink connections in place for communication between the VPC in the Teradata AWS account and the VPC in the AWS account.

For more information, see [AWS PrivateLink](https://aws.amazon.com/privatelink/) or contact your [Teradata account team.](https://www.teradata.com/About-Us/Contact)

## Direct Connect architecture
<a name="direct-connect-architecture"></a>

You can use [AWS Direct Connect](https://aws.amazon.com/directconnect/) for an architecture where hybrid connectivity is required from on-premises to Teradata VantageCloud Enterprise. Direct Connect is managed and owned by you. The following diagrams show the Direct Connect architecture where Direct Connect is used to create a dedicated network connection to your AWS account.

Direct Connect supports two architecture options. The first option is the recommended option and uses [Direct Connect gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html) and a virtual private gateway as the following diagram shows.

To build an architecture based on the preceding diagram, you must create a Direct Connect gateway in your AWS account and shut down the private virtual interface (VIF) to the Direct Connect gateway. You will then need to accept the association proposal for the virtual private gateway on the Teradata AWS account.

The second architecture option uses a hosted private VIF and a virtual private gateway as the following diagram shows.

To build an architecture based on the preceding diagram, you must create a hosted private VIF and share the VIF with Teradata VantageCloud Enterprise to establish connectivity. A private VIF is a network interface that enables you to use Direct Connect to connect with another AWS account, such as a Teradata VantageCloud Enterprise AWS account. Network egress fees apply on private VIFs.
