---
source_url: https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-bigquery.html
---

# Connecting to Google BigQuery in AWS Glue Studio
<a name="connecting-to-data-bigquery"></a>

**Note**
  You can use AWS Glue for Spark to read from and write to tables in Google BigQuery in AWS Glue 4.0 and later versions. To configure Google BigQuery with AWS Glue jobs programmatically, see  [BigQuery connections](aws-glue-programming-etl-connect-bigquery-home.md).

 AWS Glue Studio provides a visual interface to connect to BigQuery, author data integration jobs, and run them on the AWS Glue Studio serverless Spark runtime.

 When creating a connection to Google BigQuery in AWS Glue Studio, a unified connection is created. For more information, see [Considerations](using-connectors-unified-connections.md#using-connectors-unified-connections-considerations).

 Instead of creating a secret with the credentials in a specific format, `{"credentials": "base64 encoded JSON"}`, now with unified connection to Google BigQuery, you can create a secret which directly includes the JSON from Goolge BigQuery: `{"type": "service-account", ...}`.

**Topics**
+ [Creating a BigQuery connection](creating-bigquery-connection.md)
+ [Creating a BigQuery source node](creating-bigquery-source-node.md)
+ [Creating a BigQuery target node](creating-bigquery-target-node.md)
+ [Advanced options](#creating-bigquery-connection-advanced-options)

## Advanced options
<a name="creating-bigquery-connection-advanced-options"></a>

You can provide advanced options when creating a BigQuery node. These options are the same as those available when programming AWS Glue for Spark scripts.

See [ BigQuery connection option reference ](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-bigquery-home.html) in the AWS Glue developer guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
