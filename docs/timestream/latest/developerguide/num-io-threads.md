---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/num-io-threads.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `num-io-threads`
<a name="num-io-threads"></a>

**Parameter Details**

|  |  |
| --- |--- |
| Default | System logical core count (number of vCPUs) |
| Allowed Values | Integer: 1 – 2,048 |
| Category | Query Execution / I/O |

**Detailed Explanation:**

Sets the number of threads in the I/O runtime, which handles network I/O, object store operations, and other async I/O tasks. This is separate from the DataFusion query threads.

**Recommendation:** Set to the number of vCPUs on your instance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
