---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-hierarchical-keyring.html
---

# AWS KMS Hierarchical keyrings
<a name="use-hierarchical-keyring"></a>

With the AWS KMS Hierarchical keyring, you can protect your cryptographic materials under a symmetric encryption KMS key without calling AWS KMS every time you encrypt or decrypt data. It is a good choice for applications that need to minimize calls to AWS KMS, and applications that can reuse some cryptographic materials without violating their security requirements.

The Hierarchical keyring is a cryptographic materials caching solution that reduces the number of AWS KMS calls by using AWS KMS protected *branch keys* persisted in an Amazon DynamoDB table, and then locally caching branch key materials used in encrypt and decrypt operations. The DynamoDB table serves as the key store that manages and protects branch keys. It stores the active branch key and all previous versions of the branch key. The *active* branch key is the most recent branch key version. The Hierarchical keyring uses a unique data key to encrypt each message and encrypts each data encryption key for each encrypt request and encrypts each data encryption key with a unique wrapping key derived from the active branch key. The Hierarchical keyring is dependent on the hierarchy established between active branch keys and their derived wrapping keys.

The Hierarchical keyring typically uses each branch key version to satisfy multiple requests. But you control the extent to which active branch keys are reused and determine how often the active branch key is rotated. The active version of the branch key remains active until you [rotate it](rotate-branch-key.md). Previous versions of the active branch key will not be used to perform encrypt operations, but they can still be queried and used in decrypt operations.

