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
