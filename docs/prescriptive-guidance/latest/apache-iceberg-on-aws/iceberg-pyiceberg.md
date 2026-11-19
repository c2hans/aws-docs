---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-pyiceberg.html
---

# Working with Iceberg tables by using PyIceberg

[PyIceberg](https://py.iceberg.apache.org/) is the Python implementation of Apache Iceberg. It provides direct Python APIs for supported Iceberg metadata and table-data operations without requiring a JVM or a Spark or Trino cluster.

This makes PyIceberg suitable for notebooks, [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html) functions whose workload fits the Lambda runtime and resource limits, containerized workloads on [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) and [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html), Python workloads on Amazon EC2 instances, and other compatible Python environments. The environment requires network access to the required AWS endpoints and AWS permissions through an execution, task, pod, or [EC2 instance role](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html), or another supported credential provider. PyIceberg is not dependency-free: the examples use packages with native components, including PyArrow and `pyiceberg-core`. For Lambda zip packages or layers, include Linux wheels that match the Lambda Python version and `x86_64` or `arm64` architecture; a [Lambda container image](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html) is another packaging option.

This section uses PyIceberg with the AWS Glue Iceberg REST endpoint to access either of the following:
+ Self-managed Iceberg tables stored in general-purpose Amazon S3 buckets and registered in the AWS Glue Data Catalog
+ Iceberg tables hosted in Amazon S3 Tables and integrated with the AWS Glue Data Catalog

The catalog configuration and storage lifecycle differ between these hosting options. Most table-level scan and data-modification APIs are shared after a table is loaded, but catalog creation, location ownership, maintenance, and deletion behavior are hosting-specific.

**Version scope** This section describes **PyIceberg 0.12.0**. PyIceberg support changes between releases, especially for Iceberg format version 3 (V3), so check the feature matrix again before upgrading.

## Iceberg format version support in PyIceberg
<a name="iceberg-format-version-support-in-pyiceberg"></a>

PyIceberg 0.12.0 reads and writes the V2 tables used in this section. Its V3 support is read-only and feature-specific.

|
|
| **Operation** | **V2** | **V3 in PyIceberg 0.12.0** |
| --- |--- |--- |
| Load table metadata |  | Partial — V3 metadata loads when its schema uses implemented types; an unsupported type such as `variant` prevents the table from loading |
| Scan data |  | Partial — see the [V3 feature matrix](#v3-feature-support-in-pyiceberg) |
| Create table metadata in a PyIceberg-managed catalog |  | ✗ — PyIceberg 0.12.0 does not write V3 metadata |
| Upgrade an existing table |  | ✗ — PyIceberg 0.12.0 does not upgrade tables to V3 |
| `append`, `overwrite`, `delete`, and `upsert` |  | ✗ — V3 manifest writing is not implemented |

When no format version is specified, PyIceberg creates a V2 table. Keep tables written by PyIceberg on V2:

```
properties={"format-version": "2"}
```

Do not try to upgrade a V2 table by setting a property named `format-version`. `Transaction.set_properties({"format-version": "3"})` only adds a table property; it does not change the metadata's actual format version. If PyIceberg loads V3 metadata created by another implementation, that does not enable PyIceberg to commit data to the table.

### V3 feature support in PyIceberg
<a name="v3-feature-support-in-pyiceberg"></a>

The following table describes PyIceberg 0.12.0 behavior with V3 tables written by Apache Iceberg 1.11.0.

|
|
| **V3 feature** | **PyIceberg 0.12.0 behavior** |
| --- |--- |
| Deletion vectors | **Read: ** — scans correctly apply deletion vectors. **Write: ✗** |
| Nanosecond timestamps (`timestamp_ns`, `timestamptz_ns`) | **Read: ** — returned as Arrow `timestamp[ns]` and `timestamp[ns, tz=UTC]`. **Write: ✗** |
| Initial default values | **Read: ** — a value added as an Iceberg initial default is projected for older files that do not contain the column. **Write: ✗** |
| Row lineage (`_row_id`, `_last_updated_sequence_number`) | **Read: ✗** — **Write: ✗** |
| Variant without shredding | **Read: ✗** — **Write: ✗** |
| Variant with shredding | **Read: ✗** — **Write: ✗** |
| Geometry and geography | **Read: ✗** — **Write: ✗** |

PyIceberg 0.12.0 cannot write V3 manifests, so no V3 data commit succeeds. Track V3 writer work in [apache/iceberg-python\#1551](https://github.com/apache/iceberg-python/issues/1551).

## Iceberg feature support
<a name="pyiceberg-iceberg-feature-support"></a>

The following table summarizes PyIceberg 0.12.0 support when you use the AWS Glue Iceberg REST endpoint.

|
|
| **Category** | **Feature** | **Supported** |
| --- |--- |--- |
| **DDL** | Create table (`catalog.create_table(...)`) |  for V1/V2. Keep PyIceberg-written tables on V2 |
|  | `CREATE TABLE ... AS SELECT` (CTAS) | ✗ — PyIceberg does not execute SQL `SELECT`. Create the table, then append the source data in a separate commit |
|  | Drop a self-managed table (`catalog.drop_table(...)`) |  — removes the catalog registration but leaves the S3 objects in place |
|  | Delete an Amazon S3 Tables table while using the AWS Glue REST catalog | Use `catalog.purge_table(...)`. S3 Tables does not accept `catalog.drop_table(...)` because the service requires purge on delete. Purge permanently deletes the S3 table and its data |
|  | List tables (`catalog.list_tables(...)`) |  |
|  | Add, drop, or rename columns (`table.update_schema()`) |  |
|  | Type promotion (`update_schema().update_column(...)`) |  for Iceberg-supported promotions, such as `int` to `long` |
|  | Set table properties (`Transaction.set_properties(...)`) | , but setting `format-version` does not upgrade the table |
|  | Change partition spec (`table.update_spec()`) |  |
| **DML** | Append rows (`table.append(...)`) |  on V1/V2 |
|  | Overwrite rows (`table.overwrite(...)`) |  on V1/V2; copy-on-write |
|  | Delete rows (`table.delete(...)`) |  on V1/V2; copy-on-write |
|  | Update or upsert rows (`table.upsert(...)`) |  on V1/V2; copy-on-write |
|  | Write merge-on-read output, positional-delete files, or deletion vectors | ✗ — a merge-on-read delete setting falls back to copy-on-write |
|  | Automatically honor the table sort order during writes | ✗ — input rows are not automatically sorted |
| **Read** | Arrow and pandas (`to_arrow()`, `to_pandas()`) |  |
|  | DuckDB (`to_duckdb(<table_name>)`) and Polars (`to_polars()`) |  when the corresponding optional dependency is installed |
|  | Positional-delete reads |  |
|  | Equality-delete reads | ✗ |
|  | Time travel by snapshot (`table.scan(snapshot_id=...)`) |  |
|  | Branches and tags (`table.scan().use_ref(...)`) |  |
|  | Incremental append scan (`table.incremental_append_scan(...)`) |  — returns rows added by append snapshots; it is not a general CDC stream for updates and deletes |
|  | Metadata inspection (`table.inspect.snapshots()`, `.files()`, `.partitions()`, `.manifests()`, `.history()`) |  |
| **Views** | Iceberg REST View APIs through AWS Glue REST | ✗ — AWS Glue Iceberg REST does not support the Iceberg REST View APIs. PyIceberg's generic REST catalog has `list_views()` and `load_view()` only for servers that implement those endpoints |
|  | Read an [AWS Glue Iceberg materialized view](https://docs.aws.amazon.com/glue/latest/dg/materialized-views.html) through PyIceberg |  read-only — AWS Glue exposes the materialized result as a V2 Iceberg table through the endpoint. Load it with `catalog.load_table(...)`, not `load_view()`, and scan it like any table. PyIceberg does not create, refresh, alter, or drop the materialized view and does not perform automatic query rewrite |
| **Partitioning** | Hidden partitioning and V2 partition transforms |  |
|  | Partition evolution (`table.update_spec()`) |  |
|  | Metadata-only partition delete |  when the predicate selects complete partitions |
| **Security** | IAM full-table authorization through the AWS Glue REST endpoint |  |
|  | Lake Formation full-table access for an external engine |  — enable the Lake Formation setting that allows external engines to access data with full-table access (`AllowFullTableExternalDataAccess`) and grant the principal full table permissions |
|  | Lake Formation row-, column-, or cell-level filtering | ✗ in PyIceberg. External Iceberg clients must be granted full-table access |
| **Maintenance** | Compaction, sort-order compaction, or Z-order compaction | ✗ |
|  | Snapshot metadata expiration (`table.maintenance.expire_snapshots()`) |  |
|  | Orphan-file cleanup | ✗ — there is no `remove_orphan_files()` API |
|  | Roll back to a snapshot or timestamp (`table.manage_snapshots()`) |  |
| **Format** | Iceberg data-file reads | Parquet ; ORC ; Avro ✗ |
|  | Data-file writes through PyIceberg table operations | Parquet ; ORC ✗; Avro ✗ |
|  | Parquet compression | `snappy`, `zstd`, `gzip`, `brotli`, and uncompressed  |

## Prerequisites
<a name="prerequisites"></a>

Create and activate a virtual environment, and install the dependencies used by the examples:

```
python3 -m venv my_env
source my_env/bin/activate
python -m pip install --upgrade pip
python -m pip install "pyiceberg[pyarrow,pandas,pyiceberg-core,rest-sigv4]==0.12.0"
```

The extras have the following purposes:
+ `pyarrow` and `pandas` provide the data conversion APIs used in this section.
+ `pyiceberg-core` is required by PyIceberg 0.12.0 for partition transforms during partitioned writes.
+ `rest-sigv4` installs the AWS dependencies used to sign REST requests.

Install additional adapters only if you use them:

```
python -m pip install "pyiceberg[duckdb,polars]==0.12.0"
```

Verify the installed version:

```
python -c "import pyiceberg; print(pyiceberg.__version__)"
```

Configure [AWS credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html) for the IAM principal that will call AWS Glue and access the table data.

## Connecting to the Data Catalog
<a name="connecting-to-the-data-catalog"></a>

The examples store the loaded REST catalog in `rest_catalog`.

### Self-managed Iceberg on Amazon S3
<a name="self-managed-iceberg-on-amazon-s3"></a>

Use the AWS account ID as the warehouse to address the default AWS Glue Data Catalog. Replace `<aws_region>` with your AWS Region and `<aws_account_id>` with your AWS Account ID:

```
from pyiceberg.catalog import load_catalog

region = "<aws_region>"
account_id = "<aws_account_id>"

rest_catalog = load_catalog(
    "glue",
    **{
        "type": "rest",
        "uri": f"https://glue.{region}.amazonaws.com/iceberg",
        "warehouse": account_id,
        "rest.sigv4-enabled": "true",
        "rest.signing-name": "glue",
        "rest.signing-region": region,
    },
)
```

For endpoint and catalog-prefix details, see [Connecting to the Data Catalog using the AWS Glue Iceberg REST endpoint](https://docs.aws.amazon.com/glue/latest/dg/connect-glu-iceberg-rest.html).

### Amazon S3 Tables through the AWS Glue Iceberg REST endpoint
<a name="amazon-s3-tables-through-the-aws-glue-iceberg-rest-endpoint"></a>

Before using the endpoint, ensure that the table bucket is [integrated with AWS analytics services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html) and that its [namespace](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace-create.html) exists. The following configuration assumes that the table bucket and the Data Catalog are in the same AWS account. The integration creates the parent catalog `s3tablescatalog` and a child catalog for each integrated table bucket. Use the account ID and child catalog as the warehouse. Replace `<aws_region>` with your AWS Region, `<aws_account_id>` with your AWS Account ID and `<table-bucket-name>` with your own table bucket name:

```
from pyiceberg.catalog import load_catalog

region = "<aws_region>"
account_id = "<aws_account_id>"
table_bucket = "<table-bucket-name>"

rest_catalog = load_catalog(
    "s3tables",
    **{
        "type": "rest",
        "uri": f"https://glue.{region}.amazonaws.com/iceberg",
        "warehouse": f"{account_id}:s3tablescatalog/{table_bucket}",
        "rest.sigv4-enabled": "true",
        "rest.signing-name": "glue",
        "rest.signing-region": region,
    },
)
```

The integration supports either IAM access control or Lake Formation access control. With IAM access control, the caller needs permissions for both AWS Glue Data Catalog and S3 Tables resources. With Lake Formation access control, Lake Formation vends scoped credentials and provides fine-grained controls to compatible AWS analytics engines. However, PyIceberg does not apply Lake Formation row or column filters. For an external client such as PyIceberg, enable the Lake Formation setting that allows external engines to access data with full-table access. For details, see [Integrating with Amazon S3 Tables](https://docs.aws.amazon.com/glue/latest/dg/glue-federation-s3tables.html) and [Accessing Amazon S3 Tables using the AWS Glue Iceberg REST endpoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-glue-endpoint.html).

Each S3 table bucket is a separate catalog. Call `load_catalog()` once for each table bucket that the process needs to access.

### Hosting-specific lifecycle differences
<a name="hosting-specific-lifecycle-differences"></a>

|
|
| **Operation** | **Self-managed on Amazon S3** | **Amazon S3 Tables** |
| --- |--- |--- |
| Namespace | You can create it through the catalog and provide an S3 location property | Create it in S3 Tables without a location before using the Glue-integrated endpoint |
| Table location | Provide the table's S3 location | Omit the location; S3 Tables assigns and manages the table location |
| Delete | `drop_table()` removes the catalog entry and leaves files | Use `purge_table()`. S3 Tables does not accept `drop_table()` because it requires purge on delete; purge permanently deletes the table and its data |
| Maintenance | Run maintenance with a supported engine or service | Use S3 Tables maintenance capabilities |

## Listing and creating databases
<a name="listing-and-creating-databases"></a>

List namespaces:

```
databases = rest_catalog.list_namespaces()
print(databases)
```

For a self-managed catalog, you can set the namespace location. Replace `<bucket-name>` with your own bucket name:

```
database_name = "mydb"
database_path = f"s3://<bucket-name>/{database_name}"

rest_catalog.create_namespace(
    database_name,
    properties={"location": database_path},
)
```

For Amazon S3 Tables, create the namespace through Amazon S3 Tables before using the Glue-integrated endpoint. Then confirm that it is visible through the loaded PyIceberg catalog:

```
database_name = "mydb"
namespaces = rest_catalog.list_namespaces()
if (database_name,) not in namespaces:
    raise ValueError(
        f"Create namespace {database_name!r} in the S3 table bucket first"
    )
```

Run only the example that matches your hosting option.

## Creating and writing Iceberg tables
<a name="creating-and-writing-iceberg-tables"></a>

The examples in this section explicitly create V2 tables because PyIceberg 0.12.0 cannot write V3 tables.

### Unpartitioned tables
<a name="unpartitioned-tables"></a>

Define the table schema - Replace `<bucket-name>` with your own bucket name:

```
from pyiceberg.schema import Schema
from pyiceberg.types import DoubleType, NestedField, StringType

bucket_name="<bucket-name>"
database_name = "mydb"
table_name = "pyiceberg_table"
identifier = f"{database_name}.{table_name}"

schema = Schema(
    NestedField(1, "city", StringType(), required=True),
    NestedField(2, "lat", DoubleType(), required=False),
    NestedField(3, "lon", DoubleType(), required=False),
)
```

For a self-managed table, provide the table location:

```
table_path = f"s3://{bucket_name}/{database_name}/{table_name}"

table = rest_catalog.create_table(
    identifier,
    schema=schema,
    location=table_path,
    properties={"format-version": "2"},
)
```

For Amazon S3 Tables, let the service assign the location:

```
table = rest_catalog.create_table(
    identifier,
    schema=schema,
    properties={"format-version": "2"},
)
```

Run only the `create_table` example that matches your hosting option.

List the tables in the namespace:

```
tables = rest_catalog.list_tables(namespace=database_name)
print(tables)
```

Append rows with PyArrow:

```
import pyarrow as pa
from pyiceberg.io.pyarrow import schema_to_pyarrow

arrow_schema = schema_to_pyarrow(schema, include_field_ids=False)
rows = pa.Table.from_pylist(
    [
        {"city": "Amsterdam", "lat": 52.371807, "lon": 4.896029},
        {"city": "San Francisco", "lat": 37.773972, "lon": -122.431297},
        {"city": "Drachten", "lat": 53.11254, "lon": 6.0989},
        {"city": "Paris", "lat": 48.864716, "lon": 2.349014},
    ],
    schema=arrow_schema,
)

table = rest_catalog.load_table(identifier)
table.append(rows)
```

### Partitioned tables
<a name="partitioned-tables"></a>

The following table uses [hidden partitioning](https://iceberg.apache.org/docs/latest/partitioning/#icebergs-hidden-partitioning) with a day transform. Replace `<bucket-name>` with your own bucket name:

```
from pyiceberg.partitioning import PartitionField, PartitionSpec
from pyiceberg.schema import Schema
from pyiceberg.transforms import DayTransform
from pyiceberg.types import (
    DoubleType,
    FloatType,
    NestedField,
    StringType,
    TimestampType,
)

partitioned_schema = Schema(
    NestedField(1, "datetime", TimestampType(), required=True),
    NestedField(2, "drone_id", StringType(), required=True),
    NestedField(3, "lat", DoubleType(), required=False),
    NestedField(4, "lon", DoubleType(), required=False),
    NestedField(5, "height", FloatType(), required=False),
)

partition_spec = PartitionSpec(
    PartitionField(
        source_id=1,
        field_id=1000,
        transform=DayTransform(),
        name="datetime_day",
    )
)

bucket_name="<bucket-name>"
partitioned_table_name = "pyiceberg_table_partitioned"
partitioned_identifier = f"{database_name}.{partitioned_table_name}"
```

For a self-managed table:

```
partitioned_table_path = (
    f"s3://{bucket_name}/{database_name}/{partitioned_table_name}"
)

partitioned_table = rest_catalog.create_table(
    partitioned_identifier,
    schema=partitioned_schema,
    location=partitioned_table_path,
    partition_spec=partition_spec,
    properties={"format-version": "2"},
)
```

For Amazon S3 Tables:

```
partitioned_table = rest_catalog.create_table(
    partitioned_identifier,
    schema=partitioned_schema,
    partition_spec=partition_spec,
    properties={"format-version": "2"},
)
```

Append rows. PyIceberg derives the hidden partition values:

```
from datetime import datetime
import pyarrow as pa
from pyiceberg.io.pyarrow import schema_to_pyarrow

partitioned_arrow_schema = schema_to_pyarrow(
    partitioned_schema,
    include_field_ids=False,
)

partitioned_rows = pa.Table.from_pylist(
    [
        {
            "datetime": datetime(2024, 6, 1, 12, 0, 0),
            "drone_id": "drone_001",
            "lat": 52.371807,
            "lon": 4.896029,
            "height": 120.5,
        },
        {
            "datetime": datetime(2024, 6, 1, 12, 5, 0),
            "drone_id": "drone_002",
            "lat": 37.773972,
            "lon": -122.431297,
            "height": 150.0,
        },
        {
            "datetime": datetime(2024, 6, 2, 9, 0, 0),
            "drone_id": "drone_001",
            "lat": 53.11254,
            "lon": 6.0989,
            "height": 110.2,
        },
        {
            "datetime": datetime(2024, 6, 2, 9, 30, 0),
            "drone_id": "drone_003",
            "lat": 48.864716,
            "lon": 2.349014,
            "height": 145.7,
        },
    ],
    schema=partitioned_arrow_schema,
)

partitioned_table = rest_catalog.load_table(partitioned_identifier)
partitioned_table.append(partitioned_rows)
```

## Reading data
<a name="reading-data"></a>

Use `scan()` to filter rows, project columns, and set a limit:

```
table = rest_catalog.load_table(identifier)

scan_df = table.scan(
    row_filter="city == 'Amsterdam'",
    selected_fields=("city", "lat"),
    limit=100,
).to_pandas()

print(scan_df)
```

To register a scan in DuckDB, provide the required table name:

```
connection = table.scan().to_duckdb("cities")
print(connection.sql("SELECT * FROM cities").fetchall())
```

## Updating and upserting data
<a name="updating-and-upserting-data"></a>

`upsert()` updates matching rows and inserts nonmatching rows. Supply `join_cols` unless the Iceberg schema defines identifier fields:

```
upsert_rows = pa.Table.from_pylist(
    [
        {"city": "Amsterdam", "lat": 52.372, "lon": 4.900},
        {"city": "Dubai", "lat": 25.2048, "lon": 55.2708},
    ],
    schema=arrow_schema,
)

result = table.upsert(upsert_rows, join_cols=["city"])
print(result)
```

PyIceberg implements this as copy-on-write. It rewrites affected Parquet data files rather than writing positional deletes or deletion vectors.

## Deleting data
<a name="deleting-data"></a>

Delete matching rows:

```
table = rest_catalog.load_table(identifier)
table.delete("city == 'Paris'")
```

If a predicate selects complete partitions, PyIceberg can remove the matching data files as a metadata-only delete. Otherwise, it rewrites affected data files.

## Accessing metadata
<a name="pyiceberg-accessing-metadata"></a>

Access snapshot objects directly:

```
snapshots = table.snapshots()
print(snapshots)
print(table.current_snapshot())
```

Use `table.inspect` for Iceberg metadata-table-style results:

```
print(table.inspect.snapshots().to_pandas())
print(table.inspect.files().to_pandas())
print(table.inspect.manifests().to_pandas())
print(table.inspect.history().to_pandas())
```

For the complete interface, see the PyIceberg [metadata inspection API](https://py.iceberg.apache.org/reference/pyiceberg/table/inspect/).

## Using time travel and incremental scans
<a name="using-time-travel-and-incremental-scans"></a>

Read a previous snapshot:

```
snapshots = table.snapshots()
previous_snapshot_id = snapshots[-2].snapshot_id

time_travel_df = table.scan(
    snapshot_id=previous_snapshot_id,
    limit=100,
).to_pandas()

print(time_travel_df)
```

Use `incremental_append_scan()`, not `scan()`, for an incremental append range. Capture the boundary snapshots around an append:

```
start_snapshot_id = table.current_snapshot().snapshot_id

additional_rows = pa.Table.from_pylist(
    [{"city": "Tokyo", "lat": 35.6762, "lon": 139.6503}],
    schema=arrow_schema,
)
table.append(additional_rows)

end_snapshot_id = table.current_snapshot().snapshot_id

incremental_rows = table.incremental_append_scan(
    from_snapshot_id_exclusive=start_snapshot_id,
    to_snapshot_id_inclusive=end_snapshot_id,
).to_arrow()

print(incremental_rows)
```

An incremental append scan returns rows introduced by append snapshots. It does not represent deletes or a complete before-and-after change stream.

## Evolving tables
<a name="evolving-tables"></a>

Schema and partition evolution update metadata without rewriting existing data files.

### Schema evolution
<a name="schema-evolution"></a>

The following operations are sequential and refer only to columns that exist at each step:

```
from pyiceberg.types import IntegerType, LongType

table = rest_catalog.load_table(identifier)

with table.update_schema() as update:
    update.add_column("observation_count", IntegerType())

with table.update_schema() as update:
    update.update_column("observation_count", LongType())

with table.update_schema() as update:
    update.rename_column("lon", "longitude")

with table.update_schema() as update:
    update.delete_column("observation_count")
```

For the complete API, see `UpdateSchema`.

### Partition evolution
<a name="partition-evolution"></a>

This example evolves the partitioned table created earlier:

```
from pyiceberg.transforms import BucketTransform, MonthTransform

partitioned_table = rest_catalog.load_table(partitioned_identifier)

# Replace the day transform with a month transform.
with partitioned_table.update_spec() as update:
    update.remove_field("datetime_day")
    update.add_field("datetime", MonthTransform(), "datetime_month")

# Add a bucket transform.
with partitioned_table.update_spec() as update:
    update.add_field(
        "drone_id",
        BucketTransform(num_buckets=16),
        "drone_id_bucket",
    )

# Remove the bucket transform.
with partitioned_table.update_spec() as update:
    update.remove_field("drone_id_bucket")
```

Existing files retain their old partition spec. New writes use the current spec.

## Snapshot management
<a name="snapshot-management"></a>

Expire unprotected snapshot metadata by ID:

```
old_snapshot_id = table.snapshots()[0].snapshot_id
table.maintenance.expire_snapshots().by_id(old_snapshot_id).commit()
```

Or expire snapshots older than a datetime:

```
from datetime import datetime, timedelta, timezone

cutoff = datetime.now(timezone.utc) - timedelta(days=30)
table.maintenance.expire_snapshots().older_than(cutoff).commit()
```

PyIceberg 0.12.0 does not provide `retain_last()` or `remove_orphan_files()`, and snapshot expiration does not physically delete unreferenced data, manifest, or metadata files.

Roll back the current branch:

```
rollback_snapshot_id = table.snapshots()[-2].snapshot_id
table.manage_snapshots().rollback_to_snapshot(rollback_snapshot_id).commit()
```

## Working with an existing Iceberg V3 table through another catalog
<a name="working-with-an-existing-iceberg-v3-table-through-another-catalog"></a>

Use the same AWS Glue Iceberg REST endpoint configured earlier.

PyIceberg 0.12.0 can only read V3 tables that another V3-capable engine created and populated:

```
table = rest_catalog.load_table("events.v3_events")

rows = table.scan(
    selected_fields=("event_id", "event_time_ns"),
).to_arrow()
```

The scan works only for columns and features listed as readable in the [V3 feature matrix](#v3-feature-support-in-pyiceberg). Keep in mind:
+ Do not call `append`, `overwrite`, `delete`, or `upsert` on the V3 table.
+ Do not select `_row_id` or `_last_updated_sequence_number`; PyIceberg 0.12.0 cannot project these columns.
+ Do not expect a table containing `variant` to load (tables with `variant` columns fail to load).
+ Do not select geometry or geography fields. PyIceberg 0.12.0 cannot read data from these columns.

For workloads that need full V3 read and write behavior, use a V3-capable engine and catalog. Retest PyIceberg after upgrading to a release that implements V3 manifest writing and the required V3 types.
