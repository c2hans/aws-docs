---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-storage-for-vmware-professionals/high-availability-and-fault-tolerance.html
---

# High availability and fault tolerance
<a name="high-availability-and-fault-tolerance"></a>

VMware provides high availability through features like fault tolerance, requiring manual configuration and resource overhead for VM recovery and data synchronization across hosts. In contrast, AWS builds high availability into its storage services by default, using multiple Availability Zones for automatic data replication and redundancy. While VMware requires additional resources and manual configurations for high-availability setups, AWS services like Amazon S3 and Amazon EFS have a distributed architecture that natively supports cross-AZ replication. The following table provides a comparison of features.

|
|
| Aspect | VMware | AWS |
| --- |--- |--- |
| High-availability features | + Fault tolerance with identical VM copies<br />+ vSAN stretched cluster<br />+ vSphere high-availability clusters | + Automatic recovery for EC2 instances<br />+ EBS multi-attach and snapshots<br />+ EFS redundant storage across AZs<br />+ Multi-AZ storage replication<br />+ S3 with 11 nines of durability |
| Resource management | + Admission control policies<br />+ Reserved capacity for failover | + Automatic scaling<br />+ No traditional resource reservation needed<br />+ Pay-as-you-go model |
| Data protection | + Real-time synchronization for fault tolerance<br />+ VM snapshots<br />+ vSAN data replication across nodes | + Automatic data replication (S3 and EFS) across AZs<br />+ EBS snapshots<br />+ S3 cross-Region replication |
| Recovery capabilities | + Manual intervention may be required<br />+ Secondary VM takes over with no downtime (fault tolerance)<br />+ vSphere high availability | + Automatic recovery across AZs<br />+ Volume restoration from snapshots |

By default, AWS provides high availability for most storage services using Availability Zones and other mechanisms:
+ [**Amazon S3**](https://docs.aws.amazon.com/s3/)** –** Automatically replicates data across multiple AZs within a Region, providing 99.999999999% (11 nines) of durability.
+ [**Amazon EBS multi-attach and snapshots**](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html)** –** Uses snapshots stored in Amazon S3 for cross-AZ recovery. While Amazon EBS volumes don't automatically span AZs, snapshots promote volume restoration in another AZ. Volumes support various configurations including redundant array of independent disks (RAID) setups and can be resized without stopping instances.
+ [**Amazon EFS**](https://docs.aws.amazon.com/efs/)** –** Stores data redundantly across multiple AZs, maintaining availability even if one AZ fails.
+ **Automatic recovery and cross-Region replication –** Amazon EC2 instances automatically recover from hardware and network issues. Amazon S3 cross-Region replication duplicates data in other Regions for disaster recovery and compliance requirements.
