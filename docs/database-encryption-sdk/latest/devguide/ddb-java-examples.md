---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-java-examples.html
---

# Java examples
<a name="ddb-java-examples"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

The following examples show you how to use the Java client-side encryption library for DynamoDB to protect the table items in your application. You can find more examples (and contribute your own) in the [Java examples](https://github.com/aws/aws-database-encryption-sdk-dynamodb//tree/main/Examples/runtimes/java/DynamoDbEncryption/src/main/java/software/amazon/cryptography/examples) in the aws-database-encryption-sdk-dynamodb repository on GitHub.

The following examples demonstrate how to configure the Java client-side encryption library for DynamoDB in a new, unpopulated Amazon DynamoDB table. If you want to configure your existing Amazon DynamoDB tables for client-side encryption, see [Add version 4.x to an existing table](ddb-java-config-existing-table.md).

**Topics**
+ [Using the DynamoDB enhanced client](#ddb-java-enhanced-client-example)
+ [Using the low-level DynamoDB API](#ddb-java-lowlevel-API-example)
+ [Using the lower-level DynamoDbItemEncryptor](#ddb-java-itemencryptor)

## Using the DynamoDB enhanced client
<a name="ddb-java-enhanced-client-example"></a>

The following example shows how to use the DynamoDB Enhanced Client and `DynamoDbEncryptionInterceptor` with an [AWS KMS keyring](use-kms-keyring.md) to encrypt DynamoDB table items as part of your DynamoDB API calls.

You can use any supported [keyring](keyrings.md) with the DynamoDB Enhanced Client, but we recommend using one of the AWS KMS keyrings whenever possible.

**Note**
The DynamoDB Enhanced Client does not support [searchable encryption](searchable-encryption.md). Use the `DynamoDbEncryptionInterceptor` with the low-level DynamoDB API to use searchable encryption.

**See the complete code sample**: [EnhancedPutGetExample.java](https://github.com/aws/aws-database-encryption-sdk-dynamodb//blob/main/Examples/runtimes/java/DynamoDbEncryption/src/main/java/software/amazon/cryptography/examples/enhanced/EnhancedPutGetExample.java)

**Step 1: Create the AWS KMS keyring**
The following example uses `CreateAwsKmsMrkMultiKeyring` to create an AWS KMS keyring with a symmetric encryption KMS key. The `CreateAwsKmsMrkMultiKeyring` method ensures that the keyring will correctly handle both single-Region and multi-Region keys.

```
final MaterialProviders matProv = MaterialProviders.builder()
        .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
        .build();
final CreateAwsKmsMrkMultiKeyringInput keyringInput = CreateAwsKmsMrkMultiKeyringInput.builder()
        .generator(kmsKeyId)
        .build();
final IKeyring kmsKeyring = matProv.CreateAwsKmsMrkMultiKeyring(keyringInput);
```

**Step 2: Create a table schema from the annotated data class**
The following example uses the annotated data class to create the `TableSchema`.
This example assumes that the annotated data class and attribute actions were defined using the [SimpleClass.java](https://github.com/aws/aws-database-encryption-sdk-dynamodb//blob/main/Examples/runtimes/java/DynamoDbEncryption/src/main/java/software/amazon/cryptography/examples/enhanced/SimpleClass.java). For more guidance on annotating your attribute actions, see [Use an annotated data class](ddb-java-using.md#ddb-attribute-actions-annotated-data-class).
The AWS Database Encryption SDK does not support annotations on [nested attributes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-adv-features-nested.html).

```
final TableSchema<SimpleClass> schemaOnEncrypt = TableSchema.fromBean(SimpleClass.class);
```

**Step 3: Define which attributes are excluded from the signatures**
The following example assumes that all `DO_NOTHING` attributes share the distinct prefix "`:`", and uses the prefix to define the allowed unsigned attributes. The client assumes that any attribute name with the "`:`" prefix is excluded from the signatures. For more information, see [Allowed unsigned attributes](ddb-java-using.md#allowed-unauth).

```
final String unsignedAttrPrefix = ":";
```

**Step 4: Create the encryption configuration**
The following example defines a `tableConfigs` Map that represents the encryption configuration for the DynamoDB table.
This example specifies the DynamoDB table name as the [logical table name](ddb-java-using.md#logical-table-name). We strongly recommend specifying your DynamoDB table name as the logical table name when you first define your encryption configuration. For more information, see [Encryption configuration in the AWS Database Encryption SDK for DynamoDB](ddb-java-using.md#ddb-config-encrypt).
To use [searchable encryption](searchable-encryption.md) or [signed beacons](configure.md#signed-beacons), you must also include the [`SearchConfig`](ddb-java-using.md#ddb-search-config) in your encryption configuration.

```
final Map<String, DynamoDbEnhancedTableEncryptionConfig> tableConfigs = new HashMap<>();
tableConfigs.put(ddbTableName,
    DynamoDbEnhancedTableEncryptionConfig.builder()
        .logicalTableName(ddbTableName)
        .keyring(kmsKeyring)
        .allowedUnsignedAttributePrefix(unsignedAttrPrefix)
        .schemaOnEncrypt(tableSchema)
        .build());
```

**Step 5: Creates the `DynamoDbEncryptionInterceptor`**
The following example creates a new `DynamoDbEncryptionInterceptor` with the `tableConfigs` from **Step 4**.

```
final DynamoDbEncryptionInterceptor interceptor =
    DynamoDbEnhancedClientEncryption.CreateDynamoDbEncryptionInterceptor(
        CreateDynamoDbEncryptionInterceptorInput.builder()
            .tableEncryptionConfigs(tableConfigs)
            .build()
    );
```

**Step 6: Create a new AWS SDK DynamoDB client**
The following example creates a new AWS SDK DynamoDB client using the `interceptor` from **Step 5**.

```
final DynamoDbClient ddb = DynamoDbClient.builder()
        .overrideConfiguration(
                ClientOverrideConfiguration.builder()
                       .addExecutionInterceptor(interceptor)
                       .build())
        .build();
```

**Step 7: Create the DynamoDB Enhanced Client and create a table**
The following example creates the DynamoDB Enhanced Client using the AWS SDK DynamoDB client created in **Step 6** and creates a table using the annotated data class.

```
final DynamoDbEnhancedClient enhancedClient = DynamoDbEnhancedClient.builder()
        .dynamoDbClient(ddb)
        .build();
final DynamoDbTable<SimpleClass> table = enhancedClient.table(ddbTableName, tableSchema);
```

**Step 8: Encrypt and sign a table item**
The following example puts an item into the DynamoDB table using the DynamoDB Enhanced Client. The item is encrypted and signed client-side before it is send to DynamoDB.

```
final SimpleClass item = new SimpleClass();
item.setPartitionKey("EnhancedPutGetExample");
item.setSortKey(0);
item.setAttribute1("encrypt and sign me!");
item.setAttribute2("sign me!");
item.setAttribute3("ignore me!");

table.putItem(item);
```

## Using the low-level DynamoDB API
<a name="ddb-java-lowlevel-API-example"></a>

The following example shows how to use the low-level DynamoDB API with an [AWS KMS keyring](use-kms-keyring.md) to automatically encrypt and sign items client-side with your DynamoDB `PutItem` requests.

You can use any supported [keyring](keyrings.md), but we recommend using one of the AWS KMS keyrings whenever possible.

**See the complete code sample**: [BasicPutGetExample.java](https://github.com/aws/aws-database-encryption-sdk-dynamodb//blob/main/Examples/runtimes/java/DynamoDbEncryption/src/main/java/software/amazon/cryptography/examples/BasicPutGetExample.java)

**Step 1: Create the AWS KMS keyring**
The following example uses `CreateAwsKmsMrkMultiKeyring` to create an AWS KMS keyring with a symmetric encryption KMS key. The `CreateAwsKmsMrkMultiKeyring` method ensures that the keyring will correctly handle both single-Region and multi-Region keys.

```
final MaterialProviders matProv = MaterialProviders.builder()
         .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
         .build();
final CreateAwsKmsMrkMultiKeyringInput keyringInput = CreateAwsKmsMrkMultiKeyringInput.builder()
        .generator(kmsKeyId)
        .build();
final IKeyring kmsKeyring = matProv.CreateAwsKmsMrkMultiKeyring(keyringInput);
```

**Step 2: Configure your attribute actions**
The following example defines an `attributeActionsOnEncrypt` Map that represents sample [attribute actions](concepts.md#crypt-actions) for a table item.
The following example does not define any attributes as `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`. If you specify any `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attributes, then the partition and sort attributes must also be `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`.

```
final Map<String, CryptoAction> attributeActionsOnEncrypt = new HashMap<>();
// The partition attribute must be SIGN_ONLY
attributeActionsOnEncrypt.put("partition_key", CryptoAction.SIGN_ONLY);
// The sort attribute must be SIGN_ONLY
attributeActionsOnEncrypt.put("sort_key", CryptoAction.SIGN_ONLY);
attributeActionsOnEncrypt.put("attribute1", CryptoAction.ENCRYPT_AND_SIGN);
attributeActionsOnEncrypt.put("attribute2", CryptoAction.SIGN_ONLY);
attributeActionsOnEncrypt.put(":attribute3", CryptoAction.DO_NOTHING);
```

**Step 3: Define which attributes are excluded from the signatures**
The following example assumes that all `DO_NOTHING` attributes share the distinct prefix "`:`", and uses the prefix to define the allowed unsigned attributes. The client assumes that any attribute name with the "`:`" prefix is excluded from the signatures. For more information, see [Allowed unsigned attributes](ddb-java-using.md#allowed-unauth).

```
final String unsignedAttrPrefix = ":";
```

**Step 4: Define the DynamoDB table encryption configuration**
The following example defines a `tableConfigs` Map that represents the encryption configuration for this DynamoDB table.
This example specifies the DynamoDB table name as the [logical table name](ddb-java-using.md#logical-table-name). We strongly recommend specifying your DynamoDB table name as the logical table name when you first define your encryption configuration. For more information, see [Encryption configuration in the AWS Database Encryption SDK for DynamoDB](ddb-java-using.md#ddb-config-encrypt).
To use [searchable encryption](searchable-encryption.md) or [signed beacons](configure.md#signed-beacons), you must also include the [`SearchConfig`](ddb-java-using.md#ddb-search-config) in your encryption configuration.

```
final Map<String, DynamoDbTableEncryptionConfig> tableConfigs = new HashMap<>();
final DynamoDbTableEncryptionConfig config = DynamoDbTableEncryptionConfig.builder()
        .logicalTableName(ddbTableName)
        .partitionKeyName("partition_key")
        .sortKeyName("sort_key")
        .attributeActionsOnEncrypt(attributeActionsOnEncrypt)
        .keyring(kmsKeyring)
        .allowedUnsignedAttributePrefix(unsignedAttrPrefix)
        .build();
tableConfigs.put(ddbTableName, config);
```

**Step 5: Create the `DynamoDbEncryptionInterceptor`**
The following example creates the `DynamoDbEncryptionInterceptor` using the `tableConfigs` from **Step 4**.

```
DynamoDbEncryptionInterceptor interceptor = DynamoDbEncryptionInterceptor.builder()
        .config(DynamoDbTablesEncryptionConfig.builder()
                .tableEncryptionConfigs(tableConfigs)
                .build())
        .build();
```

**Step 6: Create a new AWS SDK DynamoDB client**
The following example creates a new AWS SDK DynamoDB client using the `interceptor` from **Step 5**.

```
final DynamoDbClient ddb = DynamoDbClient.builder()
        .overrideConfiguration(
                ClientOverrideConfiguration.builder()
                       .addExecutionInterceptor(interceptor)
                       .build())
        .build();
```

**Step 7: Encrypt and sign a DynamoDB table item**
The following example defines an `item` Map that represents a sample table item and puts the item in the DynamoDB table. The item is encrypted and signed client-side before it is sent to DynamoDB.

```
final HashMap<String, AttributeValue> item = new HashMap<>();
item.put("partition_key", AttributeValue.builder().s("BasicPutGetExample").build());
item.put("sort_key", AttributeValue.builder().n("0").build());
item.put("attribute1", AttributeValue.builder().s("encrypt and sign me!").build());
item.put("attribute2", AttributeValue.builder().s("sign me!").build());
item.put(":attribute3", AttributeValue.builder().s("ignore me!").build());

final PutItemRequest putRequest = PutItemRequest.builder()
        .tableName(ddbTableName)
        .item(item)
        .build();

final PutItemResponse putResponse = ddb.putItem(putRequest);
```

## Using the lower-level DynamoDbItemEncryptor
<a name="ddb-java-itemencryptor"></a>

The following example shows how to use the lower-level `DynamoDbItemEncryptor` with an [AWS KMS keyring](use-kms-keyring.md) to directly encrypt and sign table items. The `DynamoDbItemEncryptor` does not put the item in your DynamoDB table.

You can use any supported [keyring](keyrings.md) with the DynamoDB Enhanced Client, but we recommend using one of the AWS KMS keyrings whenever possible.

**Note**
The lower-level `DynamoDbItemEncryptor` does not support [searchable encryption](searchable-encryption.md). Use the `DynamoDbEncryptionInterceptor` with the low-level DynamoDB API to use searchable encryption.

**See the complete code sample**: [ItemEncryptDecryptExample.java](https://github.com/aws/aws-database-encryption-sdk-dynamodb//blob/main/Examples/runtimes/java/DynamoDbEncryption/src/main/java/software/amazon/cryptography/examples/itemencryptor/ItemEncryptDecryptExample.java)

**Step 1: Create the AWS KMS keyring**
The following example uses `CreateAwsKmsMrkMultiKeyring` to create an AWS KMS keyring with a symmetric encryption KMS key. The `CreateAwsKmsMrkMultiKeyring` method ensures that the keyring will correctly handle both single-Region and multi-Region keys.

```
final MaterialProviders matProv = MaterialProviders.builder()
         .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
         .build();
final CreateAwsKmsMrkMultiKeyringInput keyringInput = CreateAwsKmsMrkMultiKeyringInput.builder()
        .generator(kmsKeyId)
        .build();
final IKeyring kmsKeyring = matProv.CreateAwsKmsMrkMultiKeyring(keyringInput);
```

**Step 2: Configure your attribute actions**
The following example defines an `attributeActionsOnEncrypt` Map that represents sample [attribute actions](concepts.md#crypt-actions) for a table item.
The following example does not define any attributes as `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`. If you specify any `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attributes, then the partition and sort attributes must also be `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`.

```
final Map<String, CryptoAction> attributeActionsOnEncrypt = new HashMap<>();
// The partition attribute must be SIGN_ONLY
attributeActionsOnEncrypt.put("partition_key", CryptoAction.SIGN_ONLY);
// The sort attribute must be SIGN_ONLY
attributeActionsOnEncrypt.put("sort_key", CryptoAction.SIGN_ONLY);
attributeActionsOnEncrypt.put("attribute1", CryptoAction.ENCRYPT_AND_SIGN);
attributeActionsOnEncrypt.put("attribute2", CryptoAction.SIGN_ONLY);
attributeActionsOnEncrypt.put(":attribute3", CryptoAction.DO_NOTHING);
```

**Step 3: Define which attributes are excluded from the signatures**
The following example assumes that all `DO_NOTHING` attributes share the distinct prefix "`:`", and uses the prefix to define the allowed unsigned attributes. The client assumes that any attribute name with the "`:`" prefix is excluded from the signatures. For more information, see [Allowed unsigned attributes](ddb-java-using.md#allowed-unauth).

```
final String unsignedAttrPrefix = ":";
```

**Step 4: Define the `DynamoDbItemEncryptor` configuration**
The following example defines the configuration for the `DynamoDbItemEncryptor`.
This example specifies the DynamoDB table name as the [logical table name](ddb-java-using.md#logical-table-name). We strongly recommend specifying your DynamoDB table name as the logical table name when you first define your encryption configuration. For more information, see [Encryption configuration in the AWS Database Encryption SDK for DynamoDB](ddb-java-using.md#ddb-config-encrypt).

```
final DynamoDbItemEncryptorConfig config = DynamoDbItemEncryptorConfig.builder()
        .logicalTableName(ddbTableName)
        .partitionKeyName("partition_key")
        .sortKeyName("sort_key")
        .attributeActionsOnEncrypt(attributeActionsOnEncrypt)
        .keyring(kmsKeyring)
        .allowedUnsignedAttributePrefix(unsignedAttrPrefix)
        .build();
```

**Step 5: Create the `DynamoDbItemEncryptor`**
The following example creates a new `DynamoDbItemEncryptor` using the `config` from **Step 4**.

```
final DynamoDbItemEncryptor itemEncryptor = DynamoDbItemEncryptor.builder()
        .DynamoDbItemEncryptorConfig(config)
        .build();
```

**Step 6: Directly encrypt and sign a table item**
The following example directly encrypts and signs an item using the `DynamoDbItemEncryptor`. The `DynamoDbItemEncryptor` does not put the item in your DynamoDB table.

```
final Map<String, AttributeValue> originalItem = new HashMap<>();
originalItem.put("partition_key", AttributeValue.builder().s("ItemEncryptDecryptExample").build());
originalItem.put("sort_key", AttributeValue.builder().n("0").build());
originalItem.put("attribute1", AttributeValue.builder().s("encrypt and sign me!").build());
originalItem.put("attribute2", AttributeValue.builder().s("sign me!").build());
originalItem.put(":attribute3", AttributeValue.builder().s("ignore me!").build());

final Map<String, AttributeValue> encryptedItem = itemEncryptor.EncryptItem(
        EncryptItemInput.builder()
                .plaintextItem(originalItem)
                .build()
).encryptedItem();
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
