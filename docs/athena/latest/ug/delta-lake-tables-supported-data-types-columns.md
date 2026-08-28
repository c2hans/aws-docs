---
source_url: https://docs.aws.amazon.com/athena/latest/ug/delta-lake-tables-supported-data-types-columns.html
---

# Supported column data types
<a name="delta-lake-tables-supported-data-types-columns"></a>

This section describes the supported data types for non-partition and partition columns.

## Supported non-partition column data types
<a name="delta-lake-tables-supported-data-types-non-partition-columns"></a>

For non-partition columns, all data types that Athena supports except `CHAR` are supported (`CHAR` is not supported in the Delta Lake protocol itself). Supported data types include:

```
boolean
tinyint
smallint
integer
bigint
double
float
decimal
varchar
string
binary
date
timestamp
array
map
struct
```

## Supported partition column data types
<a name="delta-lake-tables-supported-data-types-partition-columns"></a>

For partition columns, Athena supports tables with the following data types:

```
boolean
integer
smallint
tinyint
bigint
decimal
float
double
date
timestamp
varchar
```

For more information about the data types in Athena, see [Data types in Amazon Athena](data-types.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
