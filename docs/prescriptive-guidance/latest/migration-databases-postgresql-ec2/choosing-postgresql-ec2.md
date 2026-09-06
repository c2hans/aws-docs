---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/choosing-postgresql-ec2.html
---

# Choosing PostgreSQL on Amazon EC2
<a name="choosing-postgresql-ec2"></a>

You have the option to migrate your on-premises PostgreSQL database to Amazon EC2 or Amazon Relational Database Service (Amazon RDS). Important considerations include cost, storage options, high availability and disaster recovery (HADR) capabilities, organizational requirements, and business goals.

In general, we recommend that you use PostgreSQL on Amazon EC2 if any of the following requirements fit your use case:
+ You want more flexibility to control database instances and to access the database file system, but you don't have time to test modernization options (for example, you have the dependency of copying the files on a database server).
+ You have a mission-critical dependency for an application on a specific PostgreSQL extension like PL/Java or any earlier version on PostGIS.
+ You want to exit your data center as quickly as possible.
+ Your application depends on a deprecated version of PostgreSQL, and you don't want to upgrade to a more recent version.
