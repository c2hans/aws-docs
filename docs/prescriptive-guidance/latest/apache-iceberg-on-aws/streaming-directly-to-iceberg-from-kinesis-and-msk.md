---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/streaming-directly-to-iceberg-from-kinesis-and-msk.html
---

# Streaming directly to Iceberg from Kinesis and MSK

Both Amazon Kinesis Data Streams and Amazon MSK can deliver records directly into Apache Iceberg tables hosted in an Amazon S3 table bucket, without a Firehose stream or a custom consumer in the middle. AWS refers to this destination as a **streaming table** — an Iceberg table that the source service creates and continuously writes to on your behalf, with automatic Parquet conversion and inline compaction. In both services the resource you create is called a **channel**. This section covers the common shape of both integrations and the key limits to design around.

**Applies only to Amazon S3 Tables**. Streaming tables do not support self-managed Iceberg tables on general-purpose Amazon S3 buckets as a destination. For streaming into self-managed Iceberg, use [Amazon Data Firehose](iceberg-firehose.md) or write a custom consumer. Both services can also deliver to general-purpose S3 buckets through the same channel API, but that path writes records in their original source format with no Iceberg table, no Parquet conversion, and no schema registry.

## Prerequisites and hard limits
<a name="prerequisites-and-hard-limits"></a>

Check these before designing around streaming tables. Several are not adjustable.
+ **Amazon Kinesis Data Streams: the source stream must use on-demand capacity mode. The service rejects provisioned streams at channel creation with **`Stream <name> ... is in Provisioned mode. Please enable On-demand mode to use this feature.` The Kinesis console lists only on-demand streams when you create a delivery.
+ **Amazon MSK: the cluster must be MSK Provisioned with Express brokers.** Standard brokers and MSK Serverless are not supported.
+ **AWS Glue Schema Registry is required**, and so is a **dead-letter queue**. Neither is optional.
+ **Same account and same Region throughout.** The source stream or cluster, the destination S3 table bucket, the AWS Glue Schema Registry, and the DLQ bucket must all be in one account and one Region. Cross-account and cross-Region delivery are both unsupported.
+ **No backfill.** A channel delivers only records produced after it becomes active. Existing data on the stream or topic is not replayed into the table.
+ **Encryption constraints.** Delivered data is encrypted with Amazon S3 managed keys (SSE-S3) by default. To use SSE-KMS you must supply a **customer managed** key — an AWS managed key (the `aws/kinesis` alias) is rejected. Additionally, if your source Kinesis data stream is itself encrypted with an AWS managed key, you cannot create a delivery at all.

## Iceberg format version support
<a name="iceberg-format-version-support"></a>

The source service (Kinesis Data Streams or Amazon MSK) creates and manages streaming tables inside your S3 table bucket. The service pins the format version; you do not choose it.

|
|
| **Iceberg feature** | **Amazon S3 Tables (streaming table)** |
| --- |--- |
| Format version 2 (V2) | Yes — data files in Apache Parquet |
| Format version 3 (V3) | Not applicable — streaming tables are created using Iceberg V2 |

## How streaming tables work
<a name="how-streaming-tables-work"></a>

The source service owns the writes. You describe **where** to deliver records (which table bucket and which channel configuration) and the source service takes care of table creation, schema application, Parquet encoding, file sizing, and per-snapshot commits. The delivery pipeline is: read from all partitions of an MSK topic or from all shards of a Kinesis stream → buffer until the data-freshness interval → validate against the registry schema and convert to the Iceberg schema → convert to Parquet → commit the new files as a snapshot.

