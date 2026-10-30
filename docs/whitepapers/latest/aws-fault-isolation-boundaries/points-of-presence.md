---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/points-of-presence.html
---

# Points of presence
<a name="points-of-presence"></a>

In addition to the AWS Regions and Availability Zones, AWS also operates a globally distributed point of presence (PoP) network. These PoPs host [Amazon CloudFront](https://aws.amazon.com/cloudfront/), a content delivery network (CDN); [Amazon Route 53](https://aws.amazon.com/de/route53/), a public DNS resolution service; and [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/), an edge networking optimization service. The global edge network currently consists of over 700 PoPs and 13 Regional Edge Caches (REC) in over 100 cities across 50 countries (current status can be found at [Amazon CloudFront Key Features](https://aws.amazon.com/cloudfront/features/)). In addition to CloudFront PoPs, there are over 900 embedded PoPs across over 300 cities in North America, Europe, and Asia. The following figure shows the global distribution of the Amazon CloudFront edge network.

![This image shows the Amazon CloudFront global edge network](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/images/amazon-cloudfront.png)

 Each PoP is isolated from the others, which means a failure affecting a single PoP or metropolitan area doesn’t impact the rest of the global network. The AWS network peers with thousands of Tier 1, 2, and 3 telecom carriers globally, is well connected with all major access networks for optimal performance, and has hundreds of terabits of deployed capacity. Edge locations are seamlessly connected to AWS Regions through the fully redundant AWS network backbone. This backbone is composed of multiple 400 GbE parallel fibers across the globe and interfaces with tens of thousands of networks.
