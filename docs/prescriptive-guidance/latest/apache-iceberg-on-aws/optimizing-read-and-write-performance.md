---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/optimizing-read-and-write-performance.html
---

# Optimizing read and write performance

This section covers best practices for tuning read and write performance on Iceberg tables on AWS. The subsections that follow are grouped by whether they benefit both reads and writes, only reads, or only writes; each shared-topic subsection carries a **Reader benefit / Writer benefit** table so the split is visible at a glance.

## Best practices that benefit both reads and writes
<a name="best-practices-that-benefit-both-reads-and-writes"></a>

The following topics improve both read and write performance, usually through different mechanisms. Each subsection carries a per-topic **Reader benefit / Writer benefit** table so you can see the split at a glance.

### Maintain tables regularly
<a name="maintain-tables-regularly"></a>

Table maintenance — **compaction**, **snapshot expiration**, and **unreferenced-files cleanup** — is what keeps Iceberg tables fast for both reads and writes. Depending on how the table is hosted:
+ **Self-managed Iceberg on Amazon S3** — either run maintenance yourself with the [Iceberg Spark procedures](self-managed-maintenance.md), or delegate it to the [AWS Glue Iceberg table optimizer](maintenance-with-the-aws-glue-data-catalog-table-optimizer.md), which schedules compaction, snapshot expiration, and unreferenced-files cleanup on your behalf.
+ **Amazon S3 Tables** — Amazon S3 [runs compaction, snapshot expiration, and unreferenced-file removal automatically](maintenance-in-amazon-s3-tables.md); no external scheduler is needed.

For the full patterns behind each approach, see [Maintaining Iceberg tables](maintaining-iceberg-tables.md).

|
|
| **Operation** | **Reader benefit** | **Writer benefit** |
| --- |--- |--- |
| **Compaction** | Consolidates small files into larger ones. Fewer Amazon S3 `GET` requests at scan time (fewer files to open) and smaller Iceberg metadata (fewer entries per manifest, fewer manifests overall) → faster query planning and scan. Compaction also merges base data files with any pending delete files (positional deletes, equality deletes, or V3 deletion vectors), materializing the latest row state into the rewritten data files, so readers scan those files directly instead of resolving deletes at read time. See [Compaction — ](self-managed-maintenance.md)`rewrite_data_files` for the detailed tuning knobs. | Every `UPDATE`, `DELETE`, or `MERGE INTO` first has to read the current table to identify which data files are impacted before it writes new files (or deletion vectors, in merge-on-read mode). In that read step the writer is a reader, so all the reader-side benefits apply here too — fewer Amazon S3 `GET` requests, smaller manifests, faster planning. Merging delete files also shrinks the working set the next writer has to reason about. |
| **Snapshot expiration** | Trimming old snapshots keeps the table's `metadata.json` small, so the engine's metadata load at the start of every query stays fast. | Every writer emits a new `metadata.json` at commit time by extending the current one; a smaller starting `metadata.json` means fewer bytes to serialize and write on every commit. |

If you're **self-managing** maintenance (not relying on the built-in S3 Tables or Glue-optimizer paths), you can approach maintenance from a preventive angle by scheduling actions off the metadata-table metrics (see [Monitoring Iceberg workloads](monitoring.md)). For example:
+ Use bin-packing compaction to group small files when a table reaches N small files.
+ Use bin-packing compaction to merge delete files when a table reaches N delete files in a given partition.
+ Remove small files that were already compacted by expiring snapshots when total storage is X times higher than active storage.

### Control file size at write time
<a name="control-file-size-at-write-time"></a>

