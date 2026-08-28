---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/best-practices.html
---

# Best practices
<a name="best-practices"></a>

Consider using the following DynamoDB design best practices:
+ [Partition key design](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-uniform-load.html) – Use a high-cardinality partition key to distribute load evenly.
+ [Adjacency list design pattern](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-adjacency-graphs.html) – Use this design pattern for managing one-to-many and many-to-many relationships.
+ [Sparse index](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes-general-sparse-indexes.html) – Use sparse index for your global secondary indexes (GSIs). When you create a GSI, you specify a partition key and optionally a sort key. Only items in the base table that contain a corresponding GSI partition key appear in the sparse index. This helps to keep GSIs smaller.
+ [Index overloading](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-gsi-overloading.html) – Use the same GSI for indexing various types of items.
+ [GSI write sharding](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes-gsi-sharding.html) – Shard wisely to distribute data across the partitions for efficient and faster queries.
+ [Large items](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-use-s3-too.html) – Store only metadata inside the table, save the blob in Amazon S3, and keep the reference in DynamoDB. Break large items into multiple items, and efficiently index by using sort keys.

For more design best practices, see the [Amazon DynamoDB documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
