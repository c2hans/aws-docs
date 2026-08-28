---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-java-migrate.html
---

# Migrate to version 4.x of the Java client-side encryption library for DynamoDB
<a name="ddb-java-migrate"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

Version 3.*x* of the Java client-side encryption library for DynamoDB is a major rewrite of the 2.*x* code base. It includes many updates, such as a new structured data format, improved multitenancy support, seamless schema changes, and searchable encryption support. Version 4.*x* of the AWS Database Encryption SDK for Java replaces the embedded 2.*x* library with an implementation based on AWS SDK for Java 2.*x*, removing the dependency on AWS SDK for Java 1.*x*. This topic provides guidance on how to migrate your code to version 4.*x*.

## Migrating from version 1.x to 2.x
<a name="ddb-java-v1-to-v2"></a>

Migrate to version 2.*x* before you migrate to version 3.*x* or 4.*x*. Version 2.*x* changed the symbol for the Most Recent Provider from `MostRecentProvider` to `CachingMostRecentProvider`. If you currently use version 1.*x* of the Java client-side encryption library for DynamoDB with the `MostRecentProvider` symbol, you must update the symbol name in your code to `CachingMostRecentProvider`. For more information, see [Updates to the Most Recent Provider](most-recent-provider.md#mrp-versions).

## Migrating from version 2.x to 3.x
<a name="ddb-java-v2-to-v3"></a>

The following procedures describe how to migrate your code from version 2.*x* to version 3.*x* of the Java client-side encryption library for DynamoDB.

### Step 1. Prepare to read items in the new format
<a name="ddb-java-migrate-step1"></a>

Complete the following steps to prepare your AWS Database Encryption SDK client to read items in the new format. After you deploy the following changes, your client will continue to behave in the same manner that it did in version 2.*x*. Your client will continue to read and write items in the version 2.*x* format, but these changes prepare the client to [read items in the new format](#ddb-java-migrate-step2).

**Update your AWS SDK for Java to version 2.x**
Version 3.*x* of the Java client-side encryption library for DynamoDB requires the [DynamoDB Enhanced Client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-enhanced-client.html). The DynamoDB Enhanced Client replaces the [DynamoDBMapper](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBMapper.Methods.html) used in previous versions. To use the enhanced client, you must use the AWS SDK for Java 2.x.
Follow the instructions for [migrating from version 1.x to 2.x of the AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration.html).
For more information on what AWS SDK for Java 2.x modules are required, see [Prerequisites](ddb-java.md#ddb-java-prerequisites).

**Configure your client to read items encrypted by legacy versions**
The following procedures provide an overview of the steps demonstrated in the code example below.

1. Create a [keyring](keyrings.md).

   Keyrings and [cryptographic materials managers](concepts.md#crypt-materials-manager) replace the cryptographic materials providers used in previous versions of the Java client-side encryption library for DynamoDB.
**Important**
The wrapping keys you specify when creating a keyring must be the same wrapping keys you used with your cryptographic materials provider in version 2.*x*.

1. Create a table schema over your annotated class.

   This step defines the attribute actions that will be used when you begin writing items in the new format.

   For guidance on using the new DynamoDB Enhanced Client, see the [Generate a `TableSchema`](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-gs-tableschema.html) in the *AWS SDK for Java Developer Guide*.

   The following example assumes you updated your annotated class from version 2.*x* using the new attribute actions annotations. For more guidance on annotating your attribute actions, see [Use an annotated data class](ddb-java-using.md#ddb-attribute-actions-annotated-data-class).
**Note**
If you specify any `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attributes, then the partition and sort attributes must also be `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`. For an example that shows the annotations used to define `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`, see [SimpleClass4.java](https://github.com/aws/aws-database-encryption-sdk-dynamodb//blob/main/Examples/runtimes/java/DynamoDbEncryption/src/main/java/software/amazon/cryptography/examples/enhanced/SimpleClass4.java).

1. Define which [attributes are excluded from the signature](ddb-java-using.md#allowed-unauth).

1. Configure an explicit map of the attribute actions configured in your version 2.x modeled class.

   This step defines the attribute actions used to write items in the old format.

1. Configure the `DynamoDBEncryptor` you used in version 2.*x* of the Java client-side encryption library for DynamoDB.

1. Configure the legacy behavior.

1. Create a `DynamoDbEncryptionInterceptor`.

1. Create a new AWS SDK DynamoDB client.

1. Create the `DynamoDBEnhancedClient` and create a table with your modeled class.

   For more information on the DynamoDB Enhanced Client, see [create an enhanced client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-getting-started-dynamodbTable.html#ddb-en-client-getting-started-dynamodbTable-eclient).

```
public class MigrationExampleStep1 {

    public static void MigrationStep1(String kmsKeyId, String ddbTableName, int sortReadValue) {
        // 1. Create a Keyring.
        //    This example creates an AWS KMS Keyring that specifies the
        //    same kmsKeyId previously used in the version 2.x configuration.
        //    It uses the 'CreateMrkMultiKeyring' method to create the
        //    keyring, so that the keyring can correctly handle both single
        //    region and Multi-Region KMS Keys.
        //    Note that this example uses the AWS SDK for Java v2 KMS client.
        final MaterialProviders matProv = MaterialProviders.builder()
                .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
                .build();
        final CreateAwsKmsMrkMultiKeyringInput keyringInput = CreateAwsKmsMrkMultiKeyringInput.builder()
                .generator({{kmsKeyId}})
                .build();
        final IKeyring kmsKeyring = matProv.CreateAwsKmsMrkMultiKeyring(keyringInput);

        // 2. Create a Table Schema over your annotated class.
        //    For guidance on using the new attribute actions
        //    annotations, see SimpleClass.java in the
        //    aws-database-encryption-sdk-dynamodb GitHub repository.
        //    All primary key attributes must be signed but not encrypted
        //    and by default all non-primary key attributes
        //    are encrypted and signed (ENCRYPT_AND_SIGN).
        //    If you want a particular non-primary key attribute to be signed but
        //    not encrypted, use the 'DynamoDbEncryptionSignOnly' annotation.
        //    If you want a particular attribute to be neither signed nor encrypted
        //    (DO_NOTHING), use the 'DynamoDbEncryptionDoNothing' annotation.
        final TableSchema<SimpleClass> schemaOnEncrypt = TableSchema.fromBean(SimpleClass.class);

        // 3. Define which attributes the client should expect to be excluded
        //    from the signature when reading items.
        //    This value represents all unsigned attributes across the entire
        //    dataset.
        final List<String> allowedUnsignedAttributes = Arrays.asList("attribute3");

        // 4. Configure an explicit map of the attribute actions configured
        //    in your version 2.x modeled class.
        final Map<String, CryptoAction> legacyActions = new HashMap<>();
        legacyActions.put("{{partition_key}}", CryptoAction.SIGN_ONLY);
        legacyActions.put("{{sort_key}}", CryptoAction.SIGN_ONLY);
        legacyActions.put("{{attribute1}}", CryptoAction.ENCRYPT_AND_SIGN);
        legacyActions.put("{{attribute2}}", CryptoAction.SIGN_ONLY);
        legacyActions.put("{{attribute3}}", CryptoAction.DO_NOTHING);

        // 5. Configure the DynamoDBEncryptor that you used in version 2.x.
        final AWSKMS kmsClient = AWSKMSClientBuilder.defaultClient();
        final DirectKmsMaterialProvider cmp = new DirectKmsMaterialProvider(kmsClient, kmsKeyId);
        final DynamoDBEncryptor oldEncryptor = DynamoDBEncryptor.getInstance(cmp);

        // 6. Configure the legacy behavior.
        //    Input the DynamoDBEncryptor and attribute actions created in
        //    the previous steps. For Legacy Policy, use
        //    'FORCE_LEGACY_ENCRYPT_ALLOW_LEGACY_DECRYPT'. This policy continues to read
        //    and write items using the old format, but will be able to read
        //    items written in the new format as soon as they appear.
        final LegacyOverride legacyOverride = LegacyOverride
                .builder()
                .encryptor(oldEncryptor)
                .policy(LegacyPolicy.FORCE_LEGACY_ENCRYPT_ALLOW_LEGACY_DECRYPT)
                .attributeActionsOnEncrypt(legacyActions)
                .build();

        // 7. Create a DynamoDbEncryptionInterceptor with the above configuration.
        final Map<String, DynamoDbEnhancedTableEncryptionConfig> tableConfigs = new HashMap<>();
        tableConfigs.put(ddbTableName,
                DynamoDbEnhancedTableEncryptionConfig.builder()
                        .logicalTableName({{ddbTableName}})
                        .keyring({{kmsKeyring}})
                        .allowedUnsignedAttributes(allowedUnsignedAttributes)
                        .schemaOnEncrypt(tableSchema)
                        .legacyOverride(legacyOverride)
                        .build());
        final DynamoDbEncryptionInterceptor interceptor =
                DynamoDbEnhancedClientEncryption.CreateDynamoDbEncryptionInterceptor(
                        CreateDynamoDbEncryptionInterceptorInput.builder()
                                .tableEncryptionConfigs(tableConfigs)
                                .build()
                );

        // 8. Create a new AWS SDK DynamoDb client using the
        //    interceptor from Step 7.
        final DynamoDbClient ddb = DynamoDbClient.builder()
                .overrideConfiguration(
                        ClientOverrideConfiguration.builder()
                                .addExecutionInterceptor(interceptor)
                                .build())
                .build();

        // 9. Create the DynamoDbEnhancedClient using the AWS SDK DynamoDb client
        //    created in Step 8, and create a table with your modeled class.
        final DynamoDbEnhancedClient enhancedClient = DynamoDbEnhancedClient.builder()
                .dynamoDbClient(ddb)
                .build();
        final DynamoDbTable<SimpleClass> table = enhancedClient.table(ddbTableName, tableSchema);
    }
}
```

### Step 2. Write items in the new format
<a name="ddb-java-migrate-step2"></a>

After you have deployed the changes from Step 1 to all readers, complete the following steps to configure your AWS Database Encryption SDK client to write items in the new format. After you deploy the following changes, your client will continue read items in the old format and start writing and reading items in the new format.

The following procedures provide an overview of the steps demonstrated in the code example below.

1. Continue configuring your keyring, table schema, legacy attribute actions, `allowedUnsignedAttributes`, and `DynamoDBEncryptor` as you did in [**Step 1**](#ddb-java-migrate-step1).

1. Update your legacy behavior to only write new items using the new format.

1. Create a `DynamoDbEncryptionInterceptor `

1. Create a new AWS SDK DynamoDB client.

1. Create the `DynamoDBEnhancedClient` and create a table with your modeled class.

   For more information on the DynamoDB Enhanced Client, see [create an enhanced client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-getting-started-dynamodbTable.html#ddb-en-client-getting-started-dynamodbTable-eclient).

```
public class MigrationExampleStep2 {

    public static void MigrationStep2(String kmsKeyId, String ddbTableName, int sortReadValue) {
        // 1. Continue to configure your keyring, table schema, legacy
        //    attribute actions, allowedUnsignedAttributes, and
        //    DynamoDBEncryptor as you did in Step 1.
        final MaterialProviders matProv = MaterialProviders.builder()
                .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
                .build();
        final CreateAwsKmsMrkMultiKeyringInput keyringInput = CreateAwsKmsMrkMultiKeyringInput.builder()
                .generator({{kmsKeyId}})
                .build();
        final IKeyring kmsKeyring = matProv.CreateAwsKmsMrkMultiKeyring(keyringInput);

        final TableSchema<SimpleClass> schemaOnEncrypt = TableSchema.fromBean(SimpleClass.class);

        final List<String> allowedUnsignedAttributes = Arrays.asList("attribute3");

        final Map<String, CryptoAction> legacyActions = new HashMap<>();
        legacyActions.put("{{partition_key}}", CryptoAction.SIGN_ONLY);
        legacyActions.put("{{sort_key}}", CryptoAction.SIGN_ONLY);
        legacyActions.put("{{attribute1}}", CryptoAction.ENCRYPT_AND_SIGN);
        legacyActions.put("{{attribute2}}", CryptoAction.SIGN_ONLY);
        legacyActions.put("{{attribute3}}", CryptoAction.DO_NOTHING);

        final AWSKMS kmsClient = AWSKMSClientBuilder.defaultClient();
        final DirectKmsMaterialProvider cmp = new DirectKmsMaterialProvider(kmsClient, kmsKeyId);
        final DynamoDBEncryptor oldEncryptor = DynamoDBEncryptor.getInstance(cmp);

        // 2. Update your legacy behavior to only write new items using the new
        //    format.
        //    For Legacy Policy, use 'FORBID_LEGACY_ENCRYPT_ALLOW_LEGACY_DECRYPT'. This policy
        //    continues to read items in both formats, but will only write items
        //    using the new format.
        final LegacyOverride legacyOverride = LegacyOverride
                .builder()
                .encryptor(oldEncryptor)
                .policy(LegacyPolicy.FORBID_LEGACY_ENCRYPT_ALLOW_LEGACY_DECRYPT)
                .attributeActionsOnEncrypt(legacyActions)
                .build();

        // 3. Create a DynamoDbEncryptionInterceptor with the above configuration.
        final Map<String, DynamoDbEnhancedTableEncryptionConfig> tableConfigs = new HashMap<>();
        tableConfigs.put(ddbTableName,
                DynamoDbEnhancedTableEncryptionConfig.builder()
                        .logicalTableName({{ddbTableName}})
                        .keyring({{kmsKeyring}})
                        .allowedUnsignedAttributes(allowedUnsignedAttributes)
                        .schemaOnEncrypt(tableSchema)
                        .legacyOverride(legacyOverride)
                        .build());
        final DynamoDbEncryptionInterceptor interceptor =
                DynamoDbEnhancedClientEncryption.CreateDynamoDbEncryptionInterceptor(
                        CreateDynamoDbEncryptionInterceptorInput.builder()
                                .tableEncryptionConfigs(tableConfigs)
                                .build()
                );

        // 4. Create a new AWS SDK DynamoDb client using the
        //    interceptor from Step 3.
        final DynamoDbClient ddb = DynamoDbClient.builder()
                .overrideConfiguration(
                        ClientOverrideConfiguration.builder()
                                .addExecutionInterceptor(interceptor)
                                .build())
                .build();

        // 5. Create the DynamoDbEnhancedClient using the AWS SDK DynamoDb Client created
        //    in Step 4, and create a table with your modeled class.
        final DynamoDbEnhancedClient enhancedClient = DynamoDbEnhancedClient.builder()
                .dynamoDbClient(ddb)
                .build();
        final DynamoDbTable<SimpleClass> table = enhancedClient.table(ddbTableName, tableSchema);
    }
}
```

After deploying the Step 2 changes, you must re-encrypt all old items in your table with the new format before you can continue on to [Step 3](#ddb-java-migrate-step3). There is no single metric or query that you can run to quickly encrypt your existing items. Use the process that makes the most sense for your system. For example, you could use an asynchronous process that slowly scans the table and the rewrites the items using the new attribute actions and encryption configuration you defined.

### Step 3. Only read and write items in the new format
<a name="ddb-java-migrate-step3"></a>

After re-encrypting all of the items in your table with the new format, you can remove the legacy behavior from your configuration. Complete the following steps to configure your client to only read and write items in the new format.

The following procedures provide an overview of the steps demonstrated in the code example below.

1. Continue configuring your keyring, table schema, and `allowedUnsignedAttributes` as you did in [**Step 1**](#ddb-java-migrate-step1). Remove the legacy attribute actions and `DynamoDBEncryptor` from your configuration.

1. Create a `DynamoDbEncryptionInterceptor`.

1. Create a new AWS SDK DynamoDB client.

1. Create the `DynamoDBEnhancedClient` and create a table with your modeled class.

   For more information on the DynamoDB Enhanced Client, see [create an enhanced client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-getting-started-dynamodbTable.html#ddb-en-client-getting-started-dynamodbTable-eclient).

```
public class MigrationExampleStep3 {

    public static void MigrationStep3(String kmsKeyId, String ddbTableName, int sortReadValue) {
        // 1. Continue to configure your keyring, table schema,
        //    and allowedUnsignedAttributes as you did in Step 1.
        //    Do not include the configurations for the DynamoDBEncryptor or
        //    the legacy attribute actions.
        final MaterialProviders matProv = MaterialProviders.builder()
                .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
                .build();
        final CreateAwsKmsMrkMultiKeyringInput keyringInput = CreateAwsKmsMrkMultiKeyringInput.builder()
                .generator({{kmsKeyId}})
                .build();
        final IKeyring kmsKeyring = matProv.CreateAwsKmsMrkMultiKeyring(keyringInput);

        final TableSchema<SimpleClass> schemaOnEncrypt = TableSchema.fromBean(SimpleClass.class);

        final List<String> allowedUnsignedAttributes = Arrays.asList("attribute3");

        // 3. Create a DynamoDbEncryptionInterceptor with the above configuration.
        //    Do not configure any legacy behavior.
        final Map<String, DynamoDbEnhancedTableEncryptionConfig> tableConfigs = new HashMap<>();
        tableConfigs.put(ddbTableName,
                DynamoDbEnhancedTableEncryptionConfig.builder()
                        .logicalTableName({{ddbTableName}})
                        .keyring({{kmsKeyring}})
                        .allowedUnsignedAttributes(allowedUnsignedAttributes)
                        .schemaOnEncrypt(tableSchema)
                        .build());
        final DynamoDbEncryptionInterceptor interceptor =
                DynamoDbEnhancedClientEncryption.CreateDynamoDbEncryptionInterceptor(
                        CreateDynamoDbEncryptionInterceptorInput.builder()
                                .tableEncryptionConfigs(tableConfigs)
                                .build()
                );

        // 4. Create a new AWS SDK DynamoDb client using the
        //    interceptor from Step 3.
        final DynamoDbClient ddb = DynamoDbClient.builder()
                .overrideConfiguration(
                        ClientOverrideConfiguration.builder()
                                .addExecutionInterceptor(interceptor)
                                .build())
                .build();

        // 5. Create the DynamoDbEnhancedClient using the AWS SDK Client
        //    created in Step 4, and create a table with your modeled class.
        final DynamoDbEnhancedClient enhancedClient = DynamoDbEnhancedClient.builder()
                .dynamoDbClient(ddb)
                .build();
        final DynamoDbTable<SimpleClass> table = enhancedClient.table(ddbTableName, tableSchema);
    }
}
```

## Migrating from version 3.x to 4.x
<a name="ddb-java-v3-to-v4"></a>

Version 4.*x* replaces AWS SDK for Java 1.x with AWS SDK for Java 2.x in the embedded version 2.*x* code. The version 3.*x* APIs are unchanged.

If your code uses only version 3.*x* APIs and does not use the embedded version 2.*x* code, no changes are required.

If your code uses the embedded version 2.*x* code, you must update your code to use the AWS SDK for Java 2.*x* symbols. For examples of the updated symbols, see [Java examples](java.md). The embedded version 2.*x* code no longer includes `DynamoDBMapper`, as AWS SDK for Java 2.*x* does not support `DynamoDBMapper`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
