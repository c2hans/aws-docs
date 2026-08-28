---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-pyiceberg.html
---

# Working with Iceberg tables by using PyIceberg
<a name="iceberg-pyiceberg"></a>

This section explains how you can interact with Iceberg tables by using [PyIceberg](https://py.iceberg.apache.org/). The examples provided are boilerplate code that you can run on [Amazon Linux 2023](https://aws.amazon.com/linux/amazon-linux-2023/) EC2 instances, [AWS Lambda](https://aws.amazon.com/lambda/) functions, or any [Python](https://www.python.org/) environment with properly configured [AWS credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html).

## Prerequisites
<a name="pyiceberg-prerequisites"></a>

**Note**
These examples use [PyIceberg 1.9.1](https://github.com/apache/iceberg/releases/tag/apache-iceberg-1.9.1).

To work with PyIceberg, you need PyIceberg and AWS SDK for Python (Boto3) installed. Here's an example of how you can set up a Python virtual environment to work with PyIceberg and AWS Glue Data Catalog:

1. Download [PyIceberg](https://pypi.org/project/pyiceberg/) by using the[ pip python package installer](https://pypi.org/project/pip/). You also need [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to interact with AWS services. You can configure a local Python virtual environment to test by using these commands:

   ```
   python3 -m venv my_env
   cd my_env/bin/
   source activate
   pip install "pyiceberg[pyarrow,pandas,glue]"
   pip install boto3
   ```

1. Run `python` to open the Python shell and test the commands.

## Connecting to the Data Catalog
<a name="pyiceberg-data-catalog"></a>

To start working with Iceberg tables in AWS Glue, you first need to connect to the AWS Glue Data Catalog.

The `load_catalog` function initializes a connection to the Data Catalog by creating a [catalog](https://py.iceberg.apache.org/reference/pyiceberg/catalog/) object that serves as your primary interface for all Iceberg operations:

```
from pyiceberg.catalog import load_catalog
region = "us-east-1"

glue_catalog = load_catalog(
    'default',
    **{
        'client.region': region
    },
    type='glue'
)
```

## Listing and creating databases
<a name="pyiceberg-list-database"></a>

To list existing databases, use the `list_namespaces` function:

```
databases = glue_catalog.list_namespaces()
print(databases)
```

To create a new database, use the `create_namespace` function:

```
database_name="mydb"
s3_db_path=f"s3://DOC-EXAMPLE-BUCKET/{database_name}"

glue_catalog.create_namespace(database_name, properties={"location": s3_db_path})
```

## Creating and writing Iceberg tables
<a name="pyiceberg-create-table"></a>

### Unpartitioned tables
<a name="unpartitioned-tables.810ff77c-69b4-5e2a-9354-5b3d74fb0a3f"></a>

Here's an example of creating an unpartitioned Iceberg table by using the `create_table` function:

```
from pyiceberg.schema import Schema
from pyiceberg.types import NestedField, StringType, DoubleType

database_name="mydb"
table_name="pyiceberg_table"
s3_table_path=f"s3://DOC-EXAMPLE-BUCKET/{database_name}/{table_name}"

schema = Schema(
    NestedField(1, "city", StringType(), required=False),
    NestedField(2, "lat", DoubleType(), required=False),
    NestedField(3, "long", DoubleType(), required=False),
)

glue_catalog.create_table(f"{database_name}.{table_name}", schema=schema, location=s3_table_path)
```

You can use the `list_tables` function to check the list of tables inside a database:

```
tables = glue_catalog.list_tables(namespace=database_name)
print(tables)
```

You can use the `append` function and PyArrow to insert data inside an Iceberg table:

```
import pyarrow as pa
df = pa.Table.from_pylist(
    [
        {"city": "Amsterdam", "lat": 52.371807, "long": 4.896029},
        {"city": "San Francisco", "lat": 37.773972, "long": -122.431297},
        {"city": "Drachten", "lat": 53.11254, "long": 6.0989},
        {"city": "Paris", "lat": 48.864716, "long": 2.349014},
    ],
)

table = glue_catalog.load_table(f"{database_name}.{table_name}")
table.append(df)
```

### Partitioned tables
<a name="partitioned-tables.828185a1-2ac7-5833-bed7-8a6cac12792c"></a>

Here's an example of creating a [partitioned ](https://iceberg.apache.org/docs/1.4.0/partitioning/)Iceberg table with [hidden partitioning ](https://iceberg.apache.org/docs/1.4.0/partitioning/#icebergs-hidden-partitioning)by using the `create_table` function and `PartitionSpec`:

```
from pyiceberg.schema import Schema
from pyiceberg.types import (
    NestedField,
    StringType,
    FloatType,
    DoubleType,
    TimestampType,
)

# Define the schema
schema = Schema(
    NestedField(field_id=1, name="datetime", field_type=TimestampType(), required=True),
    NestedField(field_id=2, name="drone_id", field_type=StringType(), required=True),
    NestedField(field_id=3, name="lat", field_type=DoubleType(), required=False),
    NestedField(field_id=4, name="lon", field_type=DoubleType(), required=False),
    NestedField(field_id=5, name="height", field_type=FloatType(), required=False),
)

from pyiceberg.partitioning import PartitionSpec, PartitionField
from pyiceberg.transforms import DayTransform

partition_spec = PartitionSpec(
    PartitionField(
        source_id=1,  # Refers to "datetime"
        field_id=1000,
        transform=DayTransform(),
        name="datetime_day"
    )
)

database_name="mydb"
partitioned_table_name="pyiceberg_table_partitioned"
s3_table_path=f"s3://DOC-EXAMPLE-BUCKET/{database_name}/{partitioned_table_name}"

glue_catalog.create_table(
    identifier=f"{database_name}.{partitioned_table_name}",
    schema=schema,
    location=s3_table_path,
    partition_spec=partition_spec
)
```

You can insert data into a partitioned table the same way as for an unpartitioned table. The partitioning is handled automatically.

```
from datetime import datetime
arrow_schema = pa.schema([
    pa.field("datetime", pa.timestamp("us"), nullable=False),
    pa.field("drone_id", pa.string(), nullable=False),
    pa.field("lat", pa.float64()),
    pa.field("lon", pa.float64()),
    pa.field("height", pa.float32()),
])

data = [
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
]

df = pa.Table.from_pylist(data, schema=arrow_schema)

table = glue_catalog.load_table(f"{database_name}.{partitioned_table_name}")
table.append(df)
```

## Reading data
<a name="pyiceberg-read-data"></a>

You can use the PyIceberg `scan` function to read data from your Iceberg tables. You can filter rows, select specific columns, and limit the number of returned records.

```
table= glue_catalog.load_table(f"{database_name}.{table_name}")
scan_df = table.scan(
    row_filter=(
        f"city = 'Amsterdam'"
    ),
    selected_fields=("city", "lat"),
    limit=100,
).to_pandas()

print(scan_df)
```

## Deleting data
<a name="pyiceberg-delete-data"></a>

The PyIceberg `delete` function lets you remove records from your table by using a `delete_filter`:

```
table = glue_catalog.load_table(f"{database_name}.{table_name}")
table.delete(delete_filter="city == 'Paris'")
```

## Accessing metadata
<a name="pyiceberg-metadata"></a>

PyIceberg provides several functions to access table metadata. Here's how you can view information about table snapshots:

```
#List of snapshots
table.snapshots()

#Current snapshot
table.current_snapshot()

#Take a previous snapshot
second_last_snapshot_id=table.snapshots()[-2].snapshot_id
print(f"Second last SnapshotID: {second_last_snapshot_id}")
```

For a detailed list of available metadata, see the [metadata](https://py.iceberg.apache.org/reference/pyiceberg/table/metadata/) code reference section of the PyIceberg documentation.

## Using time travel
<a name="pyiceberg-time-travel"></a>

You can use table snapshots for time travel to access previous states of your table. Here's how to view the table state before the last operation:

```
second_last_snapshot_id=table.snapshots()[-2].snapshot_id

time_travel_df = table.scan(
    limit=100,
    snapshot_id=second_last_snapshot_id
).to_pandas()

print(time_travel_df)
```

For a complete list of available functions, see the PyIceberg [Python API](https://py.iceberg.apache.org/api/) documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
