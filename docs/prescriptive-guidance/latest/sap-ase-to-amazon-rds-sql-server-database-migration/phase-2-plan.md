---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sap-ase-to-amazon-rds-sql-server-database-migration/phase-2-plan.html
---

# Phase 2: Plan

Based on your workload and application, choose either [RDS custom for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/working-with-custom-sqlserver.html) or [RDS for Microsoft SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html). For most database migrations, you can rehost, replatform, or refactor. The guiding principle should be how to maximize a migration's benefits.

Choosing to refactor your application and migrate to a cloud-native database such as Aurora can enhance your database application. Depending on your workload complexity, however, refactoring a database can be time-consuming and resource-intensive.

## Migration option for Amazon RDS for SQL Server
<a name="migration-option-for-9999999999999999rdslongms-.76d2a3c4-eb06-51de-a85a-e938a7f1c644"></a>

Consider whether your source database is already set up to synchronize primary and secondary database servers, and then decide how you want to synchronize your servers on AWS. The following are three approaches:
+ Multiple Availability Zones
+ Region replication
+ [Cross-Region read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.XRgn.html)

In the following architecture diagram, AWS Direct Connect establishes a dedicated, private network connection between the on-premises data center and Amazon VPC. The target database environment has a primary Amazon RDS for SQL Server deployed in one Availability Zone, with a read replica in a second Availability Zone for high availability and disaster recovery. AWS Database Migration Service (AWS DMS) manages the migration process to help minimize downtime.

![Migration architecture for Amazon RDS for SQL Server.](https://docs.aws.amazon.com/prescriptive-guidance/latest/sap-ase-to-amazon-rds-sql-server-database-migration/images/guide-img/d2f524ef-11f4-4da1-a14a-7b1e8fd93377/images/be0fabe6-9f42-458d-8233-6b1cc0359f10.png)

For enhanced security, the target environment uses private subnets. AWS Secrets Manager handles user credentials, and AWS Key Management Service (AWS KMS) provides encryption at rest for sensitive data. The entire infrastructure is monitored by Amazon CloudWatch, which tracks performance metrics and enables proactive alerting. This design helps to optimize performance while addressing any issues that arise during the migration process.
