---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-java-config-existing-table.html
---

# Configure an existing DynamoDB table to use the AWS Database Encryption SDK for DynamoDB
<a name="ddb-java-config-existing-table"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

With version 4.*x* of the Java client-side encryption library for DynamoDB, you can configure your existing Amazon DynamoDB tables for client-side encryption. This topic provides guidance on the three steps you must take to add version 4.*x* to an existing, populated DynamoDB table.

**Prerequisites**
Version 4.*x* of the Java client-side encryption library for DynamoDB requires the [DynamoDB Enhanced Client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-enhanced-client.html) provided in AWS SDK for Java 2.x . If you still use the [DynamoDBMapper](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBMapper.Methods.html), you must migrate to AWS SDK for Java 2.x to use the DynamoDB Enhanced Client.

 Follow the instructions for [migrating from version 1.x to 2.x of the AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration.html).

Then, follow the instructions to [Get Started using the DynamoDB Enhanced Client API](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-getting-started.html).

Before configuring your table to use the Java client-side encryption library for DynamoDB, you need to generate a `TableSchema` [using an annotated data class](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-gs-tableschema.html#ddb-en-client-gs-tableschema-anno-bean) and [create an enhanced client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-getting-started-dynamodbTable.html#ddb-en-client-getting-started-dynamodbTable-eclient).

## Step 1: Prepare to read and write encrypted items
<a name="ddb-java-add-step1"></a>

Complete the following steps to prepare your AWS Database Encryption SDK client to read and write encrypted items. After you deploy the following changes, your client will continue to read and write plaintext items. It will not encrypt or sign any new items written to the table, but it will be able to decrypt encrypted items as soon as they appear. These changes prepare the client to begin [encrypting new items](#ddb-java-add-step2). The following changes must be deployed to each reader before you proceed to the next step.

**1. Define your [attribute actions](concepts.md#crypt-actions)**
Update your annotated data class to include attribute actions that define which attribute values will be encrypted and signed, which will be only signed, and which will be ignored.
See the [SimpleClass.java](https://github.com/aws/aws-database-encryption-sdk-dynamodb//blob/main/Examples/runtimes/java/DynamoDbEncryption/src/main/java/software/amazon/cryptography/examples/enhanced/SimpleClass.java) in the aws-database-encryption-sdk-dynamodb repository on GitHub for more guidance on the DynamoDB Enhanced Client annotations.
By default, primary key attributes are signed but not encrypted (`SIGN_ONLY`) and all other attributes are encrypted and signed (`ENCRYPT_AND_SIGN`). To specify exceptions, use the encryption annotations defined in the Java client-side encryption library for DynamoDB. For example, if you want a particular attribute to be sign only use the `@DynamoDbEncryptionSignOnly` annotation. If you want a particular attribute to be signed and included in the encryption context, use the `@DynamoDbEncryptionSignAndIncludeInEncryptionContext` annotation. If you want a particular attribute to be neither signed nor encrypted (`DO_NOTHING`), use the `@DynamoDbEncryptionDoNothing` annotation.
If you specify any `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attributes, then the partition and sort attributes must also be `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`. For an example that shows the annotations used to define `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`, see [SimpleClass4.java](https://github.com/aws/aws-database-encryption-sdk-dynamodb//blob/main/Examples/runtimes/java/DynamoDbEncryption/src/main/java/software/amazon/cryptography/examples/enhanced/SimpleClass4.java).
For example annotations, see [Use an annotated data class](ddb-java-using.md#ddb-attribute-actions-annotated-data-class).

**2. Define which attributes will be excluded from the signatures**
The following example assumes that all `DO_NOTHING` attributes share the distinct prefix "`:`", and uses the prefix to define the allowed unsigned attributes. The client will assume that any attribute name with the "`:`" prefix is excluded from the signatures. For more information, see [Allowed unsigned attributes](ddb-java-using.md#allowed-unauth).

```
final String unsignedAttrPrefix = ":";
```

**3. Create a [keyring](keyrings.md)**
The following example creates an [AWS KMS keyring](use-kms-keyring.md). The AWS KMS keyring uses symmetric encryption or asymmetric RSA AWS KMS keys to generate, encrypt, and decrypt data keys.
This example uses `CreateMrkMultiKeyring` to create an AWS KMS keyring with a symmetric encryption KMS key. The `CreateAwsKmsMrkMultiKeyring` method ensures that the keyring will correctly handle both single-Region and multi-Region keys.

```
final MaterialProviders matProv = MaterialProviders.builder()
        .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
        .build();
final CreateAwsKmsMrkMultiKeyringInput keyringInput = CreateAwsKmsMrkMultiKeyringInput.builder()
        .generator(kmsKeyId)
        .build();
final IKeyring kmsKeyring = matProv.CreateAwsKmsMrkMultiKeyring(keyringInput);
```

**4. Define the DynamoDB table encryption configuration **
The following example defines a `tableConfigs` Map that represents the encryption configuration for this DynamoDB table.
This example specifies the DynamoDB table name as the [logical table name](ddb-java-using.md#logical-table-name). We strongly recommend specifying your DynamoDB table name as the logical table name when you first define your encryption configuration. For more information, see [Encryption configuration in the AWS Database Encryption SDK for DynamoDB](ddb-java-using.md#ddb-config-encrypt).
You must specify `FORCE_WRITE_PLAINTEXT_ALLOW_READ_PLAINTEXT` as the plaintext override. This policy continues to read and write plaintext items, reads encrypted items, and prepares the client to write encrypted items.

```
final Map<String, DynamoDbTableEncryptionConfig> tableConfigs = new HashMap<>();
final DynamoDbTableEncryptionConfig config = DynamoDbTableEncryptionConfig.builder()
        .logicalTableName(ddbTableName)
        .partitionKeyName("partition_key")
        .sortKeyName("sort_key")
        .schemaOnEncrypt(tableSchema)
        .keyring(kmsKeyring)
        .allowedUnsignedAttributePrefix(unsignedAttrPrefix)
        .plaintextOverride(PlaintextOverride.FORCE_WRITE_PLAINTEXT_ALLOW_READ_PLAINTEXT)
        .build();
tableConfigs.put(ddbTableName, config);
```

**5. Create the `DynamoDbEncryptionInterceptor`**
The following example creates the `DynamoDbEncryptionInterceptor` using the `tableConfigs` from **Step 3**.

```
DynamoDbEncryptionInterceptor interceptor = DynamoDbEncryptionInterceptor.builder()
        .config(DynamoDbTablesEncryptionConfig.builder()
                .tableEncryptionConfigs(tableConfigs)
                .build())
        .build();
```

## Step 2: Write encrypted and signed items
<a name="ddb-java-add-step2"></a>

Update the plaintext policy in your `DynamoDbEncryptionInterceptor` configuration to allow the client to write encrypted and signed items. After you deploy the following change, the client will encrypt and sign new items based on the attribute actions you configured in **Step 1**. The client will be able read plaintext items and encrypted and signed items.

Before you proceed to [Step 3](#ddb-java-add-step3), you must encrypt and sign all existing plaintext items in your table. There is no single metric or query that you can run to quickly encrypt your existing plaintext items. Use the process that makes the most sense for your system. For example, you could use an asynchronous process that slowly scans the table and the rewrites the items using the attribute actions and encryption configuration you defined. To identify the plaintext items in your table, we recommend scanning for all items that do not contain the `aws_dbe_head` and `aws_dbe_foot` attributes that the AWS Database Encryption SDK adds to items when they're encrypted and signed.

The following example updates the table encryption configuration from **Step 1**. You must update the plaintext override with `FORBID_WRITE_PLAINTEXT_ALLOW_READ_PLAINTEXT`. This policy continues to read plaintext items, but also reads and writes encrypted items. Create a new `DynamoDbEncryptionInterceptor` using the updated `tableConfigs`.

```
final Map<String, DynamoDbTableEncryptionConfig> tableConfigs = new HashMap<>();
final DynamoDbTableEncryptionConfig config = DynamoDbTableEncryptionConfig.builder()
        .logicalTableName(ddbTableName)
        .partitionKeyName("partition_key")
        .sortKeyName("sort_key")
        .schemaOnEncrypt(tableSchema)
        .keyring(kmsKeyring)
        .allowedUnsignedAttributePrefix(unsignedAttrPrefix)
        .plaintextOverride(PlaintextOverride.FORBID_WRITE_PLAINTEXT_ALLOW_READ_PLAINTEXT)
        .build();
tableConfigs.put(ddbTableName, config);
```

## Step 3: Only read encrypted and signed items
<a name="ddb-java-add-step3"></a>

After you have encrypted and signed all of your items, update the plaintext override in your `DynamoDbEncryptionInterceptor` configuration to only allow the client to read and write encrypted and signed items. After you deploy the following change, the client will encrypt and sign new items based on the attribute actions you configured in **Step 1**. The client will only be able read encrypted and signed items.

The following example updates the table encryption configuration from **Step 2**. You can either update the plaintext override with `FORBID_WRITE_PLAINTEXT_FORBID_READ_PLAINTEXT` or remove the plaintext policy from your configuration. The client only reads and writes encrypted and signed items by default. Create a new `DynamoDbEncryptionInterceptor` using the updated `tableConfigs`.

```
final Map<String, DynamoDbTableEncryptionConfig> tableConfigs = new HashMap<>();
final DynamoDbTableEncryptionConfig config = DynamoDbTableEncryptionConfig.builder()
        .logicalTableName(ddbTableName)
        .partitionKeyName("partition_key")
        .sortKeyName("sort_key")
        .schemaOnEncrypt(tableSchema)
        .keyring(kmsKeyring)
        .allowedUnsignedAttributePrefix(unsignedAttrPrefix)
        // Optional: you can also remove the plaintext policy from your configuration
        .plaintextOverride(PlaintextOverride.FORBID_WRITE_PLAINTEXT_FORBID_READ_PLAINTEXT)
        .build();
tableConfigs.put(ddbTableName, config);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
