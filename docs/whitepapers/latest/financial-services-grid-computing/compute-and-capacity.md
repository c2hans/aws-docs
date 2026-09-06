---
source_url: https://docs.aws.amazon.com/whitepapers/latest/financial-services-grid-computing/compute-and-capacity.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Compute and capacity
<a name="compute-and-capacity"></a>

 AWS offers a wide range of [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) instance types, which enable you to select the configuration that is best suited to your needs at any given time. This is a departure from the typical *Bill of Materials* approach, which limits the configurations available on-premises in favor of deployment simplicity. It also offers *evergreening*, which enables you to take advantage of the latest CPU technologies as they are released without consideration for any prior investment. HPC customers in financial services should consider the following instances types:
+  **Amazon EC2 compute-optimized instances** — These instances are optimized for compute-intensive workloads and deliver cost-effective high performance at a low price per compute ratio.
+  **Amazon EC2 General-purpose instances** —
  +  ***M*** — Commonly used in HPC applications because they offer a good balance of compute, memory, and networking resources.
  +  ***Z*** — Offer the highest CPU frequencies with a high memory footprint. These instances might be useful for latency sensitive workloads such as product pricing.
  +  ***T*** — Provide a baseline level of CPU performance with the ability to burst to a higher level when required. The use of these instances for HPC workloads can be attractive for some workloads; however, their variable performance profile can result in inconsistent behavior, which might be undesirable.
+  **Amazon EC2 memory optimized instances**—
  +  ***R*** – These instances offer higher memory-to-CPU ratios and so may be applied to X-Valuation Adjustment (XVA) calculations such as Credit Value Adjustments which typically require additional memory to calculate.
+  **Instances with the suffix *a***** have AMD processors, for example, *M7a*.
+  **Instances with the suffix *i*** have Intel processors, for example, *M6i*.
+  **Instances with the suffix *g*** have Arm-based AWS Graviton processors, for example, *M7g*.
+  **Amazon EC2 Accelerated Computing instances** use hardware accelerators, or co-processors, to perform functions such as floating-point number calculations, graphics processing, or data pattern matching, more efficiently than is possible in software running on CPUs.
  +  ***P*** — Intended for general-purpose GPU compute applications.
  +  ***G*** — Intended for graphical rendering and inferences.
  +  ***F*** — Offer customizable hardware acceleration with field programmable gate arrays (FPGAs).
  +  ***Trn*** — Powered by AWS Trainium, purpose-built for cost-effective deep learning training.
  +  ***Inf*** — Powered by AWS Inferentia, use a custom AI/ML processor from Amazon that provides low-latencey inference.

 **HPC class instances** are designed to maximize the performance of tightly coupled workloads such as computational fluid dynamics (CFD), weather forecasting and molecular analysis.

 The latest AWS instances are based on the [AWS Nitro System](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances). The Nitro System is collection of AWS-built hardware and software components that enable high performance, high availability, high security, and bare metal capabilities to eliminate virtualization overhead. By selecting Nitro based instances, HPC applications can expect performance levels that are indistinguishable to a bare-metal system while retaining all of the benefits of an ephemeral virtual host (see [Bare metal performance with the AWS Nitro System](https://aws.amazon.com/blogs/hpc/bare-metal-performance-with-the-aws-nitro-system/).

* Table 1 – Amazon EC2 instance types that are typically used for HPC workloads *

|  Instance Type  |  Family  |  Description  |
| --- | --- | --- |
|  General-purpose  |  M  |  General-purpose instances  |
|  Compute-optimized  |  C  |  For compute intensive workloads  |
|  Memory-optimized  |  R  |  For memory intensive workloads  |
|   |  X  |  For memory intensive workloads  |
|   |  Z  |  High compute capacity and high memory  |
|  Accelerated computing  |  P / G / F  |  General-purpose GPU (P), Graphical GPU (G), or FPGA (F) capabilities  |
|  HPC optimized |  HPC  |  Designed for tightly-coupled, compute-intensive HPC workloads such as computational fluid dynamics (CFD), weather forecasting, and multiphysics simulations |

 This diverse selection of instance types helps support a wide variety of workloads with optimal hardware and promotes experimentation. HPC teams can benchmark various sets of instances to optimize their scheduling strategies. Quantitative developers can try new approaches with GPUs, FPGAs, or the latest CPUs, without upfront costs or protracted procurement processes. You can immediately deploy at scale your optimal approach, without the traditional hardware lifecycle considerations.

 When you run experiments, or if a subset of production workloads requires a specific instance type, grid schedulers typically enable tasks to be directed to the appropriate hardware through compute resource groups.

 To simplify instance selection, AWS also offers [attribute-based instance type selection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html). With this feature, teams can express compute requirements in terms of: vCPUs, memory, storage, and more. Using these attributes, Amazon EC2 Auto Scaling or Amazon EC2 Fleet will choose the instances that fit the specified attributes. This removes the need to manually pick instance types, ensures access a broader range of capacity via Amazon EC2 Spot and automatically enables new instance types as they become available as long as they meet the criteria that you define.
