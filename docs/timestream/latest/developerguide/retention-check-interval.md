---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/retention-check-interval.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `retention-check-interval`
<a name="retention-check-interval"></a>

**Parameter Details**

|  |  |
| --- |--- |
| Default | 30 minutes |
| Allowed Values | Duration |
| Category | Data Lifecycle |

**Detailed Explanation:**

Controls how frequently the system evaluates and enforces retention policies.

**Recommendation:** 10–15 minutes for strict retention compliance. 30 minutes (default) for standard production. 1–6 hours for relaxed retention.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