When you instantiate the Hierarchical keyring, it creates a local cache. You specify a [cache limit](#cache-limit) that defines the maximum amount of time that the branch key materials are stored within the local cache before they expire and are evicted from the cache. The Hierarchical keyring makes one AWS KMS call to decrypt the branch key and assemble the branch key materials the first time a `branch-key-id` is specified in an operation. Then, the branch key materials are stored in the local cache and reused for all encrypt and decrypt operations that specify that `branch-key-id` until the cache limit expires. Storing branch key materials in the local cache reduces AWS KMS calls. For example, consider a cache limit of 15 minutes. If you perform 10,000 encrypt operations within that cache limit, the [traditional AWS KMS keyring](use-kms-keyring.md) would need to make 10,000 AWS KMS calls to satisfy 10,000 encrypt operations. If you have one active `branch-key-id`, the Hierarchical keyring only needs to make one AWS KMS call to satisfy 10,000 encrypt operations.

The local cache separates encryption materials from decryption materials. The encryption materials are assembled from the active branch key and reused for all encrypt operations until the cache limit expires. The decryption materials are assembled from the branch key ID and version that is identified in the encrypted field's metadata, and they are reused for all decrypt operations related to the branch key ID and version until the cache limit expires. The local cache can store multiple versions of the same branch key at a time. When the local cache is configured to use a [branch key ID supplier](#branch-key-id-supplier), it can also store branch key materials from multiple active branch keys at a time.

**Note**
All mentions of *Hierarchical keyring* in the AWS Encryption SDK refer to the AWS KMS Hierarchical keyring.

**Programming language compatibility**
The Hierarchical keyring is supported by the following programming languages and versions:
+ Version 3.*x* of the AWS Encryption SDK for Java
+ Version 4.*x* and later of the AWS Encryption SDK for .NET
+ Version 4.*x* of the AWS Encryption SDK for Python, when used with the optional MPL dependency.
+ Version 1.*x* of the AWS Encryption SDK for Rust
+ Version 0.1.*x* or later of the AWS Encryption SDK for Go
+ Version 4.1.*x* and later of the AWS Encryption SDK for JavaScript for JavaScript Node.js.
  + The AWS KMS Hierarchical keyring is not supported in the AWS Encryption SDK for JavaScript for JavaScript Browser. For current status and limitations, see the [aws-encryption-sdk-javascript](https://github.com/aws/aws-encryption-sdk-javascript/) repository on GitHub.

**Topics**
+ [How it works](#how-hierarchical-keyring-works)
+ [Prerequisites](#hierarchical-keyring-prereqs)
+ [Required permissions](#hierarchical-keyring-permissions)
+ [Choose a cache](#hierarchical-keyring-caches)
+ [Create a Hierarchical keyring](#initialize-hierarchical-keyring)

## How it works
<a name="how-hierarchical-keyring-works"></a>

The following walkthroughs describe how the Hierarchical keyring assembles encryption and decryption materials, and the different calls that the keyring makes for encrypt and decrypt operations. For technical details on the wrapping key derivation and plaintext data key encryption processes, see [AWS KMS Hierarchical keyring technical details](hierarchical-keyring-details.md).

**Encrypt and sign**
The following walkthrough describes how the Hierarchical keyring assembles encryption materials and derives a unique wrapping key.

1. The encryption method asks the Hierarchical keyring for encryption materials. The keyring generates a plaintext data key, then checks to see if there are valid branch materials in the local cache to generate the wrapping key. If there are valid branch key materials, the keyring proceeds to **Step 4**.

1. If there are no valid branch key materials, the Hierarchical keyring queries the key store for the active branch key.

   1. The key store calls AWS KMS to decrypt the active branch key and returns the plaintext active branch key. Data identifying the active branch key is serialized to provide additional authenticated data (AAD) in the decrypt call to AWS KMS.

   1. The key store returns the plaintext branch key and data that identifies it, such as the branch key version.

1. The Hierarchical keyring assembles branch key materials (the plaintext branch key and branch key version) and stores a copy of them in the local cache.

1. The Hierarchical keyring derives a unique wrapping key from the plaintext branch key and a 16-byte random salt. It uses the derived wrapping key to encrypt a copy of the plaintext data key.

The encryption method uses the encryption materials to encrypt the data. For more information, see [How the AWS Encryption SDK encrypts data](how-it-works.md#encrypt-workflow).

**Decrypt and verify**
The following walkthrough describes how the Hierarchical keyring assembles decryption materials and decrypts the encrypted data key.

1. The decryption method identifies the encrypted data key from the encrypted message, and passes it to the Hierarchical keyring.

1. The Hierarchical keyring deserializes data identifying the encrypted data key, including the branch key version, the 16-byte salt, and other information describing how the data key was encrypted.

   For more information, see [AWS KMS Hierarchical keyring technical details](hierarchical-keyring-details.md).

1. The Hierarchical keyring checks to see if there are valid branch key materials in the local cache that match the branch key version identified in **Step 2**. If there are valid branch key materials, the keyring proceeds to **Step 6**.

1. If there are no valid branch key materials, the Hierarchical keyring queries the key store for the branch key that matches the branch key version identified in **Step 2**.

   1. The key store calls AWS KMS to decrypt the branch key and returns the plaintext active branch key. Data identifying the active branch key is serialized to provide additional authenticated data (AAD) in the decrypt call to AWS KMS.

   1. The key store returns the plaintext branch key and data that identifies it, such as the branch key version.

1. The Hierarchical keyring assembles branch key materials (the plaintext branch key and branch key version) and stores a copy of them in the local cache.

1. The Hierarchical keyring uses the assembled branch key materials and the 16-byte salt identified in **Step 2** to reproduce the unique wrapping key that encrypted the data key.

1. The Hierarchical keyring uses the reproduced wrapping key to decrypt the data key and returns the plaintext data key.

The decryption method uses the decryption materials and plaintext data key to decrypt the encrypted message. For more information , see [How the AWS Encryption SDK decrypts an encrypted message](how-it-works.md#decrypt-workflow).

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

The AWS Encryption SDK doesn't require an AWS account and it doesn't depend on any AWS service. However, to use an Hierarchical keyring, you need an AWS account and the following minimum permissions on the symmetric encryption AWS KMS key(s) in your key store.
+ To encrypt and decrypt data with the Hierarchical keyring, you need [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html).
+ To [create](create-branch-keys.md) and [rotate](rotate-branch-key.md) branch keys, you need [kms:GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html) and [kms:ReEncrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html).

**Required Amazon DynamoDB permissions on the key store table**
The principals that interact with your key store also need permissions on the DynamoDB table. The set of permissions depends on the role.

**Key store user**
A key store user is the principal that uses the Hierarchical keyring to encrypt and decrypt data. A key store user needs [dynamodb:GetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html) on the key store table.

**Key store administrator**
A key store administrator is the principal that [creates](create-branch-keys.md) and [rotates](rotate-branch-key.md) branch keys. A key store administrator needs the following permissions on the key store table:
+ For reads: [dynamodb:GetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html) and dynamodb:ConditionCheckItem.
+ For transactional writes: dynamodb:ConditionCheckItem and [dynamodb:PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html). The Hierarchical keyring key store performs writes through [TransactWriteItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html); you can scope the write permissions to that operation with a `dynamodb:EnclosingOperation` condition.

For more information on controlling access to your branch keys and key store, see [Implementing least privileged permissions](keystore-least-privilege.md).

## Choose a cache
<a name="hierarchical-keyring-caches"></a>

The Hierarchical keyring reduces the number of calls made to AWS KMS by locally caching the branch key materials used in encrypt and decrypt operations. Before you [create your Hierarchical keyring](#initialize-hierarchical-keyring), you need to decide what type of cache you want to use. You can use the default cache or customize the cache to best fits your needs.

The Hierarchical keyring supports the following cache types:
+ [Default cache](#cache-default)
+ [MultiThreaded cache](#cache-multithreaded)
+ [StormTracking cache](#cache-stormtracking)
+ [Shared cache](#cache-shared)

**Important**
All supported cache types are designed to support multithreaded environments.
However, when used with the AWS Encryption SDK for Python, the Hierarchical keyring does not support multithreaded environments. For more information, see the [Python README.rst](https://github.com/aws/aws-cryptographic-material-providers-library/blob/main/AwsCryptographicMaterialProviders/runtimes/python/README.rst) file in the [aws-cryptographic-material-providers-library](https://github.com/aws/aws-cryptographic-material-providers-library/tree/main) repository on GitHub.

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
#### [ Python ]

```
default_cache = CacheTypeDefault(
    value=DefaultCache(
        entry_capacity={{100}}
    )
)
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
#### [ Go ]

```
cache := mpltypes.CacheTypeMemberDefault{
		Value: mpltypes.DefaultCache{
			EntryCapacity: 100,
		},
	}
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
#### [ Python ]

```
multithreaded_cache = CacheTypeMultiThreaded(
    value=MultiThreadedCache(
        entry_capacity={{100}},
        entry_pruning_tail_size={{1}}
    )
)
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
#### [ Go ]

```
var entryPruningTailSize int32 = 1
	cache := mpltypes.CacheTypeMemberMultiThreaded{
		Value: mpltypes.MultiThreadedCache{
			EntryCapacity:        100,
			EntryPruningTailSize: &entryPruningTailSize,
		},
	}
```

------

### StormTracking cache
<a name="cache-stormtracking"></a>

The StormTracking cache is designed to support heavily multithreaded environments. When a branch key materials entry expires, the StormTracking cache prevents multiple threads from calling AWS KMS by notifying one thread that the branch key materials entry is going to expire in advance. This ensures that only one thread sends a request to AWS KMS to refresh the cache. For more information, see [Storm Tracking Cryptographic Materials Cache](https://github.com/awslabs/aws-encryption-sdk-specification/blob/master/framework/storm-tracking-cryptographic-materials-cache.md) in the aws-encryption-sdk-specification GitHub repository.

To use the StormTracking cache, specify the following values:
+ **Entry capacity**: limits the number of branch key materials entries that can be stored in the local cache.

  Default value: 1000 entries
+ **Entry pruning tail size**: defines the number of branch key materials entries to prune at a time.

  Default value: 1 entry
+ **Grace period**: defines the number of seconds before expiration that an attempt to refresh branch key materials is made.

  Default value: 10 seconds
+ **Grace interval**: defines the number of seconds between attempts to refresh the branch key materials.

  Default value: 1 second
+ **Fan out**: defines the number of simultaneous attempts that can be made to refresh the branch key materials.

  Default value: 20 attempts
+ **In flight time to live (TTL)**: defines the number of seconds until an attempt to refresh the branch key materials times out. Any time the cache returns `NoSuchEntry` in response to a `GetCacheEntry`, that branch key is considered to be *in flight* until the same key is written with a `PutCache` entry.

  Default value: 10 seconds
+ **Sleep**: defines the number of milliseconds that a thread should sleep if the `fanOut` is exceeded.

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
#### [ Python ]

```
storm_tracking_cache = CacheTypeStormTracking(
    value=StormTrackingCache(
        entry_capacity={{100}},
        entry_pruning_tail_size={{1}},
        fan_out={{20}},
        grace_interval={{1}},
        grace_period={{10}},
        in_flight_ttl={{10}},
        sleep_milli={{20}}
    )
)
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
#### [ Go ]

```
var entryPruningTailSize int32 = 1
	cache := mpltypes.CacheTypeMemberStormTracking{
		Value: mpltypes.StormTrackingCache{
			EntryCapacity:        100,
			EntryPruningTailSize: &entryPruningTailSize,
			GraceInterval:        1,
			GracePeriod:          10,
			FanOut:               20,
			InFlightTTL:          10,
			SleepMilli:           20,
		},
	}
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
#### [ Python ]

   ```
   # Instantiate the MPL
   mat_prov: AwsCryptographicMaterialProviders = AwsCryptographicMaterialProviders(
       config=MaterialProvidersConfig()
   )

   # Create a CacheType object for the default cache
   cache: CacheType = CacheTypeDefault(
       value=DefaultCache(
           entry_capacity=100,
       )
   )

   # Create a CMC using the default cache
   cryptographic_materials_cache_input = CreateCryptographicMaterialsCacheInput(
       cache=cache,
   )

   shared_cryptographic_materials_cache = mat_prov.create_cryptographic_materials_cache(
       cryptographic_materials_cache_input
   )
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
#### [ Go ]

   ```
   import (
       "context"

   	mpl "aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygenerated"
   	mpltypes "aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygeneratedtypes"
   )

   // Instantiate the MPL
   matProv, err := mpl.NewClient(mpltypes.MaterialProvidersConfig{})
   if err != nil {
       panic(err)
   }

   // Create a CacheType object for the default cache
   cache := mpltypes.CacheTypeMemberDefault{
       Value: mpltypes.DefaultCache{
           EntryCapacity: 100,
       },
   }

   // Create a CMC using the default cache
   cmcCacheInput := mpltypes.CreateCryptographicMaterialsCacheInput{
       Cache: &cache,
   }
   sharedCryptographicMaterialsCache, err := matProv.CreateCryptographicMaterialsCache(context.Background(), cmcCacheInput)
   if err != nil {
       panic(err)
   }
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
#### [ Python ]

   ```
   # Create a CacheType object for the shared_cryptographic_materials_cache
   shared_cache: CacheType = CacheTypeShared(
       value=shared_cryptographic_materials_cache
   )
   ```

------
#### [ Rust ]

   ```
   // Create a CacheType object for the shared_cryptographic_materials_cache
   let shared_cache: CacheType = CacheType::Shared(shared_cryptographic_materials_cache);
   ```

------
#### [ Go ]

   ```
   // Create a CacheType object for the shared_cryptographic_materials_cache
   shared_cache := mpltypes.CacheTypeMemberShared{sharedCryptographicMaterialsCache}
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
#### [ Python ]

   ```
   # Create the Hierarchical keyring
   keyring_input: CreateAwsKmsHierarchicalKeyringInput = CreateAwsKmsHierarchicalKeyringInput(
       key_store=keystore,
       branch_key_id_supplier=branch_key_id_supplier,
       ttl_seconds={{600}},
       cache=shared_cache,
       partition_id={{partition_id}}
   )

   hierarchical_keyring: IKeyring = mat_prov.create_aws_kms_hierarchical_keyring(
       input=keyring_input
   )
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
#### [ Go ]

   ```
   // Create the Hierarchical keyring
   hkeyringInput := mpltypes.CreateAwsKmsHierarchicalKeyringInput{
       KeyStore:    keyStore1,
       BranchKeyId: &branchKeyId,
       TtlSeconds:  {{600}},
       Cache:       &shared_cache,
       PartitionId: {{&partitionId}},
   }
   keyring, err := matProv.CreateAwsKmsHierarchicalKeyring(context.Background(), hkeyringInput)
   if err != nil {
       panic(err)
   }
   ```

------

## Create a Hierarchical keyring
<a name="initialize-hierarchical-keyring"></a>

To create a Hierarchical keyring, you must provide the following values:
+ **A key store**

  The key store that manages and protects your branch keys. You must create and configure your key store before you create the Hierarchical keyring. For more information, see [Key stores in the AWS Encryption SDK](keystores.md).
+

  **A cache limit time to live (TTL)**

  The amount of time in seconds that a branch key materials entry within the local cache can be used before it expires. The cache limit TTL dictates how often the client calls AWS KMS to authorize use of the branch keys. This value must be greater than zero. After the cache limit TTL expires, the entry is never served, and will be evicted from the local cache.
+ **A branch key identifier**

  You can either statically configure the `branch-key-id` that identifies a single active branch key in your key store, or provide a branch key ID supplier.

  The *branch key ID supplier* uses the fields stored in the encryption context to determine which branch key is required to decrypt a record.

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
#### [ Python ]

```
import boto3
from aws_cryptographic_material_providers.keystore import KeyStore
from aws_cryptographic_material_providers.keystore.config import KeyStoreConfig
from aws_cryptographic_material_providers.keystore.models import KMSConfigurationKmsKeyArn

ddb_client = boto3.client('dynamodb', region_name="us-west-2")
kms_client = boto3.client('kms', region_name="us-west-2")

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
use aws_esdk::key_store::client as keystore_client;
use aws_esdk::key_store::types::key_store_config::KeyStoreConfig;
use aws_esdk::key_store::types::KmsConfiguration;

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
    "context"

    keystore "github.com/aws/aws-cryptographic-material-providers-library/mpl/awscryptographykeystoresmithygenerated"
    keystoretypes "github.com/aws/aws-cryptographic-material-providers-library/mpl/awscryptographykeystoresmithygeneratedtypes"
    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/service/dynamodb"
    "github.com/aws/aws-sdk-go-v2/service/kms"
)

cfg, err := config.LoadDefaultConfig(context.TODO())
if err != nil {
    panic(err)
}
ddbClient := dynamodb.NewFromConfig(cfg)
kmsClient := kms.NewFromConfig(cfg)

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
   BranchKeyId = {{branch-key-id}},
   TtlSeconds = {{600}}
};
var hierarchicalKeyring = matProv.CreateAwsKmsHierarchicalKeyring(keyringInput);
```

------
#### [ Python ]

```
mat_prov: AwsCryptographicMaterialProviders = AwsCryptographicMaterialProviders(
    config=MaterialProvidersConfig()
)

keyring_input: CreateAwsKmsHierarchicalKeyringInput = CreateAwsKmsHierarchicalKeyringInput(
    key_store=keystore,
    branch_key_id={{branch_key_id}},
    ttl_seconds={{600}}
)

hierarchical_keyring: IKeyring = mat_prov.create_aws_kms_hierarchical_keyring(
    input=keyring_input
)
```

------
#### [ Rust ]

```
let mpl_config = MaterialProvidersConfig::builder().build()?;
let mpl = mpl_client::Client::from_conf(mpl_config)?;

let hierarchical_keyring = mpl
        .create_aws_kms_hierarchical_keyring()
        .key_store(keystore.clone())
        .branch_key_id({{branch_key_id}})
        .ttl_seconds({{600}})
        .send()
        .await?;
```

------
#### [ Go ]

```
matProv, err := mpl.NewClient(mpltypes.MaterialProvidersConfig{})
if err != nil {
    panic(err)
}
hkeyringInput := mpltypes.CreateAwsKmsHierarchicalKeyringInput{
    KeyStore:    keyStore,
    BranchKeyId: {{&branchKeyID}},
    TtlSeconds:  {{600}},
}
hKeyRing, err := matProv.CreateAwsKmsHierarchicalKeyring(context.Background(), hkeyringInput)
if err != nil {
    panic(err)
}
```

------

### Create a Hierarchical keyring with a branch key ID supplier
<a name="branch-key-id-supplier-config"></a>

The following procedures demonstrate how to create a Hierarchical keyring with a branch key ID supplier.

1. Create a branch key ID supplier

   The following example defines a branch key ID supplier that uses the encryption context at encrypt or decrypt time to select the branch key ID for each tenant. For a working implementation in each language, see:
   + Java: [ExampleBranchKeyIdSupplier.java](https://github.com/aws/aws-encryption-sdk-java/blob/master/src/examples/java/com/amazonaws/crypto/examples/keyrings/hierarchical/ExampleBranchKeyIdSupplier.java)
   + C\# / .NET: [ExampleBranchKeySupplier.cs](https://github.com/aws/aws-encryption-sdk/tree/mainline/AwsEncryptionSDK/runtimes/net/Examples/Keyring/AwsKmsHierarchical/ExampleBranchKeySupplier.cs)
   + Python: [branch\_key\_id\_supplier\_example.py](https://github.com/aws/aws-encryption-sdk-python/tree/master/examples/src/branch_key_id_supplier_example.py)
   + Rust: [example\_branch\_key\_id\_supplier.rs](https://github.com/aws/aws-encryption-sdk/blob/mainline/releases/rust/esdk/examples/keyring/aws_kms_hierarchical/example_branch_key_id_supplier.rs)
   + Go: [branchkeysupplier.go](https://github.com/aws/aws-encryption-sdk/tree/mainline/releases/go/encryption-sdk/examples/keyring/awskmshierarchicalkeyring/branchkeysupplier.go)

------
#### [ Java ]

   ```
   // Define a branch key ID supplier that uses the encryption context to
   // select a branch key ID for each tenant.
   public class ExampleBranchKeyIdSupplier implements IBranchKeyIdSupplier {
       private static String branchKeyIdForTenantA;
       private static String branchKeyIdForTenantB;

       public ExampleBranchKeyIdSupplier(String tenant1Id, String tenant2Id) {
           this.branchKeyIdForTenantA = tenant1Id;
           this.branchKeyIdForTenantB = tenant2Id;
       }

       @Override
       public GetBranchKeyIdOutput GetBranchKeyId(GetBranchKeyIdInput input) {
           Map<String, String> encryptionContext = input.encryptionContext();
           if (!encryptionContext.containsKey("tenant")) {
               throw new IllegalArgumentException(
                   "EncryptionContext invalid, does not contain expected tenant key value pair.");
           }

           String tenantKeyId = encryptionContext.get("tenant");
           String branchKeyId;
           if (tenantKeyId.equals("TenantA")) {
               branchKeyId = branchKeyIdForTenantA;
           } else if (tenantKeyId.equals("TenantB")) {
               branchKeyId = branchKeyIdForTenantB;
           } else {
               throw new IllegalArgumentException("Item does not contain valid tenant ID");
           }

           return GetBranchKeyIdOutput.builder().branchKeyId(branchKeyId).build();
       }
   }

   // Create the branch key ID supplier
   final IBranchKeyIdSupplier branchKeyIdSupplier = new ExampleBranchKeyIdSupplier(
       {{branch-key-ID-tenantA}}, {{branch-key-ID-tenantB}});
   ```

------
#### [ C\# / .NET ]

   ```
   // Define a branch key ID supplier that uses the encryption context to
   // select a branch key ID for each tenant.
   public class ExampleBranchKeySupplier : BranchKeyIdSupplierBase {
       private string branchKeyTenantA;
       private string branchKeyTenantB;

       public ExampleBranchKeySupplier(string branchKeyTenantA, string branchKeyTenantB) {
           this.branchKeyTenantA = branchKeyTenantA;
           this.branchKeyTenantB = branchKeyTenantB;
       }

       // The encryption context is used to determine the Branch Key ID.
       protected override GetBranchKeyIdOutput _GetBranchKeyId(GetBranchKeyIdInput input) {
           Dictionary<string, string> encryptionContext = input.EncryptionContext;
           if (!encryptionContext.ContainsKey("tenant")) {
               throw new Exception("EncryptionContext invalid, does not contain expected tenant key value pair.");
           }

           string tenant = encryptionContext["tenant"];
           if (tenant.Equals("TenantA")) {
               return new GetBranchKeyIdOutput { BranchKeyId = branchKeyTenantA };
           }
           if (tenant.Equals("TenantB")) {
               return new GetBranchKeyIdOutput { BranchKeyId = branchKeyTenantB };
           }
           throw new Exception("Item does not have a valid tenantID.");
       }
   }

   // Create the branch key ID supplier
   var branchKeyIdSupplier = new ExampleBranchKeySupplier(
       {{branch-key-ID-tenantA}}, {{branch-key-ID-tenantB}});
   ```

------
#### [ Python ]

   ```
   # Define a branch key ID supplier that uses the encryption context to
   # select a branch key ID for each tenant.
   class ExampleBranchKeyIdSupplier(IBranchKeyIdSupplier):
       branch_key_id_for_tenant_A: str
       branch_key_id_for_tenant_B: str

       def __init__(self, tenant_1_id, tenant_2_id):
           self.branch_key_id_for_tenant_A = tenant_1_id
           self.branch_key_id_for_tenant_B = tenant_2_id

       def get_branch_key_id(
           self, param: GetBranchKeyIdInput
       ) -> GetBranchKeyIdOutput:
           encryption_context = param.encryption_context
           if "tenant" not in encryption_context:
               raise ValueError("EncryptionContext invalid, does not contain expected tenant key value pair.")

           tenant_key_id = encryption_context.get("tenant")
           if tenant_key_id == "TenantA":
               branch_key_id = self.branch_key_id_for_tenant_A
           elif tenant_key_id == "TenantB":
               branch_key_id = self.branch_key_id_for_tenant_B
           else:
               raise ValueError(f"Item does not contain valid tenant ID: {tenant_key_id=}")

           return GetBranchKeyIdOutput(branch_key_id=branch_key_id)

   # Create the branch key ID supplier
   branch_key_id_supplier: IBranchKeyIdSupplier = ExampleBranchKeyIdSupplier(
           tenant_1_id={{branch_key_id_a}},
           tenant_2_id={{branch_key_id_b}},
   )
   ```

------
#### [ Rust ]

   ```
   // Define a branch key ID supplier that uses the encryption context to
   // select a branch key ID for each tenant.
   pub struct ExampleBranchKeyIdSupplier {
       branch_key_id_for_tenant_a: String,
       branch_key_id_for_tenant_b: String,
   }

   impl ExampleBranchKeyIdSupplier {
       pub fn new(tenant_a_id: &str, tenant_b_id: &str) -> Self {
           Self {
               branch_key_id_for_tenant_a: tenant_a_id.to_string(),
               branch_key_id_for_tenant_b: tenant_b_id.to_string(),
           }
       }
   }

   // The encryption context is used to determine the Branch Key ID.
   impl BranchKeyIdSupplier for ExampleBranchKeyIdSupplier {
       fn get_branch_key_id(&self, input: GetBranchKeyIdInput) -> Result<GetBranchKeyIdOutput, Error> {
           let encryption_context: HashMap<String, String> = input.encryption_context.unwrap();
           if !encryption_context.contains_key("tenant") {
               return Err(Error::AwsCryptographicMaterialProvidersException {
                   message: "EncryptionContext invalid, does not contain expected tenant key value pair.".to_string(),
               });
           }

           let tenant_key_id: &str = encryption_context["tenant"].as_str();
           if tenant_key_id == "TenantA" {
               Ok(GetBranchKeyIdOutput::builder()
                   .branch_key_id(self.branch_key_id_for_tenant_a.clone())
                   .build()
                   .unwrap())
           } else if tenant_key_id == "TenantB" {
               Ok(GetBranchKeyIdOutput::builder()
                   .branch_key_id(self.branch_key_id_for_tenant_b.clone())
                   .build()
                   .unwrap())
           } else {
               Err(Error::AwsCryptographicMaterialProvidersException {
                   message: "Item does not contain valid tenant ID.".to_string(),
               })
           }
       }
   }

   // Create the branch key ID supplier
   let branch_key_id_supplier = ExampleBranchKeyIdSupplier::new(
       &{{branch_key_id_a}},
       &{{branch_key_id_b}},
   );
   ```

------
#### [ Go ]

   ```
   // Define a branch key ID supplier that uses the encryption context to
   // select a branch key ID for each tenant.
   type branchKeySupplier struct {
       branchKeyA string
       branchKeyB string
   }

   // The encryption context is used to determine the Branch Key ID.
   func (b *branchKeySupplier) GetBranchKeyId(input mpltypes.GetBranchKeyIdInput) (*mpltypes.GetBranchKeyIdOutput, error) {
       ec := input.EncryptionContext
       if value, exists := ec["tenant"]; !exists || value == "" {
           return nil, fmt.Errorf("EncryptionContext invalid, does not contain expected tenant key value pair.")
       }

       branchKeyIdentifier := ec["tenant"]
       if branchKeyIdentifier == "TenantA" {
           return &mpltypes.GetBranchKeyIdOutput{BranchKeyId: b.branchKeyA}, nil
       } else if branchKeyIdentifier == "TenantB" {
           return &mpltypes.GetBranchKeyIdOutput{BranchKeyId: b.branchKeyB}, nil
       } else {
           return &mpltypes.GetBranchKeyIdOutput{}, fmt.Errorf("unknown branch key identifier")
       }
   }

   // Create the branch key ID supplier
   keySupplier := branchKeySupplier{branchKeyA: {{branchKeyA}}, branchKeyB: {{branchKeyB}}}
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
#### [ Python ]

   ```
   mat_prov: AwsCryptographicMaterialProviders = AwsCryptographicMaterialProviders(
       config=MaterialProvidersConfig()
   )

   keyring_input: CreateAwsKmsHierarchicalKeyringInput = CreateAwsKmsHierarchicalKeyringInput(
       key_store=keystore,
       branch_key_id_supplier=branch_key_id_supplier,
       ttl_seconds=600,
       cache=CacheTypeDefault(
           value=DefaultCache(
               entry_capacity=100
           )
       ),
   )

   hierarchical_keyring: IKeyring = mat_prov.create_aws_kms_hierarchical_keyring(
       input=keyring_input
   )
   ```

------
#### [ Rust ]

   ```
   let mpl_config = MaterialProvidersConfig::builder().build()?;
   let mpl = mpl_client::Client::from_conf(mpl_config)?;

   let hierarchical_keyring = mpl
       .create_aws_kms_hierarchical_keyring()
       .key_store(keystore.clone())
       .branch_key_id_supplier(branch_key_id_supplier)
       .ttl_seconds(600)
       .send()
       .await?;
   ```

------
#### [ Go ]

   ```
   hkeyringInput := mpltypes.CreateAwsKmsHierarchicalKeyringInput{
       KeyStore:            keyStore,
       BranchKeyIdSupplier: &keySupplier,
       TtlSeconds:          600,
   }
   hKeyRing, err := matProv.CreateAwsKmsHierarchicalKeyring(context.Background(), hkeyringInput)
   if err != nil {
       panic(err)
   }
   ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
