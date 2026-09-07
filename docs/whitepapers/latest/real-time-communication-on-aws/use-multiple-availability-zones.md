---
source_url: https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/use-multiple-availability-zones.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Use multiple Availability Zones
<a name="use-multiple-availability-zones"></a>

Each AWS Region is subdivided into separate Availability Zones. Each Availability Zone has its own power, cooling, and network connectivity and thus forms an isolated failure domain. Within the constructs of AWS, customers are encouraged to run their workloads in more than one Availability Zone. This ensures that customer applications can withstand even a complete Availability Zone failure - a very rare event in itself. This recommendation stands for real-time SIP infrastructure as well.

![A diagram depicting handling Availability Zone failure .](https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/images/handling-az-failure.png)

Suppose a catastrophic event (such as category five hurricane) causes a complete Availability Zone outage in the us-east-1 Region. With the infrastructure running as shown in the diagram, all SIP clients that were originally registered with the nodes in the failed Availability Zone should re-register with the SIP nodes running in Availability Zone \#2. (Test this behavior with your SIP clients/phones to make sure it is supported.) Although the active SIP calls at the time of the Availability Zone outage are lost, any new calls are routed through Availability Zone 2.

To summarize, DNS SRV records should point the client to multiple ‘A’ records, one in each Availability Zone. Each of those ‘A’ records should, in turn, point to multiple IP addresses of SBCs/PBXs in that Availability Zone providing both intra- and inter-Availability Zone resiliency. Both intra- and inter-Availability Zone failover can be implemented by using IP reassignment if the IPs are public. Private IPs, however, cannot be reassigned across Availability Zones. If a customer is using private IP addressing, then they would have to rely on the SIP clients re-registering with the backup SBC/PBX for inter-Availability Zone failover.
