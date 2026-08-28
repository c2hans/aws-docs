---
source_url: https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-vertica.html
---

# Connecting to Vertica in AWS Glue Studio
<a name="connecting-to-data-vertica"></a>

 AWS Glue provides built-in support for Vertica. AWS Glue Studio provides a visual interface to connect to Vertica, author data integration jobs, and run them on the AWS Glue Studio serverless Spark runtime.

 AWS Glue Studio creates a unified connection for Vertica. For more information, see [Considerations](using-connectors-unified-connections.md#using-connectors-unified-connections-considerations).

**Topics**
+ [Creating a Vertica connection](creating-vertica-connection.md)
+ [Creating a Vertica source node](creating-vertica-source-node.md)
+ [Creating a Vertica target node](creating-vertica-target-node.md)
+ [Advanced options](#creating-vertica-connection-advanced-options)

## Advanced options
<a name="creating-vertica-connection-advanced-options"></a>

You can provide advanced options when creating a Vertica node. These options are the same as those available when programming AWS Glue for Spark scripts.

See [Vertica connections](aws-glue-programming-etl-connect-vertica-home.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
