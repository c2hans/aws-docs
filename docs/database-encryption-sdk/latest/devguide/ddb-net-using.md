---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-net-using.html
---

# Using the .NET client-side encryption library for DynamoDB
<a name="ddb-net-using"></a>

This topic explains some of the functions and helper classes in version 3.*x* of the .NET client-side encryption library for DynamoDB.

For details about programming with the .NET client-side encryption library for DynamoDB, see the [.NET examples](https://github.com/aws/aws-database-encryption-sdk-dynamodb/tree/main/Examples/runtimes/net/src/) in the aws-database-encryption-sdk-dynamodb repository on GitHub.

**Topics**
+ [Item encryptors](#ddb-net-item-encryptors)
+ [Attribute actions](#ddb-net-attribute-actions)
+ [Encryption configuration](#ddb-net-config-encrypt)
+ [Updating items](#ddb-net-update-items)

## Item encryptors
<a name="ddb-net-item-encryptors"></a>

At its core, the AWS Database Encryption SDK for DynamoDB is an item encryptor. You can use version 3.*x* of the .NET client-side encryption library for DynamoDB to encrypt, sign, verify, and decrypt your DynamoDB table items in the following ways.

**The low-level AWS Database Encryption SDK for DynamoDB API**
You can use your [table encryption configuration](#ddb-net-config-encrypt) to construct a DynamoDB client that automatically encrypts and signs items client-side with your DynamoDB `PutItem` requests. You can use this client directly, or you can construct a [document model](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/dynamodb-intro.html#dynamodb-intro-apis-document) or [object persistence model](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/dynamodb-intro.html#dynamodb-intro-apis-object-persistence).
You must use the low-level AWS Database Encryption SDK for DynamoDB API to use [searchable encryption](searchable-encryption.md).

**The lower-level `DynamoDbItemEncryptor`**
The lower-level `DynamoDbItemEncryptor` directly encrypts and signs or decrypts and verifies your table items without calling DynamoDB. It does not make DynamoDB `PutItem` or `GetItem` requests. For example, you can use the lower-level `DynamoDbItemEncryptor` to directly decrypt and verify a DynamoDB item that you have already retrieved. If you use the lower-level `DynamoDbItemEncryptor`, we recommend using the [low-level programming model](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/dynamodb-intro.html#dynamodb-intro-apis-low-level)that the SDK for .NET provides for communicating with DynamoDB.
The lower-level `DynamoDbItemEncryptor` does not support [searchable encryption](searchable-encryption.md).

## Attribute actions in the AWS Database Encryption SDK for DynamoDB
<a name="ddb-net-attribute-actions"></a>

[Attribute actions](concepts.md#crypt-actions) determine which attribute values are encrypted and signed, which are only signed, which are signed and included in the encryption context, and which are ignored.

To specify attribute actions with the .NET client, manually define attribute actions using an object model. Specify your attribute actions by creating a `Dictionary` object in which the name-value pairs represent attribute names and the specified actions.

Specify `ENCRYPT_AND_SIGN` to encrypt and sign an attribute. Specify `SIGN_ONLY` to sign, but not encrypt, an attribute. Specify `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` to sign an attribute and include it in the encryption context. You cannot encrypt an attribute without also signing it. Specify `DO_NOTHING` to ignore an attribute.

The partition and sort attributes must be either `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`. If you define any attributes as `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`, then the partition and sort attributes must also be `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`.

**Note**
After you define your attribute actions, you must define which attributes are excluded from the signatures. To make it easier to add new unsigned attributes in the future, we recommend choosing a distinct prefix (such as "`:`") to identify your unsigned attributes. Include this prefix in the attribute name for all attributes marked `DO_NOTHING` as you define your DynamoDB schema and attribute actions.

The following object model demonstrates how to specify `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`, and `DO_NOTHING` attribute actions with the .NET client. This example uses the prefix "`:`" to identify `DO_NOTHING` attributes.

**Note**
To use the `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` cryptographic action, you must use version 3.3 or later of the AWS Database Encryption SDK. Deploy the new version to all readers before [updating your data model](ddb-update-data-model.md) to include `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`.

```
var attributeActionsOnEncrypt = new Dictionary<string, CryptoAction>
{
    ["partition_key"] = CryptoAction.SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT, // The partition attribute must be signed
    ["sort_key"] = CryptoAction.SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT, // The sort attribute must be signed
    ["attribute1"] = CryptoAction.ENCRYPT_AND_SIGN,
    ["attribute2"] = CryptoAction.SIGN_ONLY,
    ["attribute3"] = CryptoAction.SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT,
    [":attribute4"] = CryptoAction.DO_NOTHING
};
```

## Encryption configuration in the AWS Database Encryption SDK for DynamoDB
<a name="ddb-net-config-encrypt"></a>

When you use the AWS Database Encryption SDK, you must explicitly define an encryption configuration for your DynamoDB table. The values required in your encryption configuration depend on whether you defined your attribute actions manually or with an annotated data class.

The following snippet defines a DynamoDB table encryption configuration using the low-level AWS Database Encryption SDK for DynamoDB API and allowed unsigned attributes defined by a distinct prefix.

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
    // Optional: SearchConfig only required if you use beacons
    Search = new SearchConfig
    {
        WriteVersion = 1, // MUST be 1
        Versions = beaconVersions
    }
};
tableConfigs.Add(ddbTableName, config);
```

**Logical table name**
A logical table name for your DynamoDB table.
The logical table name is cryptographically bound to all data stored in the table to simplify DynamoDB restore operations. We strongly recommend specifying your DynamoDB table name as the logical table name when you first define your encryption configuration. You must always specify the same logical table name. For decryption to succeed, the logical table name must match the name specified on encryption. In the event that your DynamoDB table name changes after [restoring your DynamoDB table from a backup](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Restore.Tutorial.html), the logical table name ensures that the decrypt operation still recognizes the table.

**Allowed unsigned attributes**
The attributes marked `DO_NOTHING` in your attribute actions.
The allowed unsigned attributes tell the client which attributes are excluded from the signatures. The client assumes that all other attributes are included in the signature. Then, when decrypting a record, the client determines which attributes it needs to verify and which to ignore from the allowed unsigned attributes you specified. You cannot remove an attribute from your allowed unsigned attributes.
You can define the allowed unsigned attributes explicitly by creating an array that lists all of your `DO_NOTHING` attributes. You can also specify a distinct prefix when naming your `DO_NOTHING` attributes and use the prefix to tell the client which attributes are unsigned. We strongly recommend specifying a distinct prefix because it simplifies the process of adding a new `DO_NOTHING` attribute in the future. For more information, see [Updating your data model](ddb-update-data-model.md).
If you do not specify a prefix for all `DO_NOTHING` attributes, you can configure an `allowedUnsignedAttributes` array that explicitly lists all of the attributes that the client should expect to be unsigned when it encounters them on decryption. You should only explicitly define your allowed unsigned attributes if absolutely necessary.

**Search Configuration (Optional)**
The `SearchConfig` defines the [beacon version](using-beacons.md#beacon-version).
The `SearchConfig` must be specified to use [searchable encryption](searchable-encryption.md) or [signed beacons](configure.md#signed-beacons).

**Algorithm Suite (Optional)**
The `algorithmSuiteId` defines which algorithm suite the AWS Database Encryption SDK uses.
Unless you explicitly specify an alternative algorithm suite, the AWS Database Encryption SDK uses the [default algorithm suite](supported-algorithms.md#recommended-algorithms). The default algorithm suite uses the AES-GCM algorithm with key derivation, [digital signatures](concepts.md#digital-sigs), and [key commitment](concepts.md#key-commitment). Although the default algorithm suite is likely to be suitable for most applications, you can choose an alternate algorithm suite. For example, some trust models would be satisfied by an algorithm suite without digital signatures. For information about the algorithm suites that the AWS Database Encryption SDK supports, see [Supported algorithm suites in the AWS Database Encryption SDK](supported-algorithms.md).
To select the [AES-GCM algorithm suite without ECDSA digital signatures](supported-algorithms.md#other-algorithms), include the following snippet in your table encryption configuration.

```
AlgorithmSuiteId = DBEAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_SYMSIG_HMAC_SHA384
```

## Updating items with the AWS Database Encryption SDK
<a name="ddb-net-update-items"></a>

The AWS Database Encryption SDK does not support [ddb:UpdateItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateItem.html) for items that include encrypted or signed attributes. To update an encrypted or signed attribute, you must use [ddb:PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html). When you specify the same primary key as an existing item in your `PutItem` request, the new item completely replaces the existing item. You can also use [CLOBBER](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/datamodeling/DynamoDBMapperConfig.SaveBehavior.html#CLOBBER) to clear and replace all attributes on save after updating your items.
