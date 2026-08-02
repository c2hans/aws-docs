---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-oracle-database-homogeneous-migration/introduction.html
---

# Strategies for homogeneous migration of Oracle databases to the AWS Cloud
<a name="introduction"></a>

*Rajesh kumar Sabankar, Viqash Adwani, and Jeevan Shetty, Amazon Web Services*

Enterprises that use Oracle often have a fleet of Oracle databases that host various application workloads such as commercial-off-the-shelf (COTS), independent software vendor (ISV), software as a service (SaaS), and other custom, homegrown applications. The approach for migrating these applications to the Amazon Web Services (AWS) Cloud varies based on usage and use cases. AWS approaches migrations in four phases:
+ Phase 1: Prepare
+ Phase 2: Plan
+ Phase 3: Migrate
+ Phase 4: Operate and optimize

This paper discusses these phases and covers migration approaches such as offline migration and continuous data replication. It focuses on *homogeneous migration*, where both your source and your target databases are Oracle databases.

The paper includes services and tools provided by AWS as well as migration solutions offered by Oracle. These tools facilitate various aspects of the migration process, including data validation, schema conversion, and performance optimization.

Selecting the most appropriate migration approach depends on several factors related to the database environment, including database version, size, and specific workload requirements. You can choose a migration strategy that aligns optimally with your operational needs and that minimizes disruption during the transition. This strategic flexibility is essential for ensuring that the migration process is efficient and tailored to your unique demands.

The goal of this document is to assist organizations that are in their initial phases of migrating Oracle workloads to AWS. It introduces migration options so you can choose the migration path for each of your workloads.
