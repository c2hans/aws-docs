---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/availability-zones.html
---

# Availability Zones
<a name="availability-zones"></a>

 AWS operates over 100 Availability Zones within multiple AWS Regions worldwide (current numbers can be found at [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)). An Availability Zone is one or more discrete data centers with independent and redundant power infrastructure, networking, and connectivity in an AWS Region. Availability Zones in a Region are meaningfully distant from each other, up to 60 miles (about 100 km) to prevent correlated failures, but close enough to use synchronous replication with single-digit millisecond latency. They’re designed to avoid simultaneous impact from shared fate scenarios such as utility power, water disruption, fiber isolation, earthquakes, fires, tornadoes, or floods. Common points of failure, like generators and cooling equipment, aren’t shared across Availability Zones and are designed to be supplied by different power substations. When AWS deploys updates to its services, deployments to Availability Zones in the same Region are separated in time to prevent correlated failure.

 Availability Zones in a Region are interconnected with high-bandwidth, low-latency networking, over fully redundant, dedicated metro fiber. Each Availability Zone in a Region connects to the internet through two transit centers where AWS peers with multiple [tier-1 internet providers](https://en.wikipedia.org/wiki/Tier_1_network) (for more information, see [Overview of Amazon Web Services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html?did=wp_card&trk=wp_card)).

 These features provide strong isolation of Availability Zones from each other, which we refer to as Availability Zone Independence (AZI). The logical construct of Availability Zones and their connectivity to the internet is depicted in the following figure.

![This image shows how Availability Zones consist of one or more physical data centers that are redundantly connected to each other and the internet](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/images/availability-zones.png)

 Availability Zones give you the ability to operate production applications that are more highly available, fault tolerant, and scalable than would be possible from a single data center. When your application uses multiple Availability Zones, it’s better isolated and protected from issues that impact a single Availability Zone’s physical infrastructure. This helps you build services that are redundant across Availability Zones and, if architected correctly, remain operational even if one Availability Zone experiences failures.
