---
source_url: https://docs.aws.amazon.com/route53globalresolver/1.0/userguide/disaster-recovery-resiliency.html
---

# Resilience in Amazon Route 53 Global Resolver

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

In addition to the AWS global infrastructure, Amazon Route 53 Global Resolver offers several features to help support your data resiliency and backup needs.

## Global availability and anycast routing
<a name="global-availability"></a>

Amazon Route 53 Global Resolver is designed as a globally available service that provides high availability and automatic failover capabilities:
+ **Global anycast IP addresses** - Amazon Route 53 Global Resolver uses global anycast IP addresses that automatically route DNS queries to the nearest available AWS Region, providing built-in geographic redundancy.
+ **Multi-Region deployment** - You can instantiate Amazon Route 53 Global Resolver in multiple AWS Regions simultaneously, ensuring service availability even if an entire Region becomes unavailable.
+ **Automatic routing optimization** - Queries are automatically routed to the closest geographic location, reducing latency and providing natural disaster recovery capabilities.

## DDoS protection and threat mitigation
<a name="ddos-protection"></a>

Amazon Route 53 Global Resolver includes multiple layers of protection against distributed denial-of-service (DDoS) attacks:
+ **AWS Shield integration** - Amazon Route 53 Global Resolver leverages AWS Shield to protect against common DDoS attacks at the network and transport layers.
+ **Dynamic DDoS mitigation** - Custom dynamic protection using top talker metrics and rate limiting allows Amazon Route 53 Global Resolver to quickly respond to high-volume attacks from specific source IPs.
+ **Built-in throttling and load shedding** - Automatic throttling and load shedding mechanisms help maintain service availability during attack conditions.

## Configuration backup and recovery
<a name="data-backup-recovery"></a>

Amazon Route 53 Global Resolver configuration data is automatically backed up and replicated across multiple AWS Regions:
+ **Automatic configuration replication** - DNS views, firewall rules, domain lists, and other configuration data are automatically replicated across Regions where your Amazon Route 53 Global Resolver is deployed.
+ **Cross-Region private hosted zone resolution** - Private hosted zones can be resolved globally across AWS Regions, providing redundancy for private DNS resolution.
+ **Log delivery redundancy** - Query logs can be delivered to multiple destinations (Amazon CloudWatch, Amazon Simple Storage Service, Amazon Data Firehose) to ensure audit trail preservation even during service disruptions.

## Future expansion for enhanced resilience
<a name="service-expansion"></a>

Amazon Route 53 Global Resolver will continue to expand its global footprint to provide even greater resilience:
+ **Additional Regions** - Service will expand to additional AWS Regions including opt-in regions and AWS GovCloud (US) partition.
+ **Local Zones and Edge locations** - Future expansion to AWS Local Zones and Edge Points of Presence (PoP) will provide even closer geographic proximity and enhanced resilience.
