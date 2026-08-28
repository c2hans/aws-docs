---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/keystore-actions.html
---

# Configure key store actions
<a name="keystore-actions"></a>

Key store actions determine what operations your users can perform and how their AWS KMS Hierarchical keyring uses the KMS keys allowlisted in your key store. The AWS Encryption SDK supports the following key store action configurations.

**Static**
When you statically configure your key store, the key store can only use the KMS key associated with the KMS key ARN you provide in the `kmsConfiguration` when you configure your key store actions. An exception is thrown if a different KMS key ARN is encountered when creating, versioning, or getting a branch key.
You can specify a multi-Region KMS key in your `kmsConfiguration`, but the key's entire ARN, including the region, is persisted in the branch keys derived from the KMS key. You cannot specify a key in a different region, you must provide the exact same multi-region key for the values to match.
When you statically configure your key store actions, you can perform usage operations (`GetActiveBranchKey`, `GetBranchKeyVersion`, `GetBeaconKey`) and administrative operations (`CreateKey` and `VersionKey`). `CreateKey` is a privileged operation that can add a new KMS key ARN to your key store allowlist. This KMS key can create new active branch keys. We recommend limiting access to this operation because once a KMS key is added to the key store, it cannot be deleted.

**Discovery**
When you configure your key store actions for discovery, the key store can use any AWS KMS key ARN that is allowlisted in your key store. However, an exception is thrown when a multi-Region KMS key is encountered and the region in the key's ARN does not match the region of the AWS KMS client being used.
When you configure your key store for discovery, you cannot perform administrative operations, such as `CreateKey` and `VersionKey`. You can only perform the usage operations that enable encrypt, decrypt, sign, and verify operations. For more information, see [Implementing least privileged permissions](keystore-least-privilege.md).

## Configure your key store actions
<a name="config-keystore-actions"></a>

