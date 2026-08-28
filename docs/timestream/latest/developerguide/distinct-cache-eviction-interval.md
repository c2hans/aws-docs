---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/distinct-cache-eviction-interval.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `distinct-cache-eviction-interval`
<a name="distinct-cache-eviction-interval"></a>

**Parameter Details**

|  |  |
| --- |--- |
| Default | 10 seconds |
| Allowed Values | Duration |
| Category | Caching |

**Detailed Explanation:**

The distinct value cache stores the set of unique values for tag columns. This parameter controls how frequently the cache is checked for stale entries.

**Recommendation:** Keep at 10 seconds (default) for all instance sizes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
