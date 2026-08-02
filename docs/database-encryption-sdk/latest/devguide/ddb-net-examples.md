---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-net-examples.html
---

# .NET examples
<a name="ddb-net-examples"></a>

The following examples show you how to use the .NET client-side encryption library for DynamoDB to protect the table items in your application. To find more examples (and contribute your own), see the [.NET examples](https://github.com/aws/aws-database-encryption-sdk-dynamodb//tree/main/Examples/runtimes/net/src) in the aws-database-encryption-sdk-dynamodb repository on GitHub.

The following examples demonstrate how to configure the .NET client-side encryption library for DynamoDB in a new, unpopulated Amazon DynamoDB table. If you want to configure your existing Amazon DynamoDB tables for client-side encryption, see [Add version 3.x to an existing table](ddb-net-config-existing-table.md).

**Topics**
+ [Using the low-level AWS Database Encryption SDK for DynamoDB API](#ddb-net-lowlevel-API-example)
+ [Using the lower-level `DynamoDbItemEncryptor`](#ddb-net-itemencryptor)

## Using the low-level AWS Database Encryption SDK for DynamoDB API
<a name="ddb-net-lowlevel-API-example"></a>

The following example shows how to use the low-level AWS Database Encryption SDK for DynamoDB API with an [AWS KMS keyring](use-kms-keyring.md) to automatically encrypt and sign items client-side with your DynamoDB `PutItem` requests.

You can use any supported [keyring](keyrings.md), but we recommend using one of the AWS KMS keyrings whenever possible.

**See the complete code sample**: [BasicPutGetExample.cs](https://github.com/aws/aws-database-encryption-sdk-dynamodb/tree/main/Examples/runtimes/net/src/BasicPutGetExample.cs)

**Step 1: Create the AWS KMS keyring**
The following example uses `CreateAwsKmsMrkMultiKeyring` to create an AWS KMS keyring with a symmetric encryption KMS key. The `CreateAwsKmsMrkMultiKeyring` method ensures that the keyring will correctly handle both single-Region and multi-Region keys.

```
var matProv = new MaterialProviders(new MaterialProvidersConfig());
var keyringInput = new CreateAwsKmsMrkMultiKeyringInput { Generator = kmsKeyId };
var kmsKeyring = matProv.CreateAwsKmsMrkMultiKeyring(keyringInput);
```

**Step 2: Configure your attribute actions**
The following example defines an `attributeActionsOnEncrypt` Dictionary that represents sample [attribute actions](concepts.md#crypt-actions) for a table item.
The following example does not define any attributes as `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`. If you specify any `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attributes, then the partition and sort attributes must also be `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`.

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

**Step 3: Define which attributes are excluded from the signatures**
The following example assumes that all `DO_NOTHING` attributes share the distinct prefix "`:`", and uses the prefix to define the allowed unsigned attributes. The client assumes that any attribute name with the "`:`" prefix is excluded from the signatures. For more information, see [Allowed unsigned attributes](ddb-net-using.md#net-allowed-unauth).

```
const String unsignAttrPrefix = ":";
```

**Step 4: Define the DynamoDB table encryption configuration**
The following example defines a `tableConfigs` Map that represents the encryption configuration for this DynamoDB table.
This example specifies the DynamoDB table name as the [logical table name](ddb-net-using.md#net-logical-table-name). We strongly recommend specifying your DynamoDB table name as the logical table name when you first define your encryption configuration. For more information, see [Encryption configuration in the AWS Database Encryption SDK for DynamoDB](ddb-net-using.md#ddb-net-config-encrypt).
To use [searchable encryption](searchable-encryption.md) or [signed beacons](configure.md#signed-beacons), you must also include the [`SearchConfig`](ddb-java-using.md#ddb-search-config) in your encryption configuration.

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
    AllowedUnsignedAttributePrefix = unsignAttrPrefix
};
tableConfigs.Add(ddbTableName, config);
```

**Step 5: Create a new AWS SDK DynamoDB client**
The following example creates a new AWS SDK DynamoDB client using the `TableEncryptionConfigs` from **Step 4**.

```
var ddb = new Client.DynamoDbClient(
    new DynamoDbTablesEncryptionConfig { TableEncryptionConfigs = tableConfigs });
```

**Step 6: Encrypt and sign a DynamoDB table item**
The following example defines an `item` Dictionary that represents a sample table item and puts the item in the DynamoDB table. The item is encrypted and signed client-side before it is sent to DynamoDB.

```
var item = new Dictionary<String, AttributeValue>
{
    ["partition_key"] = new AttributeValue("BasicPutGetExample"),
    ["sort_key"] = new AttributeValue { N = "0" },
    ["attribute1"] = new AttributeValue("encrypt and sign me!"),
    ["attribute2"] = new AttributeValue("sign me!"),
    [":attribute3"] = new AttributeValue("ignore me!")
};

PutItemRequest putRequest = new PutItemRequest
{
    TableName = ddbTableName,
    Item = item
};

PutItemResponse putResponse = await ddb.PutItemAsync(putRequest);
```

## Using the lower-level `DynamoDbItemEncryptor`
<a name="ddb-net-itemencryptor"></a>

The following example shows how to use the lower-level `DynamoDbItemEncryptor` with an [AWS KMS keyring](use-kms-keyring.md) to directly encrypt and sign table items. The `DynamoDbItemEncryptor` does not put the item in your DynamoDB table.

You can use any supported [keyring](keyrings.md) with the DynamoDB Enhanced Client, but we recommend using one of the AWS KMS keyrings whenever possible.

**Note**
The lower-level `DynamoDbItemEncryptor` does not support [searchable encryption](searchable-encryption.md). Use the the low-level AWS Database Encryption SDK for DynamoDB API to use searchable encryption.

**See the complete code sample**: [ItemEncryptDecryptExample.cs](https://github.com/aws/aws-database-encryption-sdk-dynamodb/tree/main/Examples/runtimes/net/src/itemencryptor/ItemEncryptDecryptExample.cs)

**Step 1: Create the AWS KMS keyring**
The following example uses `CreateAwsKmsMrkMultiKeyring` to create an AWS KMS keyring with a symmetric encryption KMS key. The `CreateAwsKmsMrkMultiKeyring` method ensures that the keyring will correctly handle both single-Region and multi-Region keys.

```
var matProv = new MaterialProviders(new MaterialProvidersConfig());
var keyringInput = new CreateAwsKmsMrkMultiKeyringInput { Generator = kmsKeyId };
var kmsKeyring = matProv.CreateAwsKmsMrkMultiKeyring(keyringInput);
```

**Step 2: Configure your attribute actions**
The following example defines an `attributeActionsOnEncrypt` Dictionary that represents sample [attribute actions](concepts.md#crypt-actions) for a table item.
The following example does not define any attributes as `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`. If you specify any `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attributes, then the partition and sort attributes must also be `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`.

```
var attributeActionsOnEncrypt = new Dictionary<String, CryptoAction>
{
    ["partition_key"] = CryptoAction.SIGN_ONLY, // The partition attribute must be SIGN_ONLY
    ["sort_key"] = CryptoAction.SIGN_ONLY, // The sort attribute must be SIGN_ONLY
    ["attribute1"] = CryptoAction.ENCRYPT_AND_SIGN,
    ["attribute2"] = CryptoAction.SIGN_ONLY,
    [":attribute3"] = CryptoAction.DO_NOTHING
};
```

**Step 3: Define which attributes are excluded from the signatures**
The following example assumes that all `DO_NOTHING` attributes share the distinct prefix "`:`", and uses the prefix to define the allowed unsigned attributes. The client assumes that any attribute name with the "`:`" prefix is excluded from the signatures. For more information, see [Allowed unsigned attributes](ddb-net-using.md#net-allowed-unauth).

```
String unsignAttrPrefix = ":";
```

**Step 4: Define the `DynamoDbItemEncryptor` configuration**
The following example defines the configuration for the `DynamoDbItemEncryptor`.
This example specifies the DynamoDB table name as the [logical table name](ddb-net-using.md#net-logical-table-name). We strongly recommend specifying your DynamoDB table name as the logical table name when you first define your encryption configuration. For more information, see [Encryption configuration in the AWS Database Encryption SDK for DynamoDB](ddb-net-using.md#ddb-net-config-encrypt).

```
var config = new DynamoDbItemEncryptorConfig
{
    LogicalTableName = ddbTableName,
    PartitionKeyName = "partition_key",
    SortKeyName = "sort_key",
    AttributeActionsOnEncrypt = attributeActionsOnEncrypt,
    Keyring = kmsKeyring,
    AllowedUnsignedAttributePrefix = unsignAttrPrefix
};
```

**Step 5: Create the `DynamoDbItemEncryptor`**
The following example creates a new `DynamoDbItemEncryptor` using the `config` from **Step 4**.

```
var itemEncryptor = new DynamoDbItemEncryptor(config);
```

**Step 6: Directly encrypt and sign a table item**
The following example directly encrypts and signs an item using the `DynamoDbItemEncryptor`. The `DynamoDbItemEncryptor` does not put the item in your DynamoDB table.

```
var originalItem = new Dictionary<String, AttributeValue>
{
    ["partition_key"] = new AttributeValue("ItemEncryptDecryptExample"),
    ["sort_key"] = new AttributeValue { N = "0" },
    ["attribute1"] = new AttributeValue("encrypt and sign me!"),
    ["attribute2"] = new AttributeValue("sign me!"),
    [":attribute3"] = new AttributeValue("ignore me!")
};

var encryptedItem = itemEncryptor.EncryptItem(
    new EncryptItemInput { PlaintextItem = originalItem }
).EncryptedItem;
```
