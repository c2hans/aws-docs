---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/considering-online-migration-options.html
---

# Considering online migration options
<a name="considering-online-migration-options"></a>

In an online migration, you migrate an on-premises database in two phases: existing data and change capture. While an on-premises database is up and running, you must first complete the full data load and then migrate changes captured during the full data load. You're ready for cutover when the on-premises and PostgreSQL on Amazon EC2 databases are both in sync. At this point, you can minimize your downtime and point the application to the new migrated PostgreSQL database on Amazon EC2. To perform an online migration, you can choose from a variety of different tools, including AWS DMS, native PostgreSQL logical replication, AWS Application Migration Service, Bucardo, and pglogical.

This section covers the following online migration options:
+ AWS DMS
+ Logical replication
+ AWS Application Migration Service
+ Bucardo
