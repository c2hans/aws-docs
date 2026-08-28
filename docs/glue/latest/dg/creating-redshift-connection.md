---
source_url: https://docs.aws.amazon.com/glue/latest/dg/creating-redshift-connection.html
---

# Creating an Amazon Redshift connection
<a name="creating-redshift-connection"></a>

## Permissions needed
<a name="creating-redshift-connection-permissions"></a>

 Additional permissions are need to use Amazon Redshift clusters and Amazon Redshift serverless environments. For more information on how to add permissions to ETL jobs, see [Review IAM permissions needed for ETL jobs](https://docs.aws.amazon.com/glue/latest/ug/setting-up.html#getting-started-min-privs-job).
+  redshift:DescribeClusters
+  redshift-serverless:ListWorkgroups
+  redshift-serverless:ListNamespaces

## Overview
<a name="w2aac25c29c13c11b5"></a>

 When adding an Amazon Redshift connection, you can choose an existing Amazon Redshift connection or create a new connection when adding a **Data source - Redshift** node in AWS Glue Studio.

 AWS Glue supports both Amazon Redshift clusters and Amazon Redshift serverless environments. When you create a connection, Amazon Redshift serverless environments display the **serverless** label next to the connection option.

 For more information on how to create a Amazon Redshift connection, see [ Moving data to and from Amazon Redshift](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-redshift.html#aws-glue-programming-etl-redshift-using).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
