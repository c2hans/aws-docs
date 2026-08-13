---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/s3-encryption-migration-v2-v3.html
---

# Amazon S3 Encryption Client Migration (V2 to V3)
<a name="s3-encryption-migration-v2-v3"></a>

**Note**
If you are using V1 of the Amazon S3 encryption client, you must first migrate to V2 before migrating to V3. See [Amazon S3 Encryption Client Migration (V1 to V2)](s3-encryption-migration-v1-v2.md).

This topic shows how to migrate your applications from Version 2 (V2) to Version 3 (V3) of the Amazon Simple Storage Service (Amazon S3) encryption client and ensure application availability throughout the migration process. V3 introduces the `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` algorithm and Commitment Policies to enhance security by protecting against data key tampering in Instruction Files.

## Migration Overview
<a name="s3-encryption-migration-v2-v3-overview"></a>

This migration happens in two phases:

1. **Update existing clients to read new formats.** First, deploy an updated version of the AWS SDK for C\+\+ to your application. This allows existing V2 encryption clients to decrypt objects written by the new V3 clients. If your application uses multiple AWS SDKs, you must upgrade each SDK separately.

2. **Migrate encryption and decryption clients to V3.** Once all of your V2 encryption clients can read new formats, you can migrate your existing encryption and decryption clients to their respective V3 versions.

## Understanding V3 Concepts
<a name="s3-encryption-migration-v2-v3-concepts"></a>

Version 3 of the Amazon S3 encryption client introduces new security features that enhance protection against data key tampering. Understanding these concepts is essential for a successful migration.

### Commitment Policy
<a name="s3-encryption-migration-v2-v3-commitment-policy"></a>

Commitment Policies control how the encryption client handles key commitment during encryption and decryption operations. V3 provides three policy options to support different migration scenarios and security requirements:

**`FORBID_ENCRYPT_ALLOW_DECRYPT`**
**Encryption behavior:** Encrypts objects without key commitment, using the same algorithms as V2.
**Decryption behavior:** Allows decryption of objects encrypted with and without key commitment.
**Security implications:** This policy does not enforce key commitment and may allow tampering with the encrypted data key in Instruction Files. Use this policy only during the initial migration phase when you need V2 clients to read newly encrypted objects.
**Version compatibility:** Objects encrypted with this policy can be read by all V2 and V3 implementations.

**`REQUIRE_ENCRYPT_ALLOW_DECRYPT` (Default)**
**Encryption behavior:** Encrypts objects with key commitment using the `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` algorithm.
**Decryption behavior:** Allows decryption of both objects encrypted with key commitment and objects encrypted without key commitment.
**Security implications:** This policy provides strong security for newly encrypted objects while maintaining backward compatibility for reading older objects. This is the recommended policy for most migration scenarios.
**Version compatibility:** Objects encrypted with this policy can only be read by V3 and the latest V2 implementations. V2 clients cannot decrypt these objects. However, V3 clients using this policy can still decrypt objects encrypted by V2 clients.

**`REQUIRE_ENCRYPT_REQUIRE_DECRYPT`**
**Encryption behavior:** Encrypts objects with key commitment using the `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` algorithm.
**Decryption behavior:** Only allows decryption of objects encrypted with key commitment. Rejects objects encrypted without key commitment.
**Security implications:** This policy provides the highest level of security by enforcing key commitment for all operations. Use this policy only after all objects have been re-encrypted with key commitment and you no longer need to read legacy V1 or V2 encrypted objects.
**Version compatibility:** Objects encrypted with this policy can only be read by V3 and the latest V2 implementations. Additionally, clients using this policy cannot decrypt objects encrypted by V1 or V2 clients.

**Migration considerations:** During migration, start with `FORBID_ENCRYPT_ALLOW_DECRYPT` if you need V2 clients to read new objects, then move to `REQUIRE_ENCRYPT_ALLOW_DECRYPT` once all clients are upgraded to V3. Finally, consider `REQUIRE_ENCRYPT_REQUIRE_DECRYPT` only after all legacy objects have been re-encrypted.

### ALG\_AES\_256\_GCM\_HKDF\_SHA512\_COMMIT\_KEY Algorithm
<a name="s3-encryption-migration-v2-v3-aes-gcm-kc"></a>

The `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` algorithm is a new encryption algorithm introduced in V3 that provides enhanced security for encrypted data keys stored in Instruction Files.

**Instruction File impact:** The `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` algorithm only impacts Instruction Files, which are separate S3 objects that store encryption metadata including the encrypted data key. Objects that store encryption metadata in object metadata (the default storage method) are not affected by this algorithm change.

