---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/resiliency.html
---

# Resiliency in MES
<a name="resiliency"></a>

Resiliency is the ability of an MES system to recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions such as misconfigurations or transient network issues. Resiliency is the primary factor that the reliability pillar of the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) depends on.

Resiliency can be divided into two main factors: availability and disaster recovery. Both areas rely on some of the same best practices, such as monitoring for failures, deploying to multiple locations, and automatic failover. However, availability focuses on components of MES microservices, whereas disaster recovery focuses on discrete copies of the entire microservice or even the whole MES system.

## Availability
<a name="availability"></a>

We define *availability* as the percentage of time that a microservice is available for use, as represented in the following formula. This percentage is calculated over a period of time, such as a month, a year, or trailing three years.

![Availability formula for MES architectures](http://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/images/guide-img/093538ca-c7c9-4311-a0e9-8a876ae66d65/images/483b039c-b09f-4d6a-baf8-d22e904d76e2.png)

This formula requires an understanding of three metrics that are common in manufacturing and equipment maintenance:
+ **Mean time between failures (MTBF)**: The average time between the start of regular operations for a microservice and its subsequent failure.
+ **Mean time to detect (MTTD)**: The average time between the occurrence of a failure and the start of repair operations.
+ **Mean time to repair (MTTR)**: The average time between the unavailability of a microservice because of a failed subsystem and its repair or return to service. MTTD is a subset of MTTR.

The following diagram illustrates these availability metrics.

![Availability metrics for MES architectures](http://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/images/guide-img/093538ca-c7c9-4311-a0e9-8a876ae66d65/images/1e1bd0c7-3d3d-4cc8-8fdb-63d8f876748c.png)

A resilient, highly available MES aims to reduce MTTR and MTTD and increase MTBF. Although an ideal design would eliminate failures, it isn't realistic. The traditional, monolithic MES failures were hard to detect and took longer to repair. Modern, cloud-native MES allows for faster detection, quick repairs, and business continuity through Multi-AZ deployments. For best practices for highly available modern systems with relevant AWS services , see the white paper, [Availability and Beyond: Understanding and Improving the Resilience of Distributed Systems on AWS](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/availability-and-beyond-improving-resilience.html).

## Disaster recovery
<a name="disaster-recovery"></a>

Disaster recovery refers to the process of preparing for, and recovering from, a technology-related disaster such as a major hardware or software failure. An event that prevents a microservice, or MES, from fulfilling its business objectives in its primary deployed location is considered a disaster. Disaster recovery is different from availability and is measured by these two metrics:
+ **Recovery time objective (RTO)**: The acceptable delay between a microservice interruption and a microservice restoration. RTO determines what is considered an acceptable time window when service is unavailable.
+ **Recovery point objective (RPO)**: The maximum acceptable amount of time since the last data recovery point. RPO determines what is considered an acceptable data loss between the last recovery point and the interruption of microservices.

The following diagram illustrates these disaster recovery metrics.

![Disaster recovery metrics for MES architectures](http://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/images/guide-img/093538ca-c7c9-4311-a0e9-8a876ae66d65/images/8592c06c-39b2-4063-afd7-515c68904d85.png)

The following diagram depicts different disaster recovery strategies.

![Disaster recovery strategies for MES architectures](http://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/images/guide-img/093538ca-c7c9-4311-a0e9-8a876ae66d65/images/5b21738d-6f99-411c-982a-59c8a173780f.png)

You can find detailed guidance on implementing these strategies in the AWS Well-Architected Framework guide, [Disaster Recovery of Workloads on AWS: Recovery in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html).
