---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/services.html
---

# Overview of AWS networking services for SaaS offerings
<a name="services"></a>

This section discusses the AWS networking services that are referenced in this guide. It also compares their capabilities and describes security considerations for each service.

**This section contains the following topics:**
+ [AWS networking services](#services-aws)
+ [Comparing service capabilities](#services-capabilities)
+ [Security features and considerations](#services-security-features)

## AWS networking services
<a name="services-aws"></a>

The following are the AWS services that are discussed consistently in this guide.

### AWS PrivateLink
<a name="9999999999999999privatelink-.f5e64620-94a9-5221-bcda-866770dfd8fa"></a>

[AWS PrivateLink](https://docs.aws.amazon.com/de_de/vpc/latest/privatelink/what-is-privatelink.html)** **is a cloud-native service that can provide access to your SaaS offering if your customers are already operating in the AWS Cloud. Your customer connects to the SaaS offering through a [interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html). This is an endpoint network interface that is provisioned in one or more subnets in the customer's AWS account. In the scenarios in this guide, the traffic travels through the interface VPC endpoint and arrives at an [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) in your account. The Network Load Balancer forwards the traffic to the SaaS application, which you have registered as an *endpoint service*. Through [resource VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/use-resource-endpoint.html), AWS PrivateLink can also help you access other resources, such as databases.

### Amazon VPC Lattice
<a name="9999999999999999vpclatlong-.5860b70b-a4b1-5ff4-b099-aa860e248d30"></a>

[Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) is an application networking service that helps SaaS providers to securely and efficiently offer their services to customers who are operating across multiple VPCs and AWS accounts. Customers access your SaaS offering through VPC Lattice, which delivers consistent network connectivity, robust access controls, and advanced traffic management. In these scenarios, traffic flows through VPC Lattice to your registered application services. It provides scalable and secure communication, regardless of which compute service you use.

### VPC peering
<a name="vpc-peering.c31b3206-3f2d-57fb-a3a9-0778f3511abb"></a>

[VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) is a networking connection between two virtual private clouds (VPCs) that routes traffic between them by using private IPv4 addresses or IPv6 addresses. VPC peering is typically used between trusted entities, like those within the same organization. Your customer creates a peering request to one of your VPCs. When you accept it, traffic can flow between both VPCs in either direction. This connection approach stands out for its uniqueness because it involves direct communication between two VPCs without any intermediary service or infrastructure to manage.

### AWS Transit Gateway
<a name="9999999999999999awstglong-.d7f4b317-f40f-57f3-aa56-05c14582ad56"></a>

[AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) is a centralized network transit hub that can connect VPCs, virtual private network (VPN) connections, [AWS Direct Connect gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html), third-party virtual appliances in a VPC, and other transit gateways. A transit gateway can have a different route table for each attachment. This provides maximum flexibility for routing, and it helps you isolate the networks. It's often used to connect many VPCs together or for centralized inspection.

### AWS Site-to-Site VPN
<a name="9999999999999999s2slong-.ae442c98-5519-590e-84dc-23c5c1882e50"></a>

[AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) can use internet protocol security (IPsec) technology to establish connections between on-premises networks, remote offices, factories, other cloud providers, and the AWS global network. The connection is established from a virtual private gateway or transit gateway in a VPC in the AWS Cloud to a physical or software-based customer gateway, which can be in the AWS Cloud, on-premises, or in another CSP's cloud. The connection can be through the Internet or through a physical AWS Direct Connect connection. It is also possible to have an [accelerated Site-to-Site VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/accelerated-vpn.html) by using AWS Global Accelerator. An accelerated connection routes traffic to an AWS edge location, and it offers reduced latency and improved performance.

### AWS Direct Connect
<a name="9999999999999999aws-dc-long-.ae7ff08e-2817-5d74-a621-d9d9c0569c60"></a>

[AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) establishes a high-speed, private connection between an on-premises data center and the AWS Cloud. By bypassing the public internet, Direct Connect provides a more reliable, secure, and consistent low latency connection to the AWS Cloud. Customers connect to one of the [Direct Connect locations](https://aws.amazon.com/directconnect/locations/) and then choose either a hosted or a dedicated connection to AWS. Although this is an uncommon architecture choice for SaaS offerings, it can be well suited for SaaS providers that have few but large enterprise consumers.

## Comparing service capabilities
<a name="services-capabilities"></a>

The following table outlines the supported capabilities of the AWS services that are discussed in this guide. The following are descriptions of the capabilities included in this table:
+ **Overlapping CIDR ranges **– Can connect two or more networks with the same or overlapping CIDR ranges
+ **Bidirectional communication** –** **Can support a two-way communication channel so that the SaaS consumer can expose internal resources, such as a database, to the SaaS provider
+ **IPv6** –** **Can support IPv6, either single or dual-stack
+ **Jumbo frame** –** **Can support jumbo frames with a frame size up to 8,500 bytes
+ **Hybrid-cloud** –** **Can support a connection with an on-premises network
+ **Multi-cloud** – Can support a connection between networks on different cloud service providers

|
|
| **Service or approach** | **Overlapping CIDR ranges** | **Bidirectional communication** | **IPv6** | **Jumbo frame** | **Hybrid cloud** | **Multi-cloud** |
| --- |--- |--- |--- |--- |--- |--- |
| **VPC peering** | No | Yes | Yes | Yes(5) | No | No |
| **AWS PrivateLink** | Yes | Yes(1) | Yes | Yes | No(6) | No(6) |
| **Amazon VPC Lattice** | Yes | Yes(1) | Yes | Yes | No(6) | No(6) |
| **AWS Transit Gateway** | No | Yes | Yes | Yes | Yes(3) | Yes(3) |
| **AWS Site-to-Site VPN** | No | Yes | Yes | No | Yes | Yes |
| **AWS Direct Connect** | No | Yes | Yes | Yes(2) | Yes | Yes |
| **Public internet access**(4) | Not applicable | No | Yes | Yes | Yes | Yes |

1. With [VPC resources](https://docs.aws.amazon.com/vpc-lattice/latest/ug/vpc-resources.html) in Amazon VPC Lattice

1. Only for private and transit virtual interfaces

1. With Site-to-Site VPN or AWS Direct Connect attachments

1. As a general term for AWS resources that make an application publicly accessible, such as an Application Load Balancer

1. Only for peering connections within one AWS Region

1. Possible through a preexisting Layer 3 connection between the environments

## Security features and considerations
<a name="services-security-features"></a>

The following table outlines the security features of the AWS services that are discussed in this guide.
+ **Means of authentication** – How you can make sure that only your customers can connect to your service. Another level of authentication for incoming requests is usually still required, especially in shared tenant environments.
+ **Encryption in transit** – Describes whether encryption in transit is provided by default. *Native encryption* describes encryption that AWS provides for all traffic within VPCs, across VPCs, or across data centers. *Supplementary encryption* describes encryption that you control and that can be stopped by the respective service.

|
|
| **Service or approach** | **Means of authentication** | **Encryption in transit** |
| --- |--- |--- |
| **VPC peering** | You initiate a peering request to the AWS account and VPC of your customer or accept a request that they initiate. See [Accept or reject a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/accept-vpc-peering-connection.html). | Native encryption only |
| **AWS PrivateLink** | You choose which AWS accounts are allowed to create endpoints to your service. These accounts are known as *allowed principals*. See [Accept or reject connection requests](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html#accept-reject-connection-requests). | Native encryption only |
| **Amazon VPC Lattice** | You share a VPC Lattice service or service network with your customers' AWS accounts. See [Share your VPC Lattice entities](https://docs.aws.amazon.com/vpc-lattice/latest/ug/sharing.html). | Native encryption and supplementary TLS encryption |
| **AWS Transit Gateway** | Your customer creates a peering attachment request from their AWS account, or you initiate the request. See [Transit gateway peering attachments in Amazon VPC Transit Gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html). | Native encryption and supplementary IPsec encryption with a VPN attachment |
| **AWS Site-to-Site VPN** | You use IPsec pre-shared keys or a private certificate on the customer's device. See [AWS Site-to-Site VPN tunnel authentication options](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-tunnel-authentication-options.html). | Supplementary IPsec encryption |
| **AWS Direct Connect** | Your customer creates a virtual interface request from their AWS account. See [Direct Connect virtual interfaces and hosted virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html). | Supplementary Layer 2 encryption possible at selected sites. See [Direct Connect Locations](https://aws.amazon.com/directconnect/locations/). |
| **Public internet access**(1) | Custom authentication is required. | Supplementary TLS encryption possible |

1. As a general term for AWS resources that make an application publicly accessible, such as an Application Load Balancer
