---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/compaction-cleanup-wait.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `compaction-cleanup-wait`
<a name="compaction-cleanup-wait"></a>

**Parameter Details**

|  |  |
| --- |--- |
| Default | 1 hour |
| Allowed Values | Duration |
| Category | Compaction |

**Detailed Explanation:**

After compaction merges source files into a new compacted file, the original source files are not deleted immediately. This parameter defines the grace period before cleanup. The delay exists because in-flight queries may still hold references to the old files.

**Recommendation:** 30 minutes for short queries only. 1 hour (default) for mixed workloads. 1–2 hours for long analytical queries (30\+ minutes).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
