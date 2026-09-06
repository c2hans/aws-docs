---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/method.html
---

# Migration approach
<a name="method"></a>

There are two approaches for migrating Oracle Database from on premises to AWS: offline migration and online migration.

## Offline migration
<a name="offline"></a>

You can use the offline migration approach when your application can afford a planned downtime. In this approach, the source database is taken offline at the beginning of the migration period, and then it's migrated over to the target database on AWS. After the migration is complete, validation and verification checks are performed in the target database to ensure data consistency. When all checks are passed, you perform a cutover by connecting the application to the target database.

Offline migration usually consists of fewer steps, has simpler architecture, and is more cost effective.

## Online migration
<a name="online"></a>

Use the online migration approach when your application requires minimal or near zero downtime. In this scenario, the source database is migrated in multiple steps to AWS. Initially, the data in the source database is copied to the target database while the source database is still running. In subsequent steps, all changes from the source database are propagated to the target database online. When the source and target databases are in sync, they are ready for cutover. During the cutover, the application switches its connections over to the target database, leaving no connections to the source database.

Online migration achieves less downtime, but it requires more steps, resources, and effort, and it's more expensive.
