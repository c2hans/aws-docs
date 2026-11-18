---
source_url: https://docs.aws.amazon.com/route53globalresolver/1.0/userguide/how-it-works.html
---

# How Amazon Route 53 Global Resolver works
<a name="how-it-works"></a>

Amazon Route 53 Global Resolver enables split-traffic DNS resolution between public and private domains, provides high availability through through the two or more AWS Regions you choose, and secures DNS queries by intercepting requests and applying DNS filtering policies. Understanding this process helps you troubleshoot issues and optimize your deployment for performance, availability, and security.

## What happens when clients make DNS queries
<a name="dns-query-flow"></a>

When someone at your location tries to query domain, Amazon Route 53 Global Resolver processes their DNS request through multiple security layers.

The DNS query processing involves these sequential steps:

1. **Query reception** - Client devices send DNS queries to Amazon Route 53 Global Resolver anycast IP addresses. The anycast routing automatically directs queries to the nearest AWS Region.

1. **Authentication** - Amazon Route 53 Global Resolver authenticates the client using configured authentication methods (token-based for DoH/DoT or IP Access Source for all protocols).

1. **Policy evaluation** - The service evaluates DNS queries against configured security policies and domain lists to determine the appropriate action (allow, block, or alert). For queries targeting private hosted zones, Amazon Route 53 Global Resolver checks if the client is authorized to access the private domain based on the DNS view rule managed by your administrator before proceeding with resolution.

1. **Resolution** - For allowed queries, Amazon Route 53 Global Resolver performs DNS resolution using public DNS resolvers or private hosted zone resolution as appropriate.

1. **Response delivery** - The service returns the DNS response to the client and logs the query details for monitoring and analysis.

## Global anycast architecture
<a name="anycast-architecture"></a>

Amazon Route 53 Global Resolver uses anycast IP addresses to provide global availability and automatic geographic routing.

Amazon Route 53 Global Resolver uses anycast IP addresses to provide:
+ **Automatic geographic routing** - DNS queries are automatically routed to the closest AWS Region for optimal performance.
+ **Built-in redundancy** - If a Region becomes unavailable, traffic automatically fails over to the next closest Region.
+ **Consistent IP addresses** - Clients use the same anycast IP addresses regardless of their location, simplifying configuration.

## Private anycast architecture with Cloud WAN
<a name="private-anycast-architecture"></a>

When clients reach the global resolver over private connections through an AWS Cloud WAN core network, Amazon Route 53 Global Resolver uses the same anycast-based geographic routing to direct queries to the closest AWS Region.

Private IP addresses are resolved with the same routing and availability benefits as public internet traffic, over private Cloud WAN connectivity instead of the internet:
+ **Automatic geographic routing** - DNS queries from a connected core network are automatically routed to the closest AWS Region for optimal performance.
+ **Built-in redundancy** - If a Region becomes unavailable, traffic automatically fails over to the next closest Region.
+ **Consistent endpoints** - Clients use the same anycast IP addresses regardless of their location, simplifying configuration.

## DNS filtering and security
<a name="filtering-and-security"></a>

Amazon Route 53 Global Resolver provides comprehensive DNS filtering and security through multiple layers. The DNS filtering and security architecture diagram illustrates how queries are processed through authentication, policy evaluation, and resolution layers.

![DNS filtering and security architecture diagram. Shows client queries processed through Global Resolver with three main processing layers: authentication layer with token validation and IP Access Source checks, policy engine with DNS filtering rules and domain lists, and resolution layer with public DNS and private hosted zone resolution. The system is supported by AWS managed domain lists for threats and content categories, custom domain lists, and real-time threat intelligence feeds.](https://docs.aws.amazon.com/route53globalresolver/1.0/userguide/images/dns-filtering-security.png)

Amazon Route 53 Global Resolver provides comprehensive DNS security through:
+ **Domain-based filtering** - Block or allow queries based on domain names using custom or AWS managed domain lists.
+ **Threat intelligence integration** - Leverage AWS managed threat intelligence to automatically block known malicious domains.
+ **Advanced threat detection** - Detect and block DNS tunneling attempts and Domain Generation Algorithm (DGA) patterns.
+ **Real-time monitoring** - Generate alerts and logs for security events and policy violations.
