---
source_url: https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/java-v4-migration.html
---

# S3 Encryption Client Migration (V3 to V4)
<a name="java-v4-migration"></a>

Version 4.*x* of the Amazon S3 Encryption Client introduces AES GCM with Key Commitment (ALG\_AES\_256\_GCM\_HKDF\_SHA512\_COMMIT\_KEY) and Commitment Policies to enhance security by protecting against data key tampering in Instruction Files. This migration guide explains how to safely upgrade from 3.*x* to 4.*x* while maintaining backward compatibility during the transition.

## Migration Overview
<a name="java-v4-migration-overview"></a>

Migrating to version 4.*x* of the Amazon S3 Encryption Client requires a two-phase approach to ensure compatibility and security. The migration path depends on your current version.

### Migrate 2.x to 3.x
<a name="java-migration-2x-to-3x"></a>

If you're using 2.*x*, you must first migrate to 3.*x* before migrating to 4.*x*. Version 3.*x* introduces significant API changes, including a simplified client builder interface that replaces the `EncryptionMaterialsProvider` pattern used in 2.*x*. For detailed instructions on upgrading from 2.*x* to 3.*x* and understanding these API changes, see [S3 Encryption Client Migration (V2 to V3)](java-v3-migration.md). After upgrading to 3.*x*, follow the migration path below to migrate to 4.*x*.

