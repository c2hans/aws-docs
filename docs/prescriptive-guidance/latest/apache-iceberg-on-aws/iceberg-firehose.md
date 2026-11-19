---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-firehose.html
---

# Working with Iceberg tables by using Amazon Data Firehose

[Amazon Data Firehose](https://aws.amazon.com/firehose/) is a serverless, no-code service for delivering data streams from over 20 sources such as AWS WAF logs, Amazon CloudWatch Logs, AWS IoT, Amazon Kinesis Data Streams, and Amazon Managed Streaming for Apache Kafka (Amazon MSK) into destinations such as Amazon S3, Amazon Redshift, Snowflake, and Splunk.

**Amazon Data Firehose can deliver streaming data to Apache Iceberg tables that are either self-managed** on Amazon S3 or **hosted in Amazon S3 Tables**.

Firehose can route records from a single stream into different Iceberg tables and automatically apply insert, update, and delete operations to records in the tables.

## Iceberg format version support in Firehose
<a name="iceberg-format-version-support-in-firehose"></a>

Amazon Data Firehose supports Iceberg format version 2 tables only. Delivery to a V3 target is rejected at runtime.

|
|
| **Iceberg feature** | **Self-managed Iceberg on S3** | **Amazon S3 Tables** |
| --- |--- |--- |
| Format version 2 (V2) | Yes | Yes |
| Format version 3 (V3) | Not supported — Firehose rejects delivery to V3 tables with `errorCode: Iceberg.InvalidIcebergVersion` ("Iceberg V3 Table format is not supported") | Not supported - same as self-managed |

## Choosing the destination
<a name="choosing-the-destination"></a>

*Both destinations use the same Amazon Data Firehose delivery stream type — Apache Iceberg Tables* — and share prerequisites such as an IAM role with permissions to write to the target tables. The following table summarizes the main configuration differences.

|
|
| **Aspect** | **Self-managed Iceberg on S3** | **Amazon S3 Tables** |
| --- |--- |--- |
| Target catalog in Firehose | AWS Glue Data Catalog (`AwsDataCatalog`) | The S3 Tables federated catalog `s3tablescatalog/<table-bucket-name> that you register in the AWS Glue Data Catalog (through the S3 Tables + AWS analytics services integration).` In the CLI/API, set `CatalogConfiguration.CatalogARN` to `arn:aws:glue:<region>:<account-id>:catalog/s3tablescatalog/<table-bucket-name>` |
| Permissions the Firehose role needs | Read and update on the target Glue database and table, plus Amazon S3 read/write on the table location. Add `lakeformation:GetDataAccess` and Lake Formation grants on the target tables if the data is registered with Lake Formation. | **IAM access control**: read and update on the Glue federated catalog entries, plus the `s3tables:` read and write actions on the target table bucket. **Lake Formation access control**: the same Glue actions plus `lakeformation:GetDataAccess` and Lake Formation grants on the target tables — no `s3tables: actions, `because Lake Formation vends the credentials. |

For the exact action lists, see [Controlling access with Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html). Scope the Glue and `s3tables:` actions to the databases and tables you actually target rather than granting them on `*`. In every combination the role also needs Amazon S3 write access to the backup bucket, plus `kinesis:` read actions if the source is Kinesis Data Streams, `lambda:InvokeFunction` and `lambda:GetFunctionConfiguration` if a Lambda transform is attached, and `logs:PutLogEvents` if error logging is enabled.

The Glue Data Catalog can be in the same account as the Firehose stream, in another account in the same Region (the default cross-account shape), or in another Region.

## How it works
<a name="how-it-works"></a>

Creating an Amazon Data Firehose stream that lands in Apache Iceberg tables requires eight decisions in the Amazon Data Firehose console (or the equivalent `CreateDeliveryStream` API parameters):

1. **Source** — Direct PUT, [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/), or [Amazon MSK](https://aws.amazon.com/msk/) with provisioned brokers. Amazon MSK Serverless is not supported as a source for the Apache Iceberg Tables destination.

1. **Destination** — select **Apache Iceberg Tables**.

1. **Data transformation with AWS Lambda (optional) — attach a Lambda function to reshape or enrich each record before Amazon Data Firehose delivers it.** Also required when the routing information for the record has to be computed rather than read directly from the payload (see [AWS Lambda transform](#aws-lambda-transform) below).

1. **Destination catalog** — **AWS Glue Data Catalog** for self-managed Iceberg on Amazon S3, or **Amazon S3 Tables catalog** for tables hosted in an S3 table bucket. See [Choosing the destination](#choosing-the-destination) above.

1. **Routing configuration** — how Firehose picks the target database, target table, and operation for each record. Configure a `MetadataExtraction` processor with a JQ query for dynamic routing, and/or add entries to `DestinationTableConfigurationList` to declare per-table record keys (`UniqueKeys`). See [Routing records to Iceberg tables](#routing-records-to-iceberg-tables) below.

1. **Buffer hints** — how much data Firehose accumulates before writing a batch: **buffer size** (1–128 MiB, default 5 MiB) and **buffer interval** (0–900 seconds, default 300 seconds). Firehose flushes when either threshold is crossed. Higher values mean fewer, larger data files — less compaction work and faster queries downstream — at the cost of delivery latency.

1. **Retry duration** — how long Firehose keeps retrying when it hits errors opening a channel to or writing to the target tables. 0–7200 seconds, default 300 seconds. Only after the retry duration expires does Firehose treat the records as failed and hand them to the S3 backup bucket.

1. **S3 backup bucket** — an S3 location where Firehose lands records it could not deliver to Iceberg (unroutable records, records referencing a non-existent database or table, records that fail schema validation, and records still undelivered after the retry duration expires). Firehose writes these under the `S3ErrorOutputPrefix` you configure, along with per-record error metadata.

**Note**
Firehose does **not** auto-create Iceberg tables. Every database and table referenced by a routed record must already exist in the target catalog before you start the stream. Pre-create the target tables with proper partitioning (and any [record keys / identifier columns](#per-record-operation-and-record-key)) with an engine such as [Amazon Athena](working-with-iceberg-tables-by-using-athena-sql-queries.md), [Amazon EMR](working-with-iceberg-in-amazon-emr-spark.md), [AWS Glue](iceberg-glue.md), or [Amazon Redshift](working-with-iceberg-tables-by-using-amazon-redshift.md).

Two constraints on how you create them:
+ **Create through Iceberg's **`GlueCatalog`** API. Amazon Data Firehose delivers only to databases and tables created through Iceberg's **`GlueCatalog` API — which is what the engines above use. Databases and tables created directly through the AWS Glue SDK are not supported as Firehose targets.
+ **No hyphens in database or table names. Amazon Data Firehose validates **`DestinationDatabaseName` and `DestinationTableName` against the pattern `[a-zA-Z0-9\.\_]+`, so only alphanumerics, dots, and underscores are accepted. `CreateDeliveryStream` fails with a `ValidationException` if either name contains a hyphen — note that engines such as Athena will happily *create* a hyphenated Iceberg database or table, so you can end up with a table you cannot target. Use underscores.

For the full step-by-step setup (console screens, CLI, and API), see [Set up the Firehose stream](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-stream.html) in the Firehose documentation.

## Per-record operation and record key
<a name="per-record-operation-and-record-key"></a>

Firehose determines two things per record: which Iceberg table it belongs to and what **operation** to apply (`insert`, `update`, or `delete`). How much of that information each record has to carry depends on the stream shape:
+ **Single-table, insert-only** — no per-record routing information is required. Amazon Data Firehose reads the target from `DestinationTableConfigurationList` and applies `insert` by default. See [Example 1](#example-1-single-table-insert-only).
+ **Single-table with updates/deletes** — records need to carry the **operation**. Firehose extracts it either with a `MetadataExtraction` JQ query (see [Example 2](#example-2-single-table-with-updatesdeletes-table-has-no-identifier-fields) and [Example 3](#example-3-single-table-with-updatesdeletes-table-has-identifier-fields)) or with an [AWS Lambda transform](#aws-lambda-transform) when routing has to be computed or the record body has to be reshaped — for instance, when the source stream carries CDC events (see the [CDC example](#example-cdc-records)).
+ **Multi-table (any operations)** — records need to carry (or the routing processor needs to compute) the **destination database**, **destination table**, and — if the stream includes updates or deletes — the **operation**. Firehose extracts these either with a `MetadataExtraction` JQ query (see [Examples 4 through 7](#example-4-multiple-tables-any-ops-all-tables-have-identifier-fields-database-in-the-record)) or with an [AWS Lambda transform](#aws-lambda-transform) when the routing keys aren't directly present on the record, or the record body has to be reshaped before delivery (see the [CDC example](#example-cdc-records) for a Debezium-style envelope that a Lambda flattens and routes).

For `update` and `delete` records, the target table must have a **record key** (also called an *identifier column set* in Iceberg) declared on it. The record key is the set of columns Firehose uses to locate the row to update or delete. You can declare it in one of two places:
+ **On the Amazon Data Firehose stream** — list the record-key columns per table in the Destination configuration JSON blob using the `UniqueKeys` field. Only tables that receive `update` or `delete` records need an entry; tables that only receive `insert` records don't need one. You can have at most one entry per table.

  **Record keys must have a name that is unique across the whole schema.** Firehose matches a unique key by column name, not by path. A key such as `UniqueKeys: ["_id"]` works whether `_id` is a top-level column or sits inside a struct, as long as no other field in the schema is called `_id`. Firehose rejects fully qualified names such as `UniqueKeys: ["top._id"]`, and it rejects a name that appears in more than one place (for example, `_id` at the top level and inside a struct). To key on a nested value whose name isn't unique, rename the field or promote it to a top-level column with an [AWS Lambda transform](#aws-lambda-transform) before delivery.

  `UniqueKeys`** is not validated when you create the stream.** `CreateDeliveryStream` accepts `UniqueKeys` entries naming columns that do not exist in the target table; the failure surfaces only at delivery time, as `Iceberg.InvalidUniqueKeys` with the message *"The configured unique keys for the table do not match with the fields present in the schema."* Records are retried for the retry duration and then land in the S3 backup bucket. Check a new stream's first delivery rather than trusting a successful `CreateDeliveryStream` call.
+ **On the Iceberg table itself** — set `identifier-field-ids` on the schema (via `WITH (identifier_columns = ARRAY['col1', 'col2'])` at create time in engines that support it, or with an `ALTER TABLE` on an existing table) so any downstream engine, not just Firehose, sees the same record key.

Either option works; declaring `identifier-field-ids` on the table makes the record key visible to every engine that reads it, not just Firehose. Concrete configurations for both options are shown in [Example 2](#example-2-single-table-with-updatesdeletes-table-has-no-identifier-fields) / [Example 3](#example-3-single-table-with-updatesdeletes-table-has-identifier-fields) (single table) and [Example 6](#example-6-multiple-tables-any-ops-some-tables-lack-identifier-fields-database-in-the-record) / [Example 7](#example-7-multiple-tables-any-ops-some-tables-lack-identifier-fields-static-database) (multi-table) below, and the Lambda-based [CDC example](#example-cdc-records) shows the same pattern applied to a Debezium envelope.

### How Firehose applies updates and deletes
<a name="how-firehose-applies-updates-and-deletes"></a>

`Amazon Data Firehose implements update` and `delete` on Iceberg tables using **equality deletes**. Each `update` or `delete` record in a batch produces an equality-delete **entry** — a row that names the record-key values Iceberg should treat as removed — and, for `update` records, a new-data-file entry that carries the replacement row. Firehose packs all the equality-delete entries produced in one batch into one or more Iceberg equality-delete files (typically one per partition of the target table that received deletes), and commits them together with the batch's new-data files in a single snapshot. The base data files are never rewritten by Firehose.

Two consequences for readers and writers:
+ **Readers must support equality deletes**. At query time, the engine merges every data file with any equality delete file that has a **higher sequence number** than the data file, filtering out rows whose record key appears in a delete file. Amazon Athena, Amazon EMR / AWS Glue Spark, Amazon Redshift (V2), Trino, and other modern Iceberg readers do this transparently. Engines that don't support equality deletes cannot correctly read the table.
+ **Compaction eventually consolidates the delete files into the base**. Running Iceberg compaction (with `delete-file-threshold` set) merges equality delete files into rewritten data files, producing an optimized read layout. For self-managed Iceberg on S3, schedule this via Spark procedures or the AWS Glue Data Catalog table optimizer; for Amazon S3 Tables, the built-in compaction handles it automatically. See [Maintaining Iceberg tables](maintaining-iceberg-tables.md).

**Upsert pattern**: Iceberg-native upserts are not a first-class Firehose primitive. To get upsert behavior, mark **every** incoming record as an `update` — Firehose treats an `update` on a key that doesn't yet exist as an insert, and on an existing key as an update. **Trade-off**: because every record is delivered as an `update`, Firehose emits an equality-delete entry for every row it writes, including brand-new rows that would otherwise not need one. Downstream readers must merge those delete entries with the base data at every scan, and compaction has more delete-file work to reconcile, so this pattern is materially more expensive at read time than a straight append. Each delete file also costs an Amazon S3 PUT. Prefer carrying the true operation (`insert`/`update`/`delete`) on each record when the source stream can distinguish them.

**Note: Amazon Data Firehose does not preserve record order on delivery to Iceberg tables.** Do not rely on two records for the same key arriving in the order they were produced — if last-write-wins ordering matters, carry a sequence or timestamp column and resolve it at read time.

## Routing records to Iceberg tables
<a name="routing-records-to-iceberg-tables"></a>

Firehose reads routing metadata (destination database, destination table, and operation) from a `MetadataExtraction` processor attached to the stream's `ProcessingConfiguration`, and reads record-key information (`UniqueKeys`) from `DestinationTableConfigurationList`. The two together determine where each record lands and how Firehose applies it. The examples below cover the common cases; each shows the target table DDL, the routing-related portion of the Iceberg destination configuration, sample input records grouped into batches, and the resulting table state after each batch.

**Reminder**: `MetadataExtraction extracts routing metadata but does not modify the record body — so any field you use purely for routing (like op`, `db`, or `table` in the examples below) also becomes a column in the target Iceberg table. The `CREATE TABLE` statements reflect that. Use an AWS Lambda transform (see [AWS Lambda transform](#aws-lambda-transform)) if you need those fields stripped from the delivered record.

### Example 1: Single table, insert-only
<a name="example-1-single-table-insert-only"></a>

Every record goes to a single table and the stream is insert-only. You do not need a processor — Amazon Data Firehose applies `insert` by default and reads the target from the single `DestinationTableConfigurationList` entry.

Target table (illustrative Apache Spark SQL):

```
CREATE TABLE mydb.events (
    id       BIGINT,
    username STRING,
    action   STRING
) USING iceberg;
```

Stream configuration (routing portion):

```
{
  "ProcessingConfiguration": {
    "Enabled": false
  },
  "DestinationTableConfigurationList": [
    {
      "DestinationDatabaseName": "mydb",
      "DestinationTableName":    "events"
    }
  ]
}
```

Sample input records (batch 1):

```
{"id": 1, "username": "alice", "action": "click"}
{"id": 2, "username": "bob",   "action": "view"}
```

State of `mydb.events` after batch 1:

|
|
| **id** | **username** | **action** |
| --- |--- |--- |
| 1 | alice | click |
| 2 | bob | view |

### Example 2: Single table with updates/deletes, table has no identifier fields
<a name="example-2-single-table-with-updatesdeletes-table-has-no-identifier-fields"></a>

Records carry a mix of `insert`, `update`, and `delete`, and the target Iceberg table does **not** have `identifier-field-ids` declared on its schema. Firehose needs both the operation (extracted from each record via a `MetadataExtraction` processor with a JQ query) and the record-key columns (declared in `UniqueKeys` on the table's `DestinationTableConfigurationList` entry).

Target table (no identifier fields, illustrative Apache Spark SQL):

```
CREATE TABLE mydb.events (
    id       BIGINT,
    op       STRING,
    username STRING
) USING iceberg;
```

Stream configuration:

```
{
  "ProcessingConfiguration": {
    "Enabled": true,
    "Processors": [
      {
        "Type": "MetadataExtraction",
        "Parameters": [
          { "ParameterName": "JsonParsingEngine",       "ParameterValue": "JQ-1.6" },
          { "ParameterName": "MetadataExtractionQuery", "ParameterValue": "{operation: .op}" }
        ]
      }
    ]
  },
  "DestinationTableConfigurationList": [
    {
      "DestinationDatabaseName": "mydb",
      "DestinationTableName":    "events",
      "UniqueKeys":              ["id"]
    }
  ]
}
```

Sample input records (batch 1 — both inserts):

```
{"id": 1, "op": "insert", "username": "alice"}
{"id": 2, "op": "insert", "username": "bob"}
```

State of `mydb.events` after batch 1:

|
|
| **id** | **op** | **username** |
| --- |--- |--- |
| 1 | insert | alice |
| 2 | insert | bob |

Sample input records (batch 2 — update \+ delete):

```
{"id": 1, "op": "update", "username": "alice_updated"}
{"id": 2, "op": "delete", "username": "bob"}
```

State of `mydb.events` after batch 2 (row `id = 2` removed by the delete):

|
|
| **id** | **op** | **username** |
| --- |--- |--- |
| 1 | update | alice\_updated |

### Example 3: Single table with updates/deletes, table has identifier fields
<a name="example-3-single-table-with-updatesdeletes-table-has-identifier-fields"></a>

Same shape as Example 2, but the target Iceberg table already has `identifier-field-ids` declared on its schema (see [Per-record operation and record key](#per-record-operation-and-record-key)). Firehose reads the record key from the table itself, so `UniqueKeys` is omitted from the `DestinationTableConfigurationList` entry — the entry is only there to name the target.

Target table (identifier field on `id`, illustrative Apache Spark SQL):

```
CREATE TABLE mydb.events (
    id       BIGINT,
    op       STRING,
    username STRING
) USING iceberg;

ALTER TABLE mydb.events SET IDENTIFIER FIELDS id;
```

Stream configuration:

```
{
  "ProcessingConfiguration": {
    "Enabled": true,
    "Processors": [
      {
        "Type": "MetadataExtraction",
        "Parameters": [
          { "ParameterName": "JsonParsingEngine",       "ParameterValue": "JQ-1.6" },
          { "ParameterName": "MetadataExtractionQuery", "ParameterValue": "{operation: .op}" }
        ]
      }
    ]
  },
  "DestinationTableConfigurationList": [
    {
      "DestinationDatabaseName": "mydb",
      "DestinationTableName":    "events"
    }
  ]
}
```

Sample records and end-of-batch states are identical to [Example 2](#example-2-single-table-with-updatesdeletes-table-has-no-identifier-fields) — this example differs only in where the record key is declared.

### Example 4: Multiple tables (any ops), all tables have identifier fields, database in the record
<a name="example-4-multiple-tables-any-ops-all-tables-have-identifier-fields-database-in-the-record"></a>

The stream fans out into several Iceberg tables and **every** target table has `identifier-field-ids` declared on its schema. The processor extracts destination database, destination table, and operation from each record. You can omit `DestinationTableConfigurationList` entirely — no per-table `UniqueKeys` are needed at the stream level.

Target tables (identifier fields declared on each, illustrative Apache Spark SQL):

```
CREATE TABLE mydb.users (
    db      STRING,
    `table` STRING,
    op      STRING,
    user_id BIGINT,
    name    STRING
) USING iceberg;
ALTER TABLE mydb.users SET IDENTIFIER FIELDS user_id;

CREATE TABLE mydb2.orders (
    db       STRING,
    `table`  STRING,
    op       STRING,
    order_id BIGINT,
    total    DOUBLE
) USING iceberg;
ALTER TABLE mydb2.orders SET IDENTIFIER FIELDS order_id;
```

Stream configuration:

```
{
  "ProcessingConfiguration": {
    "Enabled": true,
    "Processors": [
      {
        "Type": "MetadataExtraction",
        "Parameters": [
          { "ParameterName": "JsonParsingEngine",       "ParameterValue": "JQ-1.6" },
          { "ParameterName": "MetadataExtractionQuery", "ParameterValue": "{destinationDatabaseName: .db, destinationTableName: .table, operation: .op}" }
        ]
      }
    ]
  }
}
```

Sample input records (batch 1 — both inserts):

```
{"db": "mydb",  "table": "users",  "op": "insert", "user_id": 1,  "name":  "alice"}
{"db": "mydb2", "table": "orders", "op": "insert", "order_id": 42, "total": 99.99}
```

State after batch 1:

`mydb.users`:

|
|
| **db** | **table** | **op** | **user\_id** | **name** |
| --- |--- |--- |--- |--- |
| mydb | users | insert | 1 | alice |

`mydb2.orders`:

|
|
| **db** | **table** | **op** | **order\_id** | **total** |
| --- |--- |--- |--- |--- |
| mydb2 | orders | insert | 42 | 99.99 |

Sample input records (batch 2 — update \+ delete):

```
{"db": "mydb",  "table": "users",  "op": "update", "user_id": 1,  "name":  "alice_updated"}
{"db": "mydb2", "table": "orders", "op": "delete", "order_id": 42, "total": 99.99}
```

State after batch 2:

`mydb.users`:

|
|
| **db** | **table** | **op** | **user\_id** | **name** |
| --- |--- |--- |--- |--- |
| mydb | users | update | 1 | alice\_updated |

`mydb2.orders` (row `order_id = 42` removed by the delete): *no rows*

### Example 5: Multiple tables (any ops), all tables have identifier fields, static database
<a name="example-5-multiple-tables-any-ops-all-tables-have-identifier-fields-static-database"></a>

Same as [Example 4](#example-4-multiple-tables-any-ops-all-tables-have-identifier-fields-database-in-the-record), but every record lands in a single fixed database — only the table name (and the operation) is dynamic. You omit `DestinationTableConfigurationList`.

Target tables (both in the static database `mydb`; identifier fields declared on each, illustrative Apache Spark SQL):

```
CREATE TABLE mydb.users (
    `table` STRING,
    op      STRING,
    user_id BIGINT,
    name    STRING
) USING iceberg;
ALTER TABLE mydb.users SET IDENTIFIER FIELDS user_id;

CREATE TABLE mydb.orders (
    `table`  STRING,
    op       STRING,
    order_id BIGINT,
    total    DOUBLE
) USING iceberg;
ALTER TABLE mydb.orders SET IDENTIFIER FIELDS order_id;
```

Stream configuration:

```
{
  "ProcessingConfiguration": {
    "Enabled": true,
    "Processors": [
      {
        "Type": "MetadataExtraction",
        "Parameters": [
          { "ParameterName": "JsonParsingEngine",       "ParameterValue": "JQ-1.6" },
          { "ParameterName": "MetadataExtractionQuery", "ParameterValue": "{destinationDatabaseName: \"mydb\", destinationTableName: .table, operation: .op}" }
        ]
      }
    ]
  }
}
```

Sample input records (batch 1 — both inserts):

```
{"table": "users",  "op": "insert", "user_id": 1,  "name":  "alice"}
{"table": "orders", "op": "insert", "order_id": 42, "total": 99.99}
```

State after batch 1:

`mydb.users`:

|
|
| **table** | **op** | **user\_id** | **name** |
| --- |--- |--- |--- |
| users | insert | 1 | alice |

`mydb.orders`:

|
|
| **table** | **op** | **order\_id** | **total** |
| --- |--- |--- |--- |
| orders | insert | 42 | 99.99 |

Sample input records (batch 2 — update \+ delete):

```
{"table": "users",  "op": "update", "user_id": 1,  "name":  "alice_updated"}
{"table": "orders", "op": "delete", "order_id": 42, "total": 99.99}
```

State after batch 2:

`mydb.users`:

|
|
| **table** | **op** | **user\_id** | **name** |
| --- |--- |--- |--- |
| users | update | 1 | alice\_updated |

`mydb.orders` (row `order_id = 42` removed by the delete): *no rows*

### Example 6: Multiple tables (any ops), some tables lack identifier fields, database in the record
<a name="example-6-multiple-tables-any-ops-some-tables-lack-identifier-fields-database-in-the-record"></a>

Same shape as [Example 4](#example-4-multiple-tables-any-ops-all-tables-have-identifier-fields-database-in-the-record), but not every target table has `identifier-field-ids` declared. For each table that lacks it, add an entry to `DestinationTableConfigurationList` with the record-key columns in `UniqueKeys`. Tables that already have identifier fields on the Iceberg table can be omitted from the list (`orders` in this example).

Target tables (`users` and `events` have no identifier fields; `orders` has one on `order_id`, illustrative Apache Spark SQL):

```
CREATE TABLE mydb.users (
    db      STRING,
    `table` STRING,
    op      STRING,
    user_id BIGINT,
    name    STRING
) USING iceberg;
-- record key comes from Firehose UniqueKeys ["user_id"]

CREATE TABLE mydb2.events (
    db       STRING,
    `table`  STRING,
    op       STRING,
    event_id BIGINT,
    event_ts STRING,
    type     STRING
) USING iceberg;
-- record key comes from Firehose UniqueKeys ["event_id", "event_ts"]

CREATE TABLE mydb.orders (
    db       STRING,
    `table`  STRING,
    op       STRING,
    order_id BIGINT,
    total    DOUBLE
) USING iceberg;
ALTER TABLE mydb.orders SET IDENTIFIER FIELDS order_id;
```

Stream configuration:

```
{
  "ProcessingConfiguration": {
    "Enabled": true,
    "Processors": [
      {
        "Type": "MetadataExtraction",
        "Parameters": [
          { "ParameterName": "JsonParsingEngine",       "ParameterValue": "JQ-1.6" },
          { "ParameterName": "MetadataExtractionQuery", "ParameterValue": "{destinationDatabaseName: .db, destinationTableName: .table, operation: .op}" }
        ]
      }
    ]
  },
  "DestinationTableConfigurationList": [
    {
      "DestinationDatabaseName": "mydb",
      "DestinationTableName":    "users",
      "UniqueKeys":              ["user_id"]
    },
    {
      "DestinationDatabaseName": "mydb2",
      "DestinationTableName":    "events",
      "UniqueKeys":              ["event_id", "event_ts"]
    }
  ]
}
```

Sample input records (batch 1 — both inserts):

```
{"db": "mydb",  "table": "users",  "op": "insert", "user_id": 1,   "name":     "alice"}
{"db": "mydb2", "table": "events", "op": "insert", "event_id": 100, "event_ts": "2026-09-01T10:00:00Z", "type": "signup"}
```

State after batch 1:

`mydb.users`:

|
|
| **db** | **table** | **op** | **user\_id** | **name** |
| --- |--- |--- |--- |--- |
| mydb | users | insert | 1 | alice |

`mydb2.events`:

|
|
| **db** | **table** | **op** | **event\_id** | **event\_ts** | **type** |
| --- |--- |--- |--- |--- |--- |
| mydb2 | events | insert | 100 | 2026-09-01T10:00:00Z | signup |

Sample input records (batch 2 — update \+ delete):

```
{"db": "mydb",  "table": "users",  "op": "update", "user_id": 1,   "name":     "alice_updated"}
{"db": "mydb2", "table": "events", "op": "delete", "event_id": 100, "event_ts": "2026-09-01T10:00:00Z", "type": "signup"}
```

State after batch 2:

`mydb.users`:

|
|
| **db** | **table** | **op** | **user\_id** | **name** |
| --- |--- |--- |--- |--- |
| mydb | users | update | 1 | alice\_updated |

`mydb2.events` (row with `event_id = 100, event_ts = 2026-09-01T10:00:00Z` removed by the delete): *no rows*

### Example 7: Multiple tables (any ops), some tables lack identifier fields, static database
<a name="example-7-multiple-tables-any-ops-some-tables-lack-identifier-fields-static-database"></a>

Same as [Example 6](#example-6-multiple-tables-any-ops-some-tables-lack-identifier-fields-database-in-the-record), but with a static destination database. Only the table name and the operation are dynamic; the `UniqueKeys` entries in `DestinationTableConfigurationList` cover the tables that lack `identifier-field-ids`. As in Example 6, `orders` is omitted from the list because it has identifier fields set on the Iceberg table.

Target tables (all in the static database `mydb`; `users` and `events` have no identifier fields, `orders` has one on `order_id`, illustrative Apache Spark SQL):

```
CREATE TABLE mydb.users (
    `table` STRING,
    op      STRING,
    user_id BIGINT,
    name    STRING
) USING iceberg;
-- record key comes from Firehose UniqueKeys ["user_id"]

CREATE TABLE mydb.events (
    `table`  STRING,
    op       STRING,
    event_id BIGINT,
    event_ts STRING,
    type     STRING
) USING iceberg;
-- record key comes from Firehose UniqueKeys ["event_id", "event_ts"]

CREATE TABLE mydb.orders (
    `table`  STRING,
    op       STRING,
    order_id BIGINT,
    total    DOUBLE
) USING iceberg;
ALTER TABLE mydb.orders SET IDENTIFIER FIELDS order_id;
```

Stream configuration:

```
{
  "ProcessingConfiguration": {
    "Enabled": true,
    "Processors": [
      {
        "Type": "MetadataExtraction",
        "Parameters": [
          { "ParameterName": "JsonParsingEngine",       "ParameterValue": "JQ-1.6" },
          { "ParameterName": "MetadataExtractionQuery", "ParameterValue": "{destinationDatabaseName: \"mydb\", destinationTableName: .table, operation: .op}" }
        ]
      }
    ]
  },
  "DestinationTableConfigurationList": [
    {
      "DestinationDatabaseName": "mydb",
      "DestinationTableName":    "users",
      "UniqueKeys":              ["user_id"]
    },
    {
      "DestinationDatabaseName": "mydb",
      "DestinationTableName":    "events",
      "UniqueKeys":              ["event_id", "event_ts"]
    }
  ]
}
```

Sample input records (batch 1 — both inserts):

```
{"table": "users",  "op": "insert", "user_id": 1,   "name":     "alice"}
{"table": "events", "op": "insert", "event_id": 100, "event_ts": "2026-09-01T10:00:00Z", "type": "signup"}
```

State after batch 1:

`mydb.users`:

|
|
| **table** | **op** | **user\_id** | **name** |
| --- |--- |--- |--- |
| users | insert | 1 | alice |

`mydb.events`:

|
|
| **table** | **op** | **event\_id** | **event\_ts** | **type** |
| --- |--- |--- |--- |--- |
| events | insert | 100 | 2026-09-01T10:00:00Z | signup |

Sample input records (batch 2 — update \+ delete):

```
{"table": "users",  "op": "update", "user_id": 1,   "name":     "alice_updated"}
{"table": "events", "op": "delete", "event_id": 100, "event_ts": "2026-09-01T10:00:00Z", "type": "signup"}
```

State after batch 2:

`mydb.users`:

|
|
| **table** | **op** | **user\_id** | **name** |
| --- |--- |--- |--- |
| users | update | 1 | alice\_updated |

`mydb.events` (row with `event_id = 100, event_ts = 2026-09-01T10:00:00Z` removed by the delete): *no rows*

Every referenced database and table must already exist in the target catalog before the stream starts — Firehose does not auto-create them.

**Note**
JQ isn't limited to plain field extraction — the `MetadataExtractionQuery` value can be any JQ expression, including string concatenation. For example, to route records to a table whose name is derived by appending a suffix to a field:

```
{destinationDatabaseName: "userevents", destinationTableName: (.event_name + "_uk"), operation: .operation}
```

A record with `event_name = "signup"` routes to `userevents.signup_uk`, the operation is taken from `.operation`, and the database is fixed to `userevents`. Any valid [JQ 1.6](https://jqlang.github.io/jq/manual/v1.6/) expression can appear on the right-hand side of `destinationDatabaseName`, `destinationTableName`, or `operation`.

### AWS Lambda transform
<a name="aws-lambda-transform"></a>

**When to use JQ (**`MetadataExtraction`**) vs. Lambda**:
+ Use `MetadataExtraction`** (JQ)** when the routing keys (`destinationDatabaseName`, `destinationTableName`, `operation`) are already fields on the incoming record — or can be composed from them via string concatenation, conditionals, or static values — and the record body can be written to the Iceberg table as-is. `MetadataExtraction`** only extracts routing metadata; it does not modify the record body**, so every top-level field of the incoming JSON becomes a column in the Iceberg row. JQ runs in-process on each record, so it's cheaper and lower-latency than a Lambda invocation.
+ Use an AWS **Lambda** processor when JQ isn't enough. Typical cases:
  + **Record body transformation** — flatten a nested JSON structure, rename fields to match the target Iceberg schema, cast types, drop fields, or add computed columns.
  + **External state** — routing keys or record values come from a DynamoDB lookup, an API call, or another data store rather than the record itself.
  + **Record filtering** — return `Dropped` for records that shouldn't be delivered to Iceberg at all.

The Lambda function receives each record and returns the routing information in a top-level `metadata.otfMetadata` block:

```
{
  "metadata": {
    "otfMetadata": {
      "destinationDatabaseName": "IoTevents",
      "destinationTableName":    "Device1234",
      "operation":               "insert"
    }
  }
}
```
+ `destinationDatabaseName` and `destinationTableName` — required, exact matches to existing catalog entries.
+ `operation` — optional, one of `insert`, `update`, or `delete`; defaults to `insert`.

#### Example: CDC records
<a name="example-cdc-records"></a>

A common Lambda use case is delivering change-data-capture (CDC) events into Iceberg tables. CDC envelopes carry both the change payload (usually under nested `before` / `after` fields) and metadata (source table, operation code). JQ can extract the routing metadata but can't drop or restructure the envelope — with `MetadataExtraction` alone, the entire CDC envelope (`op`, `ts_ms`, `source`, `before`, `after)` would land in the Iceberg table as top-level columns, which is typically not the desired outcome. Only a Lambda processor can produce the flat row you actually need.

Target table (identifier field declared on `id` so Firehose can apply the `update` and `delete` operations correctly — an equivalent `UniqueKeys: ["id"]` entry in `DestinationTableConfigurationList` also works):

```
CREATE TABLE prod.users (
    id     BIGINT,
    email  STRING,
    status STRING
) USING iceberg;

ALTER TABLE prod.users SET IDENTIFIER FIELDS id;
```

Consider a Debezium-style CDC record from the source table `prod.users`:

```
{
  "op": "u",
  "ts_ms": 1700000000000,
  "source": { "db": "prod", "table": "users" },
  "before": { "id": 42, "email": "alice@example.com", "status": "active" },
  "after":  { "id": 42, "email": "alice@example.com", "status": "suspended" }
}
```

The Lambda function translates the CDC `op` code (Debezium uses `c`/`u`/`d`/`r` for create/update/delete/read) to Firehose's `insert`/`update`/`delete`, picks the row payload from `.after` (for inserts and updates) or `.before` (for deletes), and returns the flat payload as the record data:

```
{
  "recordId": "<input record id>",
  "result":   "Ok",
  "data":     "<base64-encoded flat payload, for example {\"id\":42,\"email\":\"alice@example.com\",\"status\":\"suspended\"}>",
  "metadata": {
    "otfMetadata": {
      "destinationDatabaseName": "prod",
      "destinationTableName":    "users",
      "operation":               "update"
    }
  }
}
```

A minimal Python implementation of that Lambda:

```
import base64
import json

# Debezium op -> Firehose op
OP_MAP = {"c": "insert", "r": "insert", "u": "update", "d": "delete"}

def lambda_handler(event, context):
    output_records = []
    for record in event["records"]:
        cdc = json.loads(base64.b64decode(record["data"]).decode("utf-8"))

        operation = OP_MAP.get(cdc["op"], "insert")
        row       = cdc["before"] if operation == "delete" else cdc["after"]

        # JSON-encode the flat row, then base64-encode the UTF-8 bytes
        flat_data = base64.b64encode(
            json.dumps(row).encode("utf-8")
        ).decode("utf-8")

        output_records.append({
            "recordId": record["recordId"],
            "result":   "Ok",
            "data":     flat_data,
            "metadata": {
                "otfMetadata": {
                    "destinationDatabaseName": cdc["source"]["db"],
                    "destinationTableName":    cdc["source"]["table"],
                    "operation":               operation,
                }
            }
        })
    return {"records": output_records}
```

Firehose delivers only the flat payload (`.after` or `.before`) as the row in the Iceberg table; the CDC envelope (`op`, `ts_ms`, `source`, and the unused half of `before` / `after`) never lands on disk.

#### Lambda buffering and retries
<a name="lambda-buffering-and-retries"></a>

When a Lambda processor is attached, Firehose batches records before invoking the function. Three optional `Parameters` on the processor control the batching and error handling — declare them alongside `LambdaArn` and `RoleArn`:
+ `BufferSizeInMBs` — the maximum size of a Lambda invocation batch. Range 0.2 MB to 3 MB; default 1 MB.
+ `BufferIntervalInSeconds` — the maximum time Firehose waits before invoking the function. Default 60 seconds.
+ `NumberOfRetries` — how many times Firehose retries a failed Lambda invocation before sending the affected records to the S3 backup bucket. Default 3.

Lower buffer values reduce end-to-end latency at the cost of more Lambda invocations; higher values batch more records per invocation. This buffering is separate from the stream-level delivery buffering described in [How it works](#how-it-works) — the Lambda-processor buffer controls **when Firehose calls the function**, and the delivery buffer controls **when Firehose commits a snapshot to the Iceberg table**.

For the full configuration surface (JSON schemas, JQ syntax, Lambda transform contract, sample Lambda code, and error-handling details), see [Route incoming records to a single Iceberg table](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-format-input-record.html) and [Route incoming records to different Iceberg tables](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-format-input-record-different.html) in the Firehose documentation.

## Considerations and limitations
<a name="considerations-and-limitations"></a>

### Record and schema requirements
<a name="record-and-schema-requirements"></a>

Firehose does not reshape records to fit the target schema — that is what a [Lambda transform](#aws-lambda-transform) is for. Without one, the incoming JSON has to already match the table:
+ **Only the first level of the JSON becomes columns.** Firehose maps top-level nodes to columns. A nested object at the top level (like `position` in the example below) maps to a single column, so the target table needs a `struct` or `map` column to receive it. Firehose supports up to 16 levels of nesting inside such a column.

  ```
  {
     "version":"2016-04-01",
     "deviceId":"<solution_unique_device_id>",
     "timestamp":"2024-01-11T20:42:45.000Z",
     "value":"<actual_value>",
     "position":{
        "x":143.595901,
        "y":476.399628,
        "z":0.24234876
     }
  }
  ```
+ **Column names and data types must match exactly.** A mismatch on either causes Firehose to error and route the record to the S3 backup bucket. An *extra* field present in the source record but absent from the table is the one tolerated case — Firehose skips it.
+ **One JSON object per record.** Send exactly one JSON object per Firehose record. If you aggregate several objects into one record, Firehose raises an error and routes the record to the S3 error bucket (under the `S3ErrorOutputPrefix` configured on the stream), with per-record error metadata. Monitor that prefix (and the corresponding `DeliveryToS3.Records` / error CloudWatch metrics) to catch producer-side framing bugs early. Records aggregated with the [Kinesis Producer Library (KPL)](https://docs.aws.amazon.com/streams/latest/dev/developing-producers-with-kpl.html) and ingested through Amazon Kinesis Data Streams are the exception: Firehose de-aggregates them automatically and treats each inner object as its own record.
+ **Amazon S3 Tables requires lowercase column names**, a constraint of the S3 Tables catalog integration rather than of Firehose.
+ Firehose writes data files in **Parquet** format and uses Iceberg's **merge-on-read (MoR)** mode.

### Throughput and partition scaling
<a name="throughput-and-partition-scaling"></a>
+ **Direct PUT throughput cap** — 5 MiB/second per stream in US East (N. Virginia), US West (Oregon), and Europe (Ireland); 1 MiB/second per stream in all other Regions. If a Direct PUT stream is throttled, Firehose raises the stream's limit automatically until throttling subsides, but the ramp is not instant — keep retrying failed records, and request a limit increase up front through the Firehose Limits form if you expect large bursts.
+ `AppendOnly`** for insert-only streams** — set `AppendOnly` to `true` and Firehose scales throughput automatically to match your ingest rate instead of holding you to the Direct PUT cap. It is settable only through the `CreateDeliveryStream` API, and only valid for insert-only workloads: setting it on a stream that carries updates or deletes produces out-of-order delivery. This is the right flag for the [Example 1](#example-1-single-table-insert-only) shape, and it is incompatible with the upsert pattern described above.
+ **Throughput trades off against active partitions** — the service is tuned for either many partitions or very high throughput, not both. The more you ingest, the fewer partitions you can actively write to.

<table>
<tbody>
</tbody>
</table>

  Ingest throughput here is measured **after** any Lambda transform, not at the source. A transform that expands records — one input event fanned out into several rows — pushes you into a lower partition tier than your source volume suggests.
+ **Spread records across source shards** — if the source is Kinesis Data Streams or Amazon MSK, choose a partition key that maps records for the same Iceberg table onto one or a few shards, and records for different tables onto different shards. That keeps Amazon S3 request rates per table prefix manageable and lets you use the aggregate throughput of all shards.

### Operational limits
<a name="operational-limits"></a>
+ **One stream per table.** Do not point multiple Firehose streams at the same Iceberg table. Iceberg uses optimistic concurrency control, so only one writer commits at a time; the others back off and retry until the retry duration expires, after which their data and delete file keys go to the S3 error prefix.
+ **Deletes are partition-scoped.** Every file Firehose writes, including delete files, is computed from the partition present in the record. Global deletes — writing an unpartitioned delete file against a partitioned table — are not supported.
+ **Bloom filters are ignored. If you set bloom filter properties on the target table, Firehose does not honor them during delivery.**
+ **Encryption for Amazon S3 Tables destinations is configured on the table bucket, not on the Firehose stream.** To encrypt delivered data with AWS KMS, set the KMS configuration on the S3 table bucket (or the target table) using SSE-KMS. KMS parameters set in the Firehose stream configuration are ignored for S3 Tables destinations.
+ **Region availability** — the Apache Iceberg Tables destination is available in all AWS Regions except the China Regions, AWS GovCloud (US) Regions, Asia Pacific (Taipei), Asia Pacific (Malaysia), Asia Pacific (New Zealand), and Mexico (Central).

### Delivery errors
<a name="delivery-errors"></a>

Firehose sends delivery errors to both CloudWatch Logs and the S3 error bucket. The common codes:

|
|
| **Error code** | **Meaning** |
| --- |--- |
| `Iceberg.NoSuchTable` | The target table does not exist, or is not in V2 format. |
| `Iceberg.InvalidTableName` | A null or empty table name was passed, or the table is not in V2 format. |
| `Iceberg.InvalidIcebergVersion` | The target table is Iceberg format version 3 — message *"Iceberg V3 Table format is not supported"*. See [Iceberg format version support in Firehose](#iceberg-format-version-support-in-firehose). |
| `Iceberg.InvalidUniqueKeys` | The configured record key does not resolve against the table schema — either the named columns are absent or ambiguous, or the key names a nested field. See [Per-record operation and record key](#per-record-operation-and-record-key). |
| `Glue.AccessDenied` | The Firehose role is missing AWS Glue permissions, or the trust policy is wrong. |
| `S3.AccessDenied` | The Firehose role is missing Amazon S3 permissions, or the trust policy is wrong. |

## Reference
<a name="reference"></a>

For the complete configuration surface — stream creation, IAM policies, prerequisites, per-record structure, error handling, and quotas — see [Deliver data to Apache Iceberg Tables with Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-destination.html). Related pages:
+ [Set up the Firehose stream](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-stream.html) — end-to-end setup.
+ [Prerequisites to use Apache Iceberg Tables as a destination](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-prereq.html) — separate prerequisite lists for self-managed Iceberg on Amazon S3 and for Amazon S3 Tables.
+ [Considerations and limitations](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-considerations.html) — throughput, partition scaling, column rules, and Region availability.
+ [Route incoming records to different Iceberg tables](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-format-input-record-different.html) — JSONQuery and Lambda routing details.
+ AWS blog: [Stream real-time data into Apache Iceberg tables in Amazon S3 using Amazon Data Firehose](https://aws.amazon.com/blogs/big-data/stream-real-time-data-into-apache-iceberg-tables-in-amazon-s3-using-amazon-data-firehose/).
+ AWS blog: [Stream data from Amazon MSK to Apache Iceberg tables in Amazon S3 and Amazon S3 Tables using Amazon Data Firehose](https://aws.amazon.com/blogs/big-data/stream-data-from-amazon-msk-to-apache-iceberg-tables-in-amazon-s3-and-amazon-s3-tables-using-amazon-data-firehose/).
