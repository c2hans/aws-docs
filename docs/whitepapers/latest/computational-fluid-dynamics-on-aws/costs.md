---
source_url: https://docs.aws.amazon.com/whitepapers/latest/computational-fluid-dynamics-on-aws/costs.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Costs
<a name="costs"></a>

 AWS offers a pay-as-you-go approach for pricing for cloud services. You pay only for the individual services you need, for as long as you use them, without long-term contracts or complex licensing. Some services and tools incur no charge, such as [AWS ParallelCluster](https://aws.amazon.com/hpc/parallelcluster/), [AWS Batch](https://aws.amazon.com/batch/), and [AWS CloudFormation](https://aws.amazon.com/cloudformation/); however, the underlying AWS components used to run cases incur charges.

 AWS charges arise primarily from the compute resources required for the CFD solution. Storage and data transfer also incur charges. Depending on your implementation, you may use additional services in your architecture, such as [AWS Lambda](https://aws.amazon.com/lambda/), [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (Amazon SNS), or [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), but cost accumulated by usage of these services is rarely significant when compared to the compute costs for CFD.

 It is common to stand up a cluster for only the time period in which it is needed. In a simple scenario, costs are associated with EC2 instances and Amazon EBS volumes. Costs incurred after shut down of the cluster include any snapshots taken of Amazon EBS volumes and any data stored on Amazon S3.

 While data transfer into Amazon EC2 from the internet is free, data transfer out of AWS can incur modest charges. Many users choose to leave their data in S3 and only move the smaller post-processed data out of AWS. Data can also be transitioned to Amazon Glacier for archival storage to reduce long-term storage costs.

 When AWS ParallelCluster is maintained for an extended period of time, the login node and Amazon EBS volumes continue to incur costs. The compute nodes scale up and down as needed, which minimizes costs to only reflect the times when the cluster is being used.

 When developing an architecture, you must monitor your workload (automatically through monitoring solutions or manually through the console) and ensure that your resources scale up and down as expected. Occasionally, hung jobs or other factors can prevent your resources from scaling properly. Logging on to the compute node and checking processes with a tool, such as [top](https://en.wikipedia.org/wiki/Top_(software)) or [htop](https://htop.dev/), can help debug issues.

 AWS provides four different ways to [pay for EC2 instances](https://aws.amazon.com/ec2/pricing/):
+  On-Demand Instances
+  Reserved Instances
+  Savings Plans
+  Spot Instances

 Amazon EC2 instance costs can be minimized by using Spot Instances, Savings Plans, and Reserved Instances.
+  **On-Demand Instances** — With On-Demand Instances, you pay for compute capacity by the hour or the second, depending on which you run. No long-term commitments or upfront payments are needed. You can increase or decrease your compute capacity depending on the demands of your application and only pay the specified per-hour rates for the instance you use.

   On-Demand Instances are the highest cost model for computing and require no upfront commitment. Cost saving is gained because costs are only incurred while the instances are in a running state. For a dynamic workload, the savings can be large. Savings occur because you can select the newest processor types, which may speed up the computations significantly.
+  **Reserved Instances** — Reserved Instances (RIs) provide you with a significant discount (up to 75%) compared to On-Demand Instance pricing. For customers that have steady state or predictable usage and can commit to using EC2 over a 1- or 3-year term, Reserved Instances provide significant savings compared to using On-Demand Instances.
+  **Savings Plans** — Savings Plans are a flexible pricing model that provides savings of up to 72% on your AWS compute usage. This pricing model offers lower prices on Amazon EC2 instances usage, regardless of instance family, size, OS, tenancy or AWS Region, and also applies to [AWS Fargate](https://aws.amazon.com/fargate/) usage.

   Savings Plans offer significant savings over On-Demand Instances, just like EC2 Reserved Instances, in exchange for a commitment to use a specific amount of compute power (measured in $/hour) for a one- or three-year period. You can sign up for Savings Plans for a one- or three-year term and easily manage your plans by taking advantage of recommendations, performance reporting, and budget alerts in the [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/).
+  **Spot Instances** — Amazon EC2 Spot Instances let you take advantage of unused EC2 capacity at up to a 90% discount compared to On-Demand prices. However, Spot Instances can be interrupted when EC2 needs to reclaim the capacity. Spot Instances are frequently the most cost-effective resource for flexible or fault-tolerant workloads and can also be used for CFD cases. Spot availability varies by spot pool (for example, Region, Availability Zone, and instance type). Consider your deployment strategy and interruption impact when determining the most cost-effective resources for your case.

   When a Spot Instance is interrupted, your case is interrupted. The interruption impact to your case depends on how your CFD application handles the interruption, and you can minimize this impact by checkpointing your simulation if supported. In addition, you can minimize the risk of Spot Instance interruption by working with the Spot Advisor, being flexible on instance type and Availability Zone, and using advanced features, such as the capacity-optimized allocation strategy in EC2 Fleet, to launch your Spot Instances. Overall, the need to occasionally restart a workload can be offset by the cost savings of Spot Instances.
+  **Combined approach** — You can easily combine Spot Instances with On-Demand and RIs to further optimize workload cost with performance. For example, in the following figure, you could use Reserved Instances for your daily workloads, Spot Instances for component exploration, and On-Demand Instances for design review.

![A graph showing EC2 cost optimization for CFD cases.](http://docs.aws.amazon.com/whitepapers/latest/computational-fluid-dynamics-on-aws/images/ec2-cost-optimization.png)
