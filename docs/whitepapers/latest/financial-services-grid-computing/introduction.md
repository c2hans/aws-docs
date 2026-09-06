---
source_url: https://docs.aws.amazon.com/whitepapers/latest/financial-services-grid-computing/introduction.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Introduction
<a name="introduction"></a>

 In general, traditional HPC systems are used to solve complex mathematical problems that require thousands or even millions of CPU hours. These systems are commonly used in academic institutions, biotech, and engineering firms. In banking organizations, HPC systems are used to quantify the risk of given products, trades, or portfolios, which enables traders to develop effective hedging strategies, price trades, and report positions to their internal control functions and ultimately to external regulators. Insurance companies leverage HPC systems in a similar way for actuarial modeling and in support of their own regulatory requirements.

 Unpredictable global events, seasonal variation, and regulatory reporting commitments contribute to a mixture of demands on HPC platforms. This includes short, latency-sensitive intraday pricing tasks, near real-time risk measures calculated in response to changing market conditions, or large overnight batch workloads and back-testing to measure the efficacy of new models to historic events. Combined, these workloads can generate hundreds of millions of tasks per day, with a significant proportion running for less than a second. As a result, these workloads are often characterized as *high-throughput computing* problems.

 Because of the regulatory landscape, demand for these calculations continues to outpace the progress of Moore’s law. Regulations such as the *Fundamental Review of the Trading Book* (FRTB) and *IFRS 17* require even more analysis. In turn, financial services organizations continue to grow their grid computing platforms and increasingly wrestle with the costs associated with purchasing and managing this infrastructure. The blog post *[How cloud increases flexibility of trading risk infrastructure for FRTB compliance](https://aws.amazon.com/blogs/industries/how-cloud-increases-flexibility-of-trading-risk-infrastructure-for-frtb-compliance/)* explores this topic in greater detail, discussing the challenges of data, compute, and the agility benefits achieved by running these workloads in the cloud.

 Risk and pricing calculations in financial services are most commonly [embarrassingly parallel](https://en.wikipedia.org/wiki/Embarrassingly_parallel) or *loosely coupled*, do not require communication between nodes to complete calculations, and broadly benefit from horizontal scalability. Because of this, they are well suited to a [shared-nothing](https://en.wikipedia.org/wiki/Shared-nothing_architecture) architectural approach, in which each compute node is independent from the other.

 For example, a financial model based on the [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_methods_in_finance) can create millions of scenarios to be divided across a large number (often hundreds or thousands) of compute nodes for calculation in parallel. Each scenario reflects a different market condition based on a number of variables.

 In general, doubling the number of compute nodes allows these tasks to be distributed more widely, which reduces by half the overall duration of the job. Access to increased compute capacity through AWS allows for additional scenarios and greater precision in the results in a given timeframe. Alternatively, you can use the additional capacity to complete the same calculations in less time.

 Financial services firms typically use a third-party grid scheduler to coordinate the allocation of compute tasks to available capacity. Grid schedulers have these features in common:
+  Scheduling logic to manage the life-cycle of tasks including retry logic, prioritization, and resource allocation. This includes an engine to allow rules to be defined to ensure that certain workloads are prioritized over others in the event that the total capacity of the grid is exhausted. This component is key to the overall throughput of the system, typically needing to place many thousands of tasks per second with the goal of maximizing effective use of the resources.
+  Infrastructure orchestration to manage the compute resources, to track which are available and their capabilities. When the grid is making use of cloud compute, this component will be responsible for coordinating scale-out/scale-in events.
+  Deployment tools to ensure that software binaries and relevant data are reliably distributed to compute nodes that are allocated a specific task.
+  Brokers are typically employed to manage the direct allocation of tasks that are submitted by a client to the compute grid. In some cases, an allocated compute node makes a direct connection back to a client to collect tasks to reduce latency. Brokers are usually horizontally scalable, and are well suited to the elasticity of cloud.

 In some cases, the client is another grid node that generates further tasks. Such multi-tier, recursive architectures are not uncommon, but present further challenges for software engineers and HPC administrators who want to maximize utilization while managing risks, such as deadlock, when parent tasks are unable to yield to child tasks.

 The key benefit of running HPC workloads on AWS is the ability to allocate large amounts of compute capacity on demand without the need to commit to the upfront and ongoing costs of a large hardware investment. Capacity can be scaled minute by minute according to your needs at the time. This avoids pre-provisioning of capacity according to some estimate of future peak demand. Because AWS infrastructure is charged by consumption of CPU-hours, it’s possible to complete the same workload in less time, for the same price, by simply scaling the capacity.

 The following figure shows two approaches to provisioning capacity. In the first, 2,000 vCPUs are provisioned for ten hours. In the second, 10,000 vCPUs are provisioned for two hours. In a vCPU-hour billing model, the overall cost is the same, but the latter produces results in one fifth of the time.

![Diagram showing Two approaches to provisioning 20 CPU-hours of capacity](http://docs.aws.amazon.com/whitepapers/latest/financial-services-grid-computing/images/two-approaches-to-provisioning.png)

 Developers of the analytics calculations used in HPC applications can use the latest CPUs, graphics processing units (GPUs), and field-programmable gate arrays (FPGAs) available through the many [Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types/). This drives efficiency-per-core, and differs from on-premises grids that tend to be a mixture of infrastructure, which reflects historic procurement rather than current needs.

 Diverse pricing models offer flexibility to these customers. For example, [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/) can reduce compute costs by up to 90%. These instances are occasionally interrupted by AWS, but HPC schedulers can typically react to these events and reschedule tasks accordingly.

 This document includes several recommended approaches to building HPC systems in the cloud, and highlights AWS services that are used by financial services organizations to help to address their compute, networking, storage, and security requirements.
