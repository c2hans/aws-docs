---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/java-examples.html
---

# Example code for the DynamoDB Encryption Client for Java
<a name="java-examples"></a>

**Note**
Our client-side encryption library was [renamed to AWS Database Encryption SDK](DDBEC-rename.md). The following topic provides information on versions 1.*x*—2.*x* of the DynamoDB Encryption Client for Java and versions 1.*x*—3.*x* of the DynamoDB Encryption Client for Python. For more information, see [AWS Database Encryption SDK for DynamoDB version support](legacy-dynamodb-encryption-client.md#legacy-support).

The following examples show you how to use the DynamoDB Encryption Client for Java to protect DynamoDB table items in your application. You can find more examples (and contribute your own) in the [examples](https://github.com/aws/aws-database-encryption-sdk-dynamodb/blob/main/Examples/runtimes/java/DDBECwithSDKV2/src/main/java/) directory of the [aws-database-encryption-sdk-dynamodb](https://github.com/aws/aws-database-encryption-sdk-dynamodb/) repository on GitHub.

**Topics**
+ [Using the DynamoDBEncryptor](#java-example-ddb-encryptor)

## Using the DynamoDBEncryptor
<a name="java-example-ddb-encryptor"></a>

This example shows how to use the lower-level [DynamoDBEncryptor](https://aws.github.io/aws-database-encryption-sdk-dynamodb/com/amazonaws/services/dynamodbv2/datamodeling/sdkv2/encryption/DynamoDBEncryptor.html) with the [Direct KMS Provider](direct-kms-provider.md). The Direct KMS Provider generates and protects its cryptographic materials under an [AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys) in AWS Key Management Service (AWS KMS) that you specify.

You can use any compatible [cryptographic materials provider](DDBEC-legacy-concepts.md#concept-material-provider) (CMP) with the `DynamoDBEncryptor`.

**See the complete code sample**: [AwsKmsEncryptedItem.java](https://github.com/aws/aws-database-encryption-sdk-dynamodb/blob/main/Examples/runtimes/java/DDBECwithSDKV2/src/main/java/AwsKmsEncryptedItem.java)

Step 1: Create the Direct KMS Provider
Create an instance of the AWS KMS client with the specified region. Then, use the client instance to create an instance of the Direct KMS Provider with your preferred AWS KMS key.
This example uses the Amazon Resource Name (ARN) to identify the AWS KMS key, but you can use [any valid key identifier](https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html#find-cmk-id-arn).

```
final String keyArn = "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab";
final String region = "us-west-2";

final KmsClient kms = KmsClient.builder().region(Region.of({{region}})).build();
final DirectKmsMaterialProvider cmp = new DirectKmsMaterialProvider(kms, {{keyArn}});
```

Step 2: Create an item
This example defines a `record` HashMap that represents a sample table item.

```
final String partitionKeyName = "partition_attribute";
final String sortKeyName = "sort_attribute";

final Map<String, AttributeValue> record = new HashMap<>();
record.put(partitionKeyName, new AttributeValue().withS("value1"));
record.put(sortKeyName, new AttributeValue().withN("55"));
record.put("example", new AttributeValue().withS("data"));
record.put("numbers", new AttributeValue().withN("99"));
record.put("binary", new AttributeValue().withB(ByteBuffer.wrap(new byte[]{0x00, 0x01, 0x02})));
record.put("test", new AttributeValue().withS("test-value"));
```

Step 3: Create a DynamoDBEncryptor
Create an instance of the `DynamoDBEncryptor` with the Direct KMS Provider.

```
final DynamoDBEncryptor encryptor = DynamoDBEncryptor.getInstance(cmp);
```

Step 4: Create a DynamoDB encryption context
The [DynamoDB encryption context](concepts.md#encryption-context) contains information about the table structure and how it is encrypted and signed.

```
final String tableName = "testTable";

final EncryptionContext encryptionContext = new EncryptionContext.Builder()
    .withTableName(tableName)
    .withHashKeyName(partitionKeyName)
    .withRangeKeyName(sortKeyName)
    .build();
```

Step 5: Create the attribute actions object
[Attribute actions](DDBEC-legacy-concepts.md#legacy-attribute-actions) determine which attributes of the item are encrypted and signed, which are only signed, and which are not encrypted or signed.
In Java, to specify attribute actions, you create a HashMap of attribute name and `EncryptionFlags` value pairs.
For example, the following Java code creates an `actions` HashMap that encrypts and signs all attributes in the `record` item, except for the partition key and sort key attributes, which are signed, but not encrypted, and the `test` attribute, which is not signed or encrypted.

```
final EnumSet<EncryptionFlags> signOnly = EnumSet.of(EncryptionFlags.SIGN);
final EnumSet<EncryptionFlags> encryptAndSign = EnumSet.of(EncryptionFlags.ENCRYPT, EncryptionFlags.SIGN);
final Map<String, Set<EncryptionFlags>> actions = new HashMap<>();

for (final String attributeName : record.keySet()) {
  switch (attributeName) {
    case partitionKeyName: // fall through to the next case
    case sortKeyName:
      // Partition and sort keys must not be encrypted, but should be signed
      actions.put(attributeName, signOnly);
      break;
    case "test":
      // Neither encrypted nor signed
      break;
    default:
      // Encrypt and sign all other attributes
      actions.put(attributeName, encryptAndSign);
      break;
  }
}
```

Step 6: Encrypt and sign the item
To encrypt and sign the table item, call the `encryptRecord` method on the instance of the `DynamoDBEncryptor`. Specify the table item (`record`), the attribute actions (`actions`), and the encryption context (`encryptionContext`).

```
final Map<String, AttributeValue> encrypted_record = encryptor.encryptRecord(record, actions, encryptionContext);
```

Step 7: Put the item in the DynamoDB table
Finally, put the encrypted and signed item in the DynamoDB table.

```
final DynamoDbClient ddb = DynamoDbClient.builder().region(Region.of(region)).build();
ddb.putItem(tableName, encrypted_record);
```
