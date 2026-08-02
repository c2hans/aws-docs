---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/DDBEC-rename.html
---

# Amazon DynamoDB Encryption Client rename
<a name="DDBEC-rename"></a>

****

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

On June 9, 2023, our client-side encryption library was renamed to AWS Database Encryption SDK. The AWS Database Encryption SDK is compatible with Amazon DynamoDB. It can decrypt and read items encrypted by the legacy DynamoDB Encryption Client. For more information on the legacy DynamoDB Encryption Client versions, see [AWS Database Encryption SDK for DynamoDB version support](legacy-dynamodb-encryption-client.md#legacy-support).

The AWS Database Encryption SDK provides version 3.*x* and later of the Java client-side encryption library for DynamoDB. Version 3.*x* is a major rewrite of the DynamoDB Encryption Client for Java. It includes many updates, such as a new structured data format, improved multitenancy support, seamless schema changes, and searchable encryption support.

To learn more about the new features introduced with the AWS Database Encryption SDK, see the following topics.

**[Searchable encryption](searchable-encryption.md)**
You can design databases that can search encrypted records without decrypting the entire database. Depending on your threat model and query requirements, you can use searchable encryption to perform exact match searches or more customized complex queries on your encrypted records.

**[Keyrings](keyrings.md)**
The AWS Database Encryption SDK uses *keyrings* to perform [envelope encryption](concepts.md#envelope-encryption). Keyrings generate, encrypt, and decrypt the data keys that protect your records. The AWS Database Encryption SDK supports AWS KMS keyrings that use symmetric encryption or asymmetric RSA [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys) to protect your data keys, and AWS KMS Hierarchical keyrings that enable you to protect your cryptographic materials under a symmetric encryption KMS key without calling AWS KMS every time you encrypt or decrypt a record. You can also specify your own key material with Raw AES keyrings and Raw RSA keyrings.

**[Seamless schema changes](ddb-update-data-model.md)**
When you configure the AWS Database Encryption SDK, you provide [cryptographic actions](concepts.md#crypt-actions) that tell the client which fields to encrypt and sign, which fields to sign (but not encrypt), and which to ignore. After you have used the AWS Database Encryption SDK to protect your records, you can still make changes to your data model. You can update your cryptographic actions, such as adding or removing encrypted fields, in a single deployment.

**[Configure existing DynamoDB tables for client-side encryption](ddb-java-config-existing-table.md)**
Legacy versions of the DynamoDB Encryption Client were designed to be implemented in new, unpopulated tables. With the AWS Database Encryption SDK for DynamoDB, you can migrate your existing Amazon DynamoDB tables to version 3.*x* or 4.*x* of the Java client-side encryption library for DynamoDB.
