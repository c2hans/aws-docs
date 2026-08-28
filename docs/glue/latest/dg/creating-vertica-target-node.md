---
source_url: https://docs.aws.amazon.com/glue/latest/dg/creating-vertica-target-node.html
---

# Creating a Vertica target node
<a name="creating-vertica-target-node"></a>

## Prerequisites needed
<a name="creating-vertica-target-node-prerequisites"></a>
+ A Vertica type AWS Glue Data Catalog connection, {{connectionName}} and a temporary Amazon S3 location, {{tempS3Path}}, as described in the previous section, [Creating a Vertica connection](creating-vertica-connection.md).

## Adding a Vertica data target
<a name="creating-vertica-target-node-add"></a>

**To add a **Data target – Vertica** node:**

1.  Choose the connection for your Vertica data source. Since you have created it, it should be available in the dropdown. If you need to create a connection, choose **Create Vertica connection**. For more information see the previous section, [Creating a Vertica connection](creating-vertica-connection.md).

    Once you have chosen a connection, you can view the connection properties by clicking **View properties**.

1. Choose the **Database** containing your table.

1. Choose the **Staging area in Amazon S3**, enter an S3A URI to {{tempS3Path}}.

1. Enter {{tableName}} and optionally select a **Schema**.

1.  In **Custom Vertica properties**, enter parameters and values as needed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
