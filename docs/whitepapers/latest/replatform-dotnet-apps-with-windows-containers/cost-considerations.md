---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/cost-considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Cost considerations
<a name="cost-considerations"></a>

## Cloud computing
<a name="cloud-computing"></a>

 With cloud computing, companies have access to a scalable platform, low-cost storage, database technologies, and tools on which to build enterprise-grade solutions. Cloud computing helps businesses reduce costs and complexity, adjust capacity on-demand, accelerate time to market, increase opportunities for innovation, and enhance security.

 Weighing the financial considerations of operating an on-premises data center compared to using cloud infrastructure is not as simple as comparing hardware, storage, and compute costs. Whether you own your own data center or rent space at a colocation facility, you have to manage investments that include capital expenditures, operational expenditures, staffing, opportunity costs, licensing, and facilities overhead.

## AWS pricing model
<a name="aws-pricing-model"></a>

 AWS offers a simple, consistent, pay-as-you-go pricing model, so you are charged only for the resources you consume. With this model, there are no upfront fees, minimum commitments, and long-term contracts required. There is also flexibility to choose the pricing model that best fits your needs if the pay-as-you-go model is not optimal for your use case. Short descriptions of all of these pricing models follow.
+  **On-Demand Instance** — With On-Demand Instances, you pay for compute capacity by the second with no minimum commitments required.
+  **Savings Plans** — A flexible pricing model offering lower prices compared to On-Demand pricing, in exchange for a specific usage commitment (measured by hourly rate) for a one-year or three-year period. AWS offers three types of Savings Plans:
  +  Compute Savings Plans
  +  EC2 Instance Savings Plans
  +  Amazon SageMaker AI Savings Plans

   Compute Savings Plans apply to usage across Amazon EC2, AWS Lambda, and AWS Fargate.
