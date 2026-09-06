---
source_url: https://docs.aws.amazon.com/whitepapers/latest/semiconductor-design-on-aws/high-availability-and-durability.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# High availability and durability
<a name="high-availability-and-durability"></a>

The AWS Global Infrastructure spans multiple locations worldwide. These locations include [Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/). Each AWS Region is a separate geographic area around the world, such as Oregon, Virginia, Ireland, and Singapore. AWS Regions are designed to be completely isolated from other Regions. Each Region has at least two Availability Zones, each including one or more data centers, that are fully interconnected with a low latency network. As of this writing, AWS has 24 Regions and 77 Availability Zones around the world. This design achieves the greatest possible fault tolerance and stability.

AWS gives you the ability to place resources, such as compute capacity and data storage, in multiple Availability Zones within a region with single millisecond latency between Availability Zones. You can protect against failures and ensure you have enough capacity to run your most compute-intensive workflows by taking advantage of multiple Regions and multiple Availability Zones. This large global footprint enables you to position computing resources near your IC design engineers in locations where low-latency performance is important. For updated information, see the [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/?hp=tile) page.
