---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/dynamodb-encryption-client.html
---

# AWS Database Encryption SDK for DynamoDB
<a name="dynamodb-encryption-client"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

The AWS Database Encryption SDK for DynamoDB is a software library that enables you to include client-side encryption in your [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) design. The AWS Database Encryption SDK for DynamoDB provides attribute-level encryption and enables you to specify which items to encrypt and which items to include in the signatures that ensure the authenticity of your data. Encrypting your sensitive data in transit and at rest helps ensure that your plaintext data isn’t available to any third party, including AWS.

**Note**
The AWS Database Encryption SDK does not support PartiQL.

In DynamoDB, a [table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.TablesItemsAttributes) is a collection of items. Each *item* is a collection of *attributes*. Each attribute has a name and a value. The AWS Database Encryption SDK for DynamoDB encrypts the values of attributes. Then, it calculates a signature over the attributes. You specify which attribute values to encrypt and which to include in the signature in the [cryptographic actions](concepts.md#crypt-actions).

The topics in this chapter provide an overview of the AWS Database Encryption SDK for DynamoDB, including which fields are encrypted, guidance on client installation and configuration, and Java examples to help you get started.

**Topics**
+ [Client-side and server-side encryption](client-server-side.md)
+ [Which fields are encrypted and signed?](DDB-encrypted-and-signed.md)
+ [Searchable encryption in DynamoDB](ddb-searchable-encryption.md)
+ [Updating your data model](ddb-update-data-model.md)
+ [AWS Database Encryption SDK for DynamoDB available programming languages](ddb-programming-languages.md)
+ [Legacy DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md)
