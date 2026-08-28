---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/supported-sql-constructs.DESCRIBE.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# DESCRIBE statements
<a name="supported-sql-constructs.DESCRIBE"></a>

You can view the metadata for a table by using the `DESCRIBE` statement. The syntax is as follows:

```
DESCRIBE database.table
```

where `table` contains the table name. The describe statement returns the column names and data types for the table.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
