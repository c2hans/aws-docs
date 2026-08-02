---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/data-migration-strategies.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data migration strategies
<a name="data-migration-strategies"></a>

 The migration strategy you choose depends on several factors:
+  The size of the database
+  Network connectivity between the source server and AWS
+  The version and edition of your Oracle Database software
+  The database options, tools, and utilities that are available
+  The amount of time that is available for migration
+  Whether the migration and switchover to AWS will be done in one step or a sequence of steps over time

 The following sections describe some common migration strategies.

## One-step migration
<a name="one-step-migration"></a>

 One-step migration is a good option for small databases that can be shut down for 24 to 72 hours. During the shut down period, all the data from the source database is extracted, and the extracted data is migrated to the destination database in AWS. The destination database in AWS is tested and validated for data consistency with the source. Once all validations have passed, the database is switched over to AWS.

## Two-step migration
<a name="two-step-migration"></a>

 Two-step migration is a commonly used method because it requires only minimal downtime and can be used for databases of any size:

1.  The data is extracted from the source database at a point in time (preferably during non-peak usage) and migrated while the database is still up and running. Because there is no downtime at this point, the migration window can be sufficiently large. After you complete the data migration, you can validate the data in the destination database for consistency with the source and test the destination database on AWS for performance, connectivity to the applications, and any other criteria as needed.

1.  Data changed in the source database after the initial data migration is propagated to the destination before switchover. This step synchronizes the source and destination databases. This should be scheduled for a time when the database can be shut down (usually over a few hours late at night on a weekend). During this process, there won’t be any more changes to the source database because it will be unavailable to the applications.

    Normally, the amount of data that is changed after the first step is small compared to the total size of the database, so this step will be quick and requires only minimal downtime. After all the changed data is migrated, you can validate the data in the destination database, perform necessary tests, and, if all tests are passed, switch over to the database in AWS.

## Minimal downtime migration
<a name="minimal-downtime-migration"></a>

 Some business situations require database migration with little to no downtime. This requires detailed planning and the necessary data replication tools for proper completion.

 These migration methodologies typically involve two components: an initial bulk extract/load, followed by the application of any changes that occurred during the time the bulk step took to run. After the changes have applied, you should validate the migrated data and conduct any necessary testing.

 The replication process synchronizes the destination database with the source database, and continues to replicate all data changes at the source to the destination.

 Synchronous replication can have an effect on the performance of the source database, so if a few minutes of downtime for the database is acceptable, then you should set up asynchronous replication instead. You can switch over to the database in AWS at any time, because the source and destination databases will always be in sync.

 There are a number of tools available to help with minimal downtime migration. The [AWS Database Migration Service](https://aws.amazon.com/dms/) (AWS DMS) supports a range of database engines, including Oracle running on-premises, in EC2, or on RDS. [Oracle GoldenGate](https://www.oracle.com/integration/goldengate/) is another option for real-time data replication. There are also third-party tools available to do the replication.

## Nearly continuous data replication
<a name="nearly-continuous-data-replication"></a>

 You can use nearly continuous data replication if the destination database in AWS is used as a clone for reporting and business intelligence (BI), or for disaster recovery (DR) purposes. In this case, the process is exactly the same as minimal downtime migration, except that there is no switchover and the replication never stops.
