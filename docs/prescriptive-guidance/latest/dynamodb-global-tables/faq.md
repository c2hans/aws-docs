---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-global-tables/faq.html
---

# FAQ
<a name="faq"></a>

This section answers frequently asked questions about DynamoDB global tables.

**What is the pricing for global tables?**
+ A write operation in a traditional DynamoDB table is priced in write capacity units (WCUs) for provisioned tables or write request units (WRUs) for on-demand tables. If you write a 5 KB item, it incurs a charge of 5 units. A write to a global table is priced in replicated write capacity Units (rWCUs) for provisioned tables or replicated write request units (rWRUs) for on-demand tables. rWCUs and rWRUs are priced the same as WCUs and WRUs.
+ rWCU and rWRU charges are incurred in every Region where the item is written directly or written through replication.
+ Cross-Region data transfer fees apply.
+ Writing to a global secondary index (GSI) is considered a local write operation and uses regular write units.
+ There is no reserved capacity available for rWCUs or rWRUs at this time. Purchasing reserved capacity for WCUs might still be beneficial for tables where GSIs consume write units.
+ When you add a new Region to a global table, DynamoDB bootstraps the new Region automatically and charges you as if it were a table restore, based on the GB size of the table. It also charges cross-Region data transfer fees.

**Which Regions do global tables support?**
+ Global tables (current, version 2019) support all AWS Regions for MREC tables and the following Region sets for MRSC tables:
  + US Region set: US East (N. Virginia), US East (Ohio), US West (Oregon)
  + EU Region set: Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt)
  + AP Region set: Asia Pacific (Tokyo), Asia Pacific (Seoul), and Asia Pacific (Osaka).

**How are GSIs handled with global tables?**
+ In global tables (current, version 2019), when you create a GSI in one Region, it's automatically created in other participating Regions and automatically backfilled.

**How do I stop the replication of a global table?**
+ You can delete a replica table the same way you would delete any other table. Deleting the global table stops replication to that Region and deletes the table copy kept in that Region. However, you cannot stop replication while keeping copies of the table as independent entities, nor can you pause replication.
+ An MRSC table must be deployed in exactly three Regions. To delete the replicas, you must delete all the replicas and the witness so that the MRSC table becomes a local table.

**How does DynamoDB Streams interact with global tables?**
+ Each global table produces an independent stream based on all its write operations, wherever they started from. You can choose to consume the DynamoDB stream in one Region or in all Regions (independently). If you want to process local but not replicated write operations, you can add your own `Regionattribute` to each item to identify the writing Region. You can then use a Lambda event filter to call the Lambda function only for write operations in the local Region. This helps with insert and update operations, but not delete operations.
+ Global tables that are configured for multi-Region eventual consistency (MREC tables) replicate changes by reading those changes from a [DynamoDB stream](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) on a replica table and applying that change to all other replica tables. Therefore, DynamoDB Streams is enabled by default on all replicas in an MREC global table and cannot be disabled on those replicas. The MREC replication process can combine multiple changes in a short period of time into a single replicated write operation. As a result, each replica's stream might contain slightly different records. DynamoDB Streams records on MREC replicas are always ordered on a per-item basis, but ordering between items might differ between replicas.
+ Global tables that are configured for multi-Region strong consistency (MRSC tables) don't use DynamoDB Streams for replication, so this feature isn't enabled by default on MRSC replicas. You can enable DynamoDB Streams on an MRSC replica. DynamoDB Streams records on MRSC replicas are identical for every replica and are always ordered on a per-item basis, but ordering between items might differ between replicas.

**How do global tables handle transactions?**
+ Transactional operations on MRSC tables will generate errors.
+ Transactional operations on MREC tables provide atomicity, consistency, isolation, durability (ACID) guarantees **only** within the Region where the write operation originally occurred. Transactions are not supported across Regions in global tables. For example, if you have an MREC global table with replicas in the US East (Ohio) and US West (Oregon) Regions and perform a `TransactWriteItems` operation in the US East (Ohio) Region, you might observe partially completed transactions in the US West (Oregon) Region as changes are replicated. Changes are replicated to other Regions only after they have been committed in the source Region.

**How do global tables interact with the DynamoDB Accelerator (DAX) cache?**
+ Global tables bypass DAX by updating DynamoDB directly, so DAX isn't aware that it's holding stale data. The DAX cache is refreshed only when the cache's TTL expires.

**Do tags on tables propagate?**
+ No, tags do not automatically propagate.

**Should I back up tables in all Regions or just one?**
+ The answer depends on the purpose of the backup.
  + If you want to ensure data durability, DynamoDB already provides that safeguard. The service ensures durability.
  + If you want to keep a snapshot for historical records (for example, to meet regulatory requirements), backing up in one Region should suffice. You can copy the backup to additional Regions by using [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html).
  + If you want to recover erroneously deleted or modified data, use [DynamoDB point-in-time recovery (PITR)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery_Howitworks.html) in one Region.

**How do I deploy global tables by using **AWS CloudFormation**?**
+ CloudFormation represents a DynamoDB table and a global table as two separate resources: `AWS::DynamoDB::Table` and  `AWS::DynamoDB::GlobalTable`. One approach is to create all tables that can potentially be global by using the `GlobalTable` construct, keep them as standalone tables initially, and add Regions later, if necessary.
+ In CloudFormation, each global table is controlled by a single stack, in a single Region, regardless of the number of replicas. When you deploy your template, CloudFormation creates and updates all replicas as part of a single stack operation. You should not deploy the same [AWS::DynamoDB::GlobalTable ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html)resource in multiple Regions. This will result in errors and is unsupported. If you deploy your application template in multiple Regions, you can use conditions to create the `AWS::DynamoDB::GlobalTable` resource in a single Region. Alternatively, you can choose to define your `AWS::DynamoDB::GlobalTable` resources in a stack that's separate from your application stack, and make sure that it's deployed to a single Region.
+ If you have a regular table and you want to convert it to a global table while keeping it managed by CloudFormation: Set the [deletion policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html) to **Retain**, remove the table from the stack, convert the table to a global table in the console, and then import the global table as a new resource to the stack. For more information, see the GitHub repository [amazon-dynamodb-table-to-global-table-cdk](https://github.com/aws-samples/amazon-dynamodb-table-to-global-table-cdk).
+ Cross-account replication is not supported at this time.