This design has a few important details:
+ **Records are JSON only.** Both integrations accept only JSON records, and every record must validate against a schema you register in the **AWS Glue Schema Registry**. The service reports records that fail validation to a **dead-letter queue** (DLQ) that you configure on the channel — they do not reach the streaming table. Note that the DLQ receives **record identifiers and error context, not full record payloads**, so it is a diagnostic channel rather than a replay source.
+ **Schema handling is strict and one-directional.** The registry schema validates and shapes records; it does **not** evolve the table. Fields present in a record but absent from the schema are **silently dropped**. Optional fields missing from a record are written as `null`. A record missing a **required** field — including the partition column — goes to the DLQ in its entirety. Maximum nesting depth for structs, maps, and lists is **16 levels**; deeper schemas are rejected when you create the channel.
+ **Partitioning is hourly on a single timestamp column, and that is the only option.** The partition transform enum contains exactly one value, `TIME_HOUR`. The source column must be a `timestamptz` — in the registry schema, a `string` field with `format: date-time`. There is no `identity`, `bucket`, `truncate`, `year`, `month`, or `day` transform, and you cannot supply more than one partition column. The partition source column is automatically marked required regardless of the schema's `required` array. If hourly partitioning on one timestamp does not suit your query patterns, streaming tables are the wrong tool.
+ **The target Iceberg table is auto-created on first delivery.** You do not call `CreateTable` yourself, and you cannot point a channel at an existing table. The table does not appear when the channel reaches `ACTIVE` — it is created when the first batch is actually delivered, so expect the namespace and table to be absent until records flow. Allow for the first data-freshness interval plus table-creation time before the table is queryable.
+ **Streaming tables are read-only from your side.** You cannot `INSERT`, `UPDATE`, `MERGE`, `DELETE`, `COPY INTO`, or write from your own engines, and you cannot change the schema, partition spec, or sort order. Enforcement is service-level: the table is marked `managedByService`, and mutating calls such as `RenameTable` and `UpdateTableMetadataLocation` fail with an explicit deny even for an account administrator. Replacing the table's own resource policy does not lift the deny. To remove older data, enable **record expiration**, which deletes records older than a retention window you set, based on the table's `timestamptz` partition column.
+ **Table maintenance remains yours to tune.** Automatic maintenance in S3 Tables — compaction, snapshot expiration, unreferenced-file removal — applies to streaming tables as to any other S3 Tables table, and the maintenance configuration is customer-writable: you can change compaction target file size, or disable compaction outright, on a streaming table. Observed defaults are snapshot management enabled with `minSnapshotsToKeep=1` and `maxSnapshotAgeHours=120`. Compaction of streaming-table files is performed by S3 Tables background maintenance on its normal schedule, not at write time — so partition granularity and delivery volume still determine whether files reach a useful size. See [Maintenance in Amazon S3 Tables](maintenance-in-amazon-s3-tables.md).
+ **Reads are unrestricted.** Any Iceberg-compatible engine — Amazon Athena, Amazon Redshift, Amazon EMR, Apache Spark, Apache Flink, Trino, PyIceberg, DuckDB, and so on — can query a streaming table exactly like any other S3 Tables table. Access control uses IAM, table bucket policies, and AWS Lake Formation the same way as for regular S3 Tables (see [Governance and access control](governance.md)).
+ **After creation, only data freshness is editable.** `UpdateChannel` accepts a data-freshness change and nothing else. To change the partition spec, table name, namespace, schema, or compression you must delete the channel and its table and create both again.

## Data freshness and batching
<a name="data-freshness-and-batching"></a>

Data freshness is the maximum buffering time before a batch is committed, and it is the only latency control you have. **The valid range is 300–900 seconds (5–15 minutes) in both services; **the service rejects values outside this range with** **`DataFreshnessInSeconds must be between 300 and 900.` There is no sub-5-minute option.

|
|
|  | **Amazon Kinesis Data Streams** | **Amazon MSK** |
| --- |--- |--- |
| Range | 300–900 seconds | 300–900 seconds |
| Default | 300 seconds | 600 seconds |

Lower values deliver sooner; higher values produce fewer, larger Parquet files and lower downstream query cost. For Amazon MSK, AWS recommends the 5-minute minimum only when the topic produces at least **2.4 MBps** of uncompressed data — below that, use a higher value so batches are worth committing.

Compression for Iceberg data files is configurable and defaults to **ZSTD**. Kinesis Data Streams accepts `ZSTD`, `SNAPPY`, or `NONE`; Amazon MSK accepts `ZSTD` or `SNAPPY` only.

### Partition granularity and file size
<a name="partition-granularity-and-file-size"></a>

Because the partition spec is fixed at hourly and the only other knob is data freshness, the file-size profile of a streaming table follows directly from delivery volume. Hourly partitioning is coarse by design, and it works well when each hour accumulates enough data per freshness interval to produce reasonably sized Parquet files. A low-volume topic or stream running at the 5-minute minimum produces up to twelve small commits per hour into a single partition, and S3 Tables background compaction consolidates those files only when it next runs. If your volume is modest, prefer a higher data-freshness value so that each commit is worth making.

