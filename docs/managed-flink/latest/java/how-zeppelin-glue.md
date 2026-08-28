---
source_url: https://docs.aws.amazon.com/managed-flink/latest/java/how-zeppelin-glue.html
---

# Work with AWS Glue
<a name="how-zeppelin-glue"></a>

Your Studio notebook stores and gets information about its data sources and sinks from AWS Glue. When you create your Studio notebook, you specify the AWS Glue database that contains your connection information. When you access your data sources and sinks, you specify AWS Glue tables contained in the database. Your AWS Glue tables provide access to the AWS Glue connections that define the locations, schemas, and parameters of your data sources and destinations.

Studio notebooks use table properties to store application-specific data. For more information, see [Table properties](how-zeppelin-glue-properties.md).

For an example of how to set up a AWS Glue connection, database, and table for use with Studio notebooks, see [Create an AWS Glue database](example-notebook.md#example-notebook-glue) in the [Tutorial: Create a Studio notebook in Managed Service for Apache Flink](example-notebook.md) tutorial.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed Service for Apache Flink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
