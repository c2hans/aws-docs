---
source_url: https://docs.aws.amazon.com/glue/latest/dg/data-mapping-rs-iceberg.html
---

# Data mapping between Amazon Redshift and Apache Iceberg
<a name="data-mapping-rs-iceberg"></a>

Redshift and Iceberg support various data types. The following compatibility matrix outlines the support and limitations when mapping data between these two data systems. Please refer to [Amazon Redshift Data Types](https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html) and [Apache Iceberg Table Specifications](https://iceberg.apache.org/spec/#primitive-types) for more details on supported data types in respective data systems.

| Redshift data type | Aliases | Iceberg data type |
| --- | --- | --- |
| SMALLINT | INT2 | int |
| INTEGER | INT, INT4 | int |
| BIGINT | INT8 | long |
| DECIMAL | NUMERIC | decimal |
| REAL | FLOAT4 | float |
| REAL | FLOAT4 | float |
| DOUBLE PRECISION | FLOAT8, FLOAT | double |
| CHAR | CHARACTER, NCHAR | string |
| VARCHAR | CHARACTER VARYING, NVARCHAR | string |
| BPCHAR |  | string |
| TEXT |  | string |
| DATE |  | date |
| TIME | TIME WITHOUT TIMEZONE | time |
| TIME | TIME WITH TIMEZONE | not supported |
| TIMESTAMP | TIMESTAMP WITHOUT TIMEZONE | TIMESTAMP |
| TIMESTAMPZ | TIMESTAMP WITH TIMEZONE | TIMESTAMPZ |
| INTERVAL YEAR TO MONTH |  | Not supported |
| INTERVAL DAY TO SECOND |  | Not supported |
| BOOLEAN | BOOL | bool |
| HLLSKETCH |  | Not supported |
| SUPER |  | Not supported |
| VARBYTE | VARBINARY, BINARY VARYING | binary |
| GEOMETRY |  | Not supported |
| GEOGRAPHY |  | Not supported |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
