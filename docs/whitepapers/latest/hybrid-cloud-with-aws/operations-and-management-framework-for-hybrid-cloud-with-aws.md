---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-with-aws/operations-and-management-framework-for-hybrid-cloud-with-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Operations and management framework for hybrid cloud with AWS
<a name="operations-and-management-framework-for-hybrid-cloud-with-aws"></a>

 The operations and management framework detailed here identifies the building blocks for architecting and implementing a hybrid cloud environment with AWS. This framework helps you identify the components and the corresponding considerations for building a hybrid cloud with AWS. This section also identifies AWS services and solutions to address the needs for each building block.

![Operations and management framework for hybrid cloud with AWS](http://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-with-aws/images/hybrid-cloud-framework.png)

* Operations and management framework for hybrid cloud with AWS *

 [AWS Outposts](https://aws.amazon.com/outposts/) vertically integrates across the layers of this framework by providing a hybrid cloud solution that brings [AWS infrastructure](https://aws.amazon.com/blogs/compute/running-aws-infrastructure-on-premises-with-aws-outposts/), [security](https://docs.aws.amazon.com/outposts/latest/userguide/security.html), [services](https://aws.amazon.com/outposts/features/), [APIs](https://docs.aws.amazon.com/outposts/latest/APIReference/Welcome.html), [management tools](https://aws.amazon.com/products/management-tools/), [support](https://aws.amazon.com/premiumsupport/) and [operating model](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-operations-integration/migration-operations-integration.pdf) to data centers, co-location spaces, or on-premises facilities. AWS Outposts eliminates the undifferentiated heavy-lifting associated with building software and systems to integrate infrastructure in a hybrid cloud environment. It provides security, performance, and operational consistencies across the hybrid environment, while addressing the needs of running applications seamlessly on-premises or the AWS Cloud.

## Hybrid cloud infrastructure
<a name="hybrid-cloud-infrastructure"></a>

 Physical infrastructure deployed on-premises and in AWS Regions provide the infrastructural foundation for a hybrid cloud. The network interconnecting these infrastructures enables traffic exchange within the hybrid environment.

### On-premises and AWS infrastructure
<a name="on-premises-and-aws-infrastructure"></a>

 The customer infrastructure includes compute servers, storage nodes, networking devices, and edge computing devices. This infrastructure is hosted in customer-owned or leased facilities, manufacturing/retail facilities, or in spaces near end-users.

 [AWS global infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) consists of more than 24 geographical regions and 77 Availability Zones as of September 2020. AWS infrastructure provides a global edge network (currently 216 [points of presence](https://en.wikipedia.org/wiki/Point_of_presence)) to AWS customers for accelerating content delivery, domain name services, global load balancing, and security.

 For on-premises infrastructure, you can deploy AWS hardware through AWS Outposts. AWS also provides edge computing infrastructure with [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/), AWS Wavelength, AWS Snowball Edge Edge and AWS IoT Greengrass.

### Network
<a name="network"></a>

 The network interconnecting on-premises infrastructure with AWS can be through dedicated physical connections, VPN, or over the internet.

 With [AWS Direct Connect](https://aws.amazon.com/directconnect/), you can establish a private virtual interface from your on-premises network directly to your Amazon VPC. This provides an elastic, simple, and consistent network experience that can also increase bandwidth throughput. With [AWS site-to-site virtual private network (VPN)](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html), you can create an IPsec VPN connection between your Amazon VPC and your on-premises network over the internet. Additionally, some applications, especially those leveraging IoT technologies, use the public internet to exchange traffic with AWS resources such as [AWS service endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) and public EC2 instances.
