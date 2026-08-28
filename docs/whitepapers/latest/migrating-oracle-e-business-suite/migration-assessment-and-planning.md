---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/migration-assessment-and-planning.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Migration assessment and planning
<a name="migration-assessment-and-planning"></a>

 Before Oracle E-Business Suite ERP can be migrated, customers need to consider the following:
+  **Edge applications** – Application discovery tools, such as [AWS Application Discovery Service](https://aws.amazon.com/application-discovery/) or [Migration Evaluator](https://aws.amazon.com/migration-evaluator/) (formerly known as TSOLogic) can provide useful information on applications and systems interacting with Oracle E-Business Suite. Analyze the edge applications to determine whether they need to be migrated to the cloud first or later. This approach can also help you calculate the impact of Oracle E-Business Suite migration.
+  **Current system utilization** – Check the current utilization of application servers, database servers, and concurrent processing servers for Oracle E-Business Suite. Utilization must be measured over a few weeks, observing the peak periods for I/O, and throughput capacity required on the database. You can get this information using various monitoring tools already available within your organization. As part of a migration exercise, discovery tools such as [AWS Application Discovery Service](https://aws.amazon.com/application-discovery/) or [Migration Evaluator](https://aws.amazon.com/migration-evaluator/) can also provide insight on current systems utilization, and appropriate instance sizing on AWS.
+  **Target instance types** – Provision a database instance for the I/O and throughput that you observed on premises to serve the real-time and the batch workloads. For more information, refer to the [Right Sizing: Provisioning Instances to Match Workloads whitepaper](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-right-sizing/cost-optimization-right-sizing.html).
+  **Downtime** – You also need to plan for a downtime to cutover to the new production instance after migration and setup is done. To reduce the downtime, you can make use of various tools that are discussed throughout the following sections.
+  **Recovery Point Objective (RPO) and Recovery Time Objective (RTO)** – Your current service level agreements (SLAs) can be improved as you migrate to the cloud. AWS recommends that you run the Oracle E-Business Suite production environment across multiple Availability Zones (AZs) within the AWS Region for high availability (HA). Each [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) instance in an AZ offers 99.99% infrastructure availability. Based on your needs, you can also have a multi-Regional setup for disaster recovery (DR).
+  **RAC versus non-RAC** – You might be running your current production databases underlying Oracle E-Business Suite on [Oracle Real Application Clusters](https://www.oracle.com/database/real-application-clusters/) (Oracle RAC). While RAC improves availability and allows more throughput, by using appropriate AWS services and other Oracle HA tools such as Oracle Data Guard, you can achieve a similar level of performance and availability without implementing RAC on AWS. While sizing database nodes on AWS, consider the aggregate CPU, memory, and throughout numbers from all instances in RAC. Oracle RAC addresses a very specific use case, and can be prohibitively expensive compared to architecting non-RAC, however in some cases Oracle RAC is the right solution depending on the business requirements and use case. We recommend customers work backwards from the workload’s requirements to determine if Oracle RAC is a good fit, and we encourage customers to consider Well-Architected alternatives first, and work backwards from the business requirements.
+  **Oracle RAC use cases:**
  +  **Scalability** – Oracle RAC was designed for scalability when single core x86 CPUs were standard. AWS offers instance types up to 224 vCPU cores and 24 TB of memory.
  +  **Availability** – When supported by the application, Oracle RAC provides local availability. Most RPO and RTO requirements can be achieved with a lower cost HA solution, within and across Availability Zones.
  +  **Performance** – Oracle RAC performance penalties due to cache fusion and other clustering overhead. In most scenarios, placing all resources on a single node will outperform the same amount of resources split between multiple nodes.
  +  **Maintenance** – When supported by the application, zero downtime, rolling maintenance can be performed on Oracle RAC clusters, reducing the required maintenance outages
+  **AWS Oracle RAC solutions:**
  +  Oracle RAC on AWS
  +  [Oracle RAC on VMC](https://aws.amazon.com/blogs/apn/virtualizing-oracle-rac-with-vmware-cloud-on-aws/)
  +  Third-party marketplace offerings, such as [FlashGrid](https://aws.amazon.com/marketplace/seller-profile?id=7dfef247-8246-458d-a962-985a43266f74)
+  **Homogeneous versus heterogeneous migration** – Depending on the source operating system (OS) you are migrating from, Oracle E-Business Suite migration can be considered homogeneous or heterogeneous. Refer to the following table to determine your migration type. If the [endian formats](https://en.wikipedia.org/wiki/Endianness) for source and target OS are different, they are considered to be the heterogeneous migrations of Oracle E-Business Suite.

 *Table 1 — Migration types*

|  **Source OS**  |   **Source Endian Format**   |   **Recommended Target OS on AWS**   |   **Target Endian Format**   |
| --- | --- | --- | --- |
|  Windows  |  Little endian  |  Windows  |  Little endian  |
|  Linux  |  Little endian  |  Linux  |  Little endian  |
|  IBM AIX  |  Big endian  |  Linux  |  Little endian  |
|  HP-UX  |  Big endian  |  Linux  |  Little endian  |
|  Solaris SPARC  |  Big endian  |  Linux  |  Little endian  |
|  Solaris x86  |  Little endian  |  Linux  |  Little endian  |

 To query the endianness of platforms, connect to the database as [SYSDBA](https://docs.oracle.com/en/database/oracle/oracle-database/19/admqs/administering-user-accounts-and-security.html#GUID-2033E766-8FE6-4FBA-97E0-2607B083FA2C) using [SQL\*Plus](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqpug/SQL-Plus-quick-start.html) and run the following command:

```
SQL> select platform_name, endian_format from v$transportable_platform;
```

 Heterogeneous migrations are more complex, because only a subset of tools is available for migration, and you need to do thorough testing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
