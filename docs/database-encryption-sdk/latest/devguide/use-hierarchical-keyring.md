---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/use-hierarchical-keyring.html
---

# AWS KMS Hierarchical keyrings
<a name="use-hierarchical-keyring"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

**Note**
As of July 24, 2023, branch keys created during the developer preview are not supported. Create new branch keys to continue using the key store that you created during the developer preview.

With the AWS KMS Hierarchical keyring, you can protect your cryptographic materials under a symmetric encryption KMS key without calling AWS KMS every time you encrypt or decrypt a record. It is a good choice for applications that need to minimize calls to AWS KMS, and applications that can reuse some cryptographic materials without violating their security requirements.

The Hierarchical keyring is a cryptographic materials caching solution that reduces the number of AWS KMS calls by using AWS KMS protected *branch keys* persisted in an Amazon DynamoDB table, and then locally caching branch key materials used in encrypt and decrypt operations. The DynamoDB table serves as the key store that manages and protects branch keys. It stores the active branch key and all previous versions of the branch key. The *active* branch key is the most recent branch key version. The Hierarchical keyring uses a unique data encryption key for each encrypt request and encrypts each data encryption key with a unique wrapping key derived from the active branch key. The Hierarchical keyring is dependent on the hierarchy established between active branch keys and their derived wrapping keys.

The Hierarchical keyring typically uses each branch key version to satisfy multiple requests. But you control the extent to which active branch keys are reused and determine how often the active branch key is rotated. The active version of the branch key remains active until you [rotate it](rotate-branch-key.md). Previous versions of the active branch key will not be used to perform encrypt operations, but they can still be queried and used in decrypt operations.

