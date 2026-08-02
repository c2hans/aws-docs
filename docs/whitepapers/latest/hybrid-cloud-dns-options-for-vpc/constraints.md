---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/constraints.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Constraints
<a name="constraints"></a>

 In addition to the concepts established so far, it is important to understand some constraints that are key in shaping the rest of this whitepaper and its solutions.

## Packet per second (PPS) per elastic network interface limit
<a name="packet-per-second-pps-per-elastic-network-interface-limit"></a>

 Each network interface in an Amazon VPC has a hard limit of 1024 packets that it can send to the Amazon-provided DNS server every second. Therefore, a computing resource on AWS that has a network interface attached to it and is sending traffic to the Amazon DNS resolver (for example, an Amazon EC2 instance or [AWS Lambda](https://aws.amazon.com/lambda/) function) falls under this hard-limit restriction. In this whitepaper, we refer to this limit as packet per second (PPS) per network interface. When you’re designing a scalable solution for name resolution, you must consider this limit, because failure to do so can result in queries to Route 53 Resolver going unanswered if the limit is reached. This limit is a key factor to be considered for the solutions proposed in this whitepaper. This limit is higher for Route 53 resolver endpoints, which have a limit of approximately 10,000 queries per second (QPS) per elastic network interface.

## Connection tracking
<a name="connection-tracking-1"></a>

 The number of simultaneous stateful connections that an Amazon EC2 security group can support by default is an extremely large value that the majority of standard TCP-based customers never encounter any issues with. In rare cases, customers with restrictive security group policies and applications that create a large number of concurrent connections, for instance a self-managed recursive DNS server, might run into issues of exhausting all simultaneous connection tracking resources. When that limit is exceeded, subsequent connections fail silently. In such cases, we recommend that you have a security group set up that you can use to disable connection tracking. To do this, set up permissive rules on both inbound and outbound connections.

## Linux resolver
<a name="linux-resolver-1"></a>

 The default maximum number of DNS servers that you can specify in the resolv.conf configuration file of a Linux resolver is three, which means it isn’t useful to specify four DNS servers in the DHCP options set because the additional DNS server won’t be used. This limit further places an upper boundary on some of the solutions discussed in this whitepaper. It is also key to note that different operating systems can handle the assignment and failover of DNS queries differently.
