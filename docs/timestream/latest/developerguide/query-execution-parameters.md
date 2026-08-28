---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/query-execution-parameters.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Category 1: Query Execution and DataFusion Engine
<a name="query-execution-parameters"></a>

These parameters control the Apache DataFusion query engine, which is responsible for executing SQL and InfluxQL queries against your data. Proper tuning of these parameters directly impacts query latency, throughput, and concurrent query capacity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