**Protection against tampering:** The `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` algorithm protects against data key tampering by cryptographically binding the encrypted data key to the encryption context. This prevents attackers from substituting a different encrypted data key in the Instruction File, which could potentially lead to decryption with an unintended key.

**Version compatibility:** Objects encrypted with the `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` algorithm can only be decrypted by V3 implementations and the latest V2 transition versions of the SDK that include V3 decryption support.

**Warning**
**Important:** Before enabling encryption with the `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` algorithm (by using `REQUIRE_ENCRYPT_ALLOW_DECRYPT` or `REQUIRE_ENCRYPT_REQUIRE_DECRYPT` commitment policies), you must ensure that all clients that will read these objects have been upgraded to V3 or the latest V2 transition version that supports V3 decryption. Failure to upgrade all readers first will result in decryption failures for newly encrypted objects.

## Update Existing Clients to Read New Formats
<a name="s3-encryption-migration-v2-v3-update-clients"></a>

You must first update your existing clients to the latest SDK release. After completing this step, your application's V2 clients will be able to decrypt objects encrypted by V3 encryption clients without updating your application's code base.

### Build and Install the Latest Version of the AWS SDK for C\+\+
<a name="s3-encryption-migration-v2-v3-build-install-sdk"></a>

 **Applications Consuming the SDK from Source**

