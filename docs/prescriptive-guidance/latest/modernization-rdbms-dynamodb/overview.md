---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-rdbms-dynamodb/overview.html
---

# DynamoDB overview
<a name="overview"></a>

Amazon DynamoDB is a NoSQL key-value and document database that provides fast and predictable performance with seamless scalability. It's a fully managed, multi-Region,  multi-active, and durable database. (The global table feature in DynamoDB synchronizes modifications made in one AWS Region to all other selected Regions automatically, to provide multi-active support.) DynamoDB has built-in security capabilities, backup and restore options, and in-memory caching for internet-scale applications.

The schemaless nature of NoSQL databases helps reduce the time and process required for pushing a database (read schema) change to production, thereby enabling rapid application development (RAD). NoSQL databases such as DynamoDB are built for high-performance read/write operations.

## Features and benefits
<a name="features"></a>

Amazon DynamoDB provides the following features and benefits:
+ No servers to manage – DynamoDB is a fully managed NoSQL database service, which means that it doesn't involve any  server maintenance overhead.
+ Schemaless – DynamoDB supports rapid application development and deployments.
+ Performance at scale – DynamoDB provides fast and predictable performance with seamless scalability.
+ ACID support – DynamoDB supports atomicity, consistency, isolation, and durability (ACID) transactions, to help you maintain data correctness.
+ Highly availability and durability – Your data is stored on solid-state disks (SSDs) and is automatically replicated across multiple Availability Zones in an AWS Region, providing built-in high availability and data durability.
+ Automatic scaling – DynamoDB uses the AWS Application Auto Scaling service to dynamically adjust provisioned throughput capacity in response to traffic patterns.
+ Flexible pricing options – DynamoDB provides two capacity modes with specific billing options: on-demand capacity mode and provisioned capacity mode.
+ Point-in-time recovery – You can enable continuous backups using point-in-time recovery to help protect your tables from accidental write or delete operations, and restore your tables to any point in time during the last 35 days.
+ Time to Live (TTL) – You can automatically delete items from a DynamoDB table after a specified duration.
+ Global tables – You can deploy multiple replicas across AWS Regions without having to build your own replication solution.
+ Global secondary indexes – You can query your DynamoDB table by using partition and sort keys that are different from the table's own partition and sort keys.
+ DAX – The DynamoDB Accelerator (DAX) caching service provides sub-millisecond response times for read operations.
+ DynamoDB Streams – This feature provides a time-ordered sequence of item-level modifications in a log to support real-time tracking and notification of changes in DynamoDB tables.

