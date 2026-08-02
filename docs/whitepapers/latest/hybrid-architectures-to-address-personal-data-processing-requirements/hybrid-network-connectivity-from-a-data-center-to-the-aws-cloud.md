---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/hybrid-network-connectivity-from-a-data-center-to-the-aws-cloud.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 1.1 Hybrid network connectivity from a data center to the AWS Cloud
<a name="hybrid-network-connectivity-from-a-data-center-to-the-aws-cloud"></a>

 Requirements addressed:
+  **REQ2** (measures to prevent unauthorized or accidental access)
+  **Customer-REQ1** (reliable connectivity to AWS services)

 AWS services – [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) and [AWS Direct Connect](https://aws.amazon.com/directconnect/)

![Private AWS resources access](http://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/images/private-aws-resources-access.png)

 Private AWS resources access

 [AWS Direct Connect](https://aws.amazon.com/directconnect/) makes it easy to establish a dedicated network connection from the customer premises to AWS through a dedicated line, which can, in many cases, reduce network costs, increase bandwidth throughput, and provide a more consistent network experience than Internet-based connections.

 Using industry standard 802.1q VLANs, this dedicated connection can be partitioned into multiple virtual interfaces. This allows using the same connection to access public resources such as objects stored in [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) using public IP address space, and private resources such as [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) instances running within an [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (VPC) using private IP space, while maintaining network separation between the public and private environments. Virtual interfaces can be reconfigured at any time to meet your changing needs. The preceding figure shows private AWS resources accessed through private virtual interface (private VIF) and [AWS PrivateLink](https://aws.amazon.com/privatelink/).

 AWS Direct Connect does not encrypt traffic that is in transit by default. To encrypt the data in transit that traverses AWS Direct Connect, customers can use the Direct Connect transit encryption options. There are two options available:

1.  To provide encryption from an on-premises data center to the AWS Direct Connect location, customers can use [MAC Security](https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACsec.html) (MACSec). MACSec is an IEEE standard that provides data confidentiality, data integrity, and data origin authenticity. Nevertheless, traffic will still be unencrypted inside the routers and data centers long the way.

1.  To provide encryption from on-premises data center to an AWS network, customers can use [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html). Site-to-Site VPN supports Internet Protocol security (IPsec) VPN connections.

 The Direct Connect connection consists of a single dedicated connection between ports on an AWS router and a Partner (or customer) router. We recommend establishing a second connection if redundancy is required. For additional resiliency, customers can implement an AWS Site-to-Site VPN connection over the internet, and configure routing to pass traffic through the VPN connection if the existing channel became unavailable. For more information, refer to the [AWS Direct Connect Resiliency Toolkit](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resilency_toolkit.html).

![Hybrid AWS resources access](http://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/images/hybrid-aws-resources-access.png)

 Hybrid AWS resources access

 Direct Connect is made through a one Gbps, 10 Gbps, or 100 Gbps ethernet port. The customer can use more than one Direct Connect connection, which can be assigned to a Link Aggregation Group (LAG). The LAG helps increase available bandwidth for the customer. Each AWS Site-to-Site VPN connection has two tunnels, and each tunnel supports a maximum throughput of up to 1.25 Gbps.

 Learn more about network resiliency and redundancy options in the [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html) whitepaper.
