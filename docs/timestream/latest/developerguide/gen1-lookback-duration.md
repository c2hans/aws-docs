---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/gen1-lookback-duration.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `gen1-lookback-duration`
<a name="gen1-lookback-duration"></a>

**Parameter Details**

|  |  |
| --- |--- |
| Default | 1 month |
| Allowed Values | Duration |
| Category | Data Lifecycle |

**Note**
Leave at the default value (1 month) in almost all cases. Setting it to a small value can cause the cluster to not initialize with the correct historical state. Only increase this value (never decrease).

**Detailed Explanation:**

Defines how far back the system looks to correctly place data into the appropriate Gen1 time partition and to reconstruct the correct historical state during initialization.

**Recommendation:** Leave at 1 month (default) for all deployments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
