---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/disaster-recovery-with-elastic-disaster-recovery.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 3.1 Disaster recovery with Elastic Disaster Recovery
<a name="disaster-recovery-with-elastic-disaster-recovery"></a>

 Requirements addressed:
+  **REQ4** (availability and durability)

 AWS services – [Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/)

![Disaster recovery solution with AWS DRS](https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/images/disaster-recovery-solution-aws-drs.png)

 Disaster recovery solution with AWS DRS

 AWS [Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/) (AWS DRS) minimizes downtime and data loss with fast, reliable recovery of on-premises and cloud-based applications using affordable storage, minimal compute, and point-in-time recovery. AWS DRS can be used to protect most critical databases, including Oracle, MySQL, and SQL Server, as well as enterprise applications such as SAP.

 AWS DRS continuously replicates block storage volumes (EBS volumes) from physical, virtual, or cloud-based servers (including operating system, system state configuration, databases, applications, and files) into a low-cost staging area subnet in a target AWS account and preferred Region.

 Replication is performed at the block level, using an agent that is installed on each source server. In case of a disaster, you can instruct AWS DRS to automatically launch thousands of machines in their fully provisioned state in minutes (failover). It can be used to continuously backup entire systems automatically, launch them in AWS in case of disaster, and then switch the workloads back (failback) to original the source servers or to any other servers that meet the prerequisites when the situation is recovered.

 This enables Recovery Point Objectives (RPOs) that happen in seconds. Automated machine conversion and orchestration enable Recovery Time Objectives (RTOs) that happen in minutes.

 For more information about AWS Elastic Disaster Recovery, refer to [Getting started with Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/getting-started.html).
