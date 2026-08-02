---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-java-using.html
---

# Using the Java client-side encryption library for DynamoDB
<a name="ddb-java-using"></a>

****

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

This topic explains some of the functions and helper classes in version 4.*x* of the Java client-side encryption library for DynamoDB.

For details about programming with the Java client-side encryption library for DynamoDB, see the [Java examples](java-examples.md), the [Java examples](https://github.com/aws/aws-database-encryption-sdk-dynamodb//tree/main/Examples/runtimes/java/DynamoDbEncryption/src/main/java/software/amazon/cryptography/examples) in the aws-database-encryption-sdk-dynamodb repository on GitHub.

**Topics**
+ [Item encryptors](#ddb-item-encryptors)
+ [Attribute actions](#ddb-attribute-actions)
+ [Encryption configuration](#ddb-config-encrypt)
+ [Updating items](#ddb-update-items)
+ [Decrypting signed sets](#ddb-java-signed-sets)

## Item encryptors
<a name="ddb-item-encryptors"></a>

At its core, the AWS Database Encryption SDK for DynamoDB is an item encryptor. You can use version 4.*x* of the Java client-side encryption library for DynamoDB to encrypt, sign, verify, and decrypt your DynamoDB table items in the following ways.

**The DynamoDB Enhanced Client**
You can configure the [DynamoDB Enhanced Client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-enhanced-client.html) with the `DynamoDbEncryptionInterceptor` to automatically encrypt and sign items client-side with your DynamoDB `PutItem` requests. With the DynamoDB Enhanced Client, you can define your attribute actions using an [annotated data class](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-gs-tableschema.html#ddb-en-client-gs-tableschema-anno-bean). We recommend using the DynamoDB Enhanced Client whenever possible.
The DynamoDB Enhanced Client does not support [searchable encryption](searchable-encryption.md).
The AWS Database Encryption SDK does not support annotations on [nested attributes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-adv-features-nested.html).

**The low-level DynamoDB API**
You can configure the [low-level DynamoDB API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.LowLevelAPI.html) with the `DynamoDbEncryptionInterceptor` to automatically encrypt and sign items client-side with your DynamoDB `PutItem` requests.
You must use the low-level DynamoDB API to use [searchable encryption](searchable-encryption.md).

**The lower-level `DynamoDbItemEncryptor`**
The lower-level `DynamoDbItemEncryptor` directly encrypts and signs or decrypts and verifies your table items without calling DynamoDB. It does not make DynamoDB `PutItem` or `GetItem` requests. For example, you can use the lower-level `DynamoDbItemEncryptor` to directly decrypt and verify a DynamoDB item that you have already retrieved.
The lower-level `DynamoDbItemEncryptor` does not support [searchable encryption](searchable-encryption.md).

## Attribute actions in the AWS Database Encryption SDK for DynamoDB
<a name="ddb-attribute-actions"></a>

[Attribute actions](concepts.md#crypt-actions) determine which attribute values are encrypted and signed, which are only signed, which are signed and included in the encryption context, and which are ignored.

**Note**
To use the `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` cryptographic action, you must use version 3.3 or later of the AWS Database Encryption SDK. Deploy the new version to all readers before [updating your data model](ddb-update-data-model.md) to include `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`.

If you use the low-level DynamoDB API or the lower-level `DynamoDbItemEncryptor`, you must manually define your attribute actions. If you use the DynamoDB Enhanced Client you can either manually define your attribute actions, or you can use an annotated data class to [generate a `TableSchema`](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-gs-tableschema.html). To simplify the configuration process, we recommend using an annotated data class. When you use an annotated data class, you only have to model your object once.

**Note**
After you define your attribute actions, you must define which attributes are excluded from the signatures. To make it easier to add new unsigned attributes in the future, we recommend choosing a distinct prefix (such as "`:`") to identify your unsigned attributes. Include this prefix in the attribute name for all attributes marked `DO_NOTHING` as you define your DynamoDB schema and attribute actions.

### Use an annotated data class
<a name="ddb-attribute-actions-annotated-data-class"></a>

Use an [annotated data class](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-gs-tableschema.html#ddb-en-client-gs-tableschema-anno-bean) to specify your attribute actions with the DynamoDB Enhanced Client and `DynamoDbEncryptionInterceptor`. The AWS Database Encryption SDK for DynamoDB uses the [standard DynamoDB attribute annotations](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/mapper/annotations/package-summary.html) that define the attribute type to determine how to protect an attribute. By default, all attributes are encrypted and signed except for primary keys, which are signed but not encrypted.

**Note**
To use the `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` cryptographic action, you must use version 3.3 or later of the AWS Database Encryption SDK. Deploy the new version to all readers before [updating your data model](ddb-update-data-model.md) to include `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`.

See [SimpleClass.java](https://github.com/aws/aws-database-encryption-sdk-dynamodb//blob/main/Examples/runtimes/java/DynamoDbEncryption/src/main/java/software/amazon/cryptography/examples/enhanced/SimpleClass.java) in the aws-database-encryption-sdk-dynamodb repository on GitHub for more guidance on the DynamoDB Enhanced Client annotations.

By default, primary key attributes are signed but not encrypted (`SIGN_ONLY`) and all other attributes are encrypted and signed (`ENCRYPT_AND_SIGN`). If you define any attributes as `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`, then the partition and sort attributes must also be `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`. To specify exceptions, use the encryption annotations defined in the Java client-side encryption library for DynamoDB. For example, if you want a particular attribute to only be signed use the `@DynamoDbEncryptionSignOnly` annotation. If you want a particular attribute to be signed and included in the encryption context, use the `@DynamoDbEncryptionSignAndIncludeInEncryptionContext`. If you want a particular attribute to be neither signed nor encrypted (`DO_NOTHING`), use the `@DynamoDbEncryptionDoNothing` annotation.

**Note**
The AWS Database Encryption SDK does not support annotations on [nested attributes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-adv-features-nested.html).

The following example shows the annotations used to define `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, and `DO_NOTHING`attribute actions. For an example that shows the annotations used to define `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`, see [SimpleClass4.java](https://github.com/aws/aws-database-encryption-sdk-dynamodb//blob/main/Examples/runtimes/java/DynamoDbEncryption/src/main/java/software/amazon/cryptography/examples/enhanced/SimpleClass4.java).

```
@DynamoDbBean
public class SimpleClass {

    private String partitionKey;
    private int sortKey;
    private String attribute1;
    private String attribute2;
    private String attribute3;

    @DynamoDbPartitionKey
    @DynamoDbAttribute(value = "partition_key")
    public String getPartitionKey() {
        return this.partitionKey;
    }

    public void setPartitionKey(String partitionKey) {
        this.partitionKey = partitionKey;
    }

    @DynamoDbSortKey
    @DynamoDbAttribute(value = "sort_key")
    public int getSortKey() {
        return this.sortKey;
    }

    public void setSortKey(int sortKey) {
        this.sortKey = sortKey;
    }

    public String getAttribute1() {
        return this.attribute1;
    }

    public void setAttribute1(String attribute1) {
        this.attribute1 = attribute1;
    }

    @DynamoDbEncryptionSignOnly
    public String getAttribute2() {
        return this.attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }

    @DynamoDbEncryptionDoNothing
    public String getAttribute3() {
        return this.attribute3;
    }

    @DynamoDbAttribute(value = ":attribute3")
    public void setAttribute3(String attribute3) {
        this.attribute3 = attribute3;
    }

}
```

Use your annotated data class to create the `TableSchema` as shown in the following snippet.

```
final TableSchema<{{SimpleClass}}> tableSchema = TableSchema.fromBean({{SimpleClass}}.class);
```

### Manually define your attribute actions
<a name="ddb-attribute-actions-manual"></a>

To manually specify attribute actions, create a `Map` object in which the name-value pairs represent attribute names and the specified actions.

Specify `ENCRYPT_AND_SIGN` to encrypt and sign an attribute. Specify `SIGN_ONLY` to sign, but not encrypt, an attribute. Specify `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` to sign an attribute and include it in the encryption context. You cannot encrypt an attribute without also signing it. Specify `DO_NOTHING` to ignore an attribute.

The partition and sort attributes must be either `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`. If you define any attributes as `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`, then the partition and sort attributes must also be `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`.

**Note**
To use the `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` cryptographic action, you must use version 3.3 or later of the AWS Database Encryption SDK. Deploy the new version to all readers before [updating your data model](ddb-update-data-model.md) to include `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`.

```
final Map<String, CryptoAction> attributeActionsOnEncrypt = new HashMap<>();
// The partition attribute must be signed
attributeActionsOnEncrypt.put("partition_key", CryptoAction.SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT);
// The sort attribute must be signed
attributeActionsOnEncrypt.put("sort_key", CryptoAction.SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT);
attributeActionsOnEncrypt.put("attribute1", CryptoAction.ENCRYPT_AND_SIGN);
attributeActionsOnEncrypt.put("attribute2", CryptoAction.SIGN_ONLY);
attributeActionsOnEncrypt.put("attribute3", CryptoAction.SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT);
attributeActionsOnEncrypt.put(":attribute4", CryptoAction.DO_NOTHING);
```

## Encryption configuration in the AWS Database Encryption SDK for DynamoDB
<a name="ddb-config-encrypt"></a>

When you use the AWS Database Encryption SDK, you must explicitly define an encryption configuration for your DynamoDB table. The values required in your encryption configuration depend on whether you defined your attribute actions manually or with an annotated data class.

The following snippet defines a DynamoDB table encryption configuration using the DynamoDB Enhanced Client, [https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-gs-tableschema.html](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-gs-tableschema.html), and allowed unsigned attributes defined by a distinct prefix.

```
final Map<String, DynamoDbEnhancedTableEncryptionConfig> tableConfigs = new HashMap<>();
tableConfigs.put(ddbTableName,
        DynamoDbEnhancedTableEncryptionConfig.builder()
            .logicalTableName(ddbTableName)
            .keyring(kmsKeyring)
            .allowedUnsignedAttributePrefix(unsignedAttrPrefix)
            .schemaOnEncrypt(tableSchema)
            // Optional: only required if you use beacons
            .search(SearchConfig.builder()
                    .writeVersion(1) // MUST be 1
                    .versions(beaconVersions)
                    .build())
            .build());
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
.algorithmSuiteId(
    DBEAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_SYMSIG_HMAC_SHA384)
```

## Updating items with the AWS Database Encryption SDK
<a name="ddb-update-items"></a>

The AWS Database Encryption SDK does not support [ddb:UpdateItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateItem.html) for items that have been encrypted or signed. To update an encrypted or signed item, you must use [ddb:PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html). When you specify the same primary key as an existing item in your `PutItem` request, the new item completely replaces the existing item. You can also use [CLOBBER](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/datamodeling/DynamoDBMapperConfig.SaveBehavior.html#CLOBBER) to clear and replace all attributes on save after updating your items.

## Decrypting signed sets
<a name="ddb-java-signed-sets"></a>

In versions 3.0.0 and 3.1.0 of the AWS Database Encryption SDK, if you define a [set type](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.SetTypes) attribute as `SIGN_ONLY`, the values of the set are canonicalized in the order that they are provided. DynamoDB does not preserve the order of sets. As a result, there is a chance that signature validation of the item that contains the set will fail. Signature validation fails when the values of the set are returned in a different order than they were provided to the AWS Database Encryption SDK, even if the set attributes contain the same values.

**Note**
Versions 3.1.1 and later of the AWS Database Encryption SDK canonicalize the values of all set type attributes, so that the values are read in the same order that they were written to DynamoDB.

If signature validation fails, the decrypt operation fails and returns the following error message.

|  |
| --- |
| software.amazon.cryptography.dbencryptionsdk.structuredencryption.model.StructuredEncryptionException: No recipient tag matched. |

If you receive the above error message, and believe that the item you are trying to decrypt includes a set that was signed using version 3.0.0 or 3.1.0, see the [DecryptWithPermute](https://github.com/aws/aws-database-encryption-sdk-dynamodb-java/tree/v3.1.1/DecryptWithPermute) directory of the aws-database-encryption-sdk-dynamodb-java repository on GitHub for details on how to successfully validate the set.
