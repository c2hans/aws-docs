---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/native-postgre-sql-client-applications.html
---

# Native PostgreSQL client applications
<a name="native-postgre-sql-client-applications"></a>

You can use native PostgreSQL client applications for an offline migration, including [pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html), [pg\_dumpall](https://www.postgresql.org/docs/current/app-pg-dumpall.html), and [pg\_restore](https://www.postgresql.org/docs/current/app-pgrestore.html). The pg\_dump utility is for backing up PostgreSQL databases. You can use pg\_dump to make consistent backups and back up a single database. To back up global objects that are common to all databases in a cluster (such as roles and tablespaces), use pg\_dumpall. We recommend that you run the pg\_dump utility as a superuser because only a superuser can perform a complete dump. The pg\_dump utility also offers options to optimize the backup process, including using the jobs option (for running the dump in parallel) and the directory format when you take the backup. For more information, see the *Options* section of the [pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html) page in the PostgreSQL documentation.

The pg\_restore utility is for restoring a PostgreSQL database from an archive created by pg\_dump. You can run the pg\_restore utility in parallel mode if you use pg\_dump in custom or directory format. To increase the performance of pg\_restore, you can tune the following parameters:
+ Set `shared_buffers` to align with your requirements and increase `maintenance_work_mem` to speed up index creation.
+ Turn off extensive logging, the autovacuum daemon, and `full_page_writes`.
+ (Optionally) Back up and restore the schema and use a data-only dump and restore. If you use this method, you can use the `disable-triggers` option to improve performance.

You can run pg\_dump and pg\_restore from your target EC2 instance. We recommend that you use [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) for better speed and performance. Finally, make sure that you have sufficient storage for the backup file.

## Architecture
<a name="architecture-native-postgresql-client-apps"></a>

The following diagram shows the architecture for migrating an on-premises PostgreSQL database to the AWS Cloud by using native PostgreSQL client applications.

![Native PostgreSQL client application architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/images/guide-img/d9d57133-1a8b-4b7f-bbe9-e908969d06b9/images/cc2228b2-7c9e-47af-8e31-243e987cd5c6.png)

The diagram shows the following workflow:

1. Take backups by using pg\_dump.

1. Create an EC2 instance and install PostgreSQL on the instance.

1. Copy the dump file to Amazon EC2.

1. Restore the backup file by using pg\_restore.

## Limitations
<a name="limitations-native-postgresql-client-apps"></a>

We recommend that you consider the following limitations of using native PostgreSQL client applications before starting your migration:
+ A dump and restore can be time-consuming for larger databases (that is, databases greater than 300 GB).
+ This option requires complete database downtime.
+ A significant amount of diskspace is required on the server to take backups and then copy the backups to Amazon EC2.
