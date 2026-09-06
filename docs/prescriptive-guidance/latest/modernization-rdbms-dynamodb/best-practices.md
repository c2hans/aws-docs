---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-rdbms-dynamodb/best-practices.html
---

# Best practices
<a name="best-practices"></a>

This section summarizes recommendations in addition to the best practices discussed in previous sections (such as storing items that are greater than 400 KB in Amazon S3, using indexes, single table design, and transactions).

## Use the object persistence access pattern
<a name="use-the-object-persistence-access-pattern.3662650c-34e7-5f0f-b691-2e41c85748b5"></a>

As discussed earlier in this guide, DynamoDB provides three access patterns. The [object persistence interface](access-patterns.md#object-persistence-interface) provides clean and easy-to-maintain code. Unless you have to customize or transform model property values during read/write operations, we recommend that you use the object persistence interface.

## Choose the correct capacity provisioning mode
<a name="choose-the-correct-capacity-provisioning-mode.a80f717d-b99f-5b2e-8b01-32a66fbe5ba1"></a>

On-demand capacity provisioning automatically scales read and write operations as your workloads ramp up and down. We recommend that you use this mode if your workload is unpredictable. The cost is usually higher than provisioned capacity mode, and is charged on a pay-as-you-use basis. We recommend that you use provisioned capacity mode when your workload is predictable and you can forecast your capacity requirements. For more information, see the [Pricing models](overview.md#features) section earlier in this guide.

## Use caching
<a name="use-caching.5dead247-ec69-5fb1-9056-3c9443c86da8"></a>

We recommend that you use caching when working with DynamoDB to reduce the cost associated with each read/write operation. Use the appropriate invalidation logic to remove items from the cache when cached data becomes stale. Identify the most frequently used endpoints to implement caching.

## Run queries instead of scans
<a name="run-queries-instead-of-scans.772bf30c-d51c-582c-a791-4979c9ccbee9"></a>

Avoid DynamoDB scans as much as possible. A DynamoDB query is more efficient and less costly than a scan operation. A query filters items based on partition key (PK) and sort key (SK) values, whereas a scan has to read all records to filter items based on the specified parameters. DynamoDB pricing is based on the volume of data read/write operations, so scans incur more cost than queries. Queries are also faster, which ultimately improves the performance of the application.

## Validate data integrity
<a name="validate-data-integrity.8a4414af-a70f-5f52-9f4f-32b2757d7f8d"></a>

DynamoDB is a NoSQL database, so it doesn't maintain relationship data or include data integrity constraints. It requires each item to have a unique combination of a primary key and sort key only.  To ensure data integrity between related items in DynamoDB table, we recommend that you perform strict validations in the application or business layer of your system.
