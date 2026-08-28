---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/java-using.html
---

# Using the DynamoDB Encryption Client for Java
<a name="java-using"></a>

**Note**
Our client-side encryption library was [renamed to AWS Database Encryption SDK](DDBEC-rename.md). The following topic provides information on versions 1.*x*—2.*x* of the DynamoDB Encryption Client for Java and versions 1.*x*—3.*x* of the DynamoDB Encryption Client for Python. For more information, see [AWS Database Encryption SDK for DynamoDB version support](legacy-dynamodb-encryption-client.md#legacy-support).

This topic explains some of the features of the DynamoDB Encryption Client in Java that might not be found in other programming language implementations.

For details about programming with the DynamoDB Encryption Client, see the [Java examples](java-examples.md), the [examples](https://github.com/aws/aws-dynamodb-encryption-java/tree/master/examples) in the `aws-dynamodb-encryption-java repository` on GitHub, and the [Javadoc](https://aws.github.io/aws-database-encryption-sdk-dynamodb/) for the DynamoDB Encryption Client.

**Topics**
+ [Item encryptors](#ddbec-item-encryptor)
+ [Attribute actions in Java](#attribute-actions-java)
+ [Overriding table names](#override-table-name)

## Item encryptors: DynamoDBEncryptor
<a name="ddbec-item-encryptor"></a>

The DynamoDB Encryption Client in Java has one [item encryptor](DDBEC-legacy-concepts.md#item-encryptor): the lower-level [DynamoDBEncryptor](https://aws.github.io/aws-database-encryption-sdk-dynamodb/com/amazonaws/services/dynamodbv2/datamodeling/sdkv2/encryption/DynamoDBEncryptor.html)

## Attribute actions in Java
<a name="attribute-actions-java"></a>

[Attribute actions](DDBEC-legacy-concepts.md#legacy-attribute-actions) determine which attribute values are encrypted and signed, which are only signed, and which are ignored.

**Important**
After you use your attribute actions to encrypt your table items, adding or removing attributes from your data model might cause a signature validation error that prevents you from decrypting your data. For a detailed explanation, see [Changing your data model](data-model.md).

### Attribute actions for the DynamoDBEncryptor
<a name="attribute-action-default"></a>

To specify attribute actions when you use the [DynamoDBEncryptor](https://aws.github.io/aws-database-encryption-sdk-dynamodb/com/amazonaws/services/dynamodbv2/datamodeling/sdkv2/encryption/DynamoDBEncryptor.html) directly, create a `HashMap` object in which the name-value pairs represent attribute names and the specified actions.

The valid values are for the attribute actions are defined in the `EncryptionFlags` enumerated type. You can use `ENCRYPT` and `SIGN` together, use `SIGN` alone, or omit both. However, if you use `ENCRYPT` alone, the DynamoDB Encryption Client throws an error. You cannot encrypt an attribute that you don't sign.

```
ENCRYPT
SIGN
```

**Warning**
Do not encrypt the primary key attributes. They must remain in plaintext so DynamoDB can find the item without running a full table scan.

If you specify a primary key in the encryption context and then specify `ENCRYPT` in the attribute action for either primary key attribute, the DynamoDB Encryption Client throws an exception.

For example, the following Java code creates an `actions` HashMap that encrypts and signs all attributes in the `record` item. The exceptions are the partition key and sort key attributes, which are signed but not encrypted, and the `test` attribute, which is not signed or encrypted.

```
final EnumSet<EncryptionFlags> signOnly = EnumSet.of(EncryptionFlags.SIGN);
final EnumSet<EncryptionFlags> encryptAndSign = EnumSet.of(EncryptionFlags.ENCRYPT, EncryptionFlags.SIGN);
final Map<String, Set<EncryptionFlags>> actions = new HashMap<>();

for (final String attributeName : record.keySet()) {
  switch (attributeName) {
    case partitionKeyName: // no break; falls through to next case
    case sortKeyName:
      // Partition and sort keys must not be encrypted, but should be signed
      actions.put(attributeName, signOnly);
      break;
    case "test":
      // Don't encrypt or sign
      break;
    default:
      // Encrypt and sign everything else
      actions.put(attributeName, encryptAndSign);
      break;
  }
}
```

Then, when you call the [encryptRecord](https://aws.github.io/aws-database-encryption-sdk-dynamodb/com/amazonaws/services/dynamodbv2/datamodeling/sdkv2/encryption/DynamoDBEncryptor.html#encryptRecord-java.util.Map-java.util.Map-com.amazonaws.services.dynamodbv2.datamodeling.sdkv2.encryption.EncryptionContext-) method of the `DynamoDBEncryptor`, specify the map as the value of the `attributeFlags` parameter. For example, this call to `encryptRecord` uses the `actions` map.

```
// Encrypt the plaintext record
final Map<String, AttributeValue> encrypted_record = encryptor.encryptRecord(record, actions, encryptionContext);
```

## Overriding table names
<a name="override-table-name"></a>

In the DynamoDB Encryption Client, the name of the DynamoDB table is an element of the [DynamoDB encryption context](concepts.md#encryption-context) that is passed to the encryption and decryption methods. When you encrypt or sign table items, the DynamoDB encryption context, including the table name, is cryptographically bound to the ciphertext. If the DynamoDB encryption context that is passed to the decrypt method doesn't match the DynamoDB encryption context that was passed to the encrypt method, the decrypt operation fails.

Occasionally, the name of a table changes, such as when you back up a table or perform a [point-in-time recovery](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.html). When you decrypt or verify the signature of these items, you must pass in the same DynamoDB encryption context that was used to encrypt and sign the items, including the original table name. The current table name is not needed.

When you use the `DynamoDBEncryptor`, you assemble the DynamoDB encryption context manually. So, do not use the table name override operators if you are using the `DynamoDBEncryptor`. Instead, create an encryption context with the original table name and submit it to the decryption method.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
