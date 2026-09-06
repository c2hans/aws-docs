---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-postgresql-on-ec2-using-ebs/conclusion.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Conclusion
<a name="conclusion"></a>

 The AWS cloud provides several options for deploying PostgreSQL and the infrastructure supporting it. Amazon Aurora for PostgreSQL and RDS for PostgreSQL provide a platform to operate, scale, and manage PostgreSQL database in AWS. It removes much of the complexity of managing and maintaining databases, allowing you to focus on improving applications. However, there are some cases where hosting PostgreSQL on Amazon EC2 and Amazon EBS brings operational flexibility and maintenance easiness. It's important to understand PostgreSQL workload and test it. This can help you decide which Amazon EC2 instance and storage to use for optimal performance and cost.

 For a balanced performance and cost consideration, General Purpose SSD Amazon EBS volumes (`gp2` and `gp3`) are good options. To maximize the benefit of `gp2`, you need to understand and monitor the burst credit. This helps determine whether you should consider other volume types. On the other hand, `gp3` provides predictable 3,000 IOPS baseline performance and 125 MiB/s, regardless of volume size. With `gp3` volumes, you can provision IOPS and throughput independently, without increasing storage size, at costs up to 20 percent lower per GB compared to `gp2` volumes. If you have mission critical PostgreSQL workloads that need more consistent IOPS, then you should use Provisioned IOPS volumes (`io1`, `io2`, `io2` Block Express).

 To maximize the benefit of both General Purpose and Provisioned IOPS volume types, AWS recommends using Amazon EBS-optimized Amazon EC2 instances and tuning database parameters to optimize storage consumption. This ensures dedicated network bandwidth for Amazon EBS volumes. You can cost effectively operate your PostgreSQL database in AWS without sacrificing performance by taking advantage of the durability, availability, and elasticity of the Amazon EBS volumes.
