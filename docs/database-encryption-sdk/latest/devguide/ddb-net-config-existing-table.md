---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-net-config-existing-table.html
---

# Configure an existing DynamoDB table to use the AWS Database Encryption SDK for DynamoDB
<a name="ddb-net-config-existing-table"></a>

With version 3.*x* of the .NET client-side encryption library for DynamoDB, you can configure your existing Amazon DynamoDB tables for client-side encryption. This topic provides guidance on the three steps you must take to add version 3.*x* to an existing, populated DynamoDB table.

## Step 1: Prepare to read and write encrypted items
<a name="ddb-net-add-step1"></a>

Complete the following steps to prepare your AWS Database Encryption SDK client to read and write encrypted items. After you deploy the following changes, your client will continue to read and write plaintext items. It will not encrypt or sign any new items written to the table, but it will be able to decrypt encrypted items as soon as they appear. These changes prepare the client to begin [encrypting new items](#ddb-net-add-step2). The following changes must be deployed to each reader before you proceed to the next step.

**1. Define your [attribute actions](concepts.md#crypt-actions)**
Create an object model to define which attribute values will be encrypted and signed, which will be only signed, and which will be ignored.
By default, primary key attributes are signed but not encrypted (`SIGN_ONLY`) and all other attributes are encrypted and signed (`ENCRYPT_AND_SIGN`).
Specify `ENCRYPT_AND_SIGN` to encrypt and sign an attribute. Specify `SIGN_ONLY` to sign, but not encrypt, an attribute. Specify `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` to sign and attribute and include it in the encryption context. You cannot encrypt an attribute without also signing it. Specify `DO_NOTHING` to ignore an attribute. For more information, see [Attribute actions in the AWS Database Encryption SDK for DynamoDB](ddb-net-using.md#ddb-net-attribute-actions).
If you specify any `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attributes, then the partition and sort attributes must also be `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`.

```
var attributeActionsOnEncrypt = new Dictionary<string, CryptoAction>
{
    ["partition_key"] = CryptoAction.SIGN_ONLY, // The partition attribute must be SIGN_ONLY
    ["sort_key"] = CryptoAction.SIGN_ONLY, // The sort attribute must be SIGN_ONLY
    ["attribute1"] = CryptoAction.ENCRYPT_AND_SIGN,
    ["attribute2"] = CryptoAction.SIGN_ONLY,
    [":attribute3"] = CryptoAction.DO_NOTHING
};
```

**2. Define which attributes will be excluded from the signatures**
The following example assumes that all `DO_NOTHING` attributes share the distinct prefix "`:`", and uses the prefix to define the allowed unsigned attributes. The client will assume that any attribute name with the "`:`" prefix is excluded from the signatures. For more information, see [Allowed unsigned attributes](ddb-net-using.md#net-allowed-unauth).

```
const String unsignAttrPrefix = ":";
```

**3. Create a [keyring](keyrings.md)**
The following example creates an [AWS KMS keyring](use-kms-keyring.md). The AWS KMS keyring uses symmetric encryption or asymmetric RSA AWS KMS keys to generate, encrypt, and decrypt data keys.
This example uses `CreateMrkMultiKeyring` to create an AWS KMS keyring with a symmetric encryption KMS key. The `CreateAwsKmsMrkMultiKeyring` method ensures that the keyring will correctly handle both single-Region and multi-Region keys.

```
var matProv = new MaterialProviders(new MaterialProvidersConfig());
var keyringInput = new CreateAwsKmsMrkMultiKeyringInput { Generator = kmsKeyId };
var kmsKeyring = matProv.CreateAwsKmsMrkMultiKeyring(keyringInput);
```

**4. Define the DynamoDB table encryption configuration **
The following example defines a `tableConfigs` Map that represents the encryption configuration for this DynamoDB table.
This example specifies the DynamoDB table name as the [logical table name](ddb-net-using.md#net-logical-table-name). We strongly recommend specifying your DynamoDB table name as the logical table name when you first define your encryption configuration.
You must specify `FORCE_WRITE_PLAINTEXT_ALLOW_READ_PLAINTEXT` as the plaintext override. This policy continues to read and write plaintext items, reads encrypted items, and prepares the client to write encrypted items.
For more information on the values included in the table encryption configuration, see [Encryption configuration in the AWS Database Encryption SDK for DynamoDB](ddb-java-using.md#ddb-config-encrypt).

```
Dictionary<String, DynamoDbTableEncryptionConfig> tableConfigs =
    new Dictionary<String, DynamoDbTableEncryptionConfig>();
DynamoDbTableEncryptionConfig config = new DynamoDbTableEncryptionConfig
{
    LogicalTableName = ddbTableName,
    PartitionKeyName = "partition_key",
    SortKeyName = "sort_key",
    AttributeActionsOnEncrypt = attributeActionsOnEncrypt,
    Keyring = kmsKeyring,
    AllowedUnsignedAttributePrefix = unsignAttrPrefix,
    PlaintextOverride = FORCE_WRITE_PLAINTEXT_ALLOW_READ_PLAINTEXT
};
tableConfigs.Add(ddbTableName, config);
```

**5. Create a new AWS SDK DynamoDB client**
he following example creates a new AWS SDK DynamoDB client using the `TableEncryptionConfigs` from **Step 4**.

```
var ddb = new Client.DynamoDbClient(
    new DynamoDbTablesEncryptionConfig { TableEncryptionConfigs = tableConfigs });
```

## Step 2: Write encrypted and signed items
<a name="ddb-net-add-step2"></a>

Update the plaintext policy in your table encryption configuration to allow the client to write encrypted and signed items. After you deploy the following change, the client will encrypt and sign new items based on the attribute actions you configured in **Step 1**. The client will be able read plaintext items and encrypted and signed items.

Before you proceed to [Step 3](#ddb-net-add-step3), you must encrypt and sign all existing plaintext items in your table. There is no single metric or query that you can run to quickly encrypt your existing plaintext items. Use the process that makes the most sense for your system. For example, you could use an asynchronous process that slowly scans the table and the rewrites the items using the attribute actions and encryption configuration you defined. To identify the plaintext items in your table, we recommend scanning for all items that do not contain the `aws_dbe_head` and `aws_dbe_foot` attributes that the AWS Database Encryption SDK adds to items when they're encrypted and signed.

The following example updates the table encryption configuration from **Step 1**. You must update the plaintext override with `FORBID_WRITE_PLAINTEXT_ALLOW_READ_PLAINTEXT`. This policy continues to read plaintext items, but also reads and writes encrypted items. Create a new AWS SDK DynamoDB client using the updated `TableEncryptionConfigs`.

```
Dictionary<String, DynamoDbTableEncryptionConfig> tableConfigs =
    new Dictionary<String, DynamoDbTableEncryptionConfig>();
DynamoDbTableEncryptionConfig config = new DynamoDbTableEncryptionConfig
{
    LogicalTableName = ddbTableName,
    PartitionKeyName = "partition_key",
    SortKeyName = "sort_key",
    AttributeActionsOnEncrypt = attributeActionsOnEncrypt,
    Keyring = kmsKeyring,
    AllowedUnsignedAttributePrefix = unsignAttrPrefix,
    PlaintextOverride = FORBID_WRITE_PLAINTEXT_ALLOW_READ_PLAINTEXT
};
tableConfigs.Add(ddbTableName, config);
```

## Step 3: Only read encrypted and signed items
<a name="ddb-net-add-step3"></a>

After you have encrypted and signed all of your items, update the plaintext override in your table encryption configuration to only allow the client to read and write encrypted and signed items. After you deploy the following change, the client will encrypt and sign new items based on the attribute actions you configured in **Step 1**. The client will only be able read encrypted and signed items.

The following example updates the table encryption configuration from **Step 2**. You can either update the plaintext override with `FORBID_WRITE_PLAINTEXT_FORBID_READ_PLAINTEXT` or remove the plaintext policy from your configuration. The client only reads and writes encrypted and signed items by default. Create a new AWS SDK DynamoDB client using the updated `TableEncryptionConfigs`.

```
Dictionary<String, DynamoDbTableEncryptionConfig> tableConfigs =
    new Dictionary<String, DynamoDbTableEncryptionConfig>();
DynamoDbTableEncryptionConfig config = new DynamoDbTableEncryptionConfig
{
    LogicalTableName = ddbTableName,
    PartitionKeyName = "partition_key",
    SortKeyName = "sort_key",
    AttributeActionsOnEncrypt = attributeActionsOnEncrypt,
    Keyring = kmsKeyring,
    AllowedUnsignedAttributePrefix = unsignAttrPrefix,
    // Optional: you can also remove the plaintext policy from your configuration
    PlaintextOverride = FORBID_WRITE_PLAINTEXT_FORBID_READ_PLAINTEXT
};
tableConfigs.Add(ddbTableName, config);
```
