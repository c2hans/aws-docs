---
source_url: https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/s3-encryption-migration-v2-v4.html
---

The AWS SDK for .NET V3 has reached end-of-support.

We recommend that you migrate to [AWS SDK for .NET V4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html). For additional details and information on how to migrate, please refer to our [end-of-support announcement](https://aws.amazon.com/blogs/developer/aws-sdk-for-net-v3-end-of-support-announcement/).

# Amazon S3 Encryption Client Migration (V2 to V4)
<a name="s3-encryption-migration-v2-v4"></a>

**Note**
If you are using V1 and want to migrate to V4, you must first migrate to V2. See [Amazon S3 Encryption Client Migration (V1 to V2)](s3-encryption-migration-v1-v2.md).

This topic shows how to migrate your applications from Version 2 (V2) of the Amazon Simple Storage Service (Amazon S3) encryption client to Version 4 (V4), and ensure application availability throughout the migration process. V4 uses AES-GCM with key commitment for content encryption and introduces Commitment Policies to enhance security against key substitution attacks.

The V4 client is available in the [Amazon.Extensions.S3.Encryption](https://www.nuget.org/packages/Amazon.Extensions.S3.Encryption) NuGet package.

**Important**
**Breaking Changes:** V4 clients configured with `REQUIRE_ENCRYPT_REQUIRE_DECRYPT` policy cannot decrypt objects encrypted with V1 or V2 clients. Only the latest V2 clients can decrypt V4-encrypted objects with key commitment. Before moving to the `REQUIRE_ENCRYPT_REQUIRE_DECRYPT` policy, you must re-encrypt all your existing data using V4 clients with key commitment enabled.

## Understanding V4 Concepts
<a name="s3-encryption-migration-v2-v4-concepts"></a>

V4 uses AES-GCM with key commitment for content encryption and introduces key security concepts that enhance the protection of your encrypted data:

### Commitment Policy
<a name="s3-encryption-migration-v2-v4-concepts-policy"></a>

Commitment Policy controls how the encryption client handles key commitment during encryption and decryption operations. V4 supports three commitment policies:

`FORBID_ENCRYPT_ALLOW_DECRYPT`
*Encryption:* Without commitment
*Decryption:* Allows non-committing objects
*Security:* Does not enforce commitment and may allow tampering
*Compatibility:* All V2 and V4 implementations can read objects encrypted with this policy

`REQUIRE_ENCRYPT_ALLOW_DECRYPT`
*Encryption:* With key commitment
*Decryption:* Allows both committing and non-committing objects
*Security:* New objects are protected against key substitution attacks, old objects still readable
*Compatibility:* Only V4 supports this policy

`REQUIRE_ENCRYPT_REQUIRE_DECRYPT`(Default for V4)
*Encryption:* With key commitment
*Decryption:* Only committing objects
*Security:* Full commitment enforcement for maximum security
*Compatibility:* Only V4 supports this policy

### AES GCM with Key Commitment
<a name="s3-encryption-migration-v2-v4-concepts-aesgcm"></a>

V4 uses AES-GCM with key commitment for content encryption, which provides enhanced security:
+ *Tampering Protection:* It protects against key substitution attacks by cryptographically binding the key to the encrypted data.
+ *Version Compatibility:* Objects encrypted with key commitment can only be decrypted by V4 clients and newer versions.

**Warning**
Before enabling key commitment encryption in production, ensure that all applications that need to decrypt your objects have been upgraded to V4 or newer as V2 client is being deprecated.

## Update Existing Clients to Read V4 Formats
<a name="s3-encryption-migration-v2-v4-update-clients"></a>

The V4 encryption client uses encryption algorithms that older versions of the client don't support. The first step in the migration is to update your V2 clients so that they can read the new V4 format.

### Update NuGet Package Dependencies
<a name="s3-encryption-migration-v2-v4-update-nuget"></a>

Update your applications to use the latest version of the [Amazon.Extensions.S3.Encryption](https://www.nuget.org/packages/Amazon.Extensions.S3.Encryption) NuGet package that includes V4 support. Perform the following steps on each of your applications:

1. Update to the latest [Amazon.Extensions.S3.Encryption](https://www.nuget.org/packages/Amazon.Extensions.S3.Encryption) package. If your project depends directly on the **AWSSDK.S3** or **AWSSDK.KeyManagementService** packages, you must either update those dependencies or remove them so that their updated versions will be pulled in with this new package.

1. Ensure your `using` statements reference the correct namespace:

   ```
   using Amazon.Extensions.S3.Encryption;
   using Amazon.Extensions.S3.Encryption.Primitives;
   ```

1. Rebuild and redeploy your application.

Your existing V2 clients will continue to work with the updated package and will be able to decrypt objects encrypted by V4 clients (depending on the commitment policy used).

### Build and Deploy Applications
<a name="s3-encryption-migration-v2-v4-build-deploy"></a>

After updating your NuGet package dependencies:

1. Build your application to ensure all dependencies are resolved correctly.

1. Test your application in a development environment to verify that existing functionality continues to work.

1. Deploy the updated application to your production environment.

This update enables your existing V2 clients to decrypt objects that will be encrypted by V4 clients, ensuring compatibility during the migration process.

## Migrate to V4 Clients
<a name="s3-encryption-migration-v2-v4-migrate"></a>

After updating your existing clients to read the new encryption format, you can proceed to safely update your applications to use V4 encryption and decryption clients. The V4 client provides enhanced security through key commitment while maintaining compatibility with existing encrypted objects.

### 4-Step Migration Process
<a name="s3-encryption-migration-v2-v4-migrate-steps"></a>

The migration from V2 to V4 follows a structured 4-step process to ensure compatibility and security. Each step represents a specific configuration that should be deployed across all your applications before proceeding to the next step.

1. **Step 0: V2 Client (Starting Point)** - Your existing V2 implementation

1. **Step 1: V4 with V2 Compatibility** - Migrate to V4 client while maintaining V2-compatible encryption behavior

1. **Step 2: V4 with Key Commitment Writes** - Start encrypting with key commitment while allowing decryption of legacy objects

1. **Step 3: V4 with Full Enforcement** - Require key commitment for both encryption and decryption

### Step 0: V2 Client (Starting Point)
<a name="s3-encryption-migration-v2-v4-step0"></a>

This represents your existing V2 client configuration. This step demonstrates the starting state before migration.

```
using Amazon.Extensions.S3.Encryption;
using Amazon.Extensions.S3.Encryption.Primitives;
using Amazon.S3.Model;

// Step 0: V2 Client - Starting configuration
var encryptionContext = new Dictionary<string, string>();
var encryptionMaterial = new EncryptionMaterialsV2(kmsKeyId, KmsType.KmsContext, encryptionContext);

#pragma warning disable 0618
var configuration = new AmazonS3CryptoConfigurationV2(SecurityProfile.V2);
#pragma warning enable 0618

var encryptionClient = new AmazonS3EncryptionClientV2(configuration, encryptionMaterial);

// Use the client for PutObject and GetObject operations
await encryptionClient.PutObjectAsync(new PutObjectRequest
{
    BucketName = bucket,
    Key = objectKey,
    ContentBody = content
});
```

### Step 1: V4 with V2 Compatibility
<a name="s3-encryption-migration-v2-v4-step1"></a>

Migrate to the V4 client while maintaining identical behavior to V2. This step uses `FORBID_ENCRYPT_ALLOW_DECRYPT` policy to encrypt without commitment and allow decryption of all objects.

```
using Amazon.Extensions.S3.Encryption;
using Amazon.Extensions.S3.Encryption.Primitives;
using Amazon.S3.Model;

// Step 1: V4 Client with V2 compatibility
var encryptionContext = new Dictionary<string, string>();
var encryptionMaterial = new EncryptionMaterialsV4(kmsKeyId, KmsType.KmsContext, encryptionContext);

var configuration = new AmazonS3CryptoConfigurationV4(
    SecurityProfile.V4,
    CommitmentPolicy.FORBID_ENCRYPT_ALLOW_DECRYPT,
    ContentEncryptionAlgorithm.AesGcm);

var encryptionClient = new AmazonS3EncryptionClientV4(configuration, encryptionMaterial);

// Use the client for PutObject and GetObject operations
await encryptionClient.PutObjectAsync(new PutObjectRequest
{
    BucketName = bucket,
    Key = objectKey,
    ContentBody = content
});
```

**Behavior:** Encrypts without commitment, can decrypt both committing and non-committing objects. Identical to V2 behavior.

### Step 2: V4 with Key Commitment Writes
<a name="s3-encryption-migration-v2-v4-step2"></a>

Start encrypting with key commitment while maintaining backward compatibility for decryption. This step uses `REQUIRE_ENCRYPT_ALLOW_DECRYPT` policy.

**Warning**
Before deploying Step 2, ensure all readers have been updated to Step 1 or later to handle key commitment encryption.

```
using Amazon.Extensions.S3.Encryption;
using Amazon.Extensions.S3.Encryption.Primitives;
using Amazon.S3.Model;

// Step 2: V4 Client with key commitment writes
var encryptionContext = new Dictionary<string, string>();
var encryptionMaterial = new EncryptionMaterialsV4(kmsKeyId, KmsType.KmsContext, encryptionContext);

var configuration = new AmazonS3CryptoConfigurationV4(
    SecurityProfile.V4,
    CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT,
    ContentEncryptionAlgorithm.AesGcmWithCommitment);

var encryptionClient = new AmazonS3EncryptionClientV4(configuration, encryptionMaterial);

// Use the client for PutObject and GetObject operations
await encryptionClient.PutObjectAsync(new PutObjectRequest
{
    BucketName = bucket,
    Key = objectKey,
    ContentBody = content
});
```

**Behavior:** Encrypts with commitment, can decrypt both committing and non-committing objects. New objects are protected against key substitution attacks.

### Step 3: V4 with Full Enforcement
<a name="s3-encryption-migration-v2-v4-step3"></a>

Require key commitment for both encryption and decryption. This step uses `REQUIRE_ENCRYPT_REQUIRE_DECRYPT` policy for maximum security.

**Warning**
Before deploying Step 3, ensure all objects in your system have been re-encrypted with key commitment (Step 2). This step will fail to decrypt objects encrypted without commitment.

```
using Amazon.Extensions.S3.Encryption;
using Amazon.Extensions.S3.Encryption.Primitives;
using Amazon.S3.Model;

// Step 3: V4 Client with full key commitment enforcement
var encryptionContext = new Dictionary<string, string>();
var encryptionMaterial = new EncryptionMaterialsV4(kmsKeyId, KmsType.KmsContext, encryptionContext);

var configuration = new AmazonS3CryptoConfigurationV4(
    SecurityProfile.V4,
    CommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT,
    ContentEncryptionAlgorithm.AesGcmWithCommitment);

var encryptionClient = new AmazonS3EncryptionClientV4(configuration, encryptionMaterial);

// Use the client for PutObject and GetObject operations
await encryptionClient.PutObjectAsync(new PutObjectRequest
{
    BucketName = bucket,
    Key = objectKey,
    ContentBody = content
});
```

**Behavior:** Encrypts with commitment, only decrypts objects encrypted with commitment. Maximum security against key substitution attacks.

## Additional Configuration Examples
<a name="s3-encryption-migration-v2-v4-examples"></a>

This section provides additional examples for configuring V4 clients with different options during migration.

### Enabling Legacy Support
<a name="s3-encryption-migration-v2-v4-examples-legacy"></a>

To enable V4 clients to read objects encrypted by V1 and V2 clients, configure the client with a commitment policy that allows legacy decryption:

```
using Amazon.Extensions.S3.Encryption;
using Amazon.Extensions.S3.Encryption.Primitives;

// Configure V4 client to read V1/V2 objects
var configuration = new AmazonS3CryptoConfigurationV4(CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT)
{
    StorageMode = CryptoStorageMode.ObjectMetadata
};

// This configuration allows:
// - Encryption: With commitment (secure)
// - Decryption: Both V2 (non-committing) and V4 (committing) objects
```

Use this configuration during migration when you need to decrypt objects encrypted by older clients while ensuring new objects are encrypted with enhanced security.

### Configuring Storage Method
<a name="s3-encryption-migration-v2-v4-examples-storage"></a>

V4 supports two storage methods for encryption metadata. Choose the method that best fits your use case:

**Object Metadata (Default)**

```
var configuration = new AmazonS3CryptoConfigurationV4(CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT)
{
    StorageMode = CryptoStorageMode.ObjectMetadata
};
// Encryption metadata is stored in S3 object metadata
```

**Instruction File**

```
var configuration = new AmazonS3CryptoConfigurationV4(CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT)
{
    StorageMode = CryptoStorageMode.InstructionFile
};
// Encryption metadata is stored in a separate S3 object (instruction file)
```

Use `InstructionFile` when you need to preserve object metadata for other purposes or when working with objects that have metadata size limitations.

### Configuring Commitment Policy
<a name="s3-encryption-migration-v2-v4-examples-policy"></a>

Choose the appropriate commitment policy based on your security requirements and migration phase:

**Migration Phase (V2 Compatibility)**

```
// For migration: encrypt without commitment, allow all decryption
var migrationConfig = new AmazonS3CryptoConfigurationV4(CommitmentPolicy.FORBID_ENCRYPT_ALLOW_DECRYPT);
```

**Transition Phase (Recommended)**

```
// For transition: encrypt with commitment, allow legacy decryption
var transitionConfig = new AmazonS3CryptoConfigurationV4(CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT);
```

**Full Security Phase**

```
// For maximum security: require commitment for both encryption and decryption
var secureConfig = new AmazonS3CryptoConfigurationV4(CommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT);
```

Start with `FORBID_ENCRYPT_ALLOW_DECRYPT` during initial migration, move to `REQUIRE_ENCRYPT_ALLOW_DECRYPT` for the transition phase, and finally use `REQUIRE_ENCRYPT_REQUIRE_DECRYPT` when all clients have been upgraded and all objects have been re-encrypted with commitment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for .NET. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-net` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
