---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-global-tables/resources.html
---

# Conclusion and resources
<a name="resources"></a>

DynamoDB global tables have very few controls but still require careful consideration. You must determine your write mode, routing model, and evacuation processes. You must instrument your application across every Region and be ready to adjust your routing or perform an evacuation to maintain global health. The reward is having a globally distributed dataset with low-latency read and write operations that is designed for 99.999% availability.

For more information about DynamoDB global tables, see the following resources:
+ [Amazon DynamoDB documentation](https://docs.aws.amazon.com/dynamodb/index.html)
+ [Amazon Application Recovery Controller (ARC)](https://aws.amazon.com/route53/application-recovery-controller/)
+ [ARC readiness checks](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.html) (AWS documentation)
+ [Route 53 routing policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html)
+ [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/)
+ [DynamoDB service-level agreement](https://aws.amazon.com/dynamodb/sla/)
+ [AWS Multi-Region Fundamentals](https://docs.aws.amazon.com/whitepapers/latest/aws-multi-region-fundamentals/aws-multi-region-fundamentals.html) (AWS whitepaper)
+ [Data resiliency design patterns with AWS](https://www.youtube.com/watch?v=7IA48SOX20c) (AWS re:Invent 2022 presentation)
+ [How Fidelity Investments and Reltio modernized with Amazon DynamoDB](https://youtu.be/QUpV5MDu4Ys?t=706) (AWS re:Invent 2022 presentation)
+ [Multi-Region design patterns and best practices](https://youtu.be/ilgpzlE7Hds?t=1882) (AWS re:invent 2022 presentation)
+ [Disaster Recovery (DR) Architecture on AWS, Part III: Pilot Light and Warm Standby](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-iii-pilot-light-and-warm-standby/) (AWS blog post)
+ [Use Region pinning to set a home Region for items in an Amazon DynamoDB global table](https://aws.amazon.com/blogs/database/use-region-pinning-to-set-a-home-region-for-items-in-an-amazon-dynamodb-global-table/) (AWS blog post)
+ [Monitoring Amazon DynamoDB for operational awareness](https://aws.amazon.com/blogs/database/monitoring-amazon-dynamodb-for-operational-awareness/) (AWS blog post)
+ [Scaling DynamoDB: How partitions, hot keys, and split for heat impact performance](https://aws.amazon.com/blogs/database/part-3-scaling-dynamodb-how-partitions-hot-keys-and-split-for-heat-impact-performance/) (AWS blog post)
+ [Multi-Region strong consistency with Amazon DynamoDB global tables](https://www.youtube.com/watch?v=R-nTs8ZD8mA) (AWS re:Invent 2024 presentation)
