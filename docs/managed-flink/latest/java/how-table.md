---
source_url: https://docs.aws.amazon.com/managed-flink/latest/java/how-table.html
---

# Review Table API components
<a name="how-table"></a>

Your Apache Flink application uses the [Apache Flink Table API](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/table/tableapi/) to interact with data in a stream using a relational model. You use the Table API to access data using Table sources, and then use Table functions to transform and filter table data. You can transform and filter tabular data using either API functions or SQL commands.

This section contains the following topics:
+ [Table API connectors](how-table-connectors.md): These components move data between your application and external data sources and destinations.
+ [Table API time attributes](how-table-timeattributes.md): This topic describes how Managed Service for Apache Flink tracks events when using the Table API.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed Service for Apache Flink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
