---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-mysql-on-ec2-using-amazon-ebs/conclusion.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Conclusion
<a name="conclusion"></a>

 The AWS Cloud provides several options for deploying MySQL and the infrastructure supporting it. Amazon RDS for MySQL provides a very good platform to operate, scale, and manage your MySQL database in AWS. It removes much of the complexity of managing and maintaining your database, allowing you to focus on improving your applications.

 However, there are some cases where MySQL on Amazon EC2 and Amazon EBS that work better for some workloads and configurations. It is important to understand your MySQL workload and test it. This can help you decide which EC2 server and storage to use for optimal performance and cost.

 For a balanced performance and cost consideration, General Purpose SSD Amazon EBS volumes (gp2 and gp3) are good options. To maximize the benefit of gp2, you need to understand and monitor the burst credit. This will help you determine whether you should consider other volume types. On the other hand, gp3 provides predictable 3,000 IOPS baseline performance and 125 MiB/s, regardless of volume size. With gp3 volumes, you can provision IOPS and throughput independently, without increasing storage size, at costs up to 20 percent lower per GB compared to gp2 volumes.

 If you have mission critical MySQL workloads that need more consistent IOPS, then you should use Provisioned IOPS volumes (io1 or io2).

 To maximize the benefit of both General Purpose and Provisioned IOPS volume types, AWS recommends using EBS-optimized EC2 instances and tuning your database parameters to optimize storage consumption. This ensures dedicated network bandwidth for your EBS volumes. You can cost effectively operate your MySQL database in AWS without sacrificing performance by taking advantage of the durability, availability, and elasticity of the EBS volumes.