When you instantiate the Hierarchical keyring, it creates a local cache. You specify a [cache limit](#cache-limit) that defines the maximum amount of time that the branch key materials are stored within the local cache before they expire and are evicted from the cache. The Hierarchical keyring makes one AWS KMS call to decrypt the branch key and assemble the branch key materials the first time a `branch-key-id` is specified in an operation. Then, the branch key materials are stored in the local cache and reused for all encrypt and decrypt operations that specify that `branch-key-id` until the cache limit expires. Storing branch key materials in the local cache reduces AWS KMS calls. For example, consider a cache limit of 15 minutes. If you perform 10,000 encrypt operations within that cache limit, the [traditional AWS KMS keyring](use-kms-keyring.md) would need to make 10,000 AWS KMS calls to satisfy 10,000 encrypt operations. If you have one active `branch-key-id`, the Hierarchical keyring only needs to make one AWS KMS call to satisfy 10,000 encrypt operations.

The local cache separates encryption materials from decryption materials. The encryption materials are assembled from the active branch key and reused for all encrypt operations until the cache limit expires. The decryption materials are assembled from the branch key ID and version that is identified in the encrypted field's metadata, and they are reused for all decrypt operations related to the branch key ID and version until the cache limit expires. The local cache can store multiple versions of the same branch key at a time. When the local cache is configured to use a [branch key ID supplier](#branch-key-id-supplier), it can also store branch key materials from multiple active branch keys at a time.

**Note**
All mentions of *Hierarchical keyring* in the AWS Database Encryption SDK refer to the AWS KMS Hierarchical keyring.

**Topics**
+ [How it works](#how-hierarchical-keyring-works)
+ [Prerequisites](#hierarchical-keyring-prereqs)
+ [Required permissions](#hierarchical-keyring-permissions)
+ [Choose a cache](#hierarchical-keyring-caches)
+ [Create a Hierarchical keyring](#initialize-hierarchical-keyring)
+ [Using the Hierarchical keyring for searchable encryption](#searchable-encryption-hierarchical-keyrings)

## How it works
<a name="how-hierarchical-keyring-works"></a>

The following walkthroughs describe how the Hierarchical keyring assembles encryption and decryption materials, and the different calls that the keyring makes for encrypt and decrypt operations. For technical details on the wrapping key derivation and plaintext data key encryption processes, see [AWS KMS Hierarchical keyring technical details](reference.md#hierarchical-keyring-details).

**Encrypt and sign**
The following walkthrough describes how the Hierarchical keyring assembles encryption materials and derives a unique wrapping key.

1. The encryption method asks the Hierarchical keyring for encryption materials. The keyring generates a plaintext data key, then checks to see if there are valid branch key materials in the local cache to generate the wrapping key. If there are valid branch key materials, the keyring proceeds to **Step 4**.

1. If there are no valid branch key materials, the Hierarchical keyring queries the key store for the active branch key.

   1. The key store calls AWS KMS to decrypt the active branch key and returns the plaintext active branch key. Data identifying the active branch key is serialized to provide additional authenticated data (AAD) in the decrypt call to AWS KMS.

   1. The key store returns the plaintext branch key and data that identifies it, such as the branch key version.

1. The Hierarchical keyring assembles branch key materials (the plaintext branch key and branch key version) and stores a copy of them in the local cache.

1. The Hierarchical keyring derives a unique wrapping key from the plaintext branch key and a 16-byte random salt. It uses the derived wrapping key to encrypt a copy of the plaintext data key.

The encryption method uses the encryption materials to encrypt and sign the record. For more information on how records are encrypted and signed in the AWS Database Encryption SDK, see [Encrypt and sign](how-it-works.md#encrypt-and-sign).

**Decrypt and verify**
The following walkthrough describes how the Hierarchical keyring assembles decryption materials and decrypts the encrypted data key.

1. The decryption method identifies the encrypted data key from the material description field of the encrypted record, and passes it to the Hierarchical keyring.

1. The Hierarchical keyring deserializes data identifying the encrypted data key, including the branch key version, the 16-byte salt, and other information describing how the data key was encrypted.

   For more information, see [AWS KMS Hierarchical keyring technical details](reference.md#hierarchical-keyring-details).

1. The Hierarchical keyring checks to see if there are valid branch key materials in the local cache that match the branch key version identified in **Step 2**. If there are valid branch key materials, the keyring proceeds to **Step 6**.

1. If there are no valid branch key materials, the Hierarchical keyring queries the key store for the branch key that matches the branch key version identified in **Step 2**.

   1. The key store calls AWS KMS to decrypt the branch key and returns the plaintext active branch key. Data identifying the active branch key is serialized to provide additional authenticated data (AAD) in the decrypt call to AWS KMS.

   1. The key store returns the plaintext branch key and data that identifies it, such as the branch key version.

1. The Hierarchical keyring assembles branch key materials (the plaintext branch key and branch key version) and stores a copy of them in the local cache.

1. The Hierarchical keyring uses the assembled branch key materials and the 16-byte salt identified in **Step 2** to reproduce the unique wrapping key that encrypted the data key.

1. The Hierarchical keyring uses the reproduced wrapping key to decrypt the data key and returns the plaintext data key.

The decryption method uses the decryption materials and plaintext data key to decrypt and verify the record. For more information on how records are decrypted and verified in the AWS Database Encryption SDK, see [Decrypt and verify](how-it-works.md#decrypt-and-verify).

## Prerequisites
<a name="hierarchical-keyring-prereqs"></a>

Before you create and use a Hierarchical keyring, ensure the following prerequisites are met.
+ You, or your key store administrator, have [created a key store](create-keystore.md) and [created at least one active branch key](create-branch-keys.md).
+ You have [configured your key store actions](keystore-actions.md#config-keystore-actions).
**Note**
How you configure your key store actions determines what operations you can perform and what KMS keys the Hierarchical keyring can use. For more information, see [Key store actions](keystore-actions.md).
+ You have the required AWS KMS permissions to access and use the key store and branch keys. For more information, see [Required permissions](#hierarchical-keyring-permissions).
+ You have reviewed the supported cache types and configured the cache type that best fits your needs. For more information, see [Choose a cache](#hierarchical-keyring-caches)

## Required permissions
<a name="hierarchical-keyring-permissions"></a>

The AWS Database Encryption SDK doesn't require an AWS account and it doesn't depend on any AWS service. However, to use an Hierarchical keyring, you need an AWS account and the following minimum permissions on the symmetric encryption AWS KMS key(s) in your key store.
+ To encrypt and decrypt data with the Hierarchical keyring, you need [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html).
+ To [create](create-branch-keys.md) and [rotate](rotate-branch-key.md) branch keys, you need [kms:GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html) and [kms:ReEncrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html).

For more information on controlling access to your branch keys and key store, see [Implementing least privileged permissions](keystore-least-privilege.md).

## Choose a cache
<a name="hierarchical-keyring-caches"></a>

The Hierarchical keyring reduces the number of calls made to AWS KMS by locally caching the branch key materials used in encrypt and decrypt operations. Before you [create your Hierarchical keyring](#initialize-hierarchical-keyring), you need to decide what type of cache you want to use. You can use the default cache or customize the cache to best fits your needs.

The Hierarchical keyring supports the following cache types:
+ [Default cache](#cache-default)
+ [MultiThreaded cache](#cache-multithreaded)
+ [StormTracking cache](#cache-stormtracking)
+ [Shared cache](#cache-shared)

### Default cache
<a name="cache-default"></a>

For most users, the Default cache fulfills their threading requirements. The Default cache is designed to support heavily multithreaded environments. When a branch key materials entry expires, the Default cache prevents multiple threads from calling AWS KMS by notifying one thread that the branch key materials entry is going to expire 10 seconds in advance. This ensures that only one thread sends a request to AWS KMS to refresh the cache.

The Default and StormTracking caches support the same threading model, but you only need to specify the entry capacity to use the Default cache. For more granular cache customizations, use the [StormTracking cache](#cache-stormtracking).

Unless you want to customize the number of branch key materials entries that can be stored in the local cache, you do not need to specify a cache type when you create the Hierarchical keyring. If you do not specify a cache type, the Hierarchical keyring uses the Default cache type and sets the entry capacity to 1000.

To customize the Default cache, specify the following values:
+ **Entry capacity**: limits the number of branch key materials entries that can be stored in the local cache.

------
#### [ Java ]

```
.cache(CacheType.builder()
        .Default(DefaultCache.builder()
        .entryCapacity({{100}})
        .build())
```

------
#### [ C\# / .NET ]

```
CacheType defaultCache = new CacheType
{
    Default = new DefaultCache{EntryCapacity = {{100}}}
};
```

------
#### [ Rust ]

```
let cache: CacheType = CacheType::Default(
    DefaultCache::builder()
        .entry_capacity({{100}})
        .build()?,
);
```

------

### MultiThreaded cache
<a name="cache-multithreaded"></a>

The MultiThreaded cache is safe to use in multithreaded environments, but it does not provide any functionality to minimize AWS KMS or Amazon DynamoDB calls. As a result, when a branch key materials entry expires, all threads will be notified at the same time. This can result in multiple AWS KMS calls to refresh the cache.

To use the MultiThreaded cache, specify the following values:
+ **Entry capacity**: limits the number of branch key materials entries that can be stored in the local cache.
+ **Entry pruning tail size**: defines the number of entries to prune if the entry capacity is reached.

------
#### [ Java ]

```
.cache(CacheType.builder()
        .MultiThreaded(MultiThreadedCache.builder()
        .entryCapacity({{100}})
        .entryPruningTailSize({{1}})
        .build())
```

------
#### [ C\# / .NET ]

```
CacheType multithreadedCache = new CacheType
{
    MultiThreaded = new MultiThreadedCache
    {
        EntryCapacity = {{100}},
        EntryPruningTailSize = {{1}}
    }
};
```

------
#### [ Rust ]

```
CacheType::MultiThreaded(
            MultiThreadedCache::builder()
                    .entry_capacity({{100}})
                    .entry_pruning_tail_size({{1}})
                    .build()?)
```

------

### StormTracking cache
<a name="cache-stormtracking"></a>

The StormTracking cache is designed to support heavily multithreaded environments. When a branch key materials entry expires, the StormTracking cache prevents multiple threads from calling AWS KMS by notifying one thread that the branch key materials entry is going to expire in advance. This ensures that only one thread sends a request to AWS KMS to refresh the cache.

To use the StormTracking cache, specify the following values:
+ **Entry capacity**: limits the number of branch key materials entries that can be stored in the local cache.

  Default value: 1000 entries
+ **Entry pruning tail size**: defines the number of branch key materials entries to prune at a time.

  Default value: 1 entry
+ **Grace period**: defines the number of seconds before expiration that an attempt to refresh branch key materials is made.

  Default value: 10 seconds
+ **Grace interval**: defines the number of seconds between attempts to refresh the branch key materials.

  Default value: 1 seconds
+ **Fan out**: defines the number of simultaneous attempts that can be made to refresh the branch key materials.

  Default value: 20 attempts
+ **In flight time to live (TTL)**: defines the number of seconds until an attempt to refresh the branch key materials times out. Any time the cache returns `NoSuchEntry` in response to a `GetCacheEntry`, that branch key is considered to be *in flight* until the same key is written with a `PutCache` entry.

  Default value: 10 seconds
+ **Sleep**: defines the number of seconds that a thread should sleep if the `fanOut` is exceeded.

  Default value: 20 milliseconds

------
#### [ Java ]

```
.cache(CacheType.builder()
        .StormTracking(StormTrackingCache.builder()
        .entryCapacity({{100}})
        .entryPruningTailSize({{1}})
        .gracePeriod({{10}})
        .graceInterval({{1}})
        .fanOut({{20}})
        .inFlightTTL({{10}})
        .sleepMilli({{20}})
        .build())
```

------
#### [ C\# / .NET ]

```
CacheType stormTrackingCache = new CacheType
{
    StormTracking = new StormTrackingCache
    {
        EntryCapacity = {{100}},
        EntryPruningTailSize = {{1}},
        FanOut = {{20}},
        GraceInterval = {{1}},
        GracePeriod = {{10}},
        InFlightTTL = {{10}},
        SleepMilli = {{20}}
    }
};
```

------
#### [ Rust ]

```
CacheType::StormTracking(
                StormTrackingCache::builder()
                    .entry_capacity({{100}})
                    .entry_pruning_tail_size({{1}})
                    .grace_period({{10}})
                    .grace_interval({{1}})
                    .fan_out({{20}})
                    .in_flight_ttl({{10}})
                    .sleep_milli({{20}})
                    .build()?)
```

------

### Shared cache
<a name="cache-shared"></a>

By default, the Hierarchical keyring creates a new local cache every time you instantiate the keyring. However, the Shared cache can help conserve memory by enabling you to share a cache across multiple Hierarchical keyrings. Rather than creating a new cryptographic materials cache for each Hierarchical keyring you instantiate, the Shared cache stores only one cache in memory, which can be used by all the Hierarchical keyrings that reference it. The Shared cache helps optimize memory usage by avoiding the duplication of cryptographic materials across keyrings. Instead, the Hierarchical keyrings can access the same underlying cache, reducing the overall memory footprint.

When you create your Shared cache, you still define the cache type. You can specify a [Default cache](#cache-default), [MultiThreaded cache](#cache-multithreaded), or [StormTracking cache](#cache-stormtracking) as the cache type, or substitute any compatible custom cache.

**Partitions**
Multiple Hierarchical keyrings can use a single Shared cache. When you create a Hierarchical keyring with a Shared cache you can define an optional **partition ID**. The partition ID distinguishes which Hierarchical keyring is writing to the cache. If two Hierarchical keyrings reference the same partition ID, [logical key store name](create-keystore.md#logical-key-store-name), and branch key ID the two keyrings will share the same cache entries in the cache. If you create two Hierarchical keyrings with the same Shared cache, but different partition IDs, each keyring will only access the cache entries from its own designated partition within the Shared cache. The partitions act as logical divisions within the shared cache, allowing each Hierarchical keyring to operate independently on its own designated partition, without interfering with the data stored in the other partition.

If you intend to reuse or share the cache entries in a partition, you must define your own partition ID. When you pass the partition ID to your Hierarchical keyring, the keyring can reuse the cache entries that are already present in the Shared cache, rather than having to retrieve and re-authorize the branch key materials again. If you do not specify a partition ID, a unique partition ID is automatically assigned to the keyring each time you instantiate the Hierarchical keyring.

The following procedures demonstrate how to create a Shared cache with the [Default cache type](#cache-default) and pass it to a Hierarchical keyring.

1. Create a `CryptographicMaterialsCache` (CMC) using the [Material Providers Library](https://github.com/aws/aws-cryptographic-material-providers-library) (MPL).

------
#### [ Java ]

   ```
   // Instantiate the MPL
   final MaterialProviders matProv =
       MaterialProviders.builder()
           .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
           .build();

   // Create a CacheType object for the Default cache
   final CacheType cache =
       CacheType.builder()
           .Default(DefaultCache.builder().entryCapacity(100).build())
           .build();

   // Create a CMC using the default cache
   final CreateCryptographicMaterialsCacheInput cryptographicMaterialsCacheInput =
       CreateCryptographicMaterialsCacheInput.builder()
           .cache(cache)
           .build();

   final ICryptographicMaterialsCache sharedCryptographicMaterialsCache =
       matProv.CreateCryptographicMaterialsCache(cryptographicMaterialsCacheInput);
   ```

------
#### [ C\# / .NET ]

   ```
   // Instantiate the MPL
   var materialProviders = new MaterialProviders(new MaterialProvidersConfig());

   // Create a CacheType object for the Default cache
   var cache = new CacheType { Default = new DefaultCache{EntryCapacity = 100} };

   // Create a CMC using the default cache
   var cryptographicMaterialsCacheInput = new CreateCryptographicMaterialsCacheInput {Cache = cache};

   var sharedCryptographicMaterialsCache = materialProviders.CreateCryptographicMaterialsCache(cryptographicMaterialsCacheInput);
   ```

------
#### [ Rust ]

   ```
   // Instantiate the MPL
   let mpl_config = MaterialProvidersConfig::builder().build()?;
   let mpl = mpl_client::Client::from_conf(mpl_config)?;

   // Create a CacheType object for the default cache
   let cache: CacheType = CacheType::Default(
       DefaultCache::builder()
           .entry_capacity(100)
           .build()?,
   );

   // Create a CMC using the default cache
   let shared_cryptographic_materials_cache: CryptographicMaterialsCacheRef = mpl.
       create_cryptographic_materials_cache()
       .cache(cache)
       .send()
       .await?;
   ```

------

1. Create a `CacheType` object for the Shared cache.

   Pass the `sharedCryptographicMaterialsCache` you created in **Step 1** to the new `CacheType` object.

------
#### [ Java ]

   ```
   // Create a CacheType object for the sharedCryptographicMaterialsCache
   final CacheType sharedCache =
       CacheType.builder()
           .Shared(sharedCryptographicMaterialsCache)
           .build();
   ```

------
#### [ C\# / .NET ]

   ```
   // Create a CacheType object for the sharedCryptographicMaterialsCache
   var sharedCache = new CacheType { Shared = sharedCryptographicMaterialsCache };
   ```

------
#### [ Rust ]

   ```
   // Create a CacheType object for the shared_cryptographic_materials_cache
   let shared_cache: CacheType = CacheType::Shared(shared_cryptographic_materials_cache);
   ```

------

1. Pass the `sharedCache` object from **Step 2** to your Hierarchical keyring.

   When you create a Hierarchical keyring with a Shared cache, you can optionally define a `partitionID` to share cache entries across multiple Hierarchical keyrings. If you do not specify a partition ID, the Hierarchical keyring automatically assigns the keyring a unique partition ID.
**Note**
Your Hierarchical keyrings will share the same cache entries in a Shared cache if you create two or more keyrings that reference the same partition ID, [logical key store name](create-keystore.md#logical-key-store-name), and branch key ID. If you do not want multiple keyrings to share the same cache entries, you must use a unique partition ID for each Hierarchical keyring.

   The following example creates a Hierarchical keyring with a [branch key ID supplier](#branch-key-id-supplier), and a [cache limit](#cache-limit) of 600 seconds. For more information on the values defined in following Hierarchical keyring configuration, see [Create a Hierarchical keyring](#initialize-hierarchical-keyring).

------
#### [ Java ]

   ```
   // Create the Hierarchical keyring
   final CreateAwsKmsHierarchicalKeyringInput keyringInput =
       CreateAwsKmsHierarchicalKeyringInput.builder()
           .keyStore(keystore)
           .branchKeyIdSupplier(branchKeyIdSupplier)
           .ttlSeconds({{600}})
           .cache(sharedCache)
           .partitionID({{partitionID}})
           .build();
   final IKeyring hierarchicalKeyring = matProv.CreateAwsKmsHierarchicalKeyring(keyringInput);
   ```

------
#### [ C\# / .NET ]

   ```
   // Create the Hierarchical keyring
   var createKeyringInput = new CreateAwsKmsHierarchicalKeyringInput
   {
      KeyStore = keystore,
      BranchKeyIdSupplier = branchKeyIdSupplier,
      Cache = sharedCache,
      TtlSeconds = {{600}},
      PartitionId = {{partitionID}}
   };
   var keyring = materialProviders.CreateAwsKmsHierarchicalKeyring(createKeyringInput);
   ```

------
#### [ Rust ]

   ```
   // Create the Hierarchical keyring
   let keyring1 = mpl
       .create_aws_kms_hierarchical_keyring()
       .key_store(key_store1)
       .branch_key_id(branch_key_id.clone())
       // CryptographicMaterialsCacheRef is an Rc (Reference Counted), so if you clone it to
       // pass it to different Hierarchical Keyrings, it will still point to the same
       // underlying cache, and increment the reference count accordingly.
       .cache(shared_cache.clone())
       .ttl_seconds({{600}})
       .partition_id({{partition_id}}.clone())
       .send()
       .await?;
   ```

------

## Create a Hierarchical keyring
<a name="initialize-hierarchical-keyring"></a>

To create a Hierarchical keyring, you must provide the following values:
+ **A key store**

  The key store that manages and protects your branch keys. You must create and configure your key store before you create the Hierarchical keyring. For more information, see [Key stores in the AWS Database Encryption SDK](keystores.md).
+

  **A cache limit time to live (TTL)**

  The amount of time in seconds that a branch key materials entry within the local cache can be used before it expires. The cache limit TTL dictates how often the client calls AWS KMS to authorize use of the branch keys. This value must be greater than zero. After the cache limit TTL expires, the entry is never served, and will be evicted from the local cache.
+ **A branch key identifier**

  You can either statically configure the `branch-key-id` that identifies a single active branch key in your key store, or provide a branch key ID supplier.

  The *branch key ID supplier* uses the fields stored in the encryption context to determine which branch key is required to decrypt a record. By default, only the partition and sort keys are included in the encryption context. However, you can use the `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` [cryptographic action](concepts.md#crypt-actions) to include additional fields in the encryption context.

  We strongly recommend using a branch key ID supplier for multitenant databases where each tenant has their own branch key. You can use the branch key ID supplier to create a friendly name for your branch key IDs to make it easy to recognize the correct branch key ID for a specific tenant. For example, the friendly name lets you refer to a branch key as `tenant1` instead of `b3f61619-4d35-48ad-a275-050f87e15122`.

  For decrypt operations, you can either statically configure a single Hierarchical keyring to restrict decryption to a single tenant, or you can use the branch key ID supplier to identify which tenant is responsible for decrypting a record.
+ **(Optional) A cache**

  If you want to customize your cache type or the number of branch key materials entries that can be stored in the local cache, specify the cache type and entry capacity when you initialize the keyring.

  The Hierarchical keyring supports the following cache types: Default, MultiThreaded, StormTracking, and Shared. For more information and examples demonstrating how to define each cache type, see [Choose a cache](#hierarchical-keyring-caches).

  If you do not specify a cache, the Hierarchical keyring automatically uses the Default cache type and sets the entry capacity to 1000.
+ **(Optional) A partition ID**

  If you specify the [Shared cache](#cache-shared), you can optionally define a partition ID. The partition ID distinguishes which Hierarchical keyring is writing to the cache. If you intend to reuse or share the cache entries in a partition, you must define your own partition ID. You can specify any string for the partition ID. If you do not specify a partition ID, a unique partition ID is automatically assigned to the keyring at creation.

  For more information, see [Partitions](#shared-cache-partitions).
**Note**
Your Hierarchical keyrings will share the same cache entries in a Shared cache if you create two or more keyrings that reference the same partition ID, [logical key store name](create-keystore.md#logical-key-store-name), and branch key ID. If you do not want multiple keyrings to share the same cache entries, you must use a unique partition ID for each Hierarchical keyring.
+ **(Optional) A list of Grant Tokens**

  If you control access to the KMS key in your Hierarchical keyring with [grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html), you must provide all necessary grant tokens when you initialize the keyring.

The following examples show how to configure a key store with a static configuration. Choose your preferred language:

------
#### [ Java ]

```
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.keystore.model.KeyStoreConfig;
import software.amazon.cryptography.keystore.model.KMSConfiguration;

final KeyStore keystore = KeyStore.builder()
        .KeyStoreConfig(KeyStoreConfig.builder()
                .ddbClient(DynamoDbClient.create())
                .ddbTableName({{keyStoreName}})
                .logicalKeyStoreName({{logicalKeyStoreName}})
                .kmsClient(KmsClient.create())
                .kmsConfiguration(KMSConfiguration.builder()
                        .kmsKeyArn({{kmsKeyArn}})
                        .build())
                .build())
        .build();
```

------
#### [ C\# / .NET ]

```
using Amazon.DynamoDBv2;
using Amazon.KeyManagementService;
using AWS.Cryptography.KeyStore;

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
#### [ Rust ]

```
use aws_db_esdk::key_store::client as keystore_client;
use aws_db_esdk::key_store::types::key_store_config::KeyStoreConfig;
use aws_db_esdk::key_store::types::KmsConfiguration;

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

After you configure your key store, use the resulting key store object to create your Hierarchical keyring. The Hierarchical keyring examples that follow use the key store object that you configured.

### Create a Hierarchical keyring with a static branch key ID
<a name="static-branch-key-id-config"></a>

The following examples demonstrate how to create a Hierarchical keyring with a static branch key ID, the [Default cache](#cache-default), and a cache limit TTL of 600 seconds.

------
#### [ Java ]

```
final MaterialProviders matProv = MaterialProviders.builder()
        .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
        .build();
final CreateAwsKmsHierarchicalKeyringInput keyringInput = CreateAwsKmsHierarchicalKeyringInput.builder()
        .keyStore(keystore)
        .branchKeyId({{branch-key-id}})
        .ttlSeconds({{600}})
        .build();
final Keyring hierarchicalKeyring = matProv.CreateAwsKmsHierarchicalKeyring(keyringInput);
```

------
#### [ C\# / .NET ]

```
var matProv = new MaterialProviders(new MaterialProvidersConfig());
var keyringInput = new CreateAwsKmsHierarchicalKeyringInput
{
   KeyStore = keystore,
   BranchKeyIdSupplier = branchKeyIdSupplier,
   TtlSeconds = {{600}}
};
var hierarchicalKeyring = matProv.CreateAwsKmsHierarchicalKeyring(keyringInput);
```

------
#### [ Rust ]

```
let mpl_config = MaterialProvidersConfig::builder().build()?;
let mpl = mpl_client::Client::from_conf(mpl_config)?;

let hierarchical_keyring = mpl
    .create_aws_kms_hierarchical_keyring()
    .branch_key_id({{branch_key_id}})
    .key_store(keystore.clone())
    .ttl_seconds({{600}})
    .send()
    .await?;
```

------

### Create a Hierarchical keyring with a branch key ID supplier
<a name="branch-key-id-supplier-config"></a>

The following procedures demonstrate how to create a Hierarchical keyring with a branch key ID supplier.

1. Create a branch key ID supplier

   The following example creates friendly names for the two branch keys created in **Step 1**, and calls `CreateDynamoDbEncryptionBranchKeyIdSupplier` to create a branch key ID supplier with the AWS Database Encryption SDK for DynamoDB client.

------
#### [ Java ]

   ```
   // Create friendly names for each branch-key-id
   class ExampleBranchKeyIdSupplier implements IDynamoDbKeyBranchKeyIdSupplier {
       private static String branchKeyIdForTenant1;
       private static String branchKeyIdForTenant2;

       public ExampleBranchKeyIdSupplier(String tenant1Id, String tenant2Id) {
           this.branchKeyIdForTenant1 = tenant1Id;
           this.branchKeyIdForTenant2 = tenant2Id;
       }
   // Create the branch key ID supplier
   final DynamoDbEncryption ddbEnc = DynamoDbEncryption.builder()
           .DynamoDbEncryptionConfig(DynamoDbEncryptionConfig.builder().build())
           .build();
   final BranchKeyIdSupplier branchKeyIdSupplier = ddbEnc.CreateDynamoDbEncryptionBranchKeyIdSupplier(
       CreateDynamoDbEncryptionBranchKeyIdSupplierInput.builder()
               .ddbKeyBranchKeyIdSupplier(new ExampleBranchKeyIdSupplier({{branch-key-ID-tenant1}}, {{branch-key-ID-tenant2}}))
               .build()).branchKeyIdSupplier();
   ```

------
#### [ C\# / .NET ]

   ```
   // Create friendly names for each branch-key-id
    class ExampleBranchKeyIdSupplier : DynamoDbKeyBranchKeyIdSupplierBase {
       private String _branchKeyIdForTenant1;
       private String _branchKeyIdForTenant2;

       public ExampleBranchKeyIdSupplier(String tenant1Id, String tenant2Id) {
           this._branchKeyIdForTenant1 = tenant1Id;
           this._branchKeyIdForTenant2 = tenant2Id;
       }
   // Create the branch key ID supplier
   var ddbEnc = new DynamoDbEncryption(new DynamoDbEncryptionConfig());
   var branchKeyIdSupplier = ddbEnc.CreateDynamoDbEncryptionBranchKeyIdSupplier(
       new CreateDynamoDbEncryptionBranchKeyIdSupplierInput
       {
           DdbKeyBranchKeyIdSupplier = new ExampleBranchKeyIdSupplier({{branch-key-ID-tenant1}}, {{branch-key-ID-tenant2}})
       }).BranchKeyIdSupplier;
   ```

------
#### [ Rust ]

   ```
   // Create friendly names for each branch_key_id
   pub struct ExampleBranchKeyIdSupplier {
       branch_key_id_for_tenant1: String,
       branch_key_id_for_tenant2: String,
   }

   impl ExampleBranchKeyIdSupplier {
       pub fn new(tenant1_id: &str, tenant2_id: &str) -> Self {
           Self {
               branch_key_id_for_tenant1: tenant1_id.to_string(),
               branch_key_id_for_tenant2: tenant2_id.to_string(),
           }
       }
   }

   // Create the branch key ID supplier
   let dbesdk_config = DynamoDbEncryptionConfig::builder().build()?;
   let dbesdk = dbesdk_client::Client::from_conf(dbesdk_config)?;
   let supplier = ExampleBranchKeyIdSupplier::new(tenant1_branch_key_id, tenant2_branch_key_id);

   let branch_key_id_supplier = dbesdk
       .create_dynamo_db_encryption_branch_key_id_supplier()
       .ddb_key_branch_key_id_supplier(supplier)
       .send()
       .await?
       .branch_key_id_supplier
       .unwrap();
   ```

------

1. Create a Hierarchical keyring

   The following examples initialize a Hierarchical keyring with the branch key ID supplier created in **Step 1**, a cache limit TLL of 600 seconds, and a maximum cache size of 1000.

------
#### [ Java ]

   ```
   final MaterialProviders matProv = MaterialProviders.builder()
           .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
           .build();
   final CreateAwsKmsHierarchicalKeyringInput keyringInput = CreateAwsKmsHierarchicalKeyringInput.builder()
           .keyStore(keystore)
           .branchKeyIdSupplier(branchKeyIdSupplier)
           .ttlSeconds({{600}})
           .cache(CacheType.builder() //OPTIONAL
                   .Default(DefaultCache.builder()
                   .entryCapacity({{100}})
                   .build())
           .build())
           .build();
   final Keyring hierarchicalKeyring = matProv.CreateAwsKmsHierarchicalKeyring(keyringInput);
   ```

------
#### [ C\# / .NET ]

   ```
   var matProv = new MaterialProviders(new MaterialProvidersConfig());
   var keyringInput = new CreateAwsKmsHierarchicalKeyringInput
   {
      KeyStore = keystore,
      BranchKeyIdSupplier = branchKeyIdSupplier,
      TtlSeconds = {{600}},
      Cache = new CacheType
      {
           Default = new DefaultCache { EntryCapacity = {{100}} }
      }
   };
   var hierarchicalKeyring = matProv.CreateAwsKmsHierarchicalKeyring(keyringInput);
   ```

------
#### [ Rust ]

   ```
   let mpl_config = MaterialProvidersConfig::builder().build()?;
   let mpl = mpl_client::Client::from_conf(mpl_config)?;

   let hierarchical_keyring = mpl
       .create_aws_kms_hierarchical_keyring()
       .branch_key_id_supplier(branch_key_id_supplier)
       .key_store(keystore.clone())
       .ttl_seconds(600)
       .send()
       .await?;
   ```

------

## Using the Hierarchical keyring for searchable encryption
<a name="searchable-encryption-hierarchical-keyrings"></a>

[Searchable encryption](searchable-encryption.md) enables you to search encrypted records without decrypting the entire database. This is accomplished by indexing the plaintext value of an encrypted field with a [beacon](beacons.md). To implement searchable encryption, you must use a Hierarchical keyring.

The key store `CreateKey` operation generates both a branch key and *beacon key*. The branch key is used in record encryption and decryption operations. The beacon key is used to generate beacons.

The branch key and beacon key are protected by the same AWS KMS key that you specify when creating your key store service. After the `CreateKey` operation calls AWS KMS to generate the branch key, it calls [kms:GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html) a second time to generate the beacon key using the following request.

```
{
   "EncryptionContext": {
      "branch-key-id" : "{{branch-key-id}}",
      "type" : {{type}},
      "create-time" : "{{timestamp}}",
      "tablename" : "{{the logical table name for your key store}}",
      "kms-arn" : {{the KMS key ARN}},
      "hierarchy-version" : 1
   },
   "KeyId": "{{the KMS key ARN}}",
   "NumberOfBytes": "32"
}
```

After generating both keys, the `CreateKey` operation calls [ddb:TransactWriteItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html) to write two new items that will persist the branch key and beacon key in your branch key store.

When you [configure a standard beacon](configure-beacons.md#config-standard-beacons), the AWS Database Encryption SDK queries the key store for the beacon key. Then, it uses an HMAC-based extract-and-expand key derivation function ([HKDF](https://en.wikipedia.org/wiki/HKDF)) to combine the beacon key with the name of the [standard beacon](beacons.md#standard-beacon-overview) to create the HMAC key for a given beacon.

Unlike branch keys, there is only one beacon key version per `branch-key-id` in a key store. The beacon key is never rotated.

### Defining your beacon key source
<a name="beacon-key-source"></a>

When you define the [beacon version](using-beacons.md#beacon-version) for your standard and compound beacons, you must identify the beacon key and define a cache limit time to live (TTL) for the beacon key materials. Beacon key materials are stored in a separate local cache from the branch keys. The following snippet demonstrates how to define the `keySource` for a single-tenant database. Identify your beacon key by the `branch-key-id` it is associated with.

------
#### [ Java ]

```
keySource(BeaconKeySource.builder()
        .single(SingleKeyStore.builder()
                .keyId({{branch-key-id}})
                .cacheTTL({{6000}})
                .build())
        .build())
```

------
#### [ C\# / .NET ]

```
KeySource = new BeaconKeySource
{
    Single = new SingleKeyStore
    {
       KeyId = {{branch-key-id}},
       CacheTTL = {{6000}}
    }
}
```

------
#### [ Rust ]

```
 .key_source(BeaconKeySource::Single(
    SingleKeyStore::builder()
        // `keyId` references a beacon key.
        // For every branch key we create in the keystore,
        // we also create a beacon key.
        // This beacon key is not the same as the branch key,
        // but is created with the same ID as the branch key.
        .key_id({{branch_key_id}})
        .cache_ttl({{6000}})
        .build()?,
))
```

------

**Defining beacon source in a multitenant database**
If you have a multitenant database, you must specify the following values when configuring the `keySource`.
+

  **keyFieldName**

  Defines the name of the field that stores the `branch-key-id` associated with the beacon key used to generated beacons for a given tenant. The `keyFieldName` can be any string, but it must be unique to all other fields in your database. When you write new records to your database, the `branch-key-id` that identifies the beacon key used to generate any beacons for that record is stored in this field. You must include this field in your beacon queries and identify the appropriate beacon key materials required to recalculate the beacon. For more information, see [Querying beacons in a multitenant database](searchable-encryption-multitenant.md#query-multitenant-beacons).
+ **cacheTTL**

  The amount of time in seconds that a beacon key materials entry within the local beacon cache can be used before it expires. This value must be greater than zero. When the cache limit TTL expires, the entry is evicted from the local cache.
+ **(Optional) A cache**

  If you want to customize your cache type or the number of branch key materials entries that can be stored in the local cache, specify the cache type and entry capacity when you initialize the keyring.

  The Hierarchical keyring supports the following cache types: Default, MultiThreaded, StormTracking, and Shared. For more information and examples demonstrating how to define each cache type, see [Choose a cache](#hierarchical-keyring-caches).

  If you do not specify a cache, the Hierarchical keyring automatically uses the Default cache type and sets the entry capacity to 1000.
The following example creates a Hierarchical keyring with a branch key ID supplier a cache limit TLL of 600 seconds, and an entry capacity of 1000.

```
final MaterialProviders matProv = MaterialProviders.builder()
        .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
        .build();
final CreateAwsKmsHierarchicalKeyringInput keyringInput = CreateAwsKmsHierarchicalKeyringInput.builder()
        .keyStore(keystore)
        .branchKeyIdSupplier(branchKeyIdSupplier)
        .ttlSeconds({{600}})
        .cache(CacheType.builder() //OPTIONAL
                .Default(DefaultCache.builder()
                        .entryCapacity({{1000}})
                        .build())
                .build());
final IKeyring hierarchicalKeyring = matProv.CreateAwsKmsHierarchicalKeyring(keyringInput);
```

```
var matProv = new MaterialProviders(new MaterialProvidersConfig());
var keyringInput = new CreateAwsKmsHierarchicalKeyringInput
{
   KeyStore = keystore,
   BranchKeyIdSupplier = branchKeyIdSupplier,
   TtlSeconds = {{600}},
   Cache = new CacheType
   {
        Default = new DefaultCache { EntryCapacity = {{1000}} }
   }
};
var hierarchicalKeyring = matProv.CreateAwsKmsHierarchicalKeyring(keyringInput);
```

```
let provider_config = MaterialProvidersConfig::builder().build()?;
    let mat_prov = client::Client::from_conf(provider_config)?;
    let kms_keyring = mat_prov
        .create_aws_kms_hierarchical_keyring()
        .branch_key_id(branch_key_id)
        .key_store(keystore.clone())
        .ttl_seconds({{600}})
        .send()
        .await?;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
