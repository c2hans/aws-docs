---
source_url: https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/high-availability-and-scalability-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# High availability and scalability on AWS
<a name="high-availability-and-scalability-on-aws"></a>

 Most providers of real-time communications align with service levels that provide availability from 99.9% to 99.999%. Depending on the degree of high availability (HA) that you want, you must take increasingly sophisticated measures along the full lifecycle of the application. AWS recommends following these guidelines to achieve a robust degree of high availability:
+  Design the system to have no single point of failure. Use automated monitoring, failure detection, and failover mechanisms for both stateless and stateful components
  +  Single points of failure (SPOF) are commonly eliminated with an N\+1 or 2N redundancy configuration, where N\+1 is achieved via load balancing among *active–active* nodes, and 2N is achieved by a pair of nodes in *active–standby* configuration.
  +  AWS has several methods for achieving HA through both approaches, such as through a scalable, load balanced cluster or assuming an *active–standby* pair.
+  Correctly instrument and test system availability.
+  Prepare operating procedures for manual mechanisms to respond to, mitigate, and recover from the failure.

 This section focuses on how to achieve no single point of failure using capabilities available on AWS. Specifically, this section describes a subset of core AWS capabilities and design patterns that allow you to build highly available real-time communication applications.
