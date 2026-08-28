---
source_url: https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/java-v3-migration.html
---

# S3 Encryption Client Migration (V2 to V3)
<a name="java-v3-migration"></a>

**Note**
If you're using S3 Encryption Client V3 and want to migrate to V4, see [S3 Encryption Client Migration (V3 to V4)](java-v4-migration.md).

The `v3Client` constructor does not use the `EncryptionMaterialsProvider` that was required in versions 1.*x* and 2.*x* of the Amazon S3 Encryption Client. Instead, you use a parameter of the `v3Client` builder to specify your wrapping key. The Amazon S3 Encryption Client supports the following wrapping keys: AWS Key Management Service (AWS KMS) symmetric [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys), raw AES-GCM (Advanced Encryption Standard/Galois Counter Mode) keys, and raw RSA keys. The Amazon S3 Encryption Client optimizes its settings based on the wrapping key type.

When updating from earlier versions of the Amazon S3 Encryption Client to version 3.*x*, you need to update your client builder code to use the new, simpler interface for the `v3Client`. If you're decrypting ciphertext that was encrypted by earlier versions of the Amazon S3 Encryption Client, you might also need to allow the Amazon S3 Encryption Client to [decrypt legacy encryption algorithms](#enable-legacy-v2-v3).

To update to Amazon S3 Encryption Client version 3.*x*, delete the code that instantiates the `EncryptionMaterialsProvider`. Then replace the code that calls the `v1Client` or `v2Client` builder with code that calls the `v3Client` builder. Use a parameter of the `v3Client` builder to specify your wrapping key.

The following examples show the equivalent code required to specify a KMS key as the wrapping key in versions 1.*x*, 2.*x*, and 3.*x* of the Amazon S3 Encryption Client.

------
#### [ Version 1.*x* ]

In Amazon S3 Encryption Client version 1.*x*, you instantiate an `EncryptionMaterialsProvider` with your wrapping key, and then specify that materials provider when instantiating the `v1Client` object.

```
// v1

class v1KMSKeyExample {
    public static void main(String[] args) {

        EncryptionMaterialsProvider materialsProvider = new KMSEncryptionMaterialsProvider({{kmsKeyId}});
        AmazonS3Encryption v1Client = AmazonS3EncryptionClient.encryptionBuilder()
                .withEncryptionMaterialsProvider({{materialsProvider}})
                .build();
    }
}
```

------
#### [ Version 2.*x* ]

In Amazon S3 Encryption Client version 2.*x*, you instantiate an `EncryptionMaterialsProvider` with your wrapping key, and then specify that materials provider when instantiating the `v2Client` object.

```
// v2

class v2KMSKeyExample {
    public static void main(String[] args) {

        EncryptionMaterialsProvider materialsProvider = new KMSEncryptionMaterialsProvider({{kmsKeyId}});
        AmazonS3EncryptionV2 v2Client = AmazonS3EncryptionClientV2.encryptionBuilder()
                .withEncryptionMaterialsProvider({{materialsProvider}})
                .build();
    }
}
```

------
#### [ Version 3.*x* ]

In Amazon S3 Encryption Client version 3.*x*, the `v3Client` constructor requires only a parameter that identifies the wrapping key. For a KMS key, use the `kmsKeyId` parameter. The value of the `kmsKeyId` parameter can be any valid KMS key identifier. For details, see [Key identifiers](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) in the *AWS Key Management Service Developer Guide*. 3.*x* clients use the default algorithm suite (ALG\_AES\_256\_GCM\_IV12\_TAG16\_NO\_KDF) which does not support key commitment and is maintained for backward compatibility. Content encrypted with this algorithm can be read by any 2.*x*, 3.*x*, or 4.*x* client.

```
// v3

class v3KMSKeyExample {
    public static void main(String[] args) {
        // Uses default algorithm without key commitment (ALG_AES_256_GCM_IV12_TAG16_NO_KDF)
        S3Client v3Client = S3EncryptionClient.builder()
                .kmsKeyId({{kmsKeyId}})
                .build();
    }
}
```

If you're using Amazon S3 Encryption Client version 3.*x* and planning to migrate to 4.*x*, use the latest 3.*x* version (3.6.0 or greater) with the following configuration:

