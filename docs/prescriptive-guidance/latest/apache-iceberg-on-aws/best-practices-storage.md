---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/best-practices-storage.html
---

# Optimizing storage
<a name="best-practices-storage"></a>

Updating or deleting data in an Iceberg table increases the number of copies of your data, as illustrated in the following diagram. The same is true for running compaction: It increases the number of data copies in Amazon S3. That's because Iceberg treats the files underlying all tables as immutable.

![Results of updating or deleting data in an Iceberg table](http://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/c7c62753-4861-4a7e-8b34-86aa38234f33.png)

Follow the best practices in this section to manage storage costs.

## Enable S3 Intelligent-Tiering
<a name="storage-s3-intelligent-tiering"></a>

Use the [Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html) storage class to automatically move data to the most cost-effective access tier when access patterns change. This option has no operational overhead or impact on performance.

**Note**
Don't use the optional tiers (such as Archive Access and Deep Archive Access) in S3 Intelligent-Tiering with Iceberg tables. To archive data, see the guidelines in the next section.

You can also use [Amazon S3 Lifecycle rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to set your own rules for moving objects to another Amazon S3 storage class, such as S3 Standard-IA or S3 One Zone-IA (see [Supported transitions and related constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html#lifecycle-general-considerations-transition-sc) in the Amazon S3 documentation).

## Archive or delete historic snapshots
<a name="storage-snapshots"></a>

For every committed transaction (insert, update, merge into, compaction) to an Iceberg table, a new version or snapshot of the table is created. Over time, the number of versions and the number of metadata files in Amazon S3 accumulate.

Keeping snapshots of a table is required for features such as snapshot isolation, table rollback, and time travel queries. However, storage costs grow with the number of versions that you retain.

The following table describes the design patterns you can implement to manage costs based on your data retention requirements.

|
|
| Design pattern | Solution | Use cases |
| --- |--- |--- |
| **Delete old snapshots** | + Use the [VACUUM statement](https://docs.aws.amazon.com/athena/latest/ug/vacuum-statement.html) in Athena to remove old snapshots. This operation doesn't incur any compute cost.+ Alternatively, you can use Spark on Amazon EMR or AWS Glue to remove snapshots.For more information, see [expire\_snapshots](https://iceberg.apache.org/docs/latest/spark-procedures/#expire_snapshots) in the Iceberg documentation. | This approach deletes snapshots that are no longer needed to reduce storage costs. You can configure how many snapshots should be retained or for how long, based on your data retention requirements.<br />This option performs a hard delete of the snapshots. You can't roll back or time travel to expired snapshots. |
| **Set retention policies for specific snapshots** | 1. Use tags to mark specific snapshots and define a retention policy in Iceberg. For more information, see [Historical Tags](https://iceberg.apache.org/docs/latest/branching/#historical-tags) in the Iceberg documentation.<br />For example, you can retain one snapshot per month for one year by using the following SQL statement in Spark on Amazon EMR:<pre>ALTER TABLE glue_catalog.db.table CREATE TAG 'EOM-01' AS OF VERSION 30 RETAIN 365 DAYS</pre><br />2. Use Spark on Amazon EMR or AWS Glue to remove the remaining untagged, intermediate snapshots. | This pattern is helpful for compliance with business or legal requirements that require you to show the state of a table at a given point in the past. By placing retention policies on specific tagged snapshots, you can remove other (untagged) snapshots that were created. This way, you can meet data retention requirements without retaining every single snapshot created. |
| **Archive old snapshots** | 1. Use Amazon S3 tags to mark objects with Spark. (Amazon S3 tags are different from Iceberg tags; for more information, see the [Iceberg documentation](https://iceberg.apache.org/docs/latest/aws/#s3-tags).) For example:<pre>spark.sql.catalog.my_catalog.s3.delete-enabled=false and spark.sql.catalog.my_catalog.s3.delete.tags.my_key=to_archive</pre><br />2. Use Spark on Amazon EMR or AWS Glue to [remove snapshots](https://iceberg.apache.org/docs/latest/spark-procedures/#expire_snapshots). When you use the settings in the example, this procedure tags objects and detaches them from the Iceberg table metadata instead of deleting them from Amazon S3.<br />3. Use S3 Life cycle rules to transition objects tagged as `to_archive` to one of the [S3 Glacier storage classes](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html).<br />4. To query archived data:[Restore the archived objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/restoring-objects.html) (this step isn't required if objects were transitioned to the Amazon Glacier Instant Retrieval storage class).[register\_table procedure](https://iceberg.apache.org/docs/latest/spark-procedures/#register_table) in Iceberg to register the snapshot as a table in the catalog.For detailed instructions, see the AWS blog post [Improve operational efficiencies of Apache Iceberg tables build on Amazon S3 data lakes](https://aws.amazon.com/blogs/big-data/improve-operational-efficiencies-of-apache-iceberg-tables-built-on-amazon-s3-data-lakes/).<br />  | This pattern allows you to keep all table versions and snapshots at a lower cost.<br />You cannot time travel or roll back to archived snapshots without first restoring those versions as new tables. This is typically acceptable for audit purposes.<br />You can combine this approach with the previous design pattern, setting retention policies for specific snapshots. |

## Delete orphan files
<a name="storage-orphan-files"></a>

In certain situations, Iceberg applications can fail before you commit your transactions. This leaves data files in Amazon S3. Because there was no commit, these files won't be associated with any table, so you might have to clean them up asynchronously.

To handle these deletions, you can use the [VACUUM statement](https://docs.aws.amazon.com/athena/latest/ug/vacuum-statement.html) in Amazon Athena. This statement removes snapshots and also deletes orphaned files. This is very cost-efficient, because Athena doesn't charge for the compute cost of this operation. Also, you don't have to schedule any additional operations when you use the `VACUUM` statement.

Alternatively, you can use Spark on Amazon EMR or AWS Glue to run the `remove_orphan_files` procedure. This operation has a compute cost and has to be scheduled independently. For more information, see the [Iceberg documentation](https://iceberg.apache.org/docs/latest/spark-procedures/#remove_orphan_files).
