---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/table-migration.html
---

# Migrating existing tables to Iceberg

This section covers how to migrate an existing table into Apache Iceberg on AWS. It applies to tables in Hive-compatible formats ([Apache Parquet](https://parquet.apache.org/), [Apache ORC](https://orc.apache.org/), Apache Avro) as well as to tables that already use a modern open table format ([Apache Hudi](https://hudi.apache.org/), Linux Foundation [Delta Lake](https://delta.io/)). Three migration approaches are available on AWS:
+ [Self-managed in-place migration to self-managed Iceberg on Amazon S3](in-place-migration-to-self-managed-iceberg-on-s3.md) — you generate Iceberg metadata files over the existing data files without rewriting them. Fast and low-cost. Only applies to targets on general Amazon S3 (self-managed); [Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables.html) is not a valid target for in-place migration.
+ [Self-managed full data migration to self-managed Iceberg on Amazon S3 or Amazon S3 Tables](self-managed-full-migration-to-iceberg-on-s3-s3-tables.md) — you read from the source table and rewrite the data as a new Iceberg table (typically with `CREATE TABLE ... AS SELECT`). Slower and more expensive, but the result is a fully independent copy that supports any source format (including CSV, JSON) and lets you re-optimize partitioning, sort order, and file sizes at migration time.
+ [Managed migration to Amazon S3 Tables](managed-migration-to-amazon-s3-tables.md) — Amazon S3 runs the migration on your behalf for Hive-format tables registered in the AWS Glue Data Catalog. No compute to provision; Amazon S3 also applies Hive-to-Iceberg conversions and output optimization.

The first two approaches are user-run — you provision the compute and control the migration end to end. The third is Amazon-managed. The following two tables compare the underlying migration mechanics (in-place vs full data rewrite); the [**Decision trees **](#decision-trees)section that follows maps a specific source and target to the appropriate approach.

**Comparison** (in-place vs full data rewrite):

|
|
| **Aspect** | **In-place (metadata-only)** | **Full data migration (rewrite)** |
| --- |--- |--- |
| Speed | Faster (minutes) — proportional to number of data files | Slower (hours or days) — proportional to volume of data |
| Cost | Lower (no data copy) | Higher (more S3 calls \+ compute) |
| Storage | Same files, new metadata (zero data movement) | New files, optimized layout (temporary double-storage during the migration until the source table is deleted) |
| Source format | Already Parquet, ORC, or Avro | Any format (including CSV, JSON) |
| Target destination | General S3 only | General S3 or Amazon S3 Tables |
| Data files | Shared between original and Iceberg table (maintenance operations on the Iceberg side can impact the source) | New independent files (no risk to source table) |

**When to choose which**:

|
|
| **Factor** | **Choose in-place** | **Choose full data migration** |
| --- |--- |--- |
| Data volume | Very large (TBs\+), rewrite cost prohibitive | Any size (for very large tables where rewrite cost is prohibitive, you can optionally migrate only the most recent data and keep the original table for historical data — consumers must then query both tables) |
| Partitioning and file layout | Current layout is acceptable | Want to optimize partitioning, sorting, or file sizes |
| Independence from source | OK sharing files with the source table temporarily | Need a fully independent copy |
| Target is Amazon S3 Tables | Not possible | Only option |

## Decision trees
<a name="decision-trees"></a>

Use the trees below to pick a migration approach for your source table. Each tree splits on target (Amazon S3 Tables or general Amazon S3) and on the properties of the source, and ends in one of the three approaches introduced above. For the mechanics, prerequisites, code examples, and known limitations of each approach — including per-source-format details (Hive, Hudi, Delta) for the in-place option — see the corresponding subsection linked in the introduction.

**Note**
: The trees point you at the migration **approach**. Before committing, confirm feasibility for your workload by reviewing the specific limitations of the tool that approach uses (Apache XTable, Delta UniForm, the S3 Tables managed migration API, or your own Spark-based rewrite) in the linked subsection — supported source versions, deletion-vector handling, column-statistics behavior, source-format coverage, and schema or type constraints vary by tool.

**Decision tree — source: Hive-style tables (Parquet, ORC, Avro, CSV, JSON)**:

![Decision tree for migrating Hive-style tables to Apache Iceberg on AWS, branching on target (S3 Tables vs general-purpose S3), source format, layout changes, and dataset size to recommend AWS-managed migration, self-managed full migration, or self-managed in-place migration.](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/7eee5d8c-19f3-46dd-baf4-e0f73d98424c.png)

**Decision tree — source: Apache Hudi tables**:

![Decision tree for migrating Apache Hudi tables to Apache Iceberg on AWS, branching on target (S3 Tables vs general-purpose S3), whether you need to reshape schema/partitioning, merge-on-read vs copy-on-write source, and whether the Hudi source can be modified, to recommend self-managed full data migration or self-managed in-place migration via Apache XTable.](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/41c621c9-9bed-4e78-a662-24d86e821eca.png)

**Decision tree — source: Delta Lake tables**:

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/474f4061-ca7d-4c8f-9c14-d9621e96740f.png)

For the mechanics, prerequisites, code, and limitations of whichever approach a tree landed you on, see its subsection: [in-place migration](in-place-migration-to-self-managed-iceberg-on-s3.md), [full data migration](self-managed-full-migration-to-iceberg-on-s3-s3-tables.md), or [managed migration to S3 Tables](managed-migration-to-amazon-s3-tables.md).
