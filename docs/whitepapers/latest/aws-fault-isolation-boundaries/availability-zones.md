---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/availability-zones.html
---

# Availability Zones
<a name="availability-zones"></a>

 AWS operates over 100 Availability Zones within several Regions around the world (current numbers can be found here: [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)). An Availability Zone is one or more discrete data centers with separate and redundant power infrastructure, networking, and connectivity in an AWS Region. Availability Zones in a Region are meaningfully distant from each other, up to 60 miles (\~100 km) to prevent correlated failures, but close enough to use synchronous replication with single-digit millisecond latency. They are designed not to be simultaneously impacted by a shared fate scenario like utility power, water disruption, fiber isolation, earthquakes, fires, tornadoes, or floods. Common points of failure, like generators and cooling equipment, are not shared across Availability Zones and are designed to be supplied by different power substations. When AWS deploys updates to its services, deployments to Availability Zones in the same Region are separated in time to prevent correlated failure.

 All Availability Zones in a Region are interconnected with high-bandwidth, low-latency networking, over fully redundant, dedicated metro fiber. Each Availability Zone in a Region connects to the internet through two transit centers where AWS peers with multiple [tier-1 internet providers](https://en.wikipedia.org/wiki/Tier_1_network) (for more information, refer to [Overview of Amazon Web Services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html?did=wp_card&trk=wp_card)*)*.

 These features provide strong isolation of Availability Zones from each other, which we refer to as Availability Zone Independence (AZI). The logical construct of Availability Zones and their connectivity to the internet is depicted in the following figure.

![This image shows how Availability Zones consist of one or more physical data centers that are redundantly connected to each other and the internet](http://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/images/availability-zones.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
