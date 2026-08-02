---
source_url: https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/cost-optimization-sustainability.html
---

# Cost optimization and sustainability
<a name="cost-optimization-sustainability"></a>

 Microservices architecture can enhance cost optimization and sustainability. By breaking an application into smaller parts, you can scale up only the services that need more resources, reducing cost and waste. This is particularly useful when dealing with variable traffic. Microservices are independently developed. So developers can do smaller updates, and reduce the resources spent on end to end testing. While updating they will have to test only a subset of the features as opposed to monoliths.

 Stateless components (services that store state in an external data store instead of a local data store) in your architecture can make use of Amazon EC2 Spot Instances, which offer unused EC2 capacity in the AWS cloud. These instances are more cost efficient than on-demand instances and are perfect for workloads that can handle interruptions. This can further cut costs while maintaining high availability.

 With isolated services, you can use cost-optimized compute options for each auto-scaling group. For example, AWS Graviton offers cost-effective, high-performance compute options for workloads that suit ARM-based instances.

 Optimizing costs and resource usage also helps minimize environmental impact, aligning with the [Sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) of the Well-Architected Framework. You can monitor your progress in reducing carbon emissions using the AWS Customer Carbon Footprint Tool. This tool provides insights into the environmental impact of your AWS usage.
