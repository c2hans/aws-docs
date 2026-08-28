---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/gen1-duration.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `gen1-duration`
<a name="gen1-duration"></a>

**Parameter Details**

|  |  |
| --- |--- |
| Default | 10 minutes |
| Allowed Values | Duration |
| Category | Data Lifecycle |

**Note**
**IMMUTABLE AFTER INITIAL SETUP:** This parameter is persisted in the catalog. Changing it after the cluster's first start causes silent deduplication failures. Set this at cluster creation time only. When cloning parameter groups, this value must be copied unchanged.

**Detailed Explanation:**

Controls the time span covered by Gen1 Parquet files. Data flows from WAL to Gen1 to Gen2 (via compaction) to Gen3\+.

**Recommendation:** 5–10 minutes for high-frequency ingestion. 10 minutes (default) for medium-frequency. 15–30 minutes for low-frequency. 30–60 minutes for batch ingestion.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