## Amazon Kinesis Data Streams → streaming table
<a name="amazon-kinesis-data-streams-streaming-table"></a>

You create a **channel** on an on-demand Kinesis data stream. Kinesis reads records from all shards, validates them against the Glue Schema Registry schema, and delivers valid records to the target Iceberg table in your table bucket. Failed records are reported to the DLQ.

Configuration inputs:
+ Source Kinesis data stream — **on-demand capacity mode only**. One stream per channel.
+ Target S3 table bucket ARN \+ namespace \+ table name. Exactly **one table configuration per channel; **the service rejects supplying more with** **`S3TablesConfigurationList should contain exactly 1 table configuration.`
+ Target table **partition spec** — one `PartitionField` whose `Transform` is `TIME_HOUR` and whose `SourceName` is a `date-time` column.
+ **Data freshness** — 300–900 seconds, default 300.
+ **Compression type** — `ZSTD` (default), `SNAPPY`, or `NONE`.
+ AWS Glue Schema Registry schema ARN, with a record format of either:
  + `JSON` — plain JSON objects, with the schema supplied out-of-band by the ARN, or
  + `GSR_JSON` — Glue Schema Registry-serialized JSON where the schema identifier is embedded in each record. (The console labels this "Glue Schema registry JSON"; `GSR_JSON` is the API value.)
+ **DLQ** — an **Amazon S3 bucket** (bucket ARN, expected bucket owner, optional error output prefix). Amazon SQS is not a valid DLQ target; the bucket ARN must match `arn:aws:s3:::<bucket-name>`.
+ Optional CloudWatch Logs delivery for diagnostics, and optional SSE-KMS with a customer managed key.

