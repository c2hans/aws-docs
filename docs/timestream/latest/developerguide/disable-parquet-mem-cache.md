---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/disable-parquet-mem-cache.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `disable-parquet-mem-cache`
<a name="disable-parquet-mem-cache"></a>

**Parameter Details**

|  |  |
| --- |--- |
| Default | FALSE |
| Allowed Values | FALSE, TRUE |
| Category | Memory Management / Caching |

**Detailed Explanation:**

When set to TRUE, completely disables the Parquet memory cache. All Parquet data reads go directly to object storage.

**Recommendation:** Keep as FALSE (default). Only set to TRUE for dedicated write-only ingestion nodes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
