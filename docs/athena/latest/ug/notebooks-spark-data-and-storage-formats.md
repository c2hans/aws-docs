---
source_url: https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-data-and-storage-formats.html
---

# Supported data and storage formats
<a name="notebooks-spark-data-and-storage-formats"></a>

The following table shows formats that are supported natively in Athena for Apache Spark.

| **Data format** | **Read** | **Write** | **Write compression** |
| --- | --- | --- | --- |
| parquet | yes | yes | none, uncompressed, snappy, gzip |
| orc | yes | yes | none, snappy, zlib, lzo |
| json | yes | yes | bzip2, gzip, deflate |
| csv | yes | yes | bzip2, gzip, deflate |
| text | yes | yes | none, bzip2, gzip, deflate |
| binary file | yes | N/A | N/A |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
