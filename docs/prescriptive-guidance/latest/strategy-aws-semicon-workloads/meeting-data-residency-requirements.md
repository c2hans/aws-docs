---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-semicon-workloads/meeting-data-residency-requirements.html
---

# Meeting data residency requirements on AWS
<a name="meeting-data-residency-requirements"></a>

The available partitions, AWS Regions, Availability Zones, and Local Zones allow companies to choose the best location for their data and workloads based on their unique requirements:
+ A [partition](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/partitions.html) is a logical group of AWS Regions. AWS commercial Regions are in the `aws` partition, Regions in China are in the `aws-cn` partition, and AWS GovCloud (US) Regions are in the `aws-us-gov` partition.
+ An [AWS Region](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/regions.html) is a separate geographic area where AWS clusters data centers.
+ Each AWS Region has multiple, isolated locations known as [Availability Zones](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/availability-zones.html).
+ A [Local Zone](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/aws-local-zones.html) is an extension of a Region that is geographically close to your users.

For more information about the currently available Regions, Availability Zones, and Local Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

A partition provides data, network, and machine isolation from Regions in other partitions. AWS partitions create logical network isolation with separate credentialed access between Regions in the different partitions. Partitions include one or more Regions, but an AWS Region exists only within one partition; an AWS Region cannot be a part of two partitions.

![Diagram of how AWS partitions logically and physically separate AWS Regions into isolated groups](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-semicon-workloads/images/guide-img/f421e0e1-7aa6-442a-ac92-5451f69fd602/images/7687c04e-2385-414f-93af-293e2ea75106.png)

You can choose between partitions based on whether a United States government security classification is required. Workloads processing [unclassified or official data](https://docs.aws.amazon.com/whitepapers/latest/data-classification/aws-recommendations.html) can use both the AWS GovCloud (US) or standard partitions. AWS also offers additional partitions accredited to operate workloads at the Secret and Top-Secret US security classification levels, but these are out of scope for this guide. For more information about operating workloads at these classification levels, see [Cloud Computing for US Defense](https://aws.amazon.com/federal/defense/) and [Cloud Computing for the US Intelligence Community](https://aws.amazon.com/federal/us-intelligence-community/).

We recommend deploying multi-Region workloads within a single partition to reduce any compliance, operational, and technical challenges. However, there are limited use cases, such as with [AWS Direct Connect](https://aws.amazon.com/blogs/publicsector/aws-hybrid-connectivity-sharing-aws-direct-connect-aws-govcloud-us-commercial-regions/) or [Amazon CloudFront](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/setting-up-cloudfront.html), where you can integrate services across multiple to meet specific objectives. For more information, contact your AWS Solutions Architect.
