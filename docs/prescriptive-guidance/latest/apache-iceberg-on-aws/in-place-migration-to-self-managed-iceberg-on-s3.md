---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/in-place-migration-to-self-managed-iceberg-on-s3.html
---

# In-place migration to self-managed Iceberg on S3

In-place migration eliminates the need to rewrite data files — Iceberg metadata files are generated over the existing data files that the source table already tracks. Because the Iceberg metadata points at those existing files, the target must live in the same Amazon S3 location as the source; **in-place migration is not available for **[**Amazon S3 Tables**](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables.html), which owns its own storage layout.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/61d0c1a5-b500-4851-af98-362991983351.png)

**Cutover note**: In every in-place migration approach shown here, the Iceberg table is derived from a source table and shares data files with it. Writes and maintenance operations on the Iceberg-generated table (for example, `expire_snapshots`, `remove_orphan_files`, or `DROP TABLE ... PURGE`) can corrupt the source data. Treat the Iceberg-generated table as **read-only** until you are ready to cut over — at cutover, stop writes on the source, redirect writers to the Iceberg table, and only then enable Iceberg-side writes and maintenance.

The tooling depends on the source table format:
+ [Hive tables (Parquet, ORC, or Avro)](hive-tables-parquet-orc-or-avro.md) — Iceberg Spark procedures: `snapshot`, `migrate`, `add_files`.
+ [Apache Hudi tables](apache-hudi-tables.md) — [Apache XTable](https://xtable.apache.org/), a sync utility that reads the Hudi commit log and writes an Iceberg metadata layer over the same Parquet data files.
+ [Delta Lake tables](delta-lake-tables.md) — either [Apache XTable](https://xtable.apache.org/) or [Delta Lake UniForm](https://docs.delta.io/latest/delta-uniform.html) (Delta's native Iceberg-metadata generation at every write).

See [Migrating existing tables to Iceberg](table-migration.md) for the comparison with full data migration and the decision tree.