Before you configure your key store actions, ensure the following prerequisites are met.
+ Determine what operations you need to perform. For more information, see [Implementing least privileged permissions](keystore-least-privilege.md).
+ Choose a logical key store name

  There must be a one-to-one mapping between the DynamoDB table name and the logical key store name. The logical key store name is cryptographically bound to all data stored in the table to simplify DynamoDB restore operations, it cannot be changed after it is initially defined by the first user. You must always specify the same logical key store name in your key store actions. For more information, see [logical key store name](create-keystore.md#logical-key-store-name).

### Static configuration
<a name="static-keystore"></a>

The following example statically configures key store actions. You must specify the name of the DynamoDB table that serves as your key store, a logical name for the key store, and the KMS key ARN that identifies a symmetric encryption KMS key.

**Note**
Carefully consider the KMS key ARN that you specify when statically configuring your key store service. The `CreateKey` operation adds the KMS key ARN to your branch key store allowlist. Once a KMS key is added to the branch key store, it cannot be deleted.

------
#### [ Java ]

```
final KeyStore keystore = KeyStore.builder().KeyStoreConfig(
	                 KeyStoreConfig.builder()
	                         .ddbClient(DynamoDbClient.create())
	                         .ddbTableName({{keyStoreName}})
	                         .logicalKeyStoreName({{logicalKeyStoreName}})
	                         .kmsClient(KmsClient.create())
	                         .kmsConfiguration(KMSConfiguration.builder()
	                                 .kmsKeyArn({{kmsKeyArn}})
	                                 .build())
	                         .build()).build();
```

------
#### [ C\# / .NET ]

```
var kmsConfig = new KMSConfiguration { KmsKeyArn = {{kmsKeyArn}} };
	 var keystoreConfig = new KeyStoreConfig
	 {
	     KmsClient = new AmazonKeyManagementServiceClient(),
	     KmsConfiguration = kmsConfig,
	     DdbTableName = {{keyStoreName}},
	     DdbClient = new AmazonDynamoDBClient(),
	     LogicalKeyStoreName = {{logicalKeyStoreName}}
	 };
	 var keystore = new KeyStore(keystoreConfig);
```

------
#### [ Python ]

```
keystore: KeyStore = KeyStore(
    config=KeyStoreConfig(
        ddb_client=ddb_client,
        ddb_table_name={{key_store_name}},
        logical_key_store_name={{logical_key_store_name}},
        kms_client=kms_client,
        kms_configuration=KMSConfigurationKmsKeyArn(
            value={{kms_key_id}}
        ),
    )
)
```

------
#### [ Rust ]

```
let sdk_config = aws_config::load_defaults(aws_config::BehaviorVersion::latest()).await;
let key_store_config = KeyStoreConfig::builder()
    .kms_client(aws_sdk_kms::Client::new(&sdk_config))
    .ddb_client(aws_sdk_dynamodb::Client::new(&sdk_config))
    .ddb_table_name({{key_store_name}})
    .logical_key_store_name({{logical_key_store_name}})
    .kms_configuration(KmsConfiguration::KmsKeyArn({{kms_key_arn}}.to_string()))
    .build()?;

let keystore = keystore_client::Client::from_conf(key_store_config)?;
```

------
#### [ Go ]

```
import (
	keystore "github.com/aws/aws-cryptographic-material-providers-library/mpl/awscryptographykeystoresmithygenerated"
	keystoretypes "github.com/aws/aws-cryptographic-material-providers-library/mpl/awscryptographykeystoresmithygeneratedtypes"
)

kmsConfig := keystoretypes.KMSConfigurationMemberkmsKeyArn{
    Value: {{kmsKeyArn}},
}
keyStore, err := keystore.NewClient(keystoretypes.KeyStoreConfig{
    DdbTableName:        {{keyStoreTableName}},
    KmsConfiguration:    &kmsConfig,
    LogicalKeyStoreName: {{logicalKeyStoreName}},
    DdbClient:           ddbClient,
    KmsClient:           kmsClient,
})
if err != nil {
    panic(err)
}
```

------

### Discovery configuration
<a name="discovery-keystore"></a>

The following example configures key store actions for discovery. You must specify the name of the DynamoDB table that serves as your key store and a logical key store name.

------
#### [ Java ]

```
final KeyStore keystore = KeyStore.builder().KeyStoreConfig(
                 KeyStoreConfig.builder()
                         .ddbClient(DynamoDbClient.create())
                         .ddbTableName({{keyStoreName}})
                         .logicalKeyStoreName({{logicalKeyStoreName}})
                         .kmsClient(KmsClient.create())
                         .kmsConfiguration(KMSConfiguration.builder()
                                 .discovery(Discovery.builder().build())
                                 .build())
                         .build()).build();
```

------
#### [ C\# / .NET ]

```
var keystoreConfig = new KeyStoreConfig
 {
     KmsClient = new AmazonKeyManagementServiceClient(),
     KmsConfiguration = new KMSConfiguration {Discovery = new Discovery()},
     DdbTableName = {{keyStoreName}},
     DdbClient = new AmazonDynamoDBClient(),
     LogicalKeyStoreName = {{logicalKeyStoreName}}
 };
 var keystore = new KeyStore(keystoreConfig);
```

------
#### [ Python ]

```
keystore: KeyStore = KeyStore(
    config=KeyStoreConfig(
        ddb_client=ddb_client,
        ddb_table_name={{key_store_name}},
        logical_key_store_name={{logical_key_store_name}},
        kms_client=kms_client,
        kms_configuration=KMSConfigurationDiscovery(
            value=Discovery()
        ),
    )
)
```

------
#### [ Rust ]

```
let key_store_config = KeyStoreConfig::builder()
        .kms_client(kms_client)
        .ddb_client(ddb_client)
        .ddb_table_name({{key_store_name}})
        .logical_key_store_name({{logical_key_store_name}})
        .kms_configuration(KmsConfiguration::Discovery(Discovery::builder().build()?))
        .build()?;
```

------
#### [ Go ]

```
import (
	keystore "github.com/aws/aws-cryptographic-material-providers-library/mpl/awscryptographykeystoresmithygenerated"
	keystoretypes "github.com/aws/aws-cryptographic-material-providers-library/mpl/awscryptographykeystoresmithygeneratedtypes"
)

kmsConfig := keystoretypes.KMSConfigurationMemberdiscovery{}
keyStore, err := keystore.NewClient(keystoretypes.KeyStoreConfig{
    DdbTableName:        {{keyStoreName}},
    KmsConfiguration:    &kmsConfig,
    LogicalKeyStoreName: {{logicalKeyStoreName}},
    DdbClient:           ddbClient,
    KmsClient:           kmsClient,
})
if err != nil {
    panic(err)
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
