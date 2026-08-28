---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/choosing-networking-and-content-delivery-service.html
---

# Choosing an AWS networking and content delivery service
<a name="choosing-networking-and-content-delivery-service"></a>

|  |  |
| --- |--- |
| **Purpose:** | Help determine which AWS networking and content delivery services are the best fit for your organization. |
| **Last updated:** | January 16, 2025 |
| **Covered services:** |  +  [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) <br />+  [AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-user-what-is.html) <br />+  [AWS Cloud WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/what-is-cloudwan.html) <br />+  [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) <br />+  [AWS Data Transfer Terminal](https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html) <br />+  [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) <br />+  [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) <br />+  [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) <br />+  [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html) <br />+  [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) <br />+  [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) <br />+  [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) <br />+  [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) <br />+  [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) <br />+  [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) <br />+  [AWS Verified Access](https://docs.aws.amazon.com/verified-access/latest/ug/what-is-verified-access.html) <br />+  [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) <br />+  [Amazon VPC IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html) <br />+  [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) <br />+  [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html)   |

Deciding on an approach to cloud networking and content delivery can be complex, especially if you’re used to managing and configuring networks with on-premises hardware. Fortunately, [building networks in the cloud](https://aws.amazon.com/what-is/computer-networking/) shares core concepts with building on-premises, such as IP addressing, load balancing, and routing. Familiarity with these concepts will help you understand what AWS services you need.

Amazon Web Services (AWS) offers 20\+ purpose-built networking and content delivery services that you can use to build, operate, and secure your cloud networks across all your cloud environments and distributed cloud and edge locations globally. You can also build network infrastructure that extends your on-premises environment to AWS.

This decision guide will help you ask the right questions to choose the networking and content delivery services and tools that fit your needs.

[![AWS Videos](http://img.youtube.com/vi/cRdDCkbE4es?start=123&end=373/0.jpg)](http://www.youtube.com/watch?v=cRdDCkbE4es?start=123&end=373)

## Understand
<a name="understand"></a>

What you build in AWS depends on your business needs. In this guide, we use the term *workloads* to refer to any collection of resources and code that delivers business value, such as a customer-facing application or a backend process.

Networking and content delivery services at AWS fall into four categories: networking foundations, global and hybrid connectivity, edge networking and content delivery, and application networking.

![Diagram showing AWS networking services for every application and workload](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/cloud-networking-from-aws.png)

**Networking foundations**

In AWS, your workloads run inside one or more [Amazon Virtual Private Cloud (VPCs)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html). After your workloads are running in VPCs, you can connect the workloads to other VPCs—such as an [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)—or you can connect them to software as a service (SaaS) services including other AWS services, such as [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html). Amazon VPC lets you provision a private, isolated section of the AWS Cloud where you can launch AWS resources in a virtual network using customer-defined IP address ranges. Amazon VPC gives you several options for connecting your AWS virtual networks with other remote networks.

**Global and hybrid connectivity**

You can use the services in this category to securely connect from on-premises networks to your workloads in the AWS Cloud. You can create a [virtual private network (VPN)](https://aws.amazon.com/what-is/vpn/) to connect remote users by using [AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-user-what-is.html), connect on-premises networks using [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html), or build a global wide area network (WAN) with [AWS Cloud WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/what-is-cloudwan.html). You can also set up a direct, private connection to the AWS Cloud using [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html), providing a direct, secure connection to the cloud with predictable performance. You may also need to connect your on-premises data centers, remote sites, and the cloud. [A hybrid network](https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/hybrid-connectivity.html) can connect these different environments.

**Edge networking and content delivery**

Services in this category help ensure higher performance through caching and optimized transport. A good example of this is [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html). You'll also want to see customer traffic optimally routed to provide availability using services such as [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html). Additionally, it's important that customer traffic is routed to make the most of the AWS global infrastructure using services such as [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html). [AWS Data Transfer Terminal](https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html) is a network-ready, physical location where you can bring your data storage devices for fast data transfer to and from the AWS Cloud.

**Application networking**

As you increase adoption of the AWS Cloud, you’ll want to consider how to connect workloads at scale, by using [AWS App Mesh](https://docs.aws.amazon.com/app-mesh/latest/userguide/what-is-app-mesh.html) and [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html), integrate the workloads in your VPCs with [APIs](https://aws.amazon.com/what-is/api/) by using [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html), and manage the IP address usage of the resources running in your VPCs by using [Amazon VPC IP Address Manager (IPAM)](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html). As customer demand increases, you can help ensure that the workloads in your VPCs can scale and provide high availability by using [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html).

**Networking security and remote access**

While Amazon VPC helps you secure access to your workloads, the services in this category offer enhanced protection against threat actors and unauthorized users by using [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html), [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html), [AWS Verified Access](https://docs.aws.amazon.com/verified-access/latest/ug/what-is-verified-access.html), and [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). To help ensure network security, consider using Amazon Route 53 DNS Firewall, [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html), [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html), [network access control lists](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html), and security groups.

## Consider
<a name="consider"></a>

It's important that you choose the networking services that fit your business needs. The following are some of the criteria to consider when choosing networking services.

------
#### [ Business objectives ]

The networking services that you choose will depend on your business objectives. Assess where you are now and where you want to be when it comes to the security, reliability, accessibility, and performance of your workloads running in the AWS Cloud.
+ Consider how the network services you use fit with your migration and integration strategies. A [hybrid networking architecture](https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/definition.html) can help you meet this need by integrating your on-premises data center and AWS.
+ Review the [networking and content delivery blogs](https://aws.amazon.com/blogs/networking-and-content-delivery/) in the *Let’s architect\!* AWS blog series to see what others are building in the AWS Cloud.
+ Examine the third-party options available to help you accelerate your networking service adoption. The [AWS Marketplace](https://aws.amazon.com/marketplace/solutions/infrastructure-software/cloud-networking) provides a curated digital catalog that you can use to find, buy, and deploy networking solutions.
+ Decide if working with an [AWS Partner](https://aws.amazon.com/partners/work-with-partners/) that specializes in networking and content delivery would be beneficial. Members of the AWS Partner Network are strategic experts and experienced builders that can help you meet your needs with the AWS Cloud.
+ Explore taking [AWS networking online courses](https://explore.skillbuilder.aws/learn/public/learning_plan/view/1944/networking-core-knowledge-badge-readiness-path) on AWS Skill Builder that cover services such as Amazon VPC, AWS Cloud WAN, and Amazon Route 53.

------
#### [ Workload characteristics ]

The networking services that you choose will depend on the characteristics of your workloads.
+ Networking services each have a particular role. Services such as AWS Cloud WAN and AWS Transit Gateway are suited for connecting workloads that are running in VPCs. Amazon API Gateway creates public APIs so that your customers can connect to your workloads. AWS Global Accelerator can help you improve the reliability, security, and latency of your workloads.
+ As the internet continues to grow, so does the need for IP addresses for devices. The most common format for IP addresses is IPv4. The latest format for IP addresses is IPv6. IPv6 provides more address space and solves the problem of [IPv4 address exhaustion](https://en.wikipedia.org/wiki/IPv4_address_exhaustion). AWS services support for IPv6 includes support for dual stack configuration (IPv4 or IPv6) or IPv6 only configurations. The number of AWS services that support IPv6 is growing continuously. To view the current services that support IPv6, see [AWS services that support IPv6](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ipv6-support.html).

------
#### [ Data protection ]

It’s important to consider the protection of your data in the AWS Cloud.
+ Businesses must protect customer data against evolving cyber risks. While Amazon VPC helps you to secure access to the workloads running in VPCs, consider enhanced data protection measures, such as AWS Network Firewall, AWS Shield, AWS WAF, and Amazon Route 53 Resolver DNS Firewall.
+ It's recommended that you employ application-level encryption (TLS), irrespective of the transport, as a defense in depth measure to help ensure confidentiality end-to-end.
+ If the workloads in your VPCs need to connect to other AWS services, you can connect to those services programmatically by using API endpoints over the public internet. However, if you want to send data over a private connection, use AWS PrivateLink. Many members of the AWS Partner Network offer their SaaS solutions through AWS PrivateLink.

------
#### [ Availability ]

*Availability* is an application’s ability to maintain uptime. It’s important that your customers can use the products and services that you build in your VPCs with minimal or no downtime.
+ The AWS global infrastructure is built on [AWS Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/?p=ngi&loc=2&refid=67adb321-e6e5-4750-92f4-b5d8e229d6bf). When you deploy your workloads to your VPCs, you should deploy to multiple Availability Zones to ensure that your workload is still available in the event of a single Availability Zone failure.
+ To improve the availability, scalability, security, and performance of the workloads running in your VPCs, consider [load balancing](https://aws.amazon.com/what-is/load-balancing/) (Elastic Load Balancing). You can use different types of load balancers depending on the needs of your applications. Each load balancer supports different types of traffic over different protocols and network layers aligned to the [Open Systems Interconnection (OSI)](https://aws.amazon.com/what-is/osi-model/) model. For more information about the differences between load balancer types, see [product comparisons](https://aws.amazon.com/elasticloadbalancing/features/#Product_comparisons).

------
#### [ Performance ]

You can use networking services to optimize for the latency, throughput, and bandwidth requirements of your workloads running on the AWS global infrastructure.
+ If you want to minimize latency to local customers using web applications around the globe, consider using Amazon CloudFront. CloudFront is a [content delivery network](https://aws.amazon.com/what-is/cdn/) that delivers content to customers with the lowest latency possible.
+ If you’re running gaming, Internet of Things (IoT), or Voice over IP (VoIP) workloads, consider using AWS Global Accelerator. This service helps you improve your workloads’ availability and performance.
+ If the workloads in your VPCs need to connect to other AWS Regions, you can connect to those services programmatically using public API endpoints.

------
#### [ Operational excellence ]

As you increase AWS Cloud adoption, you’ll want to understand what is happening across your workloads at any time. Tools and services such as [Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) and [Amazon CloudWatch Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html) can help you keep pace with changing business needs and priorities as your workloads grow.
+ Managing IP addresses of workloads running in multiple VPCs can be difficult. Consider if you need to automate IP address management across your workloads (Amazon VPC IPAM).
+ If you’re using a [microservice architecture](https://aws.amazon.com/microservices/), managing the connectivity, security, and monitoring between microservices can be a challenge. Consider if you need to automate microservice interaction (AWS App Mesh and Amazon VPC Lattice).

------
#### [ Connectivity ]

You can use networking services to connect to the AWS Cloud, connect workloads, or connect networks.
+ Consider the following for connecting to the AWS Cloud:
  + If you want to securely connect remote users to your VPCs, consider using AWS Client VPN.
  + If you want to securely connect an entire on-premises network to your VPCs, consider using AWS Site-to-Site VPN.
  + If you require more consistent performance than the internet can provide, consider a direct connection from your on-premises network to AWS (Direct Connect).
  + If you need to quickly move data into or out of the AWS Cloud, consider using AWS Data Transfer Terminal.
+ Consider the following for connecting networks:
  + If you operate in multiple AWS Regions, want to manage your own routing configurations, or prefer to use your own automation, consider using AWS Transit Gateway.
  + If you want to unify your data center, branch, and AWS networks with a WAN, consider using AWS Cloud WAN. It is also worth considering if you don't want to manage complex routing configurations or build your own automations for multi-Region connectivity.

------
#### [ Security ]

AWS provides a secure foundation for you to build and deploy your applications, but you are responsible for implementing your own security measures to protect your data, applications, and networking infrastructure, no differently than you would in an on-site data center.
+ Review and understand the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) and how it applies to security in the AWS Cloud.
+ AWS security groups and network access control lists (NACLs) can be used together or on their own to secure a network, helping you to create a defense in depth security strategy.
+ Businesses must protect their network applications against evolving cyber risks. Consider if you will need to protect your workloads against malicious attacks or malware (with [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)), distributed denial of service (DDoS) attacks (with AWS Shield), or SQL injection and cross-site scripting attacks (with AWS WAF).

  Amazon Route 53, [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html), [network access control lists](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html), and security groups are also important to consider in ensuring network security.

------

## Choose
<a name="choose"></a>

Now that you know the criteria by which you will be evaluating your networking service options, you are ready to choose which services may be a good fit.

| Service category | What is it optimized for? | AWS networking and content delivery services |
| --- |--- |--- |
| Network foundations | Optimized for getting started with AWS networking services and connecting your VPCs securely. | [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)<br />[AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)<br />[AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) |
|  Global and hybrid connectivity  |  Optimized to ensure private, secure, and global network connectivity.  |  [AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-user-what-is.html) [AWS Cloud WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/what-is-cloudwan.html) [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)  |
| --- |--- |--- |
| Edge networking and content delivery | Optimized for low latency, reliable traffic routing to and from your workloads. | [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)<br />[AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)<br />[Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)<br />[AWS Data Transfer Terminal](https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html) |
|  Application networking  |  Optimized to ensure that your workloads are highly available, adapt to demand, and can communicate with each other.  |  [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) [Amazon VPC IPAM ](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html) [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)  |
| --- |--- |--- |
| Network security and remote access | Optimized to protect your workloads against malware, DDoS, SQL injection, and cross-site scripting attacks. | [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html)<br />[AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)<br />[AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html)<br />[AWS Verified Access](https://docs.aws.amazon.com/verified-access/latest/ug/what-is-verified-access.html)<br />[AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) |

## Use
<a name="use"></a>

To explore how to use and learn more about each of the available AWS network services, we have provided a pathway to explore how each of the services work. The following section provides links to in-depth documentation, hands-on tutorials, and resources to get you started.

The following services cover global networking and VPC connectivity.

------
#### [ Amazon CloudFront ]
+ **What is Amazon CloudFront?**

  Learn about speeding up content distribution.

  [Explore the guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
+ **Getting started with Amazon CloudFront**

  Learn the basic steps to delivering content with CloudFront.

  [Explore the guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.html)
+ **Hosting on-demand streaming video with Amazon S3, Amazon CloudFront, and Amazon Route 53**

  Learn how to host videos for on-demand viewing in a secure and scalable way.

  [Get started with the tutorial](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tutorial-s3-cloudfront-route53-video-streaming.html)
+ **Deliver content faster with Amazon CloudFront**

  Learn how to decrease the end user latency of your web applications.

  [Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/deliver-content-faster/?ref=gsrchandson)

------
#### [ AWS Cloud WAN ]
+ **What is AWS Cloud WAN?**

  Learn how to build, manage, and monitor a unified global network.

  [Explore the guide](https://docs.aws.amazon.com/network-manager/latest/cloudwan/what-is-cloudwan.html)
+ **Introducing AWS Cloud WAN**

  Learn about the main use cases for AWS Cloud WAN and how to get started.

  [Read the blog](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-cloud-wan-preview/)
+ **Getting started with AWS Cloud WAN**

  Create your first global network and attach a VPC.

  [Get started with the tutorial](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-getting-started.html)

------
#### [ Direct Connect ]
+ **What is Direct Connect?**

  Learn about connecting an on-premises network to AWS.

  [Explore the guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
+ **Getting started with Direct Connect**

  Watch a brief introduction to AWS Direct Connect and how to prepare your on-premises network to connect to AWS.

  [Watch the video](https://www.youtube.com/watch?v=y4rIwSbdlS0)
+ **Connect your data center to AWS**

  Connect your data center to AWS using Direct Connect.

  [Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/connect-data-center-to-aws/?ref=gsrchandson&id=itprohandson)

------
#### [ AWS Global Accelerator ]
+ **What is AWS Global Accelerator?**

  Learn about improving the performance of your workloads.

  [Explore the guide](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)
+ **Getting started with a standard accelerator**

  Create an accelerator to improve the network performance of a workload running on an EC2 instance.

  [Get started with the tutorial](https://docs.aws.amazon.com/global-accelerator/latest/dg/getting-started-standard.html)
+ **Improve global application availability and performance for your traffic**

  Watch a brief demonstration on setting up AWS Global Accelerator to improve network performance.

  [Watch the video](https://www.youtube.com/watch?v=Docl4julOQw)

------
#### [ AWS PrivateLink ]
+ **What is AWS PrivateLink?**

  Learn how to privately connect your VPC to services.

  [Explore the guide](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)
+ **Get started with AWS PrivateLink**

  Send a request from an EC2 instance in a private subnet to Amazon CloudWatch using PrivateLink.

  [Get started with the tutorial](https://docs.aws.amazon.com/vpc/latest/privatelink/getting-started.html)
+ **Expedite your IPv6 adoption with PrivateLink services and endpoints**

  Customers with large internet footprints feel the strain of public IPv4 address exhaustion. Learn how you can increase IPv6 usage within VPCs using PrivateLink.

  [Read the blog](https://aws.amazon.com/blogs/networking-and-content-delivery/expedite-your-ipv6-adoption-with-privatelink-services-and-endpoints/)

------
#### [ Amazon Route 53 ]
+ **What is Amazon Route 53?**

  Learn about highly available and scalable domain name resolution.

  [Explore the guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)
+ **Amazon Route 53 use case tutorials**

  How to use Route 53 for use cases based on traffic and latency.

  [Get started with the tutorial](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Tutorials.html)
+ **How to register a domain name with Amazon Route 53**

  This tutorial helps you register a new domain name for a web application.

  [Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/get-a-domain/?ref=gsrchandson&id=updated)
+ **Amazon Route 53 introduction**

  Watch a brief introduction to domain name resolution and Route 53.

  [Watch the video](https://www.youtube.com/watch?v=RGWgfhZByAI)

------
#### [ AWS Data Transfer Terminal ]
+ **What is AWS Data Transfer Terminal?**

  Learn how you can quickly upload or download large datasets to the AWS Cloud using your own storage devices.

  [Explore the guide](https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html)
+ **Introducing AWS Data Transfer Terminal**

  Learn about the main use cases and how to get started.

  [Read the blog](https://aws.amazon.com/blogs/aws/new-physical-aws-data-transfer-terminals-let-you-upload-to-the-cloud-faster/)

------
#### [ AWS Site-to-Site VPN ]
+ **What is AWS Site-to-Site VPN?**

  Learn about connecting remote users to AWS over VPN.

  [Explore the guide](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
+ **Getting started with AWS Site-to-Site VPN**

  Set up a Site-to-Site VPN connection between an on-premises device and AWS.

  [Get started with the tutorial](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html)
+ **AWS Site-to-Site VPN, choosing the right options to optimize performance**

  Choose the best options when setting up a VPN connection to AWS.

  [Read the blog](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-site-to-site-vpn-choosing-the-right-options-to-optimize-performance/)

------
#### [ AWS Transit Gateway ]
+ **What is a transit gateway?**

  Learn how to connect VPCs with transit gateways.

  [Explore the guide](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
+ **Example transit gateway use cases**

  View common use cases for transit gateways.

  [Explore the guide](https://docs.aws.amazon.com/vpc/latest/tgw/TGW_Scenarios.html)
+ **AWS Transit Gateway workshop**

  In this hands-on workshop, learn how to deploy Transit Gateway in single Region and single account, multi-account, and multi-Region setups.

  [Start the workshop](https://tgw.networking-workshop.com/#/README)

------
#### [ Amazon VPC ]
+ **What is Amazon VPC?**

  Learn about virtual private clouds and the features of Amazon VPC.

  [Explore the guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
+ **Get started with Amazon VPC**

  A guide to quickly getting started with Amazon VPC.

  [Explore the guide](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-getting-started.html)
+ **Example VPC configurations**

  View example VPC configurations based on different use cases.

  [Explore the guide](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-examples-intro.html)
+ **Modular and scalable VPC architecture**

  Build a virtual networking foundation based on AWS best practices for your AWS Cloud infrastructure.

  [Get started with the tutorial](https://aws.amazon.com/quickstart/architecture/vpc/?ref=gsrchandson)

------
#### [ Amazon VPC IPAM ]
+ **What is IPAM?**

  Learn how to track and manage IP address usage.

  [Explore the guide](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html)
+ **Amazon VPC IP Address Manager (IPAM) best practices**

  Learn how to create a scalable IP address management plan.

  [Read the blog](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-vpc-ip-address-manager-best-practices/)
+ **Creating pools to manage your IP space**

  Watch a brief video introduction to VPC IPAM.

  [Watch the video](https://www.youtube.com/watch?v=11BqzuUDTMM)

------

The following services relate to application level networking.

------
#### [ Amazon API Gateway ]
+ **What is Amazon API Gateway?**

  Learn about creating APIs for your workloads.

  [Explore the guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
+ **Building APIs with Amazon API Gateway**

  Learn how to get started building APIs in AWS.

  [Watch the video](https://www.youtube.com/watch?v=XwfpPEFHKtQ)
+ **Configuring private integrations with Amazon API Gateway HTTP APIs**

  Learn how to create an API to control private access to resources in a VPC.

  [Read the blog](https://aws.amazon.com/blogs/compute/configuring-private-integrations-with-amazon-api-gateway-http-apis/)

------
#### [ AWS Client VPN ]
+ **What is AWS Client VPN?**

  Learn about connecting networks to AWS over VPN.

  [Explore the guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)
+ **Getting started with AWS Client VPN**

  Download the AWS Client VPN application and connect to AWS over VPN.

  [Explore the guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/user-getting-started.html)
+ **Scenarios and examples for AWS Client VPN**

  See examples for creating and configuring Client VPN access for your clients.

  [Explore the examples](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/how-it-works.html#scenario)

------
#### [ Elastic Load Balancing ]
+ **What is Elastic Load Balancing?**

  Learn about distributing incoming traffic across your workloads.

  [Explore the guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
+ **Getting started with Elastic Load Balancing**

  Learn the difference between the different types of load balancers and create a load balancer.

  [Explore the guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/load-balancer-getting-started.html)
+ **How to choose the right load balancer for your AWS workloads**

  Choose the right option to load balance traffic to your workloads.

  [Watch the video](https://www.youtube.com/watch?v=p0YZBF03r5A)

------
#### [ AWS Firewall Manager ]
+ **Getting started with AWS Firewall Manager policies**

  Learn how to use AWS Firewall Manager to enable a number of different types of security policies.

  [Explore the guide](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-intro.html)
+ **How to continuously audit and limit security groups with AWS Firewall Manager**

  This blog post demonstrates how to use AWS Firewall Manager to limit security groups to help ensure that only required ports are open.

  [Explore the guide](https://aws.amazon.com/blogs/security/how-to-continuously-audit-and-limit-security-groups-with-aws-firewall-manager/)
+ **Use AWS Firewall Manager to deploy protection at scale in AWS Organizations**

  This post provides step-by-step instructions to deploy and manage security policies across your AWS Organizations implementation by using AWS Firewall Manager.

  [Explore the guide](https://aws.amazon.com/blogs/security/use-aws-firewall-manager-to-deploy-protection-at-scale-in-aws-organizations/)

------
#### [ AWS Network Firewall ]
+ **What is AWS Network Firewall?**

  Learn about network firewall and intrusion detection.

  [Explore the guide](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)
+ **Getting started with AWS Network Firewall**

  Quickly create and manage a network firewall for a VPC.

  [Get started with the tutorial](https://docs.aws.amazon.com/network-firewall/latest/developerguide/getting-started.html)
+ **AWS Network Firewall animated explainer video**

  Watch a brief video introduction to AWS Network Firewall.

  [Watch the video](https://www.youtube.com/watch?v=Y7-37tkO1CA)

------
#### [ AWS Shield ]
+ **What is AWS Shield?**

  Learn about DDoS protection.

  [Explore the guide](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html#ddos-intro)
+ **Examples of basic DDoS resilient architectures**

  Learn about some common DDoS-resilient architectures.

  [Explore the guide](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-resiliency.html)
+ **AWS Shield animated explainer video**

  Watch a brief video introduction to AWS Shield.

  [Watch the video](https://www.youtube.com/watch?v=7rgiXEa0_jE)

------
#### [ AWS Verified Access ]
+ **Tutorial: Getting started with Verified Access**

  In this tutorial, you will learn how to create and configure Verified Access resources.

  [Explore the guide](https://docs.aws.amazon.com/verified-access/latest/ug/getting-started.html)
+ **AWS Verified Access Integration with third party identity providers**

  This blog post shows you how to integrate Verified Access (AVA) with the third party Okta identity provider.

  [Explore the guide](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-verified-access-integration-with-3rd-party-identity-providers/)
+ **Integrating AWS Verified Access with device trust providers**

  This blog post discusses how to architect Zero Trust based remote connectivity on AWS.

  [Explore the examples](https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-aws-verified-access-with-device-trust-providers/)

------
#### [ Amazon VPC Lattice ]
+ **What is Amazon VPC Lattice?**

  Learn about connecting, securing, and monitoring the microservices in your workloads.

  [Explore the guide](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html)
+ **Setting up Amazon VPC Lattice**

  Set up and launch VPC Lattice for the first time.

  [Explore the guide](https://docs.aws.amazon.com/vpc-lattice/latest/ug/setting-up.html)
+ **Build secure multi-account multi-VPC connectivity for your applications with Amazon VPC Lattice**

  An introduction to how you can use VPC Lattice to solve VPC connectivity challenges.

  [Read the blog](https://aws.amazon.com/blogs/networking-and-content-delivery/build-secure-multi-account-multi-vpc-connectivity-for-your-applications-with-amazon-vpc-lattice/)
+ **Amazon VPC Lattice animated explainer**

  Watch a brief animated video about VPC Lattice.

  [Watch the video](https://www.youtube.com/watch?v=fyb20oApiZw)

------
#### [ AWS WAF ]
+ **What is AWS WAF?**

  Learn about controlling access to your workloads.

  [Explore the guide](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html#waf-intro)
+ **Getting started with AWS WAF**

  Watch a brief video on how you can use AWS WAF to protect your workloads against web exploits and bots.

  [Watch the video](https://www.youtube.com/watch?v=R5XMny416vo)
+ **Video introduction to AWS WAF**

  Watch a brief video introduction to AWS WAF.

  [Watch the video](https://www.youtube.com/watch?v=nUI7G9UzyN8)

------

## Explore
<a name="explore"></a>
+ **Architecture diagrams**

  Explore reference architecture diagrams to help you build your networking and content delivery architectures on AWS.

  [Explore architecture diagrams ](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23networking-content-dev&awsf.industries=*all&awsf.business-category=*all)
+ **Whitepapers**

  Explore whitepapers to help you get started, learn best practices, and understand your networking and content delivery options.

  [Explore whitepapers](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23whitepaper&awsf.methodology=*all&awsf.tech-category=tech-category%23networking-content-dev&awsf.industries=*all&awsf.business-category=*all)
+ **AWS Solutions**

  Explore vetted solutions and architectural guidance for common use cases for networking and content delivery.

  [Explore AWS Solutions ](https://aws.amazon.com/solutions/networking/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Decision Guides. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query decision-guides` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
