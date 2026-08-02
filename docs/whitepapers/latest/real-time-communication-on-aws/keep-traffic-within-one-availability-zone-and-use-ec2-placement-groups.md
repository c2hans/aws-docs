---
source_url: https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/keep-traffic-within-one-availability-zone-and-use-ec2-placement-groups.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Keep traffic within one Availability Zone and use EC2 placement groups
<a name="keep-traffic-within-one-availability-zone-and-use-ec2-placement-groups"></a>

Also known as Availability Zone Affinity, this best practice also applies to the rare event of a complete Availability Zone failure. It is recommended that you eliminate any cross-AZ traffic such that any SIP or RTP traffic that enters one Availability Zone should remain in that Availability Zone until it exits the Region.

![A diagram depicting Availability Zone affinity (at most, 50% of active calls are lost) .](http://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/images/availability-zone-affinity.png)

The preceding figure shows a simplified architecture that uses Availability Zone affinity. The comparative advantage of this approach becomes clear if one accounts for the effects of a complete Availability Zone outage. As depicted in the diagram, if Availability Zone 2 is lost, 50% of active calls are affected at most (assuming equal load balancing between Availability Zones). Had Availability Zone Affinity not been implemented, some calls would flow between Availability Zones in one Region and a failure would most likely affect more than 50% of active calls.

To minimize latency for traffic, AWS also recommends that you consider using [EC2 placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) within each Availability Zone. Instances launched within the same EC2 placement group have higher bandwidth and reduced latency as EC2 ensures network proximity of these instances relative to each other.
