---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/encrypt-data-in-transit.html
---

# Encrypt Data in Transit
<a name="encrypt-data-in-transit"></a>

AWS strongly recommends encrypting data in transit from one system to another, including resources within and outside of AWS.

When you create an AWS account, a logically isolated section of the AWS Cloud—the [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC)—is provisioned to it. There, you can launch AWS resources in a virtual network that you define. You have complete control over your virtual networking environment, including selecting your own IP address range, creation of subnets, and configuration of route tables and network gateways. You can also create a hardware Virtual Private Network (VPN) connection between your corporate datacenter and your Amazon VPC, so you can use the AWS Cloud as an extension of your corporate datacenter.

For protecting communication between your Amazon VPC and your corporate datacenter, you can select from several VPN connectivity options, and choose one that best matches your needs. You can use the [AWS Client VPN](https://aws.amazon.com/vpn/client-vpn/) to enable secure access to your AWS resources using client-based VPN services. You can also use a third-party software VPN appliance available in the AWS Marketplace, which you can install on an Amazon EC2 instance in your Amazon VPC. Alternatively, you can create an IPsec VPN connection to protect the communication between your VPC and your remote network. To create a dedicated private connection from a remote network to your Amazon VPC, you can use [AWS Direct Connect](https://aws.amazon.com/directconnect/). You can combine this connection with an AWS Site-to-Site VPN to create an IPsec-encrypted private connection.

AWS provides HTTPS endpoints using the TLS protocol for communication, which provides encryption in transit when you use AWS APIs. You can use the [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) (ACM) service to generate, manage, and deploy the private and public certificates you use to establish encrypted transport between systems for your workloads. Elastic Load Balancing is integrated with ACM and is used to support HTTPS protocols. If your content is distributed through Amazon CloudFront, it supports encrypted endpoints.