**Note**
Direct migration from 2.*x* to 4.*x* is possible but not recommended. To avoid data access issues and ensure data accessibility across your entire infrastructure, follow the detailed migration steps in [Migrate to 4.*x*](#java-v4-migration-migrate).

### Migrate 3.x to 4.x
<a name="java-migration-3x-to-4x"></a>

If you're using 3.*x*, follow the two-phase approach below to migrate to 4.*x*. Version 4.*x* introduces Commitment Policies and AES GCM with Key Commitment (ALG\_AES\_256\_GCM\_HKDF\_SHA512\_COMMIT\_KEY) to enhance security. The client builder interface remains consistent with 3.*x*, but you will need to configure the appropriate Commitment Policy for your use case. Ensure you're using Amazon S3 Encryption Client version 3.6.0 or greater before starting Phase 1.

1. **Phase 1: Update existing 3.*x* clients to read 4.*x* formats**

   Update all existing 3.*x* clients in your environment to Amazon S3 Encryption Client version 3.6.0 or greater. This version can read objects encrypted with 4.*x* algorithms and commitment policies. This ensures that when you start encrypting with 4.*x*, your existing applications can still decrypt the new objects.

1. **Phase 2: Migrate encryption and decryption clients to 4.*x***

   After all clients can read 4.*x* formats, migrate your encryption and decryption operations to use 4.*x* clients with the appropriate Commitment Policy. This phase introduces the enhanced security features while maintaining backward compatibility with existing encrypted objects through three progressive steps.

This phased approach prevents compatibility issues and ensures that all encrypted objects remain accessible throughout the migration process.

## Understanding V4 Concepts
<a name="java-v4-migration-concepts"></a>

Version 4.*x* introduces two key security concepts that enhance protection against data tampering:

### Commitment Policy
<a name="java-v4-migration-commitment-policy"></a>

Commitment Policy controls how the encryption client handles key commitment during encryption and decryption operations. 4.*x* provides three policy options to support different migration scenarios and security requirements:

`FORBID_ENCRYPT_ALLOW_DECRYPT` (Default for 3.*x* transitional versions)
**Encryption behavior:** Encrypts objects without key commitment, using the same algorithms as 3.*x*.
**Decryption behavior:** Allows decryption of objects encrypted with and without key commitment.
**Security implications:** This policy does not enforce key commitment and may allow tampering with the encrypted data key in Instruction Files. Use this policy only during the initial migration phase when you need 3.*x* clients to read newly encrypted objects.
**Version Compatibility:** Objects encrypted with this policy can be read by any 3.*x* or 4.*x* client. This is the default (and only) policy for 3.*x* clients.

`REQUIRE_ENCRYPT_ALLOW_DECRYPT`
**Encryption behavior:** Encrypts objects with key commitment using the ALG\_AES\_256\_GCM\_HKDF\_SHA512\_COMMIT\_KEY algorithm.
**Decryption behavior:** Allows decryption of both objects encrypted with key commitment and objects encrypted without key commitment.
**Security implications:** This policy provides strong security for newly encrypted objects while maintaining backward compatibility for reading older objects. This is the recommended policy for most migration scenarios.
**Version Compatibility:** Objects encrypted with this policy can only be read by 3.*x* clients (version 3.6.0 or greater) and 4.*x* clients.

`REQUIRE_ENCRYPT_REQUIRE_DECRYPT` (Default for 4.*x*)
**Encryption behavior:** Encrypts objects with key commitment using the ALG\_AES\_256\_GCM\_HKDF\_SHA512\_COMMIT\_KEY algorithm.
**Decryption behavior:** Only allows decryption of objects encrypted with key commitment. Rejects objects encrypted without key commitment.
**Security implications:** This policy provides the highest level of security by enforcing key commitment for all operations. Use this policy only after all objects have been re-encrypted with key commitment and you no longer need to read legacy 3.*x* encrypted objects.
**Version Compatibility:** Objects encrypted with this policy can only be read by 3.*x* clients (version 3.6.0 or greater) and 4.*x* clients. This policy will reject objects encrypted without key commitment during decryption.

**Migration considerations:** During migration, start with `FORBID_ENCRYPT_ALLOW_DECRYPT` if you need 3.*x* clients to read new objects, then move to `REQUIRE_ENCRYPT_ALLOW_DECRYPT` once all clients are upgraded to 3.*x* (version 3.6.0 or greater) or 4.*x*. Finally, consider `REQUIRE_ENCRYPT_REQUIRE_DECRYPT` only after all legacy objects have been re-encrypted.

### AES GCM with Key Commitment
<a name="java-v4-migration-aes-gcm-kc"></a>

AES GCM with Key Commitment (ALG\_AES\_256\_GCM\_HKDF\_SHA512\_COMMIT\_KEY) is the new encryption algorithm suite introduced in version 4.*x* that protects against data key tampering in Instruction Files by cryptographically binding the key to its intended use.

**Instruction File impact:** The ALG\_AES\_256\_GCM\_HKDF\_SHA512\_COMMIT\_KEY algorithm only impacts Instruction Files, which are separate S3 objects that store encryption metadata including the encrypted data key. Objects that store encryption metadata in object metadata (the default storage method) are not affected by this algorithm change.

**Protection against tampering:** The ALG\_AES\_256\_GCM\_HKDF\_SHA512\_COMMIT\_KEY algorithm protects against data key tampering by cryptographically binding the encrypted data key to the encryption context. This prevents attackers from substituting a different encrypted data key in the Instruction File, which could potentially lead to decryption with an unintended key.

**Version Compatibility:** Objects encrypted with ALG\_AES\_256\_GCM\_HKDF\_SHA512\_COMMIT\_KEY can only be decrypted by 3.*x* clients (version 3.6.0 or greater) or 4.*x* clients. Earlier 3.*x* clients cannot read these objects.

**Important**
**Important:** Before enabling encryption with the ALG\_AES\_256\_GCM\_HKDF\_SHA512\_COMMIT\_KEY algorithm (by using `REQUIRE_ENCRYPT_ALLOW_DECRYPT` or `REQUIRE_ENCRYPT_REQUIRE_DECRYPT` commitment policies), you must ensure that all clients that will read these objects have been upgraded to 3.*x* (version 3.6.0 or greater) or 4.*x*. Failure to upgrade all readers first will result in decryption failures for newly encrypted objects.

## Update existing 3.*x* clients to read 4.*x* formats
<a name="java-v4-migration-update-clients"></a>

Before migrating to 4.*x* encryption, you must first update all existing 3.*x* clients to a version that can read 4.*x* encrypted objects. This ensures compatibility when you begin encrypting with 4.*x*.

### Build and install the latest S3EC version
<a name="java-v4-migration-build-install"></a>

Update your Maven or Gradle dependencies to use the latest version of the Amazon S3 Encryption Client 3.*x* that includes support for reading 4.*x* messages:

**Maven (pom.xml):**

```
<dependency>
    <groupId>software.amazon.encryption.s3</groupId>
    <artifactId>amazon-s3-encryption-client-java</artifactId>
    <version>3.6.0</version>
</dependency>
```

**Gradle (build.gradle):**

```
dependencies {
    implementation 'software.amazon.encryption.s3:amazon-s3-encryption-client-java:3.6.0'
}
```

### Build, Install, and Deploy Applications
<a name="java-v4-migration-build-deploy"></a>

After updating your dependencies, rebuild and deploy your applications:

1. **Clean and rebuild:**

   ```
   mvn clean install
   ```

   or for Gradle:

   ```
   gradle clean build
   ```

1. **Run your tests:**

   ```
   mvn test
   ```

   or for Gradle:

   ```
   gradle test
   ```

1. **Deploy updated applications:** Deploy the updated applications to all environments where S3 Encryption Client is used. Ensure all applications can successfully decrypt existing 3.*x* encrypted objects before proceeding to Phase 2.

## Migrate encryption and decryption clients to 4.*x*
<a name="java-v4-migration-migrate"></a>

After all clients in your environment can read 4.*x* formats, you can migrate your encryption and decryption operations to use 4.*x* clients. The following examples demonstrate the transition from 3.*x* to 4.*x* clients using different Commitment Policies during the transition.

### Client Migration Examples
<a name="java-v4-migration-client-transition"></a>

The following examples show how to migrate from 3.*x* to 4.*x* clients using different Commitment Policies during the transition:

**Pre-migration (3.x Client)**

```
// V3 Client (Prior 3.x versions)
// Uses default algorithm without key commitment (ALG_AES_256_GCM_IV12_TAG16_NO_KDF)
S3Client v3Client = S3EncryptionClient.builder()
        .kmsKeyId(kmsKeyId)
        .build();

// V3 Client (Latest 3.x version - 3.6.0 or greater)
// Prepare for V4 migration with FORBID_ENCRYPT_ALLOW_DECRYPT
// This allows reading both committed and non-committed objects
S3Client v3Client = S3EncryptionClient.builderV4()
        .kmsKeyId(kmsKeyId)
        .encryptionAlgorithm(AlgorithmSuite.ALG_AES_256_GCM_IV12_TAG16_NO_KDF)
        .commitmentPolicy(CommitmentPolicy.FORBID_ENCRYPT_ALLOW_DECRYPT)
        .build();
```

**During Migration (4.*x* Client with FORBID\_ENCRYPT\_ALLOW\_DECRYPT Policy)**

Update your Maven or Gradle dependencies to use the latest version of the Amazon S3 Encryption Client 4.*x*:

**Maven (pom.xml):**

```
<dependency>
    <groupId>software.amazon.encryption.s3</groupId>
    <artifactId>amazon-s3-encryption-client-java</artifactId>
    <version>{{4.x}}</version>
</dependency>
```

**Gradle (build.gradle):**

```
dependencies {
    implementation 'software.amazon.encryption.s3:amazon-s3-encryption-client-java:{{4.x}}'
}
```

After updating your dependencies, make code changes as described below. This should result in no functional changes to your application.

```
// V4 Client with FORBID_ENCRYPT_ALLOW_DECRYPT
// This maintains V2/V3 compatibility during migration
// Uses non-committing algorithm to maintain compatibility with V2/V3 clients
S3Client v4Client = S3EncryptionClient.builderV4()
        .kmsKeyId(kmsKeyId)
        .encryptionAlgorithm(AlgorithmSuite.ALG_AES_256_GCM_IV12_TAG16_NO_KDF)
        .commitmentPolicy(CommitmentPolicy.FORBID_ENCRYPT_ALLOW_DECRYPT)
        .build();
```

**During migration (4.*x* Client with REQUIRE\_ENCRYPT\_ALLOW\_DECRYPT Policy)**

After deploying the FORBID\_ENCRYPT\_ALLOW\_DECRYPT changes, make code changes as described below. This will cause your application to start writing objects encrypted with key commitment.

```
// V4 Client with REQUIRE_ENCRYPT_ALLOW_DECRYPT
// This encrypts with commitment but can read objects with or without commitment
// Uses committing algorithm to protect against data key tampering
S3Client v4Client = S3EncryptionClient.builderV4()
        .kmsKeyId(kmsKeyId)
        .commitmentPolicy(CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT)
        .build();
```

**Post-migration (4.*x* Client with default commitment policy)**

After deploying the REQUIRE\_ENCRYPT\_ALLOW\_DECRYPT changes, make code changes as described below. This will cause your application to stop reading objects encrypted without key commitment. Before deploying this change, ensure any existing objects are now encrypted with key commitment.

```
// V4 Client with default REQUIRE_ENCRYPT_REQUIRE_DECRYPT policy
// This encrypts with commitment and only reads objects with commitment (most secure)
// Uses committing algorithm by default
S3Client v4Client = S3EncryptionClient.builderV4()
        .kmsKeyId(kmsKeyId)
        .build();
```

## Enable Legacy Decryption Modes
<a name="java-v4-migration-legacy-modes"></a>

If you need to decrypt objects or data keys that were encrypted by earlier versions of the Amazon S3 Encryption Client, you need to explicitly enable this behavior when you instantiate the client.

The `enableLegacyUnauthenticatedModes` parameter of the `builderV4()` method enables the Amazon S3 Encryption Client to decrypt content encrypted with legacy unauthenticated encryption algorithms (such as AES-CBC) and to perform ranged GET requests on encrypted objects.

The `enableLegacyWrappingAlgorithms` parameter of the `builderV4()` method enables the Amazon S3 Encryption Client to decrypt data keys that were wrapped with legacy V2 wrapping algorithms.

If your `v4Client` doesn't include the necessary settings, and it encounters an object or data key encrypted with a legacy algorithm, it throws `S3EncryptionClientException`.

For example, this code builds a `v4Client` object with a user-provided raw AES wrapping key. This client always encrypts only with fully supported algorithms. However, it can decrypt objects and data keys encrypted with fully supported or legacy algorithms.

```
// v4

class v4EnableLegacyDecryptionModesExample {
    public static void main(String[] args) {
        S3Client v4Client = S3EncryptionClient.builderV4()
                .aesKey(aesKey)
                .commitmentPolicy(CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT)
                .enableLegacyUnauthenticatedModes(true)
                .enableLegacyWrappingAlgorithms(true)
                .build();
    }
}
```

The legacy decryption modes are designed to be a temporary fix. After you've re-encrypted all of your objects with fully supported algorithms, you can eliminate it from your code.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon S3 Encryption Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazon-s3-encryption-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
