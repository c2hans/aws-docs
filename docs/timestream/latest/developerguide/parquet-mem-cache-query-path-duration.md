---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/parquet-mem-cache-query-path-duration.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `parquet-mem-cache-query-path-duration`
<a name="parquet-mem-cache-query-path-duration"></a>

**Parameter Details**

|  |  |
| --- |--- |
| Default | 5 hours |
| Allowed Values | Duration |
| Category | Memory Management / Caching |

**Detailed Explanation:**

Controls how long query access path information is retained for Parquet cache entries. This metadata helps the cache make intelligent eviction decisions.

**Recommendation:** Keep at 5 hours (default). Increase to 10–15 hours for periodic queries on infrequent schedules.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
