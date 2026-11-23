---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/best-practices-storage.html
---

# Optimizing storage

Updating or deleting data in an Iceberg table increases the number of copies of your data, as illustrated in the following diagram. The same is true for running compaction: It increases the number of data copies in Amazon S3. That's because Iceberg treats the files underlying all tables as immutable.

![Results of updating or deleting data in an Iceberg table](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/c7c62753-4861-4a7e-8b34-86aa38234f33.png)

Follow the best practices in this section to manage storage costs.

## Enable Intelligent-Tiering
<a name="enable-intelligent-tiering"></a>

Iceberg tables consist of many immutable data and metadata files whose access patterns cool off over time (older partitions and older snapshots are read much less than the current ones). Enable automatic tiering to a cheaper storage class so cold data is moved out of Standard without any operational effort. The exact feature to use depends on how the table is hosted.

### Amazon S3 Tables Intelligent-Tiering
<a name="amazon-s3-tables-intelligent-tiering"></a>

For tables in Amazon S3 Tables, use the [S3 Tables Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tables-intelligent-tiering.html) storage class to lower storage cost for data whose access cools off over time, such as older partitions and files that only older snapshots reference. Amazon S3 monitors access at the data-file level and moves files through three tiers with no retrieval fees or performance impact: Frequent Access (default), Infrequent Access after 30 consecutive days without access (40% lower cost than Frequent Access), and Archive Instant Access after 90 days (68% lower cost than Infrequent Access), all with millisecond latency; a file returns to Frequent Access the first time it is read. Select the storage class when you create a table, or set it as the table bucket default with `put-table-bucket-storage-class` for tables created afterwards; existing tables stay on Standard, and files smaller than 128 KB are not tiered. Snapshot expiration and unreferenced-file removal run on all tiers, but compaction runs only on Frequent Access files, so delete files against cold data are not compacted until that data is read again or you run compaction manually from Amazon EMR.

### S3 Intelligent-Tiering for self-managed Iceberg
<a name="s3-intelligent-tiering-for-self-managed-iceberg"></a>

For self-managed Iceberg tables on general Amazon S3, use the [Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html) storage class to automatically move data to the most cost-effective access tier when access patterns change. This option has no operational overhead or impact on performance.

**Note**
Don't use the optional tiers (such as Archive Access and Deep Archive Access) in S3 Intelligent-Tiering with Iceberg tables (asynchronous retrieval breaks queries that touch archived files). To archive data, see the guidelines in the next section.

You can also use [Amazon S3 Lifecycle rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to set your own rules for moving objects to another Amazon S3 storage class, such as S3 Standard-IA or S3 One Zone-IA (see [Supported transitions and related constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html#lifecycle-general-considerations-transition-sc) in the Amazon S3 documentation).

## Archive or delete historic snapshots
<a name="archive-or-delete-historic-snapshots"></a>

For every committed transaction (insert, update, merge into, compaction) to an Iceberg table, a new version or snapshot of the table is created. Over time, the number of versions and the number of metadata files in Amazon S3 accumulate.

Keeping snapshots of a table is required for features such as snapshot isolation, table rollback, and time travel queries. However, storage costs grow with the number of versions that you retain.

The following table describes the design patterns you can implement to manage costs based on your data retention requirements.

|
|
| **Design pattern** | **Solution** | **Use cases** |
| --- |--- |--- |
| **Delete old snapshots** | Apply snapshot expiration through one of the three maintenance execution options covered in [Maintaining Iceberg tables](maintaining-iceberg-tables.md) — [self-managed with Iceberg Spark procedures](self-managed-maintenance.md) or the [AWS Glue Iceberg table optimizer](maintenance-with-the-aws-glue-data-catalog-table-optimizer.md) for self-managed Iceberg on Amazon S3, or the [built-in snapshot expiration in Amazon S3 Tables](maintenance-in-amazon-s3-tables.md) for tables in a table bucket. | This approach deletes snapshots that are no longer needed to reduce storage costs. You can configure how many snapshots should be retained or for how long, based on your data retention requirements. This option performs a hard delete of the snapshots. You can't roll back or time travel to expired snapshots. On Amazon S3 Tables set retention with `PutTableMaintenanceConfiguration`; do not set the `history.expire.*` table properties, which disable built-in expiration. |
| **Retain specific snapshots (self-managed tables only)** | 1. Use tags to mark specific snapshots and define a retention policy in Iceberg. For more information, see [Historical Tags](https://iceberg.apache.org/docs/latest/branching/#historical-tags) in the Iceberg documentation. For example, you can retain one snapshot per month for one year by using the following SQL statement in Spark on Amazon EMR:<pre>ALTER TABLE glue_catalog.db.table CREATE TAG 'EOM-01' AS OF VERSION 30 RETAIN 365 DAYS</pre><br /> 2. Use Spark on Amazon EMR or AWS Glue to remove the remaining untagged, intermediate snapshots. | This pattern is helpful for compliance with business or legal requirements that require you to show the state of a table at a given point in the past. By placing retention policies on specific tagged snapshots, you can remove other (untagged) snapshots that were created. This way, you can meet data retention requirements without retaining every single snapshot created. |

## Delete orphan files
<a name="delete-orphan-files"></a>

In certain situations, Iceberg applications can fail before you commit your transactions. This leaves data files in Amazon S3. Because there was no commit, these files won't be associated with any table, so you might have to clean them up asynchronously.

Run orphan-file cleanup through one of the three maintenance execution options covered in [Maintaining Iceberg tables](maintaining-iceberg-tables.md) — [self-managed with Iceberg Spark procedures](self-managed-maintenance.md) or the [AWS Glue Iceberg table optimizer](maintenance-with-the-aws-glue-data-catalog-table-optimizer.md) for self-managed Iceberg on Amazon S3, or the [built-in orphan-file removal in Amazon S3 Tables](maintenance-in-amazon-s3-tables.md) for tables in a table bucket.