References:
+ [Streaming tables (Amazon Kinesis Data Streams)](https://docs.aws.amazon.com/streams/latest/dev/data-delivery-st.html)
+ [Create a streaming table delivery](https://docs.aws.amazon.com/streams/latest/dev/data-delivery-st-create.html)
+ AWS blog: [Deliver real-time data to streaming tables for Apache Iceberg with Amazon Kinesis Data Streams](https://aws.amazon.com/blogs/big-data/deliver-real-time-data-to-streaming-tables-for-apache-iceberg-with-amazon-kinesis-data-streams/)

## Amazon MSK (Express brokers) → streaming table
<a name="amazon-msk-express-brokers-streaming-table"></a>

You create a **channel** on an Amazon MSK Provisioned cluster that uses **Express brokers**. MSK reads records from a Kafka topic, validates them against the Glue Schema Registry schema, and delivers valid records to the target Iceberg table. The service reports failed records to the DLQ. A single streaming table is documented to scale to **10 GBps** of delivery throughput without manual sizing.

Note that Amazon MSK addresses the destination **through the AWS Glue Data Catalog**, not by table bucket ARN directly. This means the S3 Tables integration with the Glue Data Catalog is a prerequisite on the MSK path, and the service execution role needs Glue Data Catalog permissions in addition to S3 Tables and DLQ permissions.

Configuration inputs:
+ Source Amazon MSK cluster (**Express brokers only**) and Kafka topic, via `topicConfigurationList`.
+ **Catalog** — `catalogArn`, the federated Glue Data Catalog that projects the S3 Tables bucket, plus `warehouseLocation`, the ARN of the S3 Tables bucket backing the warehouse. If `catalogArn` is omitted, MSK derives it from `warehouseLocation`.
+ **Destination table** — `destinationDatabaseName` (the namespace) and `destinationTableName`. Exactly **one table per channel **(the service caps** **`destinationTableList` at 1).
+ Target table **partition spec** — `partitionStrategy` must be `TIME_HOUR`, with `sourceList` containing exactly one timestamp column.
+ **Data freshness** — 300–900 seconds, default 600.
+ **Compression type** — `ZSTD` (default) or `SNAPPY`.
+ **Record converter** — `valueConverter` of either `JSON` (plain JSON, with a GSR schema ARN in `recordSchema.gsrArn`) or `JSON_SCHEMA_GSR` (GSR-serialized JSON with an embedded schema ID).
+ `appendOnly` — required, and must be `true`. Updates and deletes are not supported.
+ `schemaEvolution.enableSchemaEvolution` — required, and **must be **`false`** in the current release**.
+ `tableCreation.enableTableCreation` — required, and **must be **`true`** in the current release**, which is why you cannot target an existing table.
+ **DLQ** — a required Amazon S3 bucket.

Channel lifecycle states are `CREATING`, `ACTIVE`, `UPDATING`, `DELETING`, `FAILED`, `SUSPENDING`, and `SUSPENDED`; `FAILED` channels carry a `stateInfo` code and message.

References:
+ [Streaming tables with Amazon MSK](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-streaming-msk.html)
+ [Amazon MSK data delivery — supported input formats](https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-iceberg-supported-configs.html)
+ AWS blog: [Deliver Apache Kafka data to streaming tables for Apache Iceberg with Amazon MSK Express brokers](https://aws.amazon.com/blogs/big-data/deliver-apache-kafka-data-to-streaming-tables-for-apache-iceberg-with-amazon-msk-express-brokers/)

## Schema type mapping
<a name="schema-type-mapping"></a>

Streaming tables map Glue Schema Registry JSON Schema types to Iceberg types as follows.

|
|
| **JSON Schema type** | **Iceberg type** |
| --- |--- |
| `string` (plain) | `string` |
| `string` with format `date-time` | `timestamptz` (the only valid partition column type) |
| `string` with format `date` | `date` |
| `string` with format `time` | `time` |
| `string` with format `uuid` | `uuid` |
| `string` with encoding `byte` or `base64` | `binary` |
| `integer`, 32-bit or less | `int` |
| `integer`, greater than 32-bit | `long` |
| `number` with `multipleOf` | `decimal` (precision derived from `multipleOf`) |
| `number` (plain) | `double` |
| `boolean` | `boolean` |
| `object` with named properties | `struct` |
| `object` with `additionalProperties` | `map` (string keys) |
| `array` | `list` |
| `enum` | `string` |

The service maps fields in the schema's `required` array as non-nullable Iceberg columns.

## When to choose streaming tables vs. Amazon Data Firehose
<a name="when-to-choose-streaming-tables-vs-amazon-data-firehose"></a>

Both routes deliver to Iceberg tables and both are managed, so the decision usually comes down to source, record shape, partitioning needs, and DML semantics.

|
|
| **Aspect** | **Streaming tables (Kinesis / MSK direct)** | **Amazon Data Firehose to Iceberg** |
| --- |--- |--- |
| Source | A single on-demand Kinesis data stream, or a single Amazon MSK Express-brokers topic | 20\+ sources, including Kinesis Data Streams, MSK, and custom producers via Direct PUT |
| Destination hosting | Amazon S3 Tables only | Both self-managed Iceberg on Amazon S3 and Amazon S3 Tables |
| Record format | JSON only, validated against a Glue Schema Registry schema | Flexible — no built-in schema registry requirement |
| Record transformation | Not supported — records land in the table as-is after schema validation | Optional AWS Lambda transform can reshape, enrich, or filter records before delivery |
| Partitioning | **Hourly on one **`timestamptz`** column only** (`TIME_HOUR`) | Your choice, because you define the table |
| Operations | Append only (`appendOnly` must be `true`); record expiration on the `timestamptz` partition column is the only way to remove rows | `insert`, `update`, `delete` per record, in merge-on-read mode — `update` and `delete` are implemented as Iceberg **equality deletes**, so readers must support them |
| Table creation | Auto-created on first delivery; cannot target an existing table | You create the table yourself. Firehose does not auto-create tables — every database and table referenced by a routed record must already exist in the target catalog before the stream starts |
| Schema evolution | **Not supported.** The registry validates records; it does not alter the table | **Not supported.** The target Iceberg table schema must be updated manually (for example, `ALTER TABLE ADD COLUMN ...`) before Firehose can deliver records that carry the new column |
| Multi-table routing | One channel = one table, enforced by the API | JSONQuery or Lambda routing to many tables per stream |
| Latency floor | 5 minutes (300s minimum data freshness) | Seconds — buffering hints go well below a minute |
| Account / Region scope | Same account **and** same Region for stream, table bucket, registry, and DLQ | Cross-account and cross-Region Glue Data Catalog supported |
| Iceberg format | V2 | V2 only  |
| Best for | High-throughput append-only streams, already JSON with a registered schema, where hourly time partitioning fits | CDC-style workloads, mixed insert/update/delete records, sub-minute latency, custom partitioning, or delivery into self-managed Iceberg |

For the Firehose-based path, see [Working with Iceberg tables by using Amazon Data Firehose](iceberg-firehose.md).
