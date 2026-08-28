---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-format-input-record.html
---

# Route incoming records to a single Iceberg table
<a name="apache-iceberg-format-input-record"></a>

If you want Firehose to insert data to a single Iceberg table, simply configure a single database and table in your stream configuration as shown in the following example JSON. For a single table, you do not require JQ expression and Lambda function for providing the routing information to Firehose. If you provide these fields along with JQ or Lambda, then Firehose will take input from JQ or Lambda.

```
[
  {
    "DestinationDatabaseName": "UserEvents",
    "DestinationTableName": "customer_id",
    "UniqueKeys": [
      "COLUMN_PLACEHOLDER"
    ],
    "S3ErrorOutputPrefix": "OPTIONAL_PREFIX_PLACEHOLDER"
  }
]
```

In this example, Firehose routes all input records to `customer_id` table in `UserEvents` database. If you want to perform update or delete operations on a single table, then you must provide the operation for each incoming record to Firehose using either the [JSONQuery method](apache-iceberg-format-input-record-different.md#apache-iceberg-route-jq) or [Lambda method](apache-iceberg-format-input-record-different.md#apache-iceberg-route-lambda).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
