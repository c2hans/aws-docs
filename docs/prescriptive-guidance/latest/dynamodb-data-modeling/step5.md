---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step5.html
---

# Step 5. Create the DynamoDB data model
<a name="step5"></a>

## Objective
<a name="obj5"></a>
+ Create the DynamoDB data model.

## Process
<a name="proc5"></a>
+ Database engineer identifies how many tables will be required for each use case. We recommend maintaining as few tables as possible in a DynamoDB application.
+ Based on the most common access patterns, identify the primary key, which can be one of two types: a primary key with a partition key that identifies data, or a primary key with a partition key and a sort key. A sort key is a secondary key for grouping and organizing data so it can be queried within a partition efficiently. You can use sort keys to define hierarchical relationships in your data that you can query at any level of the hierarchy (see [blog post](https://aws.amazon.com/blogs/database/choosing-the-right-dynamodb-partition-key/)).
+ Partition key design:
  + Define the partition key and evaluate its distribution.
  + Identify the need for [write sharding](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-sharding.html) to distribute workloads evenly.
+ Sort key design:
  + Identify the sort key.
  + Identify the need for a composite sort key.
  + Identify the need for version control.
+ Based on the access patterns, identify the secondary indexes to satisfy the query requirements.
  + Identify the need for [local secondary indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LSI.html) (LSIs). These are indexes that have the same partition key as the base table, but a different sort key.
    + For tables with LSIs, there is a 10 GB size limit per partition key value. A table with LSIs can store any number of items, as long as the total size for any one partition key value does not exceed 10 GB.
  + Identify the need for [global secondary indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html) (GSIs). These are indexes that have a partition key and a sort key that can be different from those on the base table (see [blog post](https://aws.amazon.com/blogs/database/how-to-design-amazon-dynamodb-global-secondary-indexes/)).
  + Define the index projections. Consider projecting fewer attributes to minimize the size of items written to the index. In this step, you should determine whether you want to use the following:
    + [Sparse indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes-general-sparse-indexes.html)
    + [Materialized aggregation queries](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-gsi-aggregation.html)
    + [GSI overloading](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-gsi-overloading.html)
    + [GSI sharding](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes-gsi-sharding.html)
    + [An eventually consistent replica using GSI](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes-gsi-replica.html)
+ Database engineer determines whether the data will include large items. If so, they design the solution [by using compression or by storing data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-use-s3-too.html) in Amazon Simple Storage Service (Amazon S3).
+ Database engineer determines whether time series data will be needed. If so, they use the [time series design pattern](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-time-series.html) to model the data.
+ Database engineer determines whether the ER model includes many-to-many relationships. If so, they use an [adjacency list design pattern](https://docs.aws.amazon.com/amazondynamodb/latest/developrguide/bp-adjacency-graphs.html) to model the data.

## Tools and resources
<a name="tools5"></a>
+ [NoSQL Workbench for Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.settingup.html)  ─ Provides data modeling, data visualization, and query development and testing features to help you design your DynamoDB database
+ [NoSQL design for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-general-nosql-design.html) (DynamoDB documentation)
+ [Choosing the Right DynamoDB Partition Key](https://aws.amazon.com/blogs/database/choosing-the-right-dynamodb-partition-key/) (AWS Database blog)
+ [Best practices for using secondary indexes in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes.html) (DynamoDB documentation)
+ [How to design Amazon DynamoDB global secondary indexes](https://aws.amazon.com/blogs/database/how-to-design-amazon-dynamodb-global-secondary-indexes/) (AWS Database blog)

## RACI
<a name="raci5"></a>

|
|
| Business user | Business analyst | Solutions architect | Database engineer | Application developer | DevOps engineer |
| --- |--- |--- |--- |--- |--- |
| I | I | I | R/A |   |   |

## Outputs
<a name="outputs5"></a>
+ DynamoDB table schema that satisfies your access patterns and requirements

## Example
<a name="sample5"></a>

The following screenshot shows NoSQL Workbench.

![Screenshot showing NoSQL Workbench.](http://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/images/guide-img/225c2600-95f1-4c8c-9e23-419bc7ae3c55/images/47f3a9c6-75f6-4d92-a2c9-a5af8e87cbc1.jpeg)
