---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sap-ase-to-amazon-rds-sql-server-database-migration/phase-one-prepare.html
---

# Phase 1: Prepare

Assess the source SAP ASE database architecture to understand its dependencies and current state.

## Assess the source database
<a name="assess-the-source-database.09a2d41c-78b3-5c33-9765-c3d227346224"></a>

To assess the source database, such as objects, users, and permissions, you can use third-party tools. For more information, see [Preparation and assessment for migrating from SAP ASE to Amazon Aurora MySQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-sap-ase-aurora-mysql.assessment.html).
+ Analyze the code conversion by listing all of the application dependencies and interfaces.
+ Identify SAP application dependencies that are only supported in SAP. You may need to find an alternative method to work with Microsoft SQL.
+ Identify communication protocols.
+ Identify replication requirements and high availability/disaster recovery compliance.
+ Identify security compliance and encryption protocols.

You can use any third-party migration tool for converting the schema code, such as SAP ASE database or Amazon RDS for SQL Server. You must convert some code manually, such as non-ANSI SQL, because SQL Server may not support it. After you convert the code, conduct unit and functional testing to validate database objects. For more information, see [Migrate your SAP ASE (Sybase ASE) database to Amazon RDS for SQL Server](https://aws.amazon.com/blogs/database/migrate-your-sap-ase-sybase-ase-database-to-amazon-rds-for-sql-server/).

## Evaluate security concerns
<a name="evaluate-security-concerns.91adef1b-6494-5f25-b49d-995457fe99ec"></a>

SQL Server offers various security options that are based on enterprise compliance requirements and unique use cases. For more information, see the following documents about the security of SQL Server:
+ [Authenticate Microsoft SQL Server on Amazon EC2 using AWS Directory Service](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/authenticate-microsoft-sql-server-on-amazon-ec2-using-aws-directory-service.html)
+ [Enable transparent data encryption in Amazon RDS for SQL Server](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-transparent-data-encryption-in-amazon-rds-for-sql-server.html)

## Consult AWS Partners
<a name="consult-9999999999999999aws--partners.0de919a2-7e97-5e2f-8cdb-74ef5889655d"></a>

To reduce migration times, consider consulting with [AWS Database Migration Service Partners](https://aws.amazon.com/dms/partners/). AWS Partners have the necessary expertise to help with both homogeneous and heterogeneous migrations between different database platforms, such as SAP ASE to Amazon Aurora MySQL or Microsoft SQL Server to MySQL.

Based on your requirements and preferences, partners can provide tools and advice for how to handle migrations or troubleshoot migration aspects. Ensure that you follow AWS best practices to host your database in the AWS Cloud. For more information, see [Best practices for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.html).
