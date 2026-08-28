---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/scheduledqueries-patterns-scenario.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Scenario
<a name="scheduledqueries-patterns-scenario"></a>

The following examples use a DevOps monitoring scenario which is outlined in [Scheduled queries sample schema](scheduledqueries-common-schema-example.md).

The examples provide the scheduled query definition where you can plug in the appropriate configurations for where to receive execution status notifications for scheduled queries, where to receive reports for errors encountered during execution of a scheduled query, and the IAM role the scheduled query uses to perform its operations.

You can create these scheduled queries after filling in the preceding options, [creating the target ](https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.create-table.html) (or derived) table, and executing the through the AWS CLI. For example, assume that a scheduled query definition is stored in a file, `scheduled_query_example.json`. You can create the query using the CLI command.

```
aws timestream-query create-scheduled-query --cli-input-json  file://scheduled_query_example.json --profile aws_profile --region us-east-1
```

In the preceding command, the profile passed using the --profile option must have the appropriate permissions to create scheduled queries. See [Identity-based policies for Scheduled Queries](https://docs.aws.amazon.com/timestream/latest/developerguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-sheduledqueries) for detailed instructions for the policies and permissions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
