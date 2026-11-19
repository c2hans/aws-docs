---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/table-spec-v3.html
---

# Working with Iceberg table format specification version 3

The latest version of the Apache Iceberg table format specification is version 3. This version introduces advanced capabilities for building petabyte-scale data lakes with improved performance and reduced operational overhead. It addresses common performance bottlenecks encountered with version 2, particularly around batch updates and compliance delete operations.

Support for Iceberg version 3 varies by service, so what you can use depends on which engine you run and its version. The Spark-based engines — Amazon EMR and AWS Glue — give you access to the full V3 feature set (deletion vectors, row lineage, nanosecond timestamps, `geometry`/`geography` types, `variant` with and without shredding, and default column values) at recent release levels. Other services support only part of V3 (for example, Amazon Redshift), and some cannot read or write V3 tables at all (Amazon Athena, Trino in Amazon EMR, Amazon Data Firehose, Streaming Tables, and Glue materialized views). The matrix below shows where each service stands. Everything here applies equally to self-managed Iceberg on Amazon S3 and to Amazon S3 Tables.

## Iceberg V3 Compatibility Matrix
<a name="icebreg-v3-compatibility-matrix"></a>

|
|
| **AWS service** | **V3 support** | **Notes** |
| --- |--- |--- |
| [Amazon EMR for Apache Spark](working-with-iceberg-in-amazon-emr-spark.md) | Amazon EMR 7.12\+ | Amazon EMR 8.0\+ for VARIANT.<br />Amazon EMR 8.1\+ for NANOSECOND, GEOMETRY, GEOGRAPHY, VARIANT with shredding and Default column values |
| [AWS Glue for Spark](iceberg-glue.md) | AWS Glue 5.1\+ | AWS Glue 6.0\+ for NANOSECOND, GEOMETRY, GEOGRAPHY, VARIANT with shredding and Default column values |
| AWS Glue: [Iceberg REST API](https://docs.aws.amazon.com/glue/latest/dg/connect-glu-iceberg-rest.html), [Glue Iceberg Optimizer (managed maintenance)](maintenance-with-the-aws-glue-data-catalog-table-optimizer.md) | Yes |  |
| [Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-open-source.html): [Iceberg REST API](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-open-source.html), [managed table maintenance](maintenance-in-amazon-s3-tables.md) | Yes |  |
| [Amazon Redshift](working-with-iceberg-tables-by-using-amazon-redshift.md) | Yes - Patch 204\+ | Supported V3 features are Deletion vectors, row lineage and Default Column values. V3 support available only on Amazon Redshift Serverless (except the 4 RPU workgroup) and on provisioned clusters that use AWS Graviton-based RG instances. |
| [PyIceberg](iceberg-pyiceberg.md) | PyIceberg 0.9\+ | Support added progressively; see PyIceberg release notes |
| [Amazon Athena](working-with-iceberg-tables-by-using-athena-sql-queries.md) (SQL, Trino-based) | No | Cannot read or write V3 tables |
| [Amazon EMR \+ Trino](working-with-iceberg-tables-by-using-trino-amazon-emr.md) | No | Max Trino on Amazon EMR is 479 on emr-7.14.0, below the Trino 483\+ threshold where open-source Trino added experimental V3 support |
| [Amazon Data Firehose](iceberg-firehose.md) | No | Writes to V2 tables only |
| [Streaming tables (Amazon Kinesis Data Streams, Amazon MSK - to Iceberg)](streaming-directly-to-iceberg-from-kinesis-and-msk.md) | No | Generate V2 tables and can write to V2 only |
| [AWS Glue Iceberg materialized views](apache-iceberg-materialized-views-in-aws-glue-data-catalog.md) | No | Materialized views are always created as V2 |

**New tables default to V2** across all V3-capable services in the table above (Amazon EMR for Spark, AWS Glue for Spark, AWS Glue Data Catalog REST, Amazon Redshift, Amazon S3 Tables REST). To opt into V3 (for example with Spark), set `format-version=3` at create time (`TBLPROPERTIES ('format-version'='3')`) or run `ALTER TABLE ... SET TBLPROPERTIES ('format-version'='3')` on an existing V2 table.

Each service-specific section in this guide includes an ***Iceberg format version support* **subsection with the full V2 / V3 matrix, per-feature notes, and the exact minimum release for V3 features (where applicable) — follow the link in the leftmost column above.

## Verifying downstream engine V3 support
<a name="verifying-downstream-engine-v3-support"></a>

Before you create a V3 Iceberg table with Spark — or upgrade an existing V2 table to V3 — verify that every downstream engine that reads or writes the table also supports V3, and specifically supports the V3 features you plan to use. Notable current gaps:
+ [Amazon Athena](working-with-iceberg-tables-by-using-athena-sql-queries.md) does **not** support V3.
+ [Amazon Redshift](working-with-iceberg-tables-by-using-amazon-redshift.md) supports V3, but only for **deletion vectors, row lineage, and default column values**. Redshift does not yet support `variant`, `geometry`/`geography`, or `nanosecond` timestamps.

See the [V3 support table](#icebreg-v3-compatibility-matrix)** **at the top of this page for the full service-by-service matrix.

## Key features in version 3
<a name="key-features-in-version-3"></a>

**Deletion vectors** replace the positional delete files that were used in version 2 with an efficient binary format stored as Puffin files. This eliminates write amplification from random batch updates and General Data Protection Regulation (GDPR) compliance deletes, and significantly reduces the overhead of maintaining fresh data. Organizations that process high-frequency updates will see immediate improvements in write performance and reduced storage costs from fewer small files.

**Row lineage** enables precise change tracking at the row level through two hidden metadata columns: `_row_id` (a stable identifier for each row) and `_last_updated_sequence_number` (the sequence number at which the row was last modified). Your downstream systems can process changes incrementally, speeding up data pipelines and reducing compute costs for change data capture (CDC) workflows. This built-in capability eliminates the need for custom change tracking implementations.

Row lineage lets you detect inserts and updates cost-effectively. Every Iceberg snapshot gets a monotonically increasing sequence number, and Iceberg propagates it to each row through the `_last_updated_sequence_number` metadata column — the value equals the sequence number of the snapshot that last inserted or updated that row, and it's the key you filter on for incremental reads. The read works from a watermark: first capture the table's current snapshot sequence number as an upper bound (for example,`SELECT MAX(sequence_number) FROM db.table.entries`), then pull only the rows whose last-updated sequence falls in the half-open range above your previously processed watermark and at or below that upper bound:

```
SELECT *
FROM db.table
WHERE _last_updated_sequence_number >  :last_processed_sequence
  AND _last_updated_sequence_number <= :current_sequence
```

Because Iceberg tracks the sequence at **data-file granularity**, the engine first skips entire data files whose data sequence number falls outside that range, then filters the surviving rows by their `_last_updated_sequence_number`. Scan cost stays proportional to new or changed data rather than full table size. After a successful read, advance your watermark to `:current_sequence` for the next cycle.

Row lineage tracks **inserts and updates, not deletes.** A deleted row is removed from the table, so it no longer carries the `_last_updated_sequence_number` metadata a query reads — there's simply no surviving row to return. If you need to detect deletes for a full change-data-capture feed, don't rely on row lineage alone — use Iceberg's `create_changelog_view`[ procedure](https://iceberg.apache.org/docs/latest/spark-procedures/#create_changelog_view), which materializes a view of the changes between two snapshots with a `_change_type` column that explicitly flags each row as `INSERT`, `DELETE`, `UPDATE_BEFORE`, or `UPDATE_AFTER`.

One caveat: updates applied via **equality deletes** aren't tracked as updates — the engine can't carry the original `_row_id` forward, so the change surfaces as a removed row plus a brand-new row with a new `_row_id`.

**Nanosecond timestamps** add two new types — `timestamp_ns` (nanosecond precision without time zone) and `timestamptz_ns` (nanosecond precision with UTC time zone) — for workloads that need finer-than-microsecond time resolution and depend on ordering of events at nanosecond granularity, such as high-frequency trading, telemetry from industrial sensors, or scientific instruments.

**Geometry and geography types** add native support for two-dimensional spatial data. `geometry` uses planar (Cartesian) coordinates and is appropriate for engineering and CAD-style data. `geography` uses geodetic (spherical) coordinates on a specified reference ellipsoid and is appropriate for real-world locations on Earth. Both types unlock GIS-style queries without external add-ons — for example, geofence detection with `ST_Intersects(point_geog, fence_geog)` to find every event that fell inside a defined zone.

**Variant type** (`variant`) stores schemaless or semi-structured data (typically JSON) as a self-describing binary format alongside the row's other columns. Compared to storing raw JSON strings, `variant` gives you faster query performance, statistics that partition pruning and predicate pushdown can use, and no need to pre-define a rigid schema. V3 defines two representations:
+ *Variant without shredding* stores each value as a single binary blob per row. Writing Variant without shredding is available on Amazon EMR 8.0\+ and AWS Glue 6.0\+.
+ *Variant with shredding* projects known sub-fields out of the JSON payload into columnar storage (while still keeping the full document available), which lets query engines skip decoding the whole document when a query only needs a few sub-fields. Because the projected sub-fields live in dedicated Parquet columns, Parquet also collects per-file min/max and null-count statistics for them — enabling **file-level skipping** at scan time on predicates that target those sub-fields. Writing Variant with shredding is available on Amazon EMR 8.1\+ and AWS Glue 6.0\+.

**Default column values** let you attach a `DEFAULT` to a column at two points in its lifecycle. At table creation time (`CREATE TABLE ... col type DEFAULT <value>`), the default is applied automatically to any subsequent write that omits the column. On `ALTER TABLE ... ADD COLUMN ... DEFAULT <value>`, the default is applied at read time to existing rows in files that don't contain the column — no data rewrite is needed. This is particularly useful for backfilling metadata columns and for schema evolution scenarios that previously required a full table rewrite.

## Version compatibility
<a name="version-compatibility"></a>

Version 3 is a backward-compatible upgrade from version 2. Engines that support V3 read and write both formats, so you can:
+ Run queries across both version 2 and version 3 tables.
+ Upgrade existing version 2 tables to version 3 without data rewrites.
+ Run time travel queries that span version 2 and version 3 snapshots.
+ Use schema evolution and hidden partitioning across table versions.

## Getting started with version 3
<a name="getting-started-with-version-3"></a>

### Prerequisites
<a name="prerequisites"></a>

Before working with version 3 tables, make sure that you have:
+ An AWS account with appropriate AWS Identity and Access Management (IAM) permissions.
+ Access to one or more V3-capable AWS analytics services (Amazon EMR 8.1\+ for Spark, AWS Glue 6.0\+, for full V3 capabilities).
+ A table bucket to get started with Amazon S3 Tables or a general-purpose S3 bucket if you are building your own Iceberg infrastructure.
+ A configured AWS Glue catalog.

### Creating version 3 tables
<a name="creating-version-3-tables"></a>

#### Creating new tables
<a name="creating-new-tables"></a>

To create a new Iceberg version 3 table, set the `format-version` table property to 3. Using Spark SQL:

```
CREATE TABLE IF NOT EXISTS myns.orders_v3 (
    order_id bigint,
    customer_id string,
    order_date date,
    total_amount decimal(10,2),
    status string,
    created_at timestamp
)
USING iceberg
TBLPROPERTIES (
    'format-version' = '3'
)
```

#### Upgrading version 2 tables to version 3
<a name="upgrading-version-2-tables-to-version-3"></a>

You can upgrade existing version 2 tables to version 3 atomically without rewriting data. Using Spark SQL:

```
ALTER TABLE myns.existing_table
SET TBLPROPERTIES ('format-version' = '3')
```

**Important**
 Version 3 is a one-way upgrade. After you upgrade a table from version 2 to version 3, you cannot downgrade it back to version 2 through standard operations. What happens during upgrade:
+ A new metadata snapshot is created atomically.
+ Existing Parquet data files are reused.
+ Row lineage fields are added to the table metadata.

After the upgrade:
+ The next compaction will remove old version 2 delete files.
+ New modifications will use the version 3 deletion vector files.

The upgrade does not perform a historical backfill of row lineage change tracking records.

### Enabling deletion vectors
<a name="enabling-deletion-vectors"></a>

To take advantage of deletion vectors for updates, deletes, and merges, configure your write mode. Using Spark SQL:

```
ALTER TABLE myns.orders_v3
SET TBLPROPERTIES ('format-version' = '3',
                   'write.delete.mode' = 'merge-on-read',
                   'write.update.mode' = 'merge-on-read',
                   'write.merge.mode' = 'merge-on-read'
                  )
```

These settings ensure that update, delete, and merge operations create deletion vector files instead of rewriting entire data files.

### Using row lineage for change tracking
<a name="using-row-lineage-for-change-tracking"></a>

Version 3 automatically adds row lineage metadata fields to track changes.

Using Spark SQL:

```
# Query with parameter value provided
last_processed_sequence = 47

SELECT
    id,
    data,
    _row_id,
    _last_updated_sequence_number
FROM myns.orders_v3
WHERE _last_updated_sequence_number > :last_processed_sequence
```

The `_row_id` field uniquely identifies each row, and  `_last_updated_sequence_number` tracks when the row was last modified. Use these fields to:
+ Identify changed rows for incremental processing.
+ Track data lineage for compliance.
+ Optimize CDC pipelines.
+ Reduce compute costs by processing only changes.

## Best practices for version 3
<a name="best-practices-for-version-3"></a>

### When to use version 3
<a name="when-to-use-version-3"></a>

Consider upgrading to, or starting with, version 3 when:
+ You perform frequent batch updates or deletes.
+ Your workloads involve high-frequency upserts.
+ You require efficient CDC workflows.
+ You need better change tracking capabilities.
+ You intend to use the new data types and features such as Variants, Geospatial types, Nanosecond timestamps.

### Optimizing write performance
<a name="optimizing-write-performance"></a>
+ Enable deletion vectors for update-heavy workloads:

  ```
  ALTER TABLE mydb.mytable
  SET TBLPROPERTIES (
  'write.delete.mode' = 'merge-on-read',
  'write.update.mode' = 'merge-on-read',
  'write.merge.mode' = 'merge-on-read'
  )
  ```
+ Configure appropriate file sizes:

  ```
  ALTER TABLE mydb.mytable
  SET TBLPROPERTIES (
  'write.target-file-size-bytes' = '536870912'  -- 512 MB
  )
  ```

### Optimizing read performance
<a name="optimizing-read-performance"></a>
+ Use row lineage for incremental processing.

## Migration strategy
<a name="migration-strategy"></a>

When you migrate from version 2 to version 3, follow these best practices:
+ Test in a non-production environment first to validate the upgrade process and performance.
+ Upgrade during low-activity periods to minimize impact on concurrent operations.
+ Monitor initial performance, and track metrics after the upgrade.
+ Run compaction to consolidate delete files after the upgrade.
+ Update your team documentation to reflect version 3 features.

## Compatibility considerations
<a name="compatibility-considerations"></a>
+ Engine versions – Make sure that all engines accessing the table support version 3.
+ Third-party tools – Verify your tool's version 3 compatibility before you upgrade.
+ Monitoring – Update monitoring dashboards for version 3-specific metrics.

## Troubleshooting
<a name="troubleshooting"></a>

### Common issues
<a name="common-issues"></a>

**Error: "format-version 3 is not supported"**
+ Verify that your engine version supports version 3.  For specifics, see the table at the beginning of this section.
+ Check catalog compatibility.
+ Make sure that you're using the latest versions of AWS services.

**Performance degradation after upgrade**
+ Verify that there are no compaction failures. For more information, see [Logging and monitoring for S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-monitoring-overview.html) in the Amazon S3 documentation.
+ Confirm that deletion vectors are enabled. The following properties should be set:

  ```
  ALTER TABLE myns.orders_v3
  SET TBLPROPERTIES (
  'write.delete.mode' = 'merge-on-read',
  'write.update.mode' = 'merge-on-read',
  'write.merge.mode' = 'merge-on-read'
  )
  ```

  You can verify table properties with the following code:

  ```
  DESCRIBE FORMATTED myns.orders_v3
  ```

**Incompatibility with third-party tools**
+ Verify that the tool supports the version 3 specification.
+ Consider maintaining version 2 tables for unsupported tools.
+ Contact the tool vendor for their version 3 support timeline.

## Additional resources
<a name="additional-resources"></a>
+ [Blog: Accelerate data lake operations with Apache Iceberg V3 deletion vectors and row lineage](https://aws.amazon.com/blogs/big-data/accelerate-data-lake-operations-with-apache-iceberg-v3-deletion-vectors-and-row-lineage/)
+ [Blog: Beyond JSON blobs: Implementing the VARIANT data type in Apache Iceberg V3](https://aws.amazon.com/blogs/big-data/beyond-json-blobs-implementing-the-variant-data-type-in-apache-iceberg-v3/)
+ [Blog: Build with geospatial and variant types in Iceberg v3 on AWS Glue 6.0](https://aws.amazon.com/blogs/big-data/build-with-geospatial-and-variant-types-in-iceberg-v3-on-aws-glue-6-0/)
