---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/query-log-size.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `query-log-size`
<a name="query-log-size"></a>

**Parameter Details**

|  |  |
| --- |--- |
| Default | 1000 |
| Allowed Values | Integer: 1 – 10,000 |
| Category | Query Execution / Observability |

**Detailed Explanation:**

Controls the maximum number of entries retained in the in-memory query log for debugging and performance analysis.

**Recommendation:** 500 for db.influx.medium, 1000 (default) for most instances, 2000–5000 for db.influx.4xlarge and above.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
