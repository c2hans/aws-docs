---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-multi-region-fundamentals/single-region-resilience.html
---

# Engineering and operating for resilience in a single Region
<a name="single-region-resilience"></a>

Before you dive into multi-Region concepts, start by confirming that your workload is already as resilient as possible in a single Region. To achieve this, evaluate your workload against the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) and [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) of the AWS Well-Architected Framework, and make any necessary changes based on trade-offs and risk assessment. The following concepts are covered in the AWS Well-Architected Framework:
+ [Workload segmentation based on domain boundaries](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-your-workload-service-architecture.html)
+ [Well-defined service contracts](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-your-workload-service-architecture.html)
+ [Dependency management and coupling](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-interactions-in-a-distributed-system-to-prevent-failures.html)
+ [Handling failures, retries, and back-off strategies](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-interactions-in-a-distributed-system-to-mitigate-or-withstand-failures.html)
+ [Idempotent operations and stateful versus stateless transactions](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-interactions-in-a-distributed-system-to-mitigate-or-withstand-failures.html)
+ [Operational readiness and change management](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/operational-readiness.html)
+ [Understanding workload health](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/understanding-operational-health.html)
+ [Responding to events](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/responding-to-events.html)

To take single-Region resilience further, review and apply the concepts that are discussed in the paper [Advanced Multi-AZ Resilience Patterns: Detecting and Mitigating Gray Failures](https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/advanced-multi-az-resilience-patterns.html). This paper provides best practices for using replicas in each Availability Zone to contain failures and expands on multi-AZ concepts that are introduced in the AWS Well Architected Framework. Although a multi-Region architecture can mitigate failure modes that are bound to Availability Zones, there are trade-offs that come with a multi-Region approach that you should consider. That is why we recommend that you start with a multi-AZ approach, and then evaluate a specific workload against fundamentals for multi-Region architectures to determine if a multi-Region approach can increase the workload's resilience.