If you build and install the AWS SDK for C\+\+ from source, download or clone the SDK source from [`aws/aws-sdk-cpp`](https://github.com/aws/aws-sdk-cpp) on GitHub . Then repeat your normal build and install steps.

If you are upgrading AWS SDK for C\+\+ from a version earlier than 1.11.x, see this [CHANGELOG](https://github.com/aws/aws-sdk-cpp/blob/main/CHANGELOG.md) for breaking changes introduced in each major version. For more information about how to build and install the AWS SDK for C\+\+, see [Getting the AWS SDK for C\+\+ from source code](sdk-from-source.md).

 **Applications Consuming the SDK from Vcpkg**

If your application uses [Vcpkg](https://github.com/microsoft/vcpkg) to track SDK updates, simply use your existing Vcpkg upgrade method to upgrade the SDK to the latest version. Keep in mind, there is a delay between when a version is released and when it is available through a package manager. The most recent version is always available through [installing from source](sdk-from-source.md).

You can run the following command to upgrade package `aws-sdk-cpp`:

```
vcpkg upgrade aws-sdk-cpp
```

And verify the version of package `aws-sdk-cpp`:

```
vcpkg list aws-sdk-cpp
```

The version should be at least 1.11.x to support decryption of V3-encrypted objects.

For more information on using Vcpkg with the AWS SDK for C\+\+, see [Getting the AWS SDK for C\+\+ from a package manager](sdk-from-pm.md).

### Build, Install, and Deploy Your Applications
<a name="s3-encryption-migration-v2-v3-build-deploy-apps"></a>

If your application is statically linking against the AWS SDK for C\+\+, code changes are not required in your application, but you must build your application again to consume the latest SDK changes. This step is not necessary for dynamic linking.

After upgrading your application's dependency version and verifying application functionality, proceed to deploying your application to your fleet. Once application deployment is complete, you can proceed with the next phase for migrating your application to use the V3 encryption and decryption clients.

## Migrate Encryption and Decryption Clients to V3
<a name="s3-encryption-migration-v2-v3-migrate"></a>

The following steps show you how to successfully migrate your code from V2 to V3 of the Amazon S3 encryption client. Since code changes are required, you will need to rebuild your application regardless of whether it's statically or dynamically linking against the AWS SDK for C\+\+.

### Using V3 Encryption Clients
<a name="s3-encryption-migration-v2-v3-using-v3-clients"></a>

V3 introduces the `S3EncryptionClientV3` class and `CryptoConfigurationV3` to replace the V2 equivalents. The key differences in V3 are:
+ V3 uses `KMSWithContextEncryptionMaterials` (same as V2) but requires explicit configuration in `CryptoConfigurationV3`.
+ All `PutObject` operations require an encryption context map (can be empty).
+ V3 introduces Commitment Policies to control encryption and decryption behavior.
+ By default, V3 encrypts with key commitment using the `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` algorithm.
+ The legacy algorithm decryption configuration API changes from `config.SetSecurityProfile(SecurityProfile::V2_AND_LEGACY);` to `config.AllowLegacy();`.

 **Example: Migrating from V2 to V3 with KMS Encryption**

 *Pre-migration (V2)*

```
// Create encryption materials
auto materials = Aws::MakeShared<KMSWithContextEncryptionMaterials>("s3EncryptionV2", CUSTOMER_MASTER_KEY_ID);

// Create V2 crypto configuration
CryptoConfigurationV2 cryptoConfig(materials);

// Create V2 encryption client
S3EncryptionClientV2 encryptionClient(cryptoConfig);

// Put object with encryption context
Aws::Map<Aws::String, Aws::String> encryptionContext;
encryptionContext.emplace("client", "aws-sdk-cpp");
encryptionContext.emplace("version", "1.11.0");

PutObjectRequest putObjectRequest;
putObjectRequest.SetBucket(BUCKET_NAME);
putObjectRequest.SetKey(OBJECT_KEY);
// Set object body...

auto putOutcome = encryptionClient.PutObject(putObjectRequest, encryptionContext);

// Get object with encryption context
GetObjectRequest getObjectRequest;
getObjectRequest.SetBucket(BUCKET_NAME);
getObjectRequest.SetKey(OBJECT_KEY);

auto getOutcome = encryptionClient.GetObject(getObjectRequest, encryptionContext);
```

 *During migration (V3 with backward compatibility)*

```
// Create encryption materials
auto materials = Aws::MakeShared<KMSWithContextEncryptionMaterials>("s3EncryptionV3", CUSTOMER_MASTER_KEY_ID);

// Create V3 crypto configuration with materials
CryptoConfigurationV3 cryptoConfig(materials);

// Set commitment policy to maintain compatibility with V2 encrypted objects
// This allows V3 clients to decrypt objects encrypted by the V2 client
cryptoConfig.SetCommitmentPolicy(CommitmentPolicy::REQUIRE_ENCRYPT_ALLOW_DECRYPT);

// Create V3 encryption client
S3EncryptionClientV3 encryptionClient(cryptoConfig);

// Put object with encryption context
Aws::Map<Aws::String, Aws::String> encryptionContext;
encryptionContext.emplace("client", "aws-sdk-cpp");
encryptionContext.emplace("version", "1.11.0");

PutObjectRequest putObjectRequest;
putObjectRequest.SetBucket(BUCKET_NAME);
putObjectRequest.SetKey(OBJECT_KEY);
// Set object body...

auto putOutcome = encryptionClient.PutObject(putObjectRequest, encryptionContext);

// Get object with encryption context
GetObjectRequest getObjectRequest;
getObjectRequest.SetBucket(BUCKET_NAME);
getObjectRequest.SetKey(OBJECT_KEY);

auto getOutcome = encryptionClient.GetObject(getObjectRequest, encryptionContext);
```

 *Post-migration (V3 with key commitment)*

```
// Create encryption materials
auto materials = Aws::MakeShared<KMSWithContextEncryptionMaterials>("s3EncryptionV3", CUSTOMER_MASTER_KEY_ID);

// Create V3 crypto configuration with materials
CryptoConfigurationV3 cryptoConfig(materials);

// Use the default commitment policy (REQUIRE_ENCRYPT_REQUIRE_DECRYPT)
// This encrypts with key commitment and does not decrypt V2 objects
// cryptoConfig.SetCommitmentPolicy(CommitmentPolicy::REQUIRE_ENCRYPT_ALLOW_DECRYPT);

// Create V3 encryption client
S3EncryptionClientV3 encryptionClient(cryptoConfig);

// Put object with encryption context
Aws::Map<Aws::String, Aws::String> encryptionContext;
encryptionContext.emplace("client", "aws-sdk-cpp");
encryptionContext.emplace("version", "1.11.0");

PutObjectRequest putObjectRequest;
putObjectRequest.SetBucket(BUCKET_NAME);
putObjectRequest.SetKey(OBJECT_KEY);
// Set object body...

auto putOutcome = encryptionClient.PutObject(putObjectRequest, encryptionContext);

// Get object with encryption context
GetObjectRequest getObjectRequest;
getObjectRequest.SetBucket(BUCKET_NAME);
getObjectRequest.SetKey(OBJECT_KEY);

auto getOutcome = encryptionClient.GetObject(getObjectRequest, encryptionContext);
```

## Additional Examples
<a name="s3-encryption-migration-v2-v3-examples"></a>

This section provides additional examples for configuring V3 encryption client options to support various migration scenarios and requirements.

### Enabling Legacy Support
<a name="s3-encryption-migration-v2-v3-examples-legacy-support"></a>

V3 clients can decrypt objects encrypted by V2 clients only when using the `REQUIRE_ENCRYPT_ALLOW_DECRYPT` or `FORBID_ENCRYPT_ALLOW_DECRYPT` commitment policies. However, if you need to decrypt objects encrypted by V1 clients, you must explicitly enable legacy support using the `AllowLegacy()` method.

**When to use legacy support:**
+ You have objects in S3 that were encrypted using V1 of the S3 Encryption Client.
+ You need to read these V1-encrypted objects with your V3 client during the migration process.
+ You are using the `REQUIRE_ENCRYPT_ALLOW_DECRYPT` or `FORBID_ENCRYPT_ALLOW_DECRYPT` commitment policy.

**Warning**
Legacy support should only be enabled temporarily during migration. Once all V1 objects have been re-encrypted with V2 or V3, disable legacy support to ensure maximum security.

**Example: Enabling Legacy Support**

```
// Create encryption materials
auto materials = Aws::MakeShared<KMSWithContextEncryptionMaterials>("s3EncryptionV3", CUSTOMER_MASTER_KEY_ID);

// Create V3 crypto configuration
CryptoConfigurationV3 cryptoConfig(materials);

// Enable legacy support to read V1 encrypted objects
cryptoConfig.AllowLegacy();

// Set commitment policy (default is REQUIRE_ENCRYPT_REQUIRE_DECRYPT but we need to allow decryption)
cryptoConfig.SetCommitmentPolicy(CommitmentPolicy::REQUIRE_ENCRYPT_ALLOW_DECRYPT);

// Create V3 encryption client with legacy support enabled
S3EncryptionClientV3 encryptionClient(cryptoConfig);

// Now you can decrypt objects encrypted by V1, V2, and V3 clients
GetObjectRequest getObjectRequest;
getObjectRequest.SetBucket(BUCKET_NAME);
getObjectRequest.SetKey(LEGACY_OBJECT_KEY);

Aws::Map<Aws::String, Aws::String> encryptionContext;
auto getOutcome = encryptionClient.GetObject(getObjectRequest, encryptionContext);
```

### Configuring Storage Method
<a name="s3-encryption-migration-v2-v3-examples-storage-method"></a>

The S3 Encryption Client can store encryption metadata in two ways: as object metadata (the default) or in a separate Instruction File. You can configure the storage method using the `SetStorageMethod()` method on `CryptoConfigurationV3`.

**Storage method options:**

**`METADATA` (Default)**
Encryption metadata is stored in the object's metadata headers. This is the most common and convenient method as all encryption information is stored with the object itself.
**When to use:** Use this method for most scenarios. It simplifies object management since encryption metadata travels with the object.

**`INSTRUCTION_FILE`**
Encryption metadata is stored in a separate S3 object (the Instruction File) with the suffix `.instruction`.
**When to use:** Use this method when object metadata size is a concern or when you need to separate encryption metadata from the encrypted object. Note that using Instruction Files requires managing two S3 objects (the encrypted object and its instruction file) instead of one.

**Example: Configuring Storage Method**

```
// Create encryption materials
auto materials = Aws::MakeShared<KMSWithContextEncryptionMaterials>("s3EncryptionV3", CUSTOMER_MASTER_KEY_ID);

// Create V3 crypto configuration
CryptoConfigurationV3 cryptoConfig(materials);

// Option 1: Use metadata storage (default, can be omitted)
cryptoConfig.SetStorageMethod(StorageMethod::METADATA);

// Option 2: Use instruction file storage
cryptoConfig.SetStorageMethod(StorageMethod::INSTRUCTION_FILE);

// Create V3 encryption client with the configured storage method
S3EncryptionClientV3 encryptionClient(cryptoConfig);

// Put object - encryption metadata will be stored according to the configured method
Aws::Map<Aws::String, Aws::String> encryptionContext;
encryptionContext.emplace("client", "aws-sdk-cpp");

PutObjectRequest putObjectRequest;
putObjectRequest.SetBucket(BUCKET_NAME);
putObjectRequest.SetKey(OBJECT_KEY);
// Set object body...

auto putOutcome = encryptionClient.PutObject(putObjectRequest, encryptionContext);

// If using INSTRUCTION_FILE, a separate object with key "OBJECT_KEY.instruction" will be created
```

**Note**
When using the `INSTRUCTION_FILE` storage method, remember that deleting the encrypted object does not automatically delete the instruction file. You must manage both objects separately.