The [Maintain tables regularly](#maintain-tables-regularly) section above showed how compaction consolidates small files into bigger ones **after** they've been committed. It's better to write properly-sized files from the start, so readers benefit immediately from the first commit and the writer doesn't spend later cycles rewriting the same data. This section covers the table properties and write-side settings that influence file size at write time.

For good performance, we generally recommend keeping Parquet and ORC files larger than 100 MB. A high file count still means more Amazon S3 `GET` requests at scan time (at least one per data file, on top of the manifest and manifest-list reads), which increases both request cost and per-scan latency — even before the engine touches the actual data.

|
|
| **Reader benefit** | **Writer benefit** |
| --- |--- |
| Fewer, larger files → fewer Amazon S3 `GET` requests at scan time (one per data file, on top of the manifest and manifest-list reads) and smaller Iceberg metadata (fewer entries per manifest, fewer manifests overall) → faster query planning and scan. Larger metadata files also make query planning slower, so keeping individual data files large matters more as the table grows. | Fewer, larger data files reduce the work of the impacted-file detection step of every UPDATE, DELETE, or MERGE INTO — the writer has to open fewer files to figure out which need to be rewritten (or need a deletion vector added). |

Several table properties control the target file size. These properties are hints — the writer applies them where it can, and regular compaction reconciles the result.

|
|
| **Property** | **Default** | **Description** |
| --- |--- |--- |
| `write.target-file-size-bytes` | 512 MB | Maximum file size that Iceberg will create. Files may still be written smaller when the input batches are small. |
| `write.parquet.row-group-size-bytes` | 128 MB | Parquet row group size; controls the granularity at which readers can skip data within a file. |
| `write.orc.stripe-size-bytes` | 64 MB | ORC stripe size; same purpose as Parquet row group size. |
| `write.distribution-mode` | `none` for unpartitioned tables `hash` for partitioned tables `range` for tables with a global sort order (for example, when `ALTER TABLE ... WRITE ORDERED BY column_name` has been applied) | Iceberg-native property; honored by the Spark and Flink Iceberg writers only (Apache Spark supports all three modes; Apache Flink supports `none` and `hash`, `range` is experimental). Iceberg asks the writer to sort or shuffle data between its tasks before writing to storage. |

By table size:
+ **Small tables** (up to a few gigabytes) — reduce the target file size to 128 MB. Also reduce the row group or stripe size (for example, to 8 or 16 MB).
+ **Medium to large tables** (a few gigabytes to hundreds of gigabytes) — the defaults are a good starting point. If your queries are very selective, adjust the row group or stripe size (for example, to 16 MB).
+ **Very large tables** (hundreds of gigabytes or terabytes) — increase the target file size to 1024 MB or more, and consider increasing the row group or stripe size if your queries pull large sets of data. On Amazon S3 Tables, managed compaction targets at most 512 MB (`targetFileSizeMB`); a larger write-time target still applies to the writer, but compacted output stays at or below 512 MB

These are general guidelines. Run tests to identify the most suitable values for your specific tables and workloads, and check that the writer engines you plan to use (Apache Spark, Apache Flink, PyIceberg, Amazon Data Firehose, streaming tables, and so on) actually honor each property — not every writer supports every Iceberg table property (`write.distribution-mode` above is one example).

The properties above set a maximum file size — they don't guarantee files reach it. Regular compaction is what keeps files at the right size; see [Maintain tables regularly](#maintain-tables-regularly) above.

**Note on Amazon S3 Tables compaction**: the automatic compaction that Amazon S3 Tables runs on your behalf uses the **Parquet default row-group size of 128 MB** and does not honor a table-level override of `write.parquet.row-group-size-bytes`. If you need a different row-group size on an S3 Tables target, be aware that S3 Tables' managed compaction will normalize it back to 128 MB on subsequent rewrites.

### Hidden partitioning
<a name="hidden-partitioning"></a>

Iceberg's [hidden partitioning](https://iceberg.apache.org/docs/latest/partitioning/#icebergs-hidden-partitioning) lets you declare a partition specification that is derived from a source column (for example, `PARTITIONED BY (days(event_timestamp))`) instead of a materialized partition column. The partition value is computed by Iceberg from the source column at write time and stored in the manifest.

|
|
| **Reader benefit** | **Writer benefit** |
| --- |--- |
| Filters on the source column (`WHERE event_timestamp BETWEEN ...`) get partition pruning automatically. Readers don't need to know about the partition transform, and there's no risk of the query missing the pruning because the filter didn't reference the "correct" derived column. | Writers don't need to derive or maintain a separate partition column in the source data — no `INSERT ... SELECT event_id, ..., DATE_TRUNC('day', event_timestamp) AS day FROM ...` boilerplate and no risk of drift between the source column and the derived one. Iceberg computes the partition value on the fly during the write. |

Hidden partitioning is set at table creation or via `ALTER TABLE ... ADD PARTITION FIELD`.

### Column statistics
<a name="column-statistics"></a>

Iceberg collects column statistics (min, max, null count, and so on) at write time and stores them in the manifest files. The reader consults those statistics during scan planning to prune files that can't contain the filter value.

**Default behavior**: Iceberg collects statistics only for the [first 100 fields, counting nested fields; in each table](https://github.com/apache/iceberg/blob/ae15c7e36973501b40443e75816d3eac39eddc90/core/src/main/java/org/apache/iceberg/TableProperties.java#L276), as controlled by `write.metadata.metrics.max-inferred-column-defaults`. Two levers to tune this:
+ **Reorder columns** so that the ones you filter on fall within the first 100 (or lower the default to 20 and put them in the first 20).
+ **Explicitly configure per-column stats** if you filter on only a few columns:

  ```
  ALTER TABLE mydb.mytable SET TBLPROPERTIES (
      'write.metadata.metrics.default'         = 'none',
      'write.metadata.metrics.column.my_col_a' = 'full',
      'write.metadata.metrics.column.my_col_b' = 'full'
  );
  ```

The general recommendation is to collect statistics only for the columns you actually filter on — that's the point where both the reader and writer benefits below start to apply.

|
|
| **Reader benefit** | **Writer benefit** |
| --- |--- |
| File-level pruning through the manifests. Statistics work in two complementary patterns: **outlier or rare-value filters** (even without sorting — `temperature > 200` on data where most rows sit below 200 lets the engine skip files whose max temperature is under 200), and **range or point queries on sorted columns** (`WHERE order_id BETWEEN X AND Y` or `WHERE order_id = XXX` — sorting tightens min/max ranges across files so many more files are pruned). | Iceberg only computes statistics for the columns configured by `write.metadata.metrics.default` and the per-column overrides. Collecting statistics for fewer columns means less work at write time and smaller manifest files. |

### Choose the right update strategy (copy-on-write vs merge-on-read)
<a name="choose-the-right-update-strategy-copy-on-write-vs-merge-on-read"></a>

Iceberg supports two write modes for updates and deletes: **copy-on-write** (CoW, the default) and **merge-on-read** (MoR). They present the classic read vs write latency trade-off.

|
|
| **Mode** | **Behavior** | **Ideal use case** |
| --- |--- |--- |
| **Copy-on-write** (default) — **best for reader performance** | Updates and deletes rewrite the affected data files, so a reader scans clean files with the latest row state and does no delete resolution at scan time. | Most updates are collocated in the same table partitions (for example, daily batch loads), or each update touches only a small portion of the table (for example, less than 10-20% of the rows). |
| **Merge-on-read** — **best for writer performance** | Updates and deletes are written as separate small files (positional or equality delete files in V2, or deletion vectors in V3) instead of rewriting the base data files. This makes writes much faster, at the cost of the reader having to merge changes with the base files at scan time. | Streaming workloads with updates where speed matters, or jobs with few updates spread across many files. |

Set the mode via `write.update.mode`, `write.delete.mode`, and `write.merge.mode` — either at the table level or independently on the application side. Merge-on-read requires running regular compaction to prevent read performance from degrading over time (see [Maintain tables regularly](#maintain-tables-regularly) above).

Engines differ: Spark on Amazon EMR and AWS Glue honor these properties; Athena always writes merge-on-read; PyIceberg always writes copy-on-write.

**Note on merge-on-read and writer-as-reader.** Every `UPDATE`, `DELETE`, and `MERGE INTO` has to first identify which data files are impacted by the change — so the writer is a reader in that step, and it must compute the latest row state by merging base data files with any related delete files (positional deletes, equality deletes, or V3 deletion vectors). Merge-on-read speeds up the write phase (no base-file rewrites), but the writer-side read phase gets progressively more expensive as delete files accumulate. Without scheduled maintenance — compaction that materializes deletes back into the base files — merge-on-read eventually becomes a bottleneck for the writer itself, not just for readers.

### Prevent hot partitioning (HTTP 503 errors)
<a name="prevent-hot-partitioning-http-503-errors"></a>

Iceberg tables that handle billions of objects or process petabytes of data can produce Amazon S3 prefixes that receive a very high volume of traffic. Those hot prefixes typically surface as HTTP 503 (service unavailable) errors, which affect both readers (retries and latency spikes on high-fanout scans) and writers (commit retries and slower ingestion).

|
|
| **Reader benefit** | **Writer benefit** |
| --- |--- |
| Fewer 503s at scan time means fewer per-file retries and steadier scan wall-clock, especially for high-fanout queries that open many files in parallel. | Fewer 503s at commit time means fewer failed writes to retry and steadier throughput for high-volume ingestion. |

Iceberg-level levers help avoid hot prefixes:
+ Set `write.distribution-mode` to `hash` or `range` so that each writer task produces fewer, larger files per partition. (see [Control file size at write time](#control-file-size-at-write-time) above). Fewer files means fewer Amazon S3 requests per scan or commit, which reduces prefix pressure. This applies to both **Amazon S3 Tables** and **self-managed Iceberg** and addresses most cases.
+ For **self-managed Iceberg**, if you continue to experience 503 errors due to an immense volume of data in your workloads, set `write.object-storage.enabled` to `true`. This instructs Iceberg to hash object names and distribute the load across multiple, randomized Amazon S3 prefixes.

Beyond these levers, **Amazon S3 Tables** are less prone to 503s in the first place: table buckets deliver **up to 10× the transactions per second (TPS)** of a general Amazon S3 bucket for the same table access patterns, so the underlying prefix-scaling headroom is substantially higher — no `write.object-storage.enabled` equivalent is needed.

For more information on the Iceberg properties above, see [Write properties](https://iceberg.apache.org/docs/latest/configuration/#write-properties) in the Iceberg documentation.

### Use ZSTD compression
<a name="use-zstd-compression"></a>

ZSTD has been the **default Parquet compression codec for new Iceberg tables** since [Iceberg 1.4.0](https://iceberg.apache.org/releases/#140-release). Because Iceberg writes Parquet by default, this covers most tables. If your runtime is on an older Iceberg version, or you want to opt into ZSTD for the Avro or ORC file formats, set the table property `write.<file_type>.compression-codec` explicitly (for example, `write.parquet.compression-codec = 'zstd'`).

|
|
| **Reader benefit** | **Writer benefit** |
| --- |--- |
| ZSTD's decompression is fast (close to Snappy) while its compression ratio is significantly better than Snappy's and close to GZIP's. Smaller files mean less data to fetch from Amazon S3 for the same query — lower request cost and shorter scan wall-clock, even before the engine touches the rows. | ZSTD's compression throughput is significantly higher than GZIP's while producing files close to GZIP's size, so writes get much smaller output without paying a large CPU cost. Smaller output means fewer bytes uploaded to Amazon S3 per commit and lower steady-state storage. |

Snappy might give slightly faster decompression per byte or the best raw write throughput, but has a lower compression ratio than ZSTD, so both readers and writers move more bytes through Amazon S3. In most workloads the ratio wins; keep the ZSTD default unless a benchmark for your workload shows Snappy is faster end-to-end. Compression levels can be adjusted to suit your needs; see [ZSTD compression levels in Athena](https://docs.aws.amazon.com/athena/latest/ug/compression-support-zstd-levels.html) for a concrete example.

## Best practices for reads only
<a name="best-practices-for-reads-only"></a>

### Set the sort order
<a name="set-the-sort-order"></a>

To improve read performance on Iceberg tables, sort your table on one or more columns that are frequently used in query filters. Sorting, combined with Iceberg's column statistics, makes file pruning significantly more efficient — see the sorted-columns bullet in [Column statistics](#column-statistics) for the mechanism. Sorting also reduces the number of Amazon S3 requests for queries that use the sort columns.

You can set a hierarchical sort order at the table level by running a DDL statement with Spark. After you set the sort order, writers **that support it** apply this sorting to subsequent data write operations — not every writer honors Iceberg's table-level sort order. Each service chapter in this guide includes an *Iceberg feature support* table that indicates whether write-side sort order is honored, so consult the chapter for each engine you plan to write from (see, for example, [Amazon EMR Spark](working-with-iceberg-in-amazon-emr-spark.md), [AWS Glue](iceberg-glue.md), [Amazon Athena](working-with-iceberg-tables-by-using-athena-sql-queries.md), [Amazon Redshift](working-with-iceberg-tables-by-using-amazon-redshift.md), [Amazon Data Firehose](iceberg-firehose.md), or [PyIceberg](iceberg-pyiceberg.md)).

Two Spark DDL variants are commonly used, and they differ in how they distribute data across writer tasks:
+ `ALTER TABLE <table> WRITE DISTRIBUTED BY PARTITION LOCALLY ORDERED BY column_name` — sets `write.distribution-mode` to `hash` and applies a **local** sort order per task. Data is hash-shuffled by partition, and each writer task sorts its own portion locally before writing. For a big ingestion this produces multiple files per partition, each locally sorted internally; files within the same partition can still have overlapping `[min, max]` ranges for the sort column.
+ `ALTER TABLE <table> WRITE ORDERED BY column_name` — sets `write.distribution-mode` to `range` and applies a **global** sort order. Data is range-partitioned across writer tasks based on both the partition column and the sort column, so files within the same partition end up with **non-overlapping** `[min, max]` ranges for the sort column within a single ingestion job.

Choosing between them:
+ `LOCALLY ORDERED BY` is cheaper at write time — hash shuffle plus a per-task sort, no global sampling — and is a good fit for streaming or incremental writes.
+ `WRITE ORDERED BY` (range distribution) is more expensive: it needs a global sampling pass before writing so Spark can compute range boundaries. It's worth the extra cost when a single ingestion job produces many files inside the same partition, because those files come out with disjoint sort-column ranges and readers can prune aggressively. Note that non-overlap is guaranteed **within** an ingestion job, not **across** jobs — different jobs writing to the same partition can still produce overlapping ranges, which is why running regular compaction (with the sort order applied) matters.

For example, in tables that are partitioned by date (`yyyy-mm-dd`) where most queries filter by `uuid`, use `WRITE DISTRIBUTED BY PARTITION LOCALLY ORDERED BY uuid` for lightweight ingestion writes, or `WRITE ORDERED BY uuid` when a batch ingestion is large enough to justify the global sort. For the full list of available DDL options, see the [Iceberg documentation](https://iceberg.apache.org/docs/latest/spark-ddl/#alter-table--write-ordered-by).

Changing the sort order doesn't affect existing data files. You can use Iceberg compaction to apply the sort order on those.

## Best practices for writes only
<a name="best-practices-for-writes-only"></a>

### Set the table distribution mode
<a name="set-the-table-distribution-mode"></a>

Iceberg offers multiple write distribution modes that define how write data is distributed across Spark tasks. For an overview of the available modes, see [Writing Distribution Modes](https://iceberg.apache.org/docs/latest/spark-writes/#writing-distribution-modes) in the Iceberg documentation.

For use cases that prioritize write speed, especially in streaming workloads, set `write.distribution-mode` to `none`. This ensures that Iceberg doesn't request additional Spark shuffling and that data is written as it becomes available in Spark tasks. This mode is particularly suitable for Spark Structured Streaming applications.

**Note**
setting the write distribution mode to `none` tends to produce numerous small files, which degrades read performance. Combine `none` with regular compaction to consolidate small files into properly sized ones — see [Maintain tables regularly](#maintain-tables-regularly).

### Choose the right file format
<a name="choose-the-right-file-format"></a>

Iceberg supports writing data in Parquet, ORC, and Avro formats. Parquet is the default format. Parquet and ORC are columnar formats that offer superior read performance but are generally slower to write. This is the typical trade-off between read and write performance.

If write speed is important for your use case, such as in streaming workloads, consider writing in Avro format by setting `write-format` to `Avro` in the writer's options. Because Avro is a row-based format, it provides faster write times at the cost of slower read performance.

To improve read performance, run regular compaction to merge and transform small Avro files into larger Parquet files. The outcome of the compaction process is governed by the `write.format.default` table setting. The default format for Iceberg is Parquet, so if you write in Avro and then run compaction, Iceberg transforms the Avro files into Parquet files.

The following Spark example creates an Iceberg table with `write.format.default = parquet` (so compaction produces Parquet files), and streams into it using the per-write `write-format = avro` option for faster writes:

```
spark.sql(f"""
    CREATE TABLE IF NOT EXISTS {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME} (
        col_1 float,
        <other columns>,
        ts timestamp)
    USING iceberg
    PARTITIONED BY (days(ts))
    OPTIONS (
      'format-version'='2',
      'write.format.default'='parquet')
""")

query = df \
    .writeStream \
    .format("iceberg") \
    .option("write-format", "avro") \
    .outputMode("append") \
    .trigger(processingTime='60 seconds') \
    .option("path", f"{CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}") \
    .option("checkpointLocation", f"s3://{BUCKET_NAME}/checkpoints/iceberg/") \
    .start()
```

### Improve MERGE performance
<a name="improve-merge-performance"></a>

Every `UPDATE`, `DELETE`, and `MERGE INTO` — whether the table uses copy-on-write, merge-on-read with positional deletes (V2), or merge-on-read with deletion vectors (V3) — starts by identifying which data files in the target table are impacted by the change. On Spark, that detection step follows a fixed pattern:

1. **Read the current Iceberg table** applying the filters present in the `ON` clause (call it `T1`).

1. **Read the source DataFrame** being merged in (call it `T2`).

1. **Join **`T1`** and **`T2` on the `ON` clause equality predicates, using a **left semi join** — the result is the rows in the Iceberg table that match rows in the source DataFrame.

1. **Extract the file names** from those matching rows via Iceberg's `_file` hidden column, which every row carries and which points to the data file the row belongs to.

1. **Select the distinct file names** — that's the list of files the MERGE has to rewrite (copy-on-write) or produce delete-file entries for (merge-on-read).

The performance issue: **Spark doesn't dynamically infer partition filters during MERGE**. If your Iceberg table is partitioned by day and the batch you're merging in is confined to a single day, the `ON` clause typically references only join keys — not partition columns. Without an explicit partition predicate in the `ON` clause, Iceberg has to inspect **every partition's files** to build `T1`, even though only one partition will ever match. On large tables this can dominate the MERGE cost.

To fix this, add a filter on the Iceberg table's partition values as part of the `ON` clause. You can compute the filter bounds dynamically from the source DataFrame so the extra predicate is always tight and doesn't need to be hard-coded per batch. This changes the semantics of the MERGE: a target row that matches the join keys but falls outside the partition predicate is treated as not matched, and the source row is inserted as a new row. Use this technique only when the partition column value of a given key never changes (for example, an immutable event time). If it can change, keep the ON clause on the keys alone and accept the wider scan.

Example — a sales table `sales_db.web_sales` partitioned by day, and a MERGE from a batch that covers only a single day. First, compute the partition-value range from the source DataFrame:

```
bounds = spark.sql("""
      SELECT count(*) AS row_count,
             count(ws_sales_time) AS timestamp_count,
             min(ws_sales_time) AS min_ts,
             max(ws_sales_time) AS max_ts
      FROM upsert_day_1
""").first()

if bounds.row_count == 0:
    return

if bounds.timestamp_count != bounds.row_count:
    raise ValueError("NULL partition values require explicit handling")
```

Then include those bounds as an extra predicate in the `ON` clause, alongside the join keys:

```
spark.sql("""
  MERGE INTO sales_db.web_sales t
  USING upsert_day_1 s
     ON t.ws_order_number = s.ws_order_number
    AND t.ws_item_sk = s.ws_item_sk
    AND t.ws_sales_time BETWEEN :min_ts AND :max_ts
  WHEN MATCHED THEN UPDATE SET *
  WHEN NOT MATCHED THEN INSERT *
""", args={"min_ts": bounds.min_ts, "max_ts": bounds.max_ts})
```

The extra `BETWEEN` predicate on `ws_sales_time` (a partition column) lets Iceberg prune the target down to just the partitions the source batch actually covers — typically one or two days — before the semi-join in step 3 runs. On a table with hundreds of partitions, this can cut the file listing and read work in the detection step by orders of magnitude.

When the source batch covers **specific, non-contiguous partition values** rather than a contiguous range, use an `IN` filter instead of `BETWEEN`. Compute the distinct partition-transform values from the source DataFrame, format them into a comma-separated list, and inject that list into the `ON` clause. For example, on a table partitioned by `hours(ws_sales_time)`:

```
distinct_hours = spark.sql("""
    SELECT DISTINCT hours(ws_sales_time)
    FROM upsert_day_1
""").collect()

hours_list = ",".join(f"'{row[0]}'" for row in distinct_hours)

spark.sql(f"""
    MERGE INTO sales_db.web_sales t
    USING upsert_day_1 s
       ON t.ws_order_number = s.ws_order_number
      AND t.ws_item_sk      = s.ws_item_sk
      AND hours(t.ws_sales_time) IN ({hours_list})
    WHEN MATCHED     THEN UPDATE SET *
    WHEN NOT MATCHED THEN INSERT *
""")
```

Rule of thumb: use `BETWEEN` when the source is a **contiguous range** on a partition column (typical for hourly or daily batch loads), and `IN` when the source is a **sparse set of specific partition values** (typical for CDC upserts or backfills that touch arbitrary historical partitions).

The partition predicate has a second benefit. Iceberg uses the predicates pushed down from the `ON` clause as the conflict detection filter when it validates the commit, so under the default `serializable` isolation a concurrent append is a conflict only if it lands inside the predicate's partitions. Without the predicate, any concurrent append anywhere in the table can fail the `MERGE` with `ValidationException`. See [Handling write concurrency](handling-write-concurrency.md).
