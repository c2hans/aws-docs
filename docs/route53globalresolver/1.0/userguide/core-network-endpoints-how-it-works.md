---
source_url: https://docs.aws.amazon.com/route53globalresolver/1.0/userguide/core-network-endpoints-how-it-works.html
---

# How core network endpoints work

A Cloud WAN core network is a managed, global network that connects your virtual private clouds (VPCs), AWS Regions, and on-premises locations. A core network is divided into *segments*, which are isolated routing domains that group network traffic.

When you create a core network endpoint, the global resolver connects to the core network that you specify. Amazon Route 53 Global Resolver then makes the core network's segments available as access sources. You can reference a segment as an access source in your access control configuration, so that clients reaching the global resolver from that segment are authorized to resolve DNS queries. Because a global resolver runs across the AWS Regions that you choose, the connected segments are available as access sources in each of those Regions.
