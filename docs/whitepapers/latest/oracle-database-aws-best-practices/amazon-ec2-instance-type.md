---
source_url: https://docs.aws.amazon.com/whitepapers/latest/oracle-database-aws-best-practices/amazon-ec2-instance-type.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon EC2 instance type
<a name="amazon-ec2-instance-type"></a>

 AWS has a large number of Amazon EC2 instance types available, so you can choose the instance type that best fits your workload. However, not all the available instance types are best suited for running Oracle Database.

 If you use Amazon RDS for your Oracle Database, AWS filters out some of the instance types based on best practices, and gives you the various options in T- class, M-class and R-class instances. AWS recommends that you choose db.m- based or r-based Amazon RDS instances for any enterprise database workloads. R5 instances are well suited for memory intensive applications such as high-performance databases.

For the latest information about RDS instances, refer to [Amazon RDS for Oracle Database Pricing](https://aws.amazon.com/rds/oracle/pricing/). Your choice of the Amazon RDS instance type should be based on the database workload and the Oracle Database licenses available.

 If you’re running your self-managed database on Amazon EC2, you have many more choices available for the Amazon EC2 instance type. This is often one of the reasons users opt to run Oracle Database on Amazon EC2 instead of using Amazon RDS.

Very small instance types are not suitable because Oracle Database is resource-intensive when it comes to CPU usage. Instances with a larger memory footprint help improve database performance by providing better caching and a bigger system global area (SGA). AWS recommends that you choose instances that have a good balance of memory and CPU.

Choose the instance type that matches the Oracle Database licenses you are planning to use and the architecture you are planning to implement. For architectures best suited for your business needs, refer to the whitepaper [Advanced Architectures for Oracle Database on Amazon EC2.](https://d1.awsstatic.com/whitepapers/aws-advanced-architectures-for-oracle-db-on-ec2.pdf)

 Oracle Database uses disk storage heavily for read/write operations, so AWS highly recommends that you use only instances optimized for Amazon Elastic Block Store (Amazon EBS). Amazon EBS-optimized instances deliver dedicated throughput between Amazon EC2 and Amazon EBS. Bandwidth and throughput to the storage subsystem is crucial for good database performance. Choose instances with higher network performance for better database performance.

 The following instance families are best suited for running Oracle Database on Amazon EC2.

|  **Instance family**  |  **Features**  |
| --- | --- |
|  M family  |  +   EBS-optimized by default at no additional cost  <br />+   Support for [Enhanced Networking](https://aws.amazon.com/ec2/faqs/#Enhanced_Networking)  <br />+   Balance of compute, memory, and network resources    |
|  X family  | +   Lowest price per GiB of RAM  <br />+   SSD Storage and EBS-optimized by default and at no additional cost  <br />+   Ability to control processor C-state and P-state configuration    |
|  R family  | +   Optimized for memory-intensive applications  <br />+   High-frequency Intel Xeon E5-2686 v4 (Broadwell) Processors  <br />+   DDR4 Memory  <br />+   Support for [Enhanced Networking](https://aws.amazon.com/ec2/faqs/#Enhanced_Networking)  <br />+ R5b instances support bandwidth up to 60Gbps and EBS performance of 260K IOPS, providing 3x higher [EBS-Optimized](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) performance compared to R5 instances  |
|  I family  | +   Optimized for low latency, very high random I/O performance, high sequential read throughput, and provides high IOPS at a low cost  <br />+   NVMe SSD ephemeral storage  <br />+   Support for [TRIM](https://aws.amazon.com/ec2/faqs/#Do_High_IO_Instances_Support_Trim)  <br />+   Support for [Enhanced Networking](https://aws.amazon.com/ec2/faqs/#Enhanced_Networking)    |
|  Z1d family  |  +   Sustained all core frequency of 4.0 GHz  <br />+   Delivers a 1:8 vCPU to memory ratio    |
