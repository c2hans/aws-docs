---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-right-sizing/overview-amazon-ec2-amazon-rds.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Overview of Amazon EC2 and Amazon RDS Instance Families
<a name="overview-amazon-ec2-amazon-rds"></a>

 Picking an [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) instance for a given workload means finding the instance family that most closely matches the CPU and memory needs of your workload. Amazon EC2 provides a wide selection of instances, which gives you lots of flexibility to right size your compute resources to match capacity needs at the lowest cost. There are five families of EC2 instances with different options for CPU, memory, and network resources:
+  **General purpose** (includes T2, M3, and M4 instance types) – T2 instances are a very low-cost option that provide a small amount of CPU resources that can be increased in short bursts when additional cycles are available. They are well suited for lower throughput applications such as administrative applications or low-traffic websites. M3 and M4 instances provide a balance of CPU, memory, and network resources and are ideal for running small and midsize databases, more memory-intensive data processing tasks, caching fleets, and backend servers.
+  **Compute optimized** (includes the C3 and C4 instance types) – Have a higher ratio of virtual CPUs to memory than the other families and the lowest cost per virtual CPU of all the EC2 instance types. Consider compute-optimized instances first if you are running CPU-bound, scale-out applications such as frontend fleets for high-traffic websites, on-demand batch processing, distributed analytics, web servers, video encoding, and high-performance science and engineering applications.
+  **Memory optimized** (includes the X1, R3, and R4 instance types) – Designed for memory-intensive applications, these instances have the lowest cost per GiB of RAM of all EC2 instance types. Use these instances if your application is memory-bound.
+  **Storage optimized** (includes the I3 and D2 instance types) – Optimized to deliver tens of thousands of low-latency, random input/output (I/O) operations per second (IOPS) to applications. Storage-optimized instances are best for large deployments of NoSQL databases.

   I3 instances are designed for I/O-intensive workloads and equipped with super-efficient NVMe SSD storage. These instances can deliver up to 3.3 million IOPS in 4 KB blocks and up to 16 GB/second of sequential disk throughput.

   D2 or dense storage instances are designed for workloads that require high sequential read and write access to very large data sets, such as Hadoop distributed computing, massively parallel processing data warehousing, and log-processing applications.
+  **Accelerated computing** (includes the P2, G3, and F1 instance types) – Provide access to hardware-based compute accelerators such as graphics processing units (GPUs) or field programmable gate arrays (FPGAs). Accelerated-computing instances enable more parallelism for higher throughput on compute-intensive workloads.

 [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS) database instances are similar to Amazon EC2 instances in that there are different families to suit different workloads. These database instance families are optimized for memory, performance, or I/O:
+  **Standard performance** (includes the M3 and M4 instance types) – Designed for general-purpose database workloads that don’t run many in-memory functions. This family has the most options for provisioning increased IOPS.
+  **Burstable performance** (includes T2 instance types) – For workloads that require burstable performance capacity.
+  **Memory optimized** (includes the R3 and R4 instance types) – Optimized for in-memory functions and big data analysis.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
