---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/scaling-amazon-eks-infrastructure/cost-optimization.html
---

# Cost optimization
<a name="cost-optimization"></a>

To support effective resource control, Kubernetes cost minimization is crucial for enterprises using this container orchestration technology. It's difficult to properly track spending in Kubernetes settings because of their complexity, which include multiple components such as pods and nodes. Through the application of cost optimization techniques, businesses can see where their resources are being spent and appropriately assign expenses to departments or projects.

Although dynamic scaling has advantages, if not properly managed, it can result in unforeseen expenses. Efficient cost management helps to allocate resources only when they're truly required, averting unanticipated surges in expenditures.

This section discusses the following approaches to cost optimization:
+ [Kubecost](#kubecost)
+ [Goldilocks](#goldilocks)
+ [AWS Fargate](#fargate)
+ [Spot Instances](#spot)
+ [Reserved Instances](#reserved)
+ [AWS Graviton instances](#graviton)

## Kubecost
<a name="kubecost"></a>

[Kubecost](https://www.kubecost.com/products/kubecost-cloud/) is a cost management solution that helps businesses track, control, and maximize their expenditure on cloud infrastructure. It's made specifically for Kubernetes clusters. Kubecost gives you insights into resource utilization and real-time cost awareness, enabling you to better understand where and how much of your cloud resources are being used. With these insights, you can optimize your infrastructure spending, improve resource efficiency, and make more informed decisions about your cloud investments.

Kubecost provides the following key features:
+ **Cost allocation** – Kubecost offers thorough cost allocation for Kubernetes resources, including workloads, services, namespaces, and labels. This feature helps teams to monitor costs by environment, project, or team.
+ **Real-time cost monitoring** – It offers real-time monitoring of cloud costs, giving organizations immediate insights into spending patterns and helping to prevent unexpected cost overruns.
+ **Optimization recommendations** – Kubecost offers practical suggestions for minimizing resource utilization, including reducing idle resources, right-sizing workloads, and maximizing storage expenses.
+ **Budgeting and alerts** – Kubecost users can create budgets and receive reminders when an expenditure approaches or surpasses predetermined criteria. This feature helps teams adhere to financial constraints.

## Goldilocks
<a name="goldilocks"></a>

[Goldilocks](https://github.com/FairwindsOps/goldilocks) is a Kubernetes utility designed to help users optimize their resource requests and limits for Kubernetes workloads. It provides recommendations on how to configure the CPU and memory resources for containers running in a Kubernetes cluster. These recommendations help you make sure that applications have the right number of resources to perform efficiently without waste. This optimization can lead to cost savings, improved performance, and more efficient use of Kubernetes clusters.

Goldilocks provides the following key features:
+ **Resource recommendations** – Goldilocks determines the ideal settings for resource requests and restrictions by analyzing past CPU and memory consumption statistics for Kubernetes workloads. By doing this, it becomes easier to avoid under- or over-provisioning, which can result in performance problems and resource waste.
+ **VPA integration** – Goldilocks leverages the Kubernetes Vertical Pod Autoscaler (VPA) to gather data and provide recommendations. It runs in a "recommendation mode," meaning it doesn't actually change resource settings but offers guidance on what those settings should be.
+ **Namespace-based analysis** – Goldilocks gives you the ability to finely regulate which workloads are optimized and monitored by allowing you to target particular namespaces for analysis.
+ **Visual dashboard** – The web-based dashboard displays suggested resource requests and restrictions visually, which makes it straightforward for you to understand and take action on the data.
+ **Non-intrusive operation** – Goldilocks doesn't alter the cluster's setup because it operates in recommendation mode. If you want, you can manually apply the recommended resource settings after reviewing the recommendations.

## AWS Fargate
<a name="fargate"></a>

In the context of Amazon EKS, [AWS Fargate](https://docs.aws.amazon.com/eks/latest/userguide/fargate.html) allows you to run Kubernetes pods without managing the underlying Amazon EC2 instances. It's a serverless compute engine that lets you focus on deploying and scaling containerized applications without worrying about the infrastructure.

AWS Fargate provides the following key features:
+ **No infrastructure management** – Fargate eliminates the need to provision, manage, or scale Amazon EC2 instances or Kubernetes nodes. AWS handles all the infrastructure management, including patching and scaling.
+ **Pod-level isolation** – Unlike worker nodes that are based on Amazon EC2, Fargate provides task or pod-level isolation. Each pod runs in its own isolated compute environment, which enhances security and performance.
+ **Automatic scaling** – Fargate automatically scales Kubernetes pods based on demand. You don't need to manage scaling policies or node pools.
+ **Per-second billing** – You only pay for the vCPU and memory resources consumed by each pod for the exact duration it runs, which is a cost-effective option for certain workloads.
+ **Reduced overhead** – By eliminating the need to manage EC2 instances, Fargate allows you to focus on building and managing your applications rather than infrastructure operations.

## Spot Instances
<a name="spot"></a>

[Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) offer significant savings over On-Demand Instance pricing and are an affordable option for running Amazon EC2 worker nodes in an Amazon EKS cluster. However, [AWS can interrupt Spot Instances](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-leveraging-ec2-spot-instances/how-spot-instances-work.html) in the event that On-Demand Instance capacity is needed. AWS can reclaim Spot Instances with a 2-minute notice when the capacity is needed, making them less reliable for critical, stateful workloads.

For workloads that are sensitive to cost and can withstand disruptions, Spot Instances in Amazon EKS are a good option. Using a combination of Spot Instances and On-Demand Instances in a Kubernetes cluster helps you save money without sacrificing availability for vital workloads.

Spot Instances provides the following key features:
+ **Cost savings** – Spot Instances can be less expensive than On-Demand Instance [pricing](https://aws.amazon.com/ec2/pricing/on-demand/), making them ideal for cost-sensitive workloads.
+ **Ideal for fault-tolerant workloads** – Well suited for stateless, fault-tolerant workloads such as batch processing, CI/CD jobs, machine learning, or large-scale data processing where instances can be replaced without major disruption.
+ **Auto-Scaling group integration** – Amazon EKS integrates Spot Instances with Kubernetes Cluster Autoscaler, which can automatically replace interrupted Spot Instance nodes with other available Spot Instances or On-Demand Instances.

## Reserved Instances
<a name="reserved"></a>

In Amazon EKS, [Reserved Instances](https://aws.amazon.com/ec2/pricing/reserved-instances/) is a pricing model for the Amazon EC2 worker nodes that run your Kubernetes workloads. By using Reserved Instances, you commit to using specific instance types for a 1- year or 3-year term, in exchange for cost savings compared to On-Demand Instance pricing. Reserving instances in Amazon EKS is an affordable way to perform consistent, long-term workloads on Amazon EC2 worker nodes.

Reserved Instances are commonly used for Amazon EC2. However, the worker nodes in your Amazon EKS cluster (which are EC2 instances) can also benefit from this cost-saving model, provided the workload requires long-term, predictable usage.

Production services, databases, and other stateful applications that need high availability and consistent performance are examples of stable workloads that are well suited for Reserved Instances.

Reserved Instances provides the following key features:
+ **Cost savings** – Reserved Instances offer savings compared to On-Demand instances, depending on the term length (1 or 3 years) and [payment plan](https://aws.amazon.com/ec2/pricing/reserved-instances/pricing/) (All Upfront, Partial Upfront, or No Upfront).
+ **Long-term commitment** – You commit to a 1-year or 3-year term for a specific instance type, size, and AWS Region. This is ideal for workloads that are stable and run continuously over time.
+ **Predictable pricing** – Because you're committed to a specific term, Reserved Instances provide predictable monthly or upfront costs, making it easier to budget for long-term workloads.
+ **Instance flexibility** – With Convertible Reserved Instances, you can change the instance type, family, or size during the reservation period. Convertible Reserved Instances offer more flexibility than Standard Reserved Instances, which don't allow changes.
+ **Guaranteed capacity** – Reserved Instances ensure that capacity is available in the Availability Zone where the reservation is made, which is crucial for critical workloads that need consistent compute power.
+ **No interruption risk** – Unlike Spot Instances, Reserved Instances are not subject to interruption by AWS. This makes them ideal for running mission-critical workloads that require guaranteed uptime.

## AWS Graviton instances
<a name="graviton"></a>

[AWS Graviton](https://aws.amazon.com/ec2/graviton/) is a family of ARM-based processors designed by AWS to provide improved performance and cost-efficiency for cloud workloads. In the context of Amazon EKS, you can use Graviton instances as worker nodes to run your Kubernetes workloads, offering significant performance gains and cost savings.

Graviton instances are an excellent option for cloud-native and compute-intensive applications because they offer a higher price-performance ratio than x86 instances. However, when you consider adopting Graviton instances, take ARM compatibility into account.

AWS Graviton instances provide the following key features:
+ **ARM-based architecture** – AWS Graviton processors are built on ARM architecture, which is different from traditional x86 architectures but highly efficient for many workloads.
+ **Cost-efficient** – Amazon EC2 instances based on Graviton typically offer better price-performance compared to x86-based EC2 instances. This makes them an attractive option for Kubernetes clusters that run Amazon EKS.
+ **Performance** – Graviton2 processors, the second generation of AWS Graviton, offer significant improvements in terms of compute performance, memory throughput, and energy efficiency. They're ideal for CPU-intensive and memory-intensive workloads.
+ **Diverse instance types** – Graviton instances come in various families, such as t4g, m7g, c7g, and r7g, covering a range of use cases from general purpose to compute-optimized, memory-optimized, and burstable workloads.
+ **Amazon EKS node groups** – You can configure node groups that are managed by Amazon EKS or self-managed node groups to include Graviton-based instances. With this approach, you can run workloads that are optimized for ARM architecture on the same Kubernetes cluster alongside x86-based instances.
