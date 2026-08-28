---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/compaction-gen2-duration.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `compaction-gen2-duration`
<a name="compaction-gen2-duration"></a>

**Parameter Details**

|  |  |
| --- |--- |
| Default | 20 minutes |
| Allowed Values | Duration |
| Category | Compaction |

**Note**
**IMMUTABLE AFTER INITIAL SETUP:** This parameter is persisted in the catalog. Changing it after the cluster's first start causes silent data divergence. Set this at cluster creation time only. When cloning parameter groups, this value must be copied unchanged.

**Detailed Explanation:**

Defines the time span that each Gen2 compacted file should cover. InfluxDB 3 uses a tiered compaction strategy: Gen0 (raw WAL snapshots), Gen1 (controlled by `gen1-duration`), Gen2 (this parameter), Gen3\+ (controlled by `compaction-multipliers`).

**Recommendation:** 20 minutes (default) for real-time monitoring. 1 hour for operational dashboards. 2–4 hours for analytical/batch queries.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
