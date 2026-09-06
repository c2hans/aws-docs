---
source_url: https://docs.aws.amazon.com/whitepapers/latest/big-data-analytics-options/amazon-compute-services.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon Compute Services (EC2, EKS, and ECS)
<a name="amazon-compute-services"></a>

[Amazon EC2](https://aws.amazon.com/ec2/), with instances acting as AWS virtual machines, provides an ideal platform for operating your own self-managed big data analytics applications on AWS infrastructure. Almost any software you can install on Linux or Windows virtualized environments can be run on Amazon EC2, and you can use the pay-as-you-go pricing model.

AWS Graviton processors are custom built by AWS using 64-bit Arm Neoverse cores to deliver the best price performance for your cloud workloads running in Amazon EC2. Amazon EC2 provides the broadest and deepest portfolio of compute instances, including many that are powered by latest-generation Intel and AMD processors. AWS Graviton processors add even more choice to help customers optimize performance and cost for their workloads.

What you don’t get are the application-level managed services that come with the other services mentioned in this whitepaper. There are many options for self-managed big data analytics:
+  A NoSQL offering, such as MongoDB
+  A data warehouse or columnar store like Vertica
+  A Hadoop cluster
+  An Apache Storm cluster
+  An Apache Kafka environment

Any self-managed big data workload that runs on EC2 can also run on an AWS fully managed container orchestration service such as [ Amazon ECS](https://aws.amazon.com/ecs/), [Amazon EKS](https://aws.amazon.com/eks/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc&eks-blogs.sort-by=item.additionalFields.createdDate&eks-blogs.sort-order=desc), and [AWS Fargate](https://aws.amazon.com/fargate/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc&fargate-blogs.sort-by=item.additionalFields.createdDate&fargate-blogs.sort-order=desc). Fargate is a serverless compute engine for containers that works with ECS and EKS.

## Ideal usage patterns
<a name="ideal-usage-patterns-7"></a>
+  **Specialized environment** – When running a custom application, a variation of a standard Hadoop set or an application not covered by another AWS offering, Amazon EC2 provides the flexibility and scalability to meet your computing needs.
+  **Compliance requirements** – Certain compliance requirements may require you to run applications yourself on Amazon EC2 instead of using a managed service offering.

## Cost model
<a name="cost-model-compute"></a>

 Amazon EC2 has a variety of instance types in a number of instance families (standard, high CPU, high memory, high I/O, and so on), and different pricing options (On-Demand, Compute Savings plan, Reserved, and Spot). At the time of this writing, when running applications on ECS, you pay only for underlying EC2 instances, with no additional charge for using ECS. However, for EKS, you pay an additional $0.10 per hour for each EKS cluster you have, along with underlying EC2 instances. AWS Fargate pricing is calculated based on the vCPU, memory, and storage resources used from the time you start to download your container image until the [Amazon ECS task](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html) or [Amazon EKS2 pod](https://docs.aws.amazon.com/eks/latest/userguide/pod-networking.html) finishes, rounded up to the nearest second.

While cost is dependent on various factors based on the use case, Graviton2 instances have in general been able to provide better price/performance over previous generation instances. Depending on your application requirements, you may want to use additional services along with Amazon EC2, EKS, or ECS, such as [Amazon Elastic Block Store ](http://aws.amazon.com/ebs/) (Amazon EBS) for directly attached persistent storage, or S3 as a durable object store; each comes with its own pricing model. If you do run your big data application on Amazon EC2, EKS, or ECS, you are responsible for any license fees just as you would be in your own data center. The [AWS Marketplace](https://aws.amazon.com/marketplace) offers many different third-party, big data software packages pre-configured to launch with a simple click of a button.

## Performance
<a name="performance-compute"></a>

 Performance in Amazon EC2, EKS, or ECS is driven by the instance type that you choose for your big data platform. Each instance type has a different amount of CPU, RAM, storage, IOPs, and networking capability so that you can pick the right performance level for your application requirements.

## Durability and availability
<a name="durability-and-availability-compute"></a>

Critical applications should be run in a cluster across multiple Availability Zones within an AWS Region so that any instance or data center failure does not affect application users. For non-uptime critical applications, you can back up your application to Amazon S3 and restore to any Availability Zone in the Region if an instance or zone failure occurs. Other options exist, depending on which application you are running and the requirements, such as mirroring your application.

## Scalability and elasticity
<a name="scalability-and-elasticity-compute"></a>

 [Auto Scaling](https://aws.amazon.com/autoscaling/) is a service that enables you to automatically scale your Amazon EC2 capacity up or down according to conditions that you define. With Auto Scaling, you can ensure that the number of EC2 instances you’re using scales up seamlessly during demand spikes to maintain performance, and scales down automatically during demand lulls to minimize costs. Auto Scaling is particularly well suited for applications that experience hourly, daily, or weekly variability in usage. Auto Scaling is enabled by CloudWatch and available at no additional charge beyond CloudWatch fees.

## Interfaces
<a name="interfaces-compute"></a>

 Amazon EC2, EKS, and ECS can be managed programmatically via API, SDK, or the AWS Management Console. Metrics for compute utilization, memory utilization, storage utilization, network consumption, and read/write traffic to your instances are free of charge using the console or CloudWatch API operations.

 The interfaces for your big data analytics software that you run on top of Amazon EC2 varies based on the characteristics of the software you choose.

## Anti-patterns
<a name="anti-patterns-compute"></a>

 Amazon EC2 has the following anti-patterns:
+  **Managed service** – If your requirement is a managed service offering where you abstract the infrastructure layer and administration from the big data analytics, then this “do it yourself” model of managing your own analytics software on Amazon EC2 may not be the correct choice.
+  **Lack of expertise or resources** – If your organization does not have, or does not want to expend, the resources or expertise to install and manage a high-availability installation for the system in question, you should consider using the AWS equivalent such as Amazon EMR, DynamoDB, Amazon Kinesis Data Streams, or Amazon Redshift.
