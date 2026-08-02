---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/assessment-engineering-ops.html
---

# Operational excellence metrics related to network access for SaaS offerings
<a name="assessment-engineering-ops"></a>

## Operational resilience and disaster recovery
<a name="assessment-engineering-ops-resilience"></a>

The network access approach should help the SaaS offering withstand various types of disruptions and quickly recover from any disasters.

### High-score criteria
<a name="high-score-criteria.7b6d4628-4b85-5f2d-98bd-76ad4fd3a60a"></a>

Established and tested disaster recovery plans consistently show that the network access approach meets the disaster recovery requirements. The network access approach supports high-availability configurations, and it supports automatic, quick, and reliable failover mechanisms.

### Low-score indicators
<a name="low-score-indicators.3911fe42-471e-5735-a246-2e1ef64d01b8"></a>

The network access approach makes it difficult to build a coherent disaster recovery strategy. You observe prolonged recovery times after disruptions. Frequent operational failures of the network infrastructure are impacting service delivery.

### Self-assessment questions
<a name="self-assessment-questions.a9ac7284-fe94-528d-ab24-970fdac6f306"></a>
+ When was the last disaster recovery drill, and what were the outcomes?
+ How long does it take to recover critical services after a disruption? What portion of the network infrastructure needs to be redeployed?
+ What improvements can be made to the network infrastructure to streamline your disaster recovery plans?
+ Are redundancies in place for the most critical network components?
+ Have you automated the potential redeployment of network infrastructure after a critical outage?
+ How does the network access approach support fault tolerance and reliability? Are there built-in mechanisms to handle network interruptions and maintain data integrity?

## Service and application performance monitoring
<a name="assessment-engineering-ops-monitoring"></a>

The networking access approach can affect the performance monitoring tools that are used to validate optimal operation and service uptime. Depending on the service, you might have access to low-level metrics (such as packet drop rates) or higher-level metrics (such as session duration). Low-level metrics provide detailed technical insight into network behavior but can be complex to interpret. In contrast, higher-level metrics often offer a more direct and easier way to gauge overall user experience. This is because they aggregate the impact of underlying network conditions into clear indicators of service quality.

### High-score criteria
<a name="high-score-criteria.fa419569-0c85-5fdf-b1c5-b03c8a0d09cb"></a>

Comprehensive monitoring tools that provide near real-time insights are readily available. You have automated alerts and response systems that address performance issues. You can predict potential service bottlenecks or failures before they affect users.

### Low-score indicators
<a name="low-score-indicators.00e6ae46-5f81-56aa-8d0c-c9d1a0a67e6d"></a>

Frequent service interruptions or performance issues happen without being observed or acted upon. The lack of visibility into service performance results in slow response to performance bottlenecks. Multi-party teams are required to troubleshoot network infrastructure issues.

### Self-assessment questions
<a name="self-assessment-questions.c83f9ba3-afa8-57b4-a8b8-6907f0845419"></a>
+ Which monitoring tools and network infrastructure metrics are currently available? How effective are they at detecting service anomalies?
+ How quickly can you identify and resolve performance issues?
+ Do you have mechanisms in place that predict potential performance problems?
+ What improvements can you make to enhance observability capabilities?
