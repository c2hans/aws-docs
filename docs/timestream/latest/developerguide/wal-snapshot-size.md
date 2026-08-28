---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/wal-snapshot-size.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `wal-snapshot-size`
<a name="wal-snapshot-size"></a>

**Parameter Details**

|  |  |
| --- |--- |
| Default | 600 |
| Allowed Values | Integer: 1 – 10,000 |
| Category | WAL / Ingestion |

**Detailed Explanation:**

Controls the size threshold (in number of WAL operations) at which a WAL snapshot is triggered, persisting data to Parquet files.

**Recommendation:** 300 for all instance sizes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
