---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/delete-grace-period.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `delete-grace-period`
<a name="delete-grace-period"></a>

**Parameter Details**

|  |  |
| --- |--- |
| Default | 24 hours |
| Allowed Values | Duration |
| Category | Data Lifecycle |

**Detailed Explanation:**

When data is marked for deletion, this parameter defines the grace period before the deletion is physically applied. During this period, the data remains queryable (soft delete).

**Recommendation:** 15 minutes for dev/test. 1 hour for standard production. 4–24 hours for compliance-sensitive environments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
