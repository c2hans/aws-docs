---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/instances.html
---

# EC2 instances and layout
<a name="instances"></a>

SQL Server databases that support EnterpriseOne typically require:
+ x86/x64 CPUs
+ High-performance local instance storage for `tempdb`
+ Large amount of memory for buffer cache
+ High storage throughput and IOPS
+ High network throughput
+ Low vCPU count

**Note**
This section provides specific EC2 instance type and Amazon Elastic Block Store (Amazon EBS) storage recommendations, based on the information available at the time of this writing. As AWS adds support for new EC2 instances, Amazon EBS storage types, and Amazon FSx storage types, better options might become available. For the latest information, see the [Resources](resources.md) section of this guide.

The Amazon EC2 [X2iedn](https://aws.amazon.com/ec2/instance-types/x2i/) instance type is the preferred instance type for SQL Server databases that support EnterpriseOne. X2iedn provides high Amazon EBS throughput, high network throughput, and a large quantity of memory and quantity of instance storage per vCPU provisioned. It also supports [Provisioned IOPS SSD (io2) Block Express](https://aws.amazon.com/ebs/provisioned-iops/).

Some EnterpriseOne processes might require low-latency write I/O to support chatty commits. The volume type with the lowest latency write I/O is io2 Block Express, which is available only on a subset of x86/x64 instances that contain instance storage, including X2idn and X2iedn instances. When you use other x86/x64 instances that have instance storage, the lowest latency write I/O volume type will be `io2`.
