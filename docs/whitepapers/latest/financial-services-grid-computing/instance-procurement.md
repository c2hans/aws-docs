---
source_url: https://docs.aws.amazon.com/whitepapers/latest/financial-services-grid-computing/instance-procurement.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Instance procurement
<a name="instance-procurement"></a>

 In addition to the instance types shown in Table 1, there are also options for procuring instances in AWS:
+  [Amazon EC2 On-Demand Instances](https://aws.amazon.com/ec2/pricing/on-demand/) offer capacity as required, for as long as they are needed. You are only charged for the time that the instance is active. These are ideal for components that benefit from elasticity and predictable availability, such as brokers, compute instances hosting long-running tasks, or tasks that generate further generations of tasks.
+  [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/pricing/) are particularly appropriate for HPC compute instances because they let you take advantage of unused Amazon EC2 capacity in the AWS Cloud. Spot Instances can occasionally be ended by AWS when capacity is constrained in a specific pool. Auto Scaling groups help to re-provision Spot capacity from other eligible pools where spare capacity is available. Grid schedulers can typically accommodate these occasional interruptions and reschedule tasks accordingly.
+  [Savings Plans](https://aws.amazon.com/savingsplans/) are a flexible pricing model that also provides savings of up to 72% on your AWS compute usage regardless of instance family, size, operating system (OS), tenancy or [AWS Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/). Savings Plans offer significant discounts in exchange for a commitment to use a specific amount of compute power (measured in $/hour) for a one- or three-year period. Savings Plans are ideal for long-running hosts such as HPC Controller nodes or for a *baseline* of compute capacity that will be kept online for a majority of the time.

   [AWS Capacity Blocks for ML](https://aws.amazon.com/ec2/capacityblocks/) allow you to reserve latest generation GPU instances for a future date. Capacity Blocks can be used to reserve instances with a duration from one day up to two weeks, enabling experimentation and prototyping as well as ML model training and fine-tuning on highly sought-after GPU instances. Instances will be available for the reserved time and until 30 minutes before the end time of the Capacity Block. The last 30 minutes of the reservation are not charged in the price of the Capacity Block.

   It’s important to note that regardless of the procurement model selected the instances delivered by AWS are exactly the same.

## Compute instance provisioning and management strategies
<a name="compute-instance-provisioning-and-management-strategies"></a>

 Spot Instances are unsuitable for workloads that are not instance flexible; for example, systems where deterministic performance is critical. Spot is not suitable either for stateful, fault-intolerant, or workloads that require tightly coupled communication between instance nodes. They are also not recommended for workloads that are intolerant of occasional periods when the target capacity is not completely available. However, many financial services organizations make use of Spot Instances for part of their HPC workloads. AWS provides services and features to maximize the benefits and availability of Spot instances. For example, when provisioning Spot instances using EC2 Fleet the following allocation strategies can be employed:
+  **Price-capacity-optimized (recommended)** - This strategy identifies the deepest pools of capacity to reduce interruption rates and then requests instances from the lowest priced instances from those pools.
+  **Capacity-optimized** - Automatically launches Spot Instances into the most available pools by looking at real-time capacity data and predicting which are the most available.
+  **Lowest-price** - Instances come from the lowest priced pool that has available capacity.
+  **Diversified** - Spot Instances are distributed across all Spot capacity pools.

AWS provides two mechanisms to advise on interruptions. The first, a Spot Instance interruption notice, is a warning that is issued two minutes before Amazon EC2 interrupts a Spot Instance. You can configure your Spot Instances to be stopped or hibernated, instead of being ended when they are interrupted. Amazon EC2 will then automatically resume them when capacity becomes available in the same Availability Zone and instance type. The second mechanims is the EC2 Instance rebalance recommendation, a signal that notifies you when a Spot Instance is at elevated risk of interruption. The signal gives you the opportunity to proactively manage the Spot Instance in advance of a possible two-minute Spot Instance interruption notice. You can decide to rebalance your workload to new or existing Spot Instances that are not at an elevated risk of interruption. AWS has made it easy for you to use this new signal by using the Capacity Rebalancing feature in EC2 [Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html) and [Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html).

 If hibernation is configured, this feature operates like closing and opening the lid on a laptop computer, and saves the memory state to an [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) disk. However, this approach to managing interruptions should be used with caution because the grid scheduler might not be able to track such quiesced workloads, which could result in timeouts and rescheduling tasks if the hibernated image is not reactivated quickly.

 [Amazon EC2 Fleet](https://aws.amazon.com/blogs/aws/ec2-fleet-manage-thousands-of-on-demand-and-spot-instances-with-one-request/) enables you to quickly create fleets that are diversified by using EC2 On-Demand Instances, Reserved Instances, and Spot Instances. With this approach, you can optimize your HPC capacity management plan according to the changing demands of your workloads. Note that EC2 Spot Fleet is a legacy API with no planned investment.

EC2 Fleet integrates with [Amazon EventBridge](https://aws.amazon.com/eventbridge/) to notify you about important Fleet events, state changes, and errors. This enables you to automate actions in response to Fleet state changes, and monitor the state of your Fleet from a central place without needing to continuously poll Fleet APIs.

 [Amazon EC2 Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html) contain a collection of Amazon EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management. An Auto Scaling group enables you to use Amazon EC2 Auto Scaling features, such as health check replacements and scaling policies. Additionally, you can select instance purchase options such as On-Demand and Spot, use attribute-based instance selection, and price capacity automation.

 A note on EC2 Fleet vs. Autoscaling groups. EC2 Fleet is suitable for workloads that require a fixed set of instances to run. Autoscaling can achieve many of the same goals through attribute-based instance selection: Selecting a range of CPUs, and memory for instance as well as the pricing strategy you’d prefer (Spot, On-Demand or Savings Plans). In most HPC cases we suggest you use Autoscaling.

 [Amazon EC2 launch templates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) contain the configuration information used to launch an instance. The template can define the Amazon Machine Image (AMI) ID (Operating system image), instance type, and network settings for the compute instances. You can use Launch Templates with EC2 Fleet or Amazon EC2 Auto Scaling and they make it easier to implement and track configuration standards.

 Launch Template versioning can be used within the [EC2 Auto Scaling Group ‘Instance Refresh’](https://aws.amazon.com/blogs/compute/introducing-instance-refresh-for-ec2-auto-scaling/) feature to update pools of capacity while minimizing interruptions to the workload. All you need to do is specify the percentage of healthy instances to keep in the group while the Auto Scaling group terminates and launches instances. You can also specify the warm-up time, which is the time period that the Auto Scaling group waits between instances that get refreshed via Instance Refresh.

## Capacity management
<a name="capacity-management"></a>

 As the financial services industry increasingly relies on complex computational models, the need for scalable and cost-effective capacity management solutions becomes paramount. This section explores various strategies and best practices for capacity management in AWS, empowering financial organizations to optimize their compute resources and meet the demands of high throughput computing workloads. By leveraging AWS services and tools, financial institutions can enhance performance, reduce costs, and ensure smooth operations for their critical financial applications.

 One option to begin an HPC deployment is to use only On-Demand Instances. After you understand the performance of your workloads, you can develop and optimize a strategy to provision instances using Savings Plans, Spot, Auto Scaling Groups, or Amazon EC2 Fleet.

 For example, you can deploy a number of instances covered by Savings Plans to host core grid services, such as schedulers, that are required to be available at all times. You can then provision On-Demand Instances during the intraday period to ensure predictable performance for synchronous pricing calculations. Highly optimized grids end up using a mix of all the purchasing options. For End of Day (EOD) batches, it's common for 60% to 80% of capacity to be provisioned using Spot Instances.

 Understanding the importance of instance diversification and availability is key to successfully provisioning Spot capacity at scale. The Spot Placement Score (SPS) can be used to get a score from 1-9 indicating how likely a Spot capacity request will succeed in a region or Availability Zone. Spot is spare capacity and as such it fluctuates over time. Projects like the [Spot Placement Score Tracker](https://aws.amazon.com/blogs/compute/optimizing-amazon-ec2-spot-instances-with-spot-placement-scores/) can be used to track the best regions to run large Spot workloads at scale. This can be useful in the definition of multi-region strategies, where, when regulatory framework allows, the workload can be run on the regions that optimize for capacity availability and price performance.

 The following figure shows two approaches to provisioning. In each case, 10,000 vCPUs of Savings Plan-based capacity remain online for the stateful scheduling components.

 In the first case, 20,000 further vCPUs are provisioned using On-Demand Instances for ten hours to accommodate a batch that runs for 200,000 vCPU hours with a ten-hour SLA.

 In the second approach, the 20,000 vCPUs are provisioned at the outset using On-Demand Instances to provide confidence in the batch delivery, but 70,000 vCPUs based on low-cost Spot Instances are also added. Because of the volume of Spot Instances, the batch completes much more quickly (in about three hours) and at a significantly reduced cost. However, if the Spot Instances were not available for any reason, the batch would still complete on time with the On-Demand Instances provisioned.

![Diagrams showing two contrasting AWS instance provisioning strategies](https://docs.aws.amazon.com/whitepapers/latest/financial-services-grid-computing/images/instance-provisioning-strategies.png)

## Attribute-based instance type selection
<a name="attribute-based-instance-type-selection"></a>

 Attribute-based instance type selection circumvents the need to directly specify instance types for your workloads and instead allows you to express requirements such as vCPUs, memory, storage, and other attributes and leave AWS to select the instances. There are advantages to this approach: it reduces the need for you to research instance types, it ensures that as new instance types become available that you can take advantage of the immediately (as long as they meet your requirements), and it helps with diversification of instance types, opening up more pools from which to provision Spot instances.

## Amazon EC2 Fleet
<a name="ec2-fleet"></a>

 EC2 Fleet enables you to quickly create fleets that are diversified by using EC2 On-Demand Instances, Savings Plans, and Spot Instances. With this approach, you can optimize your HPC capacity management plan according to the changing demands of your workloads.

 For capacity management use-cases requiring custom scale in and scale out strategies we recommend using [EC2 Fleet Instant](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instant-fleet.html) request type. This is a synchronous one-time request that makes only one attempt to launch your desired capacity. This will allow you to bulk request instances without the autoscaling functionality, allowing you to develop scaling strategies for your specific use-case.

## Amazon EC2 Auto Scaling
<a name="ec2-auto-scaling"></a>

 One of the key benefits of deploying applications in the AWS Cloud is *elasticity*. [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) enables HPC managers to configure Amazon EC2 instance provisioning and decommissioning events based on the real-time demands of their platform. The concept of ‘Instance Weightings’ allows Auto Scaling groups to start instances from a diverse pool of instance types to meet an overall capacity target for the workload. Though grids were previously provisioned based on predictions of peak demands (with periods of both constraint and idle capacity), Amazon EC2 Auto Scaling has a rich API that enables it to be integrated with schedulers to easily manage scaling events.

 When you remove hosts from a running cluster, make sure to allow for a *drain down* period. During this period, the targeted host stops taking on new work, but is allowed to complete work in progress. When you select nodes for removal, avoid any long-running tasks, so that the shutdown is not delayed and you don’t lose progress on those calculations. If the scheduler allows a query of total runtime of tasks in progress, grouped by instance, you can use this to identify which are the optimal candidates for removal, specifically the instances with the lowest aggregate total of runtime by tasks in progress.

 Where capacity is managed automatically, Amazon EC2 Auto Scaling groups offer [‘scale-in’ protection as well as configurable termination policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html) to allow HPC managers to minimize disruption to tasks in flight. Scale-in protection allows an Auto Scaling Group, or an individual instance to be marked as ‘InService’ and so ineligible for termination in a ‘scale-in’ event. You also have the option to build custom ending policies using [AWS Lambda](https://aws.amazon.com/lambda/) to give more control over which instances are ended. These protections can be controlled by an API for integration with the scheduler to automate the drain down process.

 Paradoxically, adding instances to a cluster can temporarily slow the flow of tasks if those new instances need some time to reach optimal performance, as binaries are loaded into memory and local caches are populated. Amazon EC2 Auto Scaling groups also support *warm pools*. A warm pool is a pool of pre-initialized EC2 instances that sits alongside the Auto Scaling group. Whenever your application needs to scale out, the Auto Scaling group can draw on the warm pool to meet its new desired capacity. The goal of a warm pool is to ensure that instances are ready to quickly start serving application traffic, accelerating the response to a scale-out event. This is known as a *warm start*.

 So far, this section has addressed compute instance provisioning at the host level. Increasingly customers are looking to serverless solutions based on either container technologies such as [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (Amazon ECS), [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS), or [AWS Lambda](https://aws.amazon.com/lambda/).

 For both Amazon ECS and Amazon EKS, the [AWS Fargate](https://aws.amazon.com/fargate/) serverless compute engine removes the need to orchestrate infrastructure capacity to support containers. Fargate allocates the right amount of compute, eliminating the need to choose instances and scale cluster capacity. You pay only for the resources required to run your containers, so there is no over-provisioning and paying for additional servers.

 Fargate supports both Spot Pricing for ECS and Compute Savings Plans for Amazon ECS and Amazon EKS.

 For customers using [AWS Lambda](https://aws.amazon.com/lambda/), there are no instances to be scaled; however there is the concept of *Concurrency* which is the number of instances of a function which can serve requests at a time. There are default Regional concurrency limits which can be increased through a request in the Support Center console. Financial services firms have already built completely serverless HPC solutions based on Lambda (similar to the architecture outlined [here](task-scheduling-and-infrastructure-orchestration.md#ServerlessHPC)) that support tens of millions of calculations per day.

 In addition to considering alternative CPU architectures and accelerated computing options, customers are increasingly looking at their existing dependencies on commercial operating systems such as Microsoft Windows. Such dependencies are often historical, stemming from risk management systems built around spreadsheets, however today the cost premiums can be very material especially when compared to deeply discounted EC2 capacity under Amazon EC2 Spot.

 AWS offers a variety of Linux distributions including Red Hat, SUSE, CentOS, Debian, Kali, Ubuntu, and Amazon Linux. The latter is a supported and maintained Linux image provided by AWS for use on Amazon EC2 (it can also be run on-premises for development and testing). It is designed to provide a stable, secure, and high-performance run environment for applications running on Amazon EC2. It supports the latest EC2 instance type features, and includes packages that enable easy integration with AWS. AWS provides ongoing security and maintenance updates to all instances running the Amazon Linux AMI, and it is provided at no additional charge to Amazon EC2 users.
