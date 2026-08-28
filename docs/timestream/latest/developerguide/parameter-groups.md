---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/parameter-groups.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Parameter Groups for DB Clusters in Amazon Timestream
<a name="parameter-groups"></a>

Database parameters specify how the database is configured. You manage your database configuration by associating your DB instances with parameter groups.

Timestream defines parameter groups with default settings. You can also define your own parameter groups with customized settings. **Parameter groups for Core and Enterprise editions, while similar, are not identical or interchangeable.**

For InfluxDB 3, cluster configurations are managed through parameter groups. These parameter groups contain engine configuration values that determine how your InfluxDB 3 cluster operates.

**Important:** All parameters are startup-only. There is no runtime reconfiguration mechanism. To change any parameter, the node/cluster must be restarted with updated arguments.

**Topics**
+ [Parameter Group Characteristics](parameter-group-characteristics.md)
+ [Creating Parameter Groups with the AWS CLI](creating-parameter-groups-cli.md)
+ [Supported Instance Types and Specifications](supported-instance-types.md)
+ [Detailed Parameter Reference](detailed-parameter-reference.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
