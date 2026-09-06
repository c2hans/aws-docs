---
source_url: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-is-different-in-the-cloud.html
---

# Disaster recovery is different in the cloud
<a name="disaster-recovery-is-different-in-the-cloud"></a>

 Disaster recovery strategies evolve with technical innovation. A disaster recovery plan on-premises may involve physically transporting tapes or replicating data to another site. Your organization needs to re-evaluate the business impact, risk, and cost of its previous disaster recovery strategies in order to fulfill its DR objectives on AWS. Disaster recovery in the AWS Cloud includes the following advantages over traditional environments:
+  Recover quickly from a disaster with reduced complexity
+  Simple and repeatable testing allow you to test more easily and more frequently
+  Lower management overhead decreases operational burden
+  Opportunities to automate decrease chances of error and improve recovery time

 AWS allows you to trade the fixed capital expense of a physical backup data center for the variable operating expense of a rightsized environment in the cloud, which can significantly reduce cost.

 For a lot of organizations, on-premises disaster recovery was based around the risk of disruption to a workload or workloads in a data center and the recovery of backed up or replicated data to a secondary data center. When organizations deploy workloads on AWS, they can implement a well-architected workload and rely on the design of the AWS Global Cloud Infrastructure to help mitigate the effect of such disruptions. See the [AWS Well-Architected Framework - Reliability Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) for more information on architectural best practices for designing and operating reliable, secure, efficient, and cost-effective workloads in the cloud. Use the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/) to review your workloads periodically to ensure that they follow the best practices and guidance of the Well-Architected Framework. The tool is available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected/).

 If your workloads are on AWS, you don’t need to worry about data center connectivity (with the exception of your ability to access it), power, air conditioning, fire suppression and hardware. All of this is managed for you and you have access to multiple fault-isolated Availability Zones (each made up of one or more discrete data centers).

## Single AWS Region
<a name="single-aws-region"></a>

 For a disaster event based on disruption or loss of one physical data center, implementing a highly available workload in multiple Availability Zones within a single AWS Region helps mitigate against natural and technical disasters. Continuous backup of data within this single Region can reduce the risk to human threats, such as an error or unauthorized activity that could result in data loss. Each AWS Region is comprised of multiple Availability Zones, each isolated from faults in the other zones. Each Availability Zone in turn consists of one or more discrete physical data centers. To better isolate impactful issues and achieve high availability, you can partition workloads across multiple zones in the same Region. Availability Zones are designed for physical redundancy and provide resilience, allowing for uninterrupted performance, even in the event of power outages, Internet downtime, floods, and other natural disasters. See [AWS Global Cloud Infrastructure](https://www.infrastructure.aws/) to discover how AWS does this.

 By deploying across multiple Availability Zones in a single AWS Region, your workload is better protected against failure of a single (or even multiple) data centers. For extra assurance with your single-Region deployment, you can back up data and configuration (including infrastructure definition) to another Region. This strategy reduces the scope of your disaster recovery plan to only include data backup and restoration. Leveraging multi-region resiliency by backing up to another AWS Region is simple and inexpensive relative to the other multi-Region options described in the following section. For example, backing up to [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3) gives you access to immediate retrieval of your data. However if your DR strategy for portions of your data has more relaxed requirements for retrieval times (from minutes to hours), then using [Amazon Glacier or Amazon Glacier Deep Archive](https://aws.amazon.com/glacier/) will significantly reduce costs of your backup and recovery strategy.

 Some workloads may have regulatory data residency requirements. If this applies to your workload in a locality that currently has only one AWS Region, then in addition to designing multi-AZ workloads for high availability as discussed above, you can also use the AZs within that Region as discrete locations, which can be helpful for addressing data residency requirements applicable to your workload within that Region. The DR strategies described in the following sections use multiple AWS Regions, but can also be implemented using Availability Zones instead of Regions.

## Multiple AWS Regions
<a name="multiple-aws-regions"></a>

 For a disaster event that includes the risk of losing multiple data centers a significant distance away from each other, you should consider disaster recovery options to mitigate against natural and technical disasters that affect an entire Region within AWS. All of the options described in the following sections can be implemented as multi-Region architectures to protect against such disasters.
