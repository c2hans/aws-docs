---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/client-server-side.html
---

# Client-side and server-side encryption
<a name="client-server-side"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

The AWS Database Encryption SDK for DynamoDB supports *client-side encryption*, where you encrypt your table data before you send it to your database. However, DynamoDB provides a server-side *encryption at rest* feature that transparently encrypts your table when it is persisted to disk and decrypts it when you access the table.

The tools that you choose depend on the sensitivity of your data and the security requirements of your application. You can use both the AWS Database Encryption SDK for DynamoDB and encryption at rest. When you send encrypted and signed items to DynamoDB, DynamoDB doesn't recognize the items as being protected. It just detects typical table items with binary attribute values.

**Server-side encryption at rest**

DynamoDB supports [encryption at rest](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EncryptionAtRest.html), a *server-side encryption* feature in which DynamoDB transparently encrypts your tables for you when the table is persisted to disk, and decrypts them when you access the table data.

When you use an AWS SDK to interact with DynamoDB, by default, your data is encrypted in transit over an HTTPS connection, decrypted at the DynamoDB endpoint, and then re-encrypted before being stored in DynamoDB.
+ **Encryption by default.** DynamoDB transparently encrypts and decrypts all tables when they are written. There is no option to enable or disable encryption at rest.
+ **DynamoDB creates and manages the cryptographic keys. **The unique key for each table is protected by an [AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys) that never leaves [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/) (AWS KMS) unencrypted. By default, DynamoDB uses an [AWS owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) in the DynamoDB service account, but you can choose an [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) or [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) in your account to protect some or all of your tables.
+ **All table data is encrypted on disk. **When an encrypted table is saved to disk, DynamoDB encrypts all table data, including the [primary key](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey) and local and global [secondary indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.SecondaryIndexes). If your table has a sort key, some of the sort keys that mark range boundaries are stored in plaintext in the table metadata.
+ **Objects related to tables are encrypted, too.** Encryption at rest protects [DynamoDB streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html), [global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html), and [backups](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.html) whenever they are written to durable media.
+ **Your items are decrypted when you access them. **When you access the table, DynamoDB decrypts the part of the table that includes your target item, and returns the plaintext item to you.

**AWS Database Encryption SDK for DynamoDB**

Client-side encryption provides end-to-end protection for your data, in transit and at rest, from its source to storage in DynamoDB. Your plaintext data is never exposed to any third party, including AWS. You can use the AWS Database Encryption SDK for DynamoDB with new DynamoDB tables, or you can migrate your existing Amazon DynamoDB tables to the latest version of the AWS Database Encryption SDK for DynamoDB.
+ **Your data is protected in transit and at rest.** It is never exposed to any third party, including AWS.
+ **You can sign your table Items.** You can direct the AWS Database Encryption SDK for DynamoDB to calculate a signature over all or part of a table item, including the primary key attributes. This signature allows you to detect unauthorized changes to the item as a whole, including adding or deleting attributes, or swapping attribute values.
+ **You determine how your data is protected **by [selecting a keyring](keyrings.md). Your keyring determines the wrapping keys that protect your data keys, and ultimately, your data. Use the most secure wrapping keys that are practical for your task.
+ **The AWS Database Encryption SDK for DynamoDB doesn't encrypt the entire table.** You choose which attributes are encrypted in your items. The AWS Database Encryption SDK for DynamoDB does not encrypt an entire item. It does not encrypt attribute names, or the names or values of the primary key (partition key and sort key) attributes.

**AWS Encryption SDK**

If you are encrypting data that you store in DynamoDB, we recommend the AWS Database Encryption SDK for DynamoDB.

The [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/) is a client-side encryption library that helps you to encrypt and decrypt generic data. Although it can protect any type of data, it isn't designed to work with structured data, like database records. Unlike the AWS Database Encryption SDK for DynamoDB, the AWS Encryption SDK cannot provide item-level integrity checking and it has no logic to recognize attributes or prevent encryption of primary keys.

If you use the AWS Encryption SDK to encrypt any element of your table, remember that it isn't compatible with the AWS Database Encryption SDK for DynamoDB. You cannot encrypt with one library and decrypt with the other.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