+  **Reserved Instance** — For longer-term savings, you can purchase in advance. In addition to providing a significant discount (up to 60 percent) compared to On-Demand Instance pricing, Reserved Instances allow you to reserve capacity.
+  **Spot Instance** — You can bid for unused Amazon EC2 capacity. Instances are charged the Spot Price, which is set by Amazon EC2 and fluctuates, depending on supply and demand. For more information, refer to [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/).

 For more information, refer to the [AWS Cloud Economics Center](https://aws.amazon.com/economics/) and [Savings Plans](https://aws.amazon.com/savingsplans/).

## AWS container services
<a name="aws-container-services"></a>

 There are several cost aspects to consider when running applications on AWS. These include but are not limited to storage, data transfer, service usage, compute, and operations. When considering replatforming to Windows containers, it’s important to evaluate the resource utilization of the existing application. One of the primary benefits of containers is the ability to *bin-pack* several containerized application instances on a reduced footprint of infrastructure. This leads to improvements in resource utilization which can result in considerable cost savings.

 A common concern when considering a replatforming effort is the cost of changing application code or introducing new DevOps processes needed to build and deploy the application. When targeting Windows containers, application developers can minimize the number of changes needed for this new environment, and in many cases find that there are no changes required to the code itself. Modifying [CI/CD](https://en.wikipedia.org/wiki/CI/CD) processes to deliver container images as the build artifact as opposed to traditional application binaries require changes, but has the benefit of removing the step of installing and configuring code in the target environment; instead, the container image can be fully configured at build time and tested as part of the build pipeline prior to delivery.

 Finally, there is an additional cost component that is frequently overlooked which is managing the server infrastructure and application deployment. In a traditional on-premises environment, application servers must be configured to run the application as part of the application deployment process; this can be a time-consuming process, and dependencies may differ from application to application.

 The fact that the application container image delivers the application dependencies and application code as a single, pre-packaged build artifact dramatically simplifies the deployment process and time needed for any troubleshooting. Additionally, this delivery mechanism decouples the configuration and patching of servers from the run environment, and allows the operations management team to have a single, unified process for managing the server infrastructure, which reduces management overhead.

## Cost comparison
<a name="cost-comparison"></a>

 There are four different services that AWS provides to run Windows container-based applications (containers on Amazon EC2, Amazon EKS, Amazon ECS, and AWS Fargate). To understand the cost implications of running containers on each of these services, this guide presents an example of a simple application architecture and compares the cost of running it on each service with an On-Demand pricing model in the `us-east-1` Region. You can choose a different pricing structure such as Spot Instances or Saving Plans, which are supported for the services covered in this guide. The examples in the following sections were generated by the [AWS Pricing Calculator](https://calculator.aws/#/estimate?id=962adcc4611ed94c0aef310846f355dc2b247ba9).

 This guide focuses on compute (where the containers run) and operations cost (staffing) of managing the compute resources. It does not include the cost consolidation of *bin-packing* applications or of running a database to simplify the analysis.

 As the baseline for the comparison, this guide uses an application running on Windows in Amazon EC2, as shown in the following diagram.

![Architecture diagram showing a legacy .NET application on Amazon EC2 costing USD$192.57 a month.](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/legacy-dotnet-app-on-ec2-windows.png)

### Summary by service
<a name="summary-by-service"></a>

 The following table represents the summary of running the above application on each AWS container service. These figures include the cost of compute, the Amazon VPC, and ELB. You can see that running on Linux costs less than running on Windows for each service which is influenced by the license-included cost of Windows. Additionally, the cost for Amazon EKS compared to the other options is higher due to the per-cluster cost of cluster management.

* Table 4 – Monthly cost summary by service *

|  Service  |  Monthly cost  |
| --- | --- |
|  Amazon EC2  |  $192.57 ([details](https://calculator.aws/#/estimate?id=0edb5bb42e05b928bb33280f39eb5ce8d1320d9a))  |
|  Amazon EKS  |  $265.57 ([details](https://calculator.aws/#/estimate?id=eb7d83bfdc8604447dca6c0fa873d679d3ef90f9))  |
|  Amazon ECS  |  $192.57 ([details](https://calculator.aws/#/estimate?id=0edb5bb42e05b928bb33280f39eb5ce8d1320d9a))  |
|  AWS Fargate  |  $124.41 ([details](https://calculator.aws/#/estimate?id=451e0a2f96e0d7f1ae05291abad50165cb72bbc9))  |

## Self-managed containers on Amazon EC2
<a name="self-managed-containers-on-amazon-ec2"></a>

 Running self-managed containers on Amazon EC2 gives you the highest level of control over the underlying compute but it comes with the highest TCO as you manage the entirety of the container’s lifecycle. Additionally, you are responsible for optimally utilizing the underlying compute, rather than leaving this to the managed container orchestrator. For more information, refer to the details links in the preceding table.
+  **Amazon EKS** — With Amazon EKS, you pay $0.10 per hour for each cluster that you create. You can use a single Amazon EKS cluster to run multiple applications by taking advantage of Kubernetes namespaces and IAM security policies. You can run Windows containers on Amazon EKS using the Amazon EC2 launch type and on-premises using [AWS Outposts](https://aws.amazon.com/outposts/) or [Amazon EKS Anywhere](https://aws.amazon.com/eks/eks-anywhere/).

   If you are using Amazon EC2 (including with Amazon EKS–managed node groups), you pay for AWS resources (such as EC2 instances or EBS volumes) you create to run your Kubernetes worker nodes. You only pay for what you use, as you use it; there are no minimum fees and no upfront commitments.

   The calculations in this guide use Amazon EC2 for compute. For more details on Amazon EKS pricing, refer to the [Amazon EKS pricing](https://aws.amazon.com/eks/pricing/) webpage.
+  **Amazon ECS** — With Amazon ECS, there is no additional charge for the cluster orchestrator. You can run Windows containers on Amazon ECS using the Amazon EC2 launch type and on-premises using AWS Outposts or Amazon ECS Anywhere. Again, you only pay for what you use, as you use it; there are no minimum fees and no upfront commitments.

   The calculations in this guide use EC2 for compute. For more details on ECS pricing, refer to the [Amazon ECS pricing](https://aws.amazon.com/ecs/pricing/) webpage.
+  **AWS Fargate** — With AWS Fargate, there are no upfront costs and you pay only for the resources you use. You pay for the amount of vCPU, memory, and storage resources consumed by your containerized applications running on [Amazon ECS](https://aws.amazon.com/ecs/) or [Amazon EKS](https://aws.amazon.com/eks/).

   The calculations in this guide use Fargate for compute. For more details on Fargate pricing, refer to the [AWS Fargate pricing](https://aws.amazon.com/fargate/pricing/) webpage.

### Operational costs (staffing)
<a name="operational-costs-staffing"></a>

 One of the benefits of using managed services is that you can save time by not having to perform operations that are considered undifferentiated heavy lifting. Managed services in AWS such as Amazon ECS and Amazon EKS remove the burden of managing your container orchestrator, freeing your resources to focus more on building your applications to drive business outcomes.