```
// 3.x (Latest 3.x version - 3.6.0 or greater for 4.x migration)

class v3TransitionalKMSKeyExample {
    public static void main(String[] args) {
        // Explicitly set your commitment policy to FORBID_ENCRYPT_ALLOW_DECRYPT
        S3Client v3Client = S3EncryptionClient.builderV4()
                .kmsKeyId({{kmsKeyId}})
                .encryptionAlgorithm(AlgorithmSuite.ALG_AES_256_GCM_IV12_TAG16_NO_KDF)
                // This will allow your writers to continue writing messages without commitment
                // while being able to read messages with or without commitment.
                .commitmentPolicy(CommitmentPolicy.FORBID_ENCRYPT_ALLOW_DECRYPT)
                .build();
    }
}
```

------

## Key API Changes in Versions 3.6.0 and Greater
<a name="v3-transitional-api-changes"></a>

If you're using Amazon S3 Encryption Client version 3.*x* and planning to migrate to 4.*x*, you need to be aware of key API changes introduced in versions 3.6.0 and greater. These versions introduce new builder methods and parameters to support commitment policies and algorithm suite configuration in preparation for 4.*x*.

**Key API Changes:**
+ `builderV4()` method: Use this method when configuring commitment policies and algorithm suites for 4.*x* migration. The standard `builder()` method is marked as deprecated and will be removed in 4.*x*.
+ `encryptionAlgorithm()` parameter: Explicitly specify the encryption algorithm suite. For transitional versions, use `AlgorithmSuite.ALG_AES_256_GCM_IV12_TAG16_NO_KDF` (AES-256-GCM without key derivation function or key commitment) to maintain backward compatibility with earlier 3.*x* clients.
+ `commitmentPolicy()` parameter: Set the commitment policy for your use case. For transitional versions, use `CommitmentPolicy.FORBID_ENCRYPT_ALLOW_DECRYPT` to allow your writers to continue writing messages without commitment while being able to read messages with or without commitment.

The standard `builder()` method remains available in versions 3.6.0 and greater for backward compatibility, but it is marked as deprecated and will be removed in 4.*x*. To prepare for the upgrade to 4.*x*, migrate your code to use `builderV4()` with the appropriate commitment policy configuration.

The `builderV4()` method implements a subset of the functionality found in the 4.*x* client, but the behavior is the same. See [Migrating to 4.*x*](java-v4-migration.md) for more information on migrating from 3.*x* to 4.*x*.

## Enable Legacy Decryption Modes
<a name="enable-legacy-v2-v3"></a>

If you need to decrypt objects or data keys that were encrypted by earlier versions of the Amazon S3 Encryption Client, you need to explicitly enable this behavior when you instantiate the client.

The `enableLegacyUnauthenticatedModes` parameter of the `builderV4()` method enables the Amazon S3 Encryption Client to decrypt content encrypted with legacy unauthenticated encryption algorithms (such as AES-CBC) and to perform ranged GET requests on encrypted objects.

The `enableLegacyWrappingAlgorithms` parameter of the `builderV4()` method enables the Amazon S3 Encryption Client to decrypt data keys that were wrapped with legacy V2 wrapping algorithms.

If your `v3Client` doesn't include the necessary settings, and it encounters an object or data key encrypted with a legacy algorithm, it throws `S3EncryptionClientException`.

For example, this code builds a `v3Client` object with a user-provided raw AES wrapping key. This client always encrypts only with fully supported algorithms. However, it can decrypt objects and data keys encrypted with fully supported or legacy algorithms.

```
// v3

class v3EnableLegacyDecryptionModesExample {
    public static void main(String[] args) {
        S3Client v3Client = S3EncryptionClient.builderV4()
                .aesKey({{aesKey}})
                .encryptionAlgorithm(AlgorithmSuite.ALG_AES_256_GCM_IV12_TAG16_NO_KDF)
                .commitmentPolicy(CommitmentPolicy.FORBID_ENCRYPT_ALLOW_DECRYPT)
                .enableLegacyUnauthenticatedModes({{true}})
                .enableLegacyWrappingAlgorithms({{true}})
                .build();
    }
}
```

The legacy decryption modes are designed to be a temporary fix. After you've re-encrypted all of your objects with fully supported algorithms, you can eliminate it from your code.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon S3 Encryption Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazon-s3-encryption-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
