---
source_url: https://docs.aws.amazon.com/glue/latest/dg/creating-azuresql-target-node.html
---

# Creating a Azure SQL target node
<a name="creating-azuresql-target-node"></a>

## Prerequisites needed
<a name="creating-azuresql-target-node-prerequisites"></a>
+ A AWS Glue Azure SQL connection, configured with an AWS Secrets Manager secret, as described in the previous section, [Creating a Azure SQL connection](creating-azuresql-connection.md).
+ Appropriate permissions on your job to read the secret used by the connection.
+ A Azure SQL table you would like to write to, {{tableName}}.

  An Azure SQL table is identified by its database, schema and table name. You must provide the database name and table name when connecting to Azure SQL. You also must provide the schema if it is not the default, "public". Database is provided through a URL property in {{connectionName}} , schema and table name through the `dbtable`.

## Adding a Azure SQL data target
<a name="creating-azuresql-target-node-add"></a>

**To add a **Data target – Azure SQL** node:**

1.  Choose the connection for your Azure SQL data source. Since you have created it, it should be available in the dropdown. If you need to create a connection, choose **Create Azure SQL connection**. For more information see the previous section, [Creating a Azure SQL connection](creating-azuresql-connection.md).

    Once you have chosen a connection, you can view the connection properties by clicking **View properties**.

1. Configure **Table name** by providing {{tableName}}.

1.  In **Custom Azure SQL properties**, enter parameters and values as needed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
