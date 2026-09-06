---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/best-practices.html
---

# Best practices
<a name="best-practices"></a>

We recommend the following best practices for accessing archived data:
+ For huge archival datasets, we recommend creating AWS Glue tables on top of the data so that they can be read by using query engines such Athena and Amazon Redshift. Both Athena and Amazon Redshift provide horizontal scaling of query performance. They also use a pay-per-query model, which is cost-effective in a one-time querying scenario. Additionally, Amazon Redshift has Advanced Query Accelerator (AQUA) engines under the hood, which speeds up read performance at no extra cost.
+ Archived data offloaded regularly in Amazon S3 should not be stored as a heap dump. Instead, it should be saved as a new partition. A date partition will separate data into date dimensions (for example, `year=<value>/month=<value>/day=<value>`). This is extremely beneficial in two situations:
  + If AWS Glue tables are created by AWS Glue crawlers, these partitions act as pseudo columns. This enhances read performance by restricting data scanned to the partitions in the range query.
  + This helps in an S3 Glacier restoration operation when you are restoring only a subset of the object as S3 Standard.
+ AWS Glue crawlers show great value when archived data saved in Amazon S3 is partitioned physically. Every time that data is off-loaded as new prefix partition, the crawler scans only the new partition and updates the metadata for that partition. If the schema of the table changes, those changes will be captured in partition-level metadata.
