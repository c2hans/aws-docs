---
source_url: https://docs.aws.amazon.com/redshift/latest/mgmt/odbc20-converting-data-types.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Data types conversions
<a name="odbc20-converting-data-types"></a>

The Amazon Redshift ODBC driver version 2.x supports many common data formats, converting between Amazon Redshift and SQL data types.

The following table lists the supported data type mappings.

| Amazon Redshift type | SQL type |
| --- | --- |
| BIGINT | SQL\_BIGINT |
| BOOLEAN | SQL\_BIT |
| CHAR | SQL\_CHAR |
| DATE | SQL\_TYPE\_DATE |
| DECIMAL | SQL\_NUMERIC |
| DOUBLE PRECISION | SQL\_DOUBLE |
| GEOGRAPHY | SQL\_ LONGVARBINARY |
| GEOMETRY | SQL\_ LONGVARBINARY |
| INTEGER | SQL\_INTEGER |
| REAL | SQL\_REAL |
| SMALLINT | SQL\_SMALLINT |
| SUPER | SQL\_LONGVARCHAR |
| TEXT | SQL\_LONGVARCHAR |
| TIME | SQL\_TYPE\_TIME |
| TIMETZ | SQL\_TYPE\_TIME |
| TIMESTAMP | SQL\_TYPE\_ TIMESTAMP |
| TIMESTAMPTZ | SQL\_TYPE\_ TIMESTAMP |
| VARBYTE | SQL\_LONGVARBINARY |
| VARCHAR | SQL\_VARCHAR |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
