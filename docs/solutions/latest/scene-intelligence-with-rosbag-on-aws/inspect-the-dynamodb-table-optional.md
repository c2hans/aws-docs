---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/inspect-the-dynamodb-table-optional.html
---

# Inspect the DynamoDB table (optional)
<a name="inspect-the-dynamodb-table-optional"></a>

After the DAG completes, the solution writes the application of the Spark code (business logic) to a DynamoDB table, and then forwards it OpenSearch Service.

Complete the following steps to inspect the DynamoDB table.

1. Sign in to the [Amazon DynamoDB console](https://console.aws.amazon.com/dynamodb).

1. Choose **Tables** from the navigation menu.

1. Select the `addf-aws-solutions-core-metadata-storage-Rosbag-Scene-Metadata` table to see the output.

    **Example DynamoDB table displaying extracted rosbag data.**
![addf aws solutions core metadata storage rosbag scene metadata](http://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/images/addf-aws-solutions-core-metadata-storage-rosbag-scene-metadata.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Scene Intelligence with Rosbag on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
