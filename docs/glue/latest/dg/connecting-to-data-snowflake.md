---
source_url: https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-snowflake.html
---

# Connecting to Snowflake in AWS Glue Studio
<a name="connecting-to-data-snowflake"></a>

**Note**
 You can use AWS Glue for Spark to read from and write to tables in Snowflake in AWS Glue 4.0 and later versions. To configure a Snowflake connection with AWS Glue jobs programatically, see [Redshift connections](aws-glue-programming-etl-connect-redshift-home.md).

 AWS Glue provides built-in support for Snowflake. AWS Glue Studio provides a visual interface to connect to Snowflake, author data integration jobs, and run them on the AWS Glue Studio serverless Spark runtime.

 AWS Glue Studio creates a unified connection for Snowflake. For more information, see [Considerations](using-connectors-unified-connections.md#using-connectors-unified-connections-considerations).

**Topics**
+ [Creating a Snowflake connection](creating-snowflake-connection.md)
+ [Creating a Snowflake source node](creating-snowflake-source-node.md)
+ [Creating a Snowflake target node](creating-snowflake-target-node.md)
+ [Set up the Authorization Code flow for Snowflake](snowflake-setup-authorization-code-flow.md)
+ [Advanced options](#creating-snowflake-connection-advanced-options)

## Advanced options
<a name="creating-snowflake-connection-advanced-options"></a>

See [ Snowflake connections ](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-snowflake-home.html) in the AWS Glue developer guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