For more information about these benefits, see [Amazon DynamoDB Features](https://aws.amazon.com/dynamodb/features/) on the AWS website. The following sections discuss some of the features that are relevant to modernizing your database workloads by migrating from an RDBMS to DynamoDB.

### Partition keys
<a name="partition-keys.9b4b1ce6-a125-5045-ba73-33fbc50d038f"></a>

DynamoDB is schemaless, so it's not necessary to define all attributes for a table. The partition key attribute is required, and the sort key is optional. The rest of the attributes are arbitrary and can vary per item. We recommend that you choose a partition key with high cardinality so that frequently accessed items don't reside on the same partition. This practice helps you avoid data access imbalances and hot partitions. For more information, see [Best practices for designing and using partition keys effectively](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html) in the DynamoDB documentation.

### Indexes
<a name="indexes.bb308ee7-cb90-5cef-9f45-d7fc4053c15d"></a>

Indexes give you access to alternate query patterns and can speed up queries. You should create indexes carefully, regardless of whether you're using a relational database or DynamoDB. Whenever a write operation occurs on a table, all the indexes for that table must be updated.

A global secondary index contains a selection of attributes from the base table, but they are organized by a primary key that is different from the table's own primary key. In DynamoDB, global secondary indexes are sparse by default. That is, the sort key is optional and doesn't appear in every table item. To take advantage of this feature, you can create global secondary indexes that store and project only the required attributes. You can have up to 20 global secondary indexes on a DynamoDB table. For more information about this feature, see [Using global secondary indexes in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html) in the DynamoDB documentation.

### Time to Live
<a name="time-to-live.66869e21-4c77-5dcc-ab5e-4b31df10bc7a"></a>

You can set a Time to Live (TTL) property on a DynamoDB table to define a per-item (record) timestamp to specify when an item is no longer needed. Shortly after the specified timestamp, DynamoDB deletes the item from the table without consuming any additional capacity units. For more information about this feature, see [Expiring items by using DynamoDB Time to Live](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html) in the DynamoDB documentation.

### Pricing models
<a name="pricing-models.815556b2-2479-5aa2-b1b1-006852956689"></a>

DynamoDB offers two pricing models to choose from: provisioned capacity and on-demand capacity. Your choice of the pricing model depends on your projected workloads.

|  |  |  |  |
| --- |--- |--- |--- |
| Pricing model | Workload type | Cost | Read/write throughput |
| Provisioned capacity | Predictable | Lower | You specify the number of read/write operations per second in terms of read capacity units (RCUs) and write capacity units (WCUs). For example:For an item up to 4 KB in size, 1 RCU can perform 2 eventually consistent reads per second.For an item up to 1 KB in size, 1 WCU can perform 2 eventually consistent reads per second.<br />You can enable automatic scaling to adjust capacity in response to traffic changes. |
| On-demand capacity | Dynamic | Higher | You don't specify throughput requirements. DynamoDB accommodates your workloads automatically.<br />You're charged for the reads and writes that your application performs on your tables in terms of read request units and write request units. For example:An 8 KB item requires 1 read request unit for an eventually consistent read and 8 write request units for a non-transactional write operation. |

For more information about these two models, see [Read/write capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html) in the DynamoDB documentation.

### Transactions
<a name="transactions.a93d1949-853e-5b3c-b05f-ab33f052747c"></a>

DynamoDB supports atomicity, consistency, isolation, and durability (ACID) transactions across one or more tables within a single AWS account and AWS Region.

To manage changes to multiple items within and across tables, you can use the DynamoDB transactional TransactWriteItems and TransactGetItems APIs.
+ TransactWriteItems is a batch operation that contains a write set with one or more PutItem, UpdateItem, and DeleteItem actions. TransactWriteItems can optionally check for prerequisite conditions that must be satisfied before making updates. These conditions might involve the same items as those in the write set, or different items. If any condition isn't met, the transaction is rejected.
+ TransactGetItems is a batch operation that contains a read set with one or more GetItem actions. If you issue a TransactGetItems request on an item that is part of an active write transaction, the read transaction is canceled. To get the previously committed value, you can use a standard read operation.

For more information about these APIs, see [Amazon DynamoDB transactions: how it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transaction-apis.html) in the DynamoDB documentation.

**Limitations**

DynamoDB transactional API operations have the following constraints:
+ A transaction cannot update more than 100 unique items.
+ A transaction cannot contain more than 4 MB of data.
+ No two actions in a transaction can work against the same item in the same table. For example, you cannot run both ConditionCheck and Update actions on the same item in one transaction.
+ A transaction cannot operate on tables in more than one AWS account or Region.
+ Transactional operations provide ACID guarantees only within the AWS Region where the write operation originally takes place. Transactions are not supported across Regions in global tables.
+ The object persistence model doesn't support transactions. To use the transaction feature, you must access the database and tables using the [DynamoDB low-level API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.LowLevelAPI.html).

### Large components
<a name="large-components.18f99c2e-82e0-53db-a012-9837cfc6e311"></a>

DynamoDB has a size limit of 400 KB for each item. This limit includes both attribute name (binary length with UTF-8 encoding) and attribute value (again binary length). The attribute name counts toward the size limit. For example, consider an item that has two attributes: one attribute named "country-code" with value "IN" and another attribute named "country-phone-prefix" with value "91". The total size of that item is 36 bytes.

**Workaround:**

If an item is associated with many attributes and properties, or a large amount of data, its size might exceed 400 KB. In this case, you can store the serialized item in Amazon Simple Storage Service (Amazon S3) in JSON format, and save the Amazon S3 location as an attribute (S3Location) in the item. Read and write operations for that item fetch the S3 object and update the JSON string. The primary key, sort key, and all attributes used by local indexes and global secondary indexes should be stored in the table along with the S3Location attribute. This requires additional logic in the application (data access layer) to check for the S3Location attribute and to fetch the complete item data from Amazon S3.

### Backup and restore
<a name="backup-and-restore.5f09f785-cd21-5843-8706-c7f63e6650e4"></a>

Backup and restore support is a common feature expectation in any database. DynamoDB natively supports backup and restore within the same account, but you can perform table copy across multiple accounts by using other options or processes. These processes do not consume any read/write capacity units. For more information, see the guide [Cross-account full table copy options for Amazon DynamoDB](https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-full-table-copy-options/welcome.html) on the AWS Prescriptive Guidance website.

**Limitations**

DynamoDB currently supports cross-account backup and restore using AWS Backup, but the account has to be part of the same organization. You can address this limitation by adopting one of the following solutions:
+ Custom implementation in a programming language of your choice (for example, .NET, Java, or Python) by using an [AWS SDK](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.html). You can scan items from the source table in account A and write items (BatchWrite) to a table in account B. You can run this code on the server, on an on-premises computer, or in AWS Lambda (if the database is small and is the script takes less than 15 minutes to run). For more information, see the pattern [Copy Amazon DynamoDB tables across accounts using a custom implementation](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-amazon-dynamodb-tables-across-accounts-using-a-custom-implementation.html) on the AWS Prescriptive Guidance website.
+ Using AWS Glue. For information about this option, see the guide [Cross-account full table copy options for Amazon DynamoDB](https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-full-table-copy-options/welcome.html) on the AWS Prescriptive Guidance website.

## Language and SDK support
<a name="language-sdk"></a>

The [AWS SDKs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.html) provide a simplified programming interface to AWS services and support for .NET, Java, JavaScript, Node.js, Python, PHP, and Ruby.

You can choose from three patterns to access DynamoDB tables by using an AWS SDK: object persistence model (high-level interface), document interfaces, and low-level interfaces. For detailed information, see [Access patterns](access-patterns.md) later in this guide.
