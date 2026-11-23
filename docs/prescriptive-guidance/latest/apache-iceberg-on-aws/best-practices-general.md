---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/best-practices-general.html
---

# General best practices

Regardless of your use case, when you use Apache Iceberg on AWS, we recommend that you follow these general best practices.

## Choose the Iceberg table format version based on the features you need and the consumers of the table
<a name="choose-the-iceberg-table-format-version-based-on-the-features-you-need-and-the-consumers-of-the-table"></a>

Iceberg V2 is broadly supported by every AWS analytics service and ingestion path that writes Iceberg (Athena, Redshift, EMR, Glue Spark, Firehose, streaming tables) and open-source clients such as PyIceberg. Iceberg V3 adds deletion vectors, row lineage, `variant`, `geometry`/`geography`, and nanosecond timestamps, but is not yet supported by every consumer — see the [V3 support table notes](table-spec-v3.md) first.

Carefully evaluate every downstream consumer's capabilities alongside the V3 features you plan to use. Picking V3 — or a specific V3 feature — that one of your readers can't handle produces a table that part of your pipeline can't consume, and it's a hard problem to unwind because V3 upgrades are one-way. No AWS engine creates V3 tables by default; you opt in per table with `format-version=3`.

## Use the AWS Glue Data Catalog as your data catalog
<a name="use-the-aws-glue-data-catalog-as-your-data-catalog"></a>

Athena uses the AWS Glue Data Catalog by default.

When you use Spark on Amazon EMR or AWS Glue to work with Iceberg, add the following configuration to your Spark session to use the AWS Glue Data Catalog. For more information, see the section [Spark configurations for Iceberg in AWS Glue](iceberg-glue.md) earlier in this guide.

```
"spark.sql.catalog.<your_catalog_name>.type": "glue"
```

For third-party or open-source Iceberg clients (open-source Apache Spark, Trino, Flink, PyIceberg, DuckDB, and so on), use the [AWS Glue Iceberg REST endpoint](https://docs.aws.amazon.com/glue/latest/dg/connect-glu-iceberg-rest.html) at `https://glue.<REGION>.amazonaws.com/iceberg` with SigV4 signing (`rest.signing-name=glue`) — the unified path for every Iceberg table registered in the AWS Glue Data Catalog, both self-managed Iceberg on Amazon S3 and Amazon S3 Tables buckets federated through `s3tablescatalog`. This gives every Iceberg REST-compliant client an IAM-authenticated entry point to the AWS Glue Data Catalog without a service-specific catalog integration, and lets you layer AWS Lake Formation on top for centralized governance (permissions on tables and databases, and column, row, or cell filters where the engine supports Lake Formation enforcement).

## Federate external Iceberg catalogs into the AWS Glue Data Catalog
<a name="federate-external-iceberg-catalogs-into-the-aws-glue-data-catalog"></a>

If parts of your Iceberg estate live in other catalogs — Databricks Unity Catalog, Snowflake Horizon / Apache Polaris, or any Iceberg REST-compatible catalog — register them as [federated catalogs in the AWS Glue Data Catalog](catalog-federation-for-apache-iceberg-tables.md). Federation gives you a consolidated view of every Iceberg table (native \+ federated) through a single metadata plane, centralized governance through AWS Lake Formation, and read access from both AWS analytics services (Amazon Athena, Amazon Redshift, Amazon EMR Spark, AWS Glue Spark) and third-party Iceberg clients (open-source Apache Spark, Trino, Flink, PyIceberg, DuckDB) via the AWS Glue Iceberg REST endpoint — without moving or copying data.

## Prefer the simplest managed option that meets your requirements
<a name="prefer-the-simplest-managed-option-that-meets-your-requirements"></a>

When a managed AWS path can produce the same result as a custom Spark or Flink pipeline, prefer the managed path — you skip a pipeline you'd otherwise have to build, monitor, and maintain. The pointers below are hints, not rules; the underlying principle is to reduce heavy lifting by leaning on managed ingestion, refresh, and maintenance whenever the fit is right.
+ **Streaming into an Iceberg table** — before writing a custom Spark or Flink streaming job, check whether [Amazon Data Firehose](iceberg-firehose.md) or [direct-to-Iceberg streaming tables from Amazon Kinesis Data Streams or Amazon MSK](streaming-directly-to-iceberg-from-kinesis-and-msk.md) already cover the shape of your source and target.
+ **Pre-aggregated or gold-layer tables refreshed on a schedule** — before building a CDC \+ MERGE \+ retry orchestration, check whether an [Iceberg materialized view](apache-iceberg-materialized-views-in-aws-glue-data-catalog.md) with `SCHEDULE REFRESH` covers the refresh cadence you need.
+ **Migrations from a Hive-format source into Amazon S3 Tables** — before spinning up a Spark full-migration job, check whether [managed migration to Amazon S3 Tables](managed-migration-to-amazon-s3-tables.md) covers your source.
+ **Table maintenance** — before scheduling your own compaction, snapshot expiration, and unreferenced-files cleanup, check whether [Amazon S3 Tables built-in maintenance](maintenance-in-amazon-s3-tables.md) or the [AWS Glue Iceberg table optimizer](maintenance-with-the-aws-glue-data-catalog-table-optimizer.md) already provide it for your hosting option.
